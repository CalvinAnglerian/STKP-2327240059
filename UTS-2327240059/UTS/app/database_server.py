import os
import time
import threading
import sqlite3
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn

DB_PATH = "/data/airport.db"
os.makedirs("/data", exist_ok=True)

# Maksimal 2 request masuk critical section
critical_semaphore = threading.BoundedSemaphore(2)

stats_lock = threading.Lock()
active_requests = 0
max_active_requests = 0


def initialize_database():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS checkins (
                passenger_id TEXT PRIMARY KEY,
                passenger_name TEXT NOT NULL,
                flight_code TEXT NOT NULL,
                checked_in_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def check_in(passenger_id, passenger_name, flight_code):
    global active_requests, max_active_requests

    # Sinkronisasi critical section
    with critical_semaphore:

        with stats_lock:
            active_requests += 1
            max_active_requests = max(
                max_active_requests,
                active_requests
            )

            current = active_requests

        print(
            f"[DATABASE] MASUK critical section "
            f"| aktif={current} "
            f"| penumpang={passenger_id}",
            flush=True
        )

        try:
            # Simulasi proses database
            time.sleep(3)

            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("""
                    INSERT INTO checkins
                    (passenger_id, passenger_name, flight_code)
                    VALUES (?, ?, ?)
                """, (
                    passenger_id,
                    passenger_name,
                    flight_code
                ))
                conn.commit()

            return {
                "success": True,
                "message": "Check-in berhasil",
                "passenger_id": passenger_id,
                "passenger_name": passenger_name,
                "flight_code": flight_code
            }

        except sqlite3.IntegrityError:
            return {
                "success": False,
                "message": "ID penumpang sudah terdaftar",
                "passenger_id": passenger_id
            }

        finally:
            with stats_lock:
                active_requests -= 1
                current = active_requests

            print(
                f"[DATABASE] KELUAR critical section "
                f"| aktif={current} "
                f"| penumpang={passenger_id}",
                flush=True
            )


def get_stats():
    with stats_lock:
        return {
            "active_requests": active_requests,
            "max_active_requests": max_active_requests,
            "semaphore_limit": 2
        }


def list_checkins():
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("""
            SELECT passenger_id, passenger_name,
                   flight_code, checked_in_at
            FROM checkins
        """).fetchall()

    return [
        {
            "passenger_id": row[0],
            "passenger_name": row[1],
            "flight_code": row[2],
            "checked_in_at": row[3]
        }
        for row in rows
    ]


class ThreadedXMLRPCServer(
    ThreadingMixIn,
    SimpleXMLRPCServer
):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":

    initialize_database()

    server = ThreadedXMLRPCServer(
        ("0.0.0.0", 9001),
        allow_none=True,
        logRequests=False
    )

    server.register_function(check_in, "check_in")
    server.register_function(get_stats, "get_stats")
    server.register_function(list_checkins, "list_checkins")

    print(
        "[DATABASE] XML-RPC server berjalan di port 9001",
        flush=True
    )

    print(
        "[DATABASE] Batas critical section = 2 request",
        flush=True
    )

    server.serve_forever()