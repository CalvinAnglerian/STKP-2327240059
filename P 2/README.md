Pertemuan 2 (Monolitik)

# docker hub : download image

Di 
# C:\Users\user602>docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# C:\Users\user602>docker image ls
                                                                                                    i Info →   U  In Use
IMAGE                                            ID             DISK USAGE   CONTENT SIZE   EXTRA
mongodb/mongodb-community-server:8.3-ubi9-slim   04bf69d01eaa        658MB          160MB    U

# C:\Users\user602>docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


Di Vscode
# docker compose ps : hanya melihat bagian di dalam directory (folder) saja, bukan semuanya  

# docker compose up -d : untuk digunakan untuk menjalankan dan mengaktifkan semua layanan (container) yang 
#                        terdaftar di dalam file docker-compose.yaml Anda secara otomatis di latar belakang.

# ipconfig : ngecek ip di device

# docker compose down : menghentikan docker compose ps

# docker compose down -v --rmi all --remove-orphans : menghapus semuanya