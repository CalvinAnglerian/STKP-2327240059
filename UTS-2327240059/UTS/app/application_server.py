import time
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn

DATABASE_URL = "http://database:9001/"


def call_database(method_name, *args):

    with xmlrpc.client.ServerProxy(
        DATABASE_URL,
        allow_none=True
    ) as database:

        return getattr(database, method_name)(*args)


def process_check_in(
    passenger_id,
    passenger_name,
    flight_code
):

    print(
        f"[APPLICATION] Menerima request: {passenger_id}",
        flush=True
    )

    try:

        result = call_database(
            "check_in",
            passenger_id,
            passenger_name,
            flight_code
        )

        print(
            f"[APPLICATION] Hasil database: "
            f"{result.get('message')}",
            flush=True
        )

        return result

    except Exception as exc:

        return {
            "success": False,
            "message": str(exc),
            "passenger_id": passenger_id
        }


def get_database_stats():
    return call_database("get_stats")


def get_all_checkins():
    return call_database("list_checkins")


class ThreadedXMLRPCServer(
    ThreadingMixIn,
    SimpleXMLRPCServer
):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":

    # Menunggu database siap
    while True:
        try:
            call_database("get_stats")
            break
        except Exception:
            print(
                "[APPLICATION] Menunggu Database Server...",
                flush=True
            )
            time.sleep(2)

    server = ThreadedXMLRPCServer(
        ("0.0.0.0", 8000),
        allow_none=True,
        logRequests=False
    )

    server.register_function(
        process_check_in,
        "process_check_in"
    )

    server.register_function(
        get_database_stats,
        "get_database_stats"
    )

    server.register_function(
        get_all_checkins,
        "get_all_checkins"
    )

    print(
        "[APPLICATION] XML-RPC server berjalan di port 8000",
        flush=True
    )

    server.serve_forever()