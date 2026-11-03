import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from presentation_client import (
    check_in,
    get_stats,
    get_all_checkins
)


def simulate_checkin(passenger):

    passenger_id, passenger_name, flight_code = passenger

    try:

        result = check_in(
            passenger_id,
            passenger_name,
            flight_code
        )

        status = "BERHASIL" if result["success"] else "GAGAL"

        print(
            f"{passenger_id}: {status} - {result['message']}"
        )

    except Exception as error:

        print(f"{passenger_id}: ERROR - {error}")


def main():

    passengers = [
        ("P001", "Andi", "GA101"),
        ("P002", "Budi", "GA101"),
        ("P003", "Citra", "GA101"),
        ("P004", "Dewi", "GA101"),
        ("P005", "Eko", "GA101"),
        ("P006", "Fitri", "GA101")
    ]

    print("=== SIMULASI CHECK-IN BANDARA ===")
    print("Mengirim 6 request secara bersamaan...\n")

    start = time.time()

    with ThreadPoolExecutor(max_workers=6) as executor:

        futures = [
            executor.submit(simulate_checkin, passenger)
            for passenger in passengers
        ]

        for future in as_completed(futures):
            future.result()

    print(f"\nWaktu pengujian: {time.time() - start:.2f} detik")

    stats = get_stats()
    records = get_all_checkins()

    print("\n=== HASIL PENGUJIAN ===")
    print("Batas semaphore        :", stats["semaphore_limit"])
    print("Maksimal request aktif :", stats["max_active_requests"])
    print("Request aktif sekarang :", stats["active_requests"])
    print("Data check-in tersimpan:", len(records))

    if stats["max_active_requests"] <= 2:
        print("\nSTATUS: BERHASIL")
        print("Maksimal hanya 2 request mengakses critical section.")
    else:
        print("\nSTATUS: GAGAL")


if __name__ == "__main__":
    main()