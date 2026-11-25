1. docker compose up -d --build coordinator worker1 worker2

<!-- Push Heartbeat --> cara jalankannya
2. docker exec -it coordinator python3 app/coordinator.py
3. docker exec -it worker1 python3 app/worker.py
4. docker exec -it worker2 python3 app/worker.py

<!-- Active-Passive Failover -->
5. docker exec -it coordinator python3 app/coordinator-failover.py
6. docker exec -it worker1 python3 app/worker-failover.py
7. docker exec -it worker2 python3 app/worker-failover.py

<!-- Belum dicoba/jalankan -->