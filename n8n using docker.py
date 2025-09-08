#Instalasi n8n Menggunakan Docker di Ubuntu 

Membuat Folder untuk Project

Pertama, siapkan direktori project agar file konfigurasi dan data n8n lebih rapi. Jalankan perintah berikut:

    sudo apt update && sudo apt upgrade -y
    mkdir -p ~/n8n-server/n8n-data

    n8n-server → folder utama project
    n8n-data → tempat penyimpanan data (database SQLite, konfigurasi internal, dsb.)

Menginstall Docker dan Docker Compose
Pastikan sistem Ubuntu Anda sudah update, lalu install Docker dan Docker Compose:

    apt install docker.io #install docker
    apt install docker-compose-plugin #install docker compose 

Membuat File Konfigurasi n8n
Buat file .env di dalam folder n8n-server:
nano .env

    #en8n Configuration 
    N8N_BASIC_AUTH_ACTIVE=true
    N8N_BASIC_AUTH_USER=Your-User
    N8N_BASIC_AUTH_PASSWORD=Your-Password
    N8N_HOST=Your-IP-Server
    N8N_PORT=5678
    N8N_PROTOCOL=http
    N8N_SECURE_COOKIE=false  # Temporarily disable secure cookie to avoid HTTP access issues
    NODE_ENV=production

    N8N_BASIC_AUTH_ACTIVE → aktifkan login basic auth
     N8N_BASIC_AUTH_USER / PASSWORD → username & password login
     N8N_HOST → IP server (misal: 192.168.1.100 atau domain)
     N8N_PORT → port yang digunakan (default 5678)
     N8N_SECURE_COOKIE → set false bila akses masih via HTTP

Membuat File docker-compose.yml
Buat file docker-compose.yml di folder n8n-server:
nano docker-compose.yml 

     #file yml 
    services:
      n8n:
        image: n8nio/n8n
        restart: always
        container_name: n8n-server  # Custom container name
        ports:
          - "5678:5678"
        env_file:
          - .env
        volumes:
          - ./n8n-data:/home/node/.n8n

Menjalankan n8n dengan Docker
Masih di dalam folder n8n-server, jalankan perintah:

    docker-compose up -d

Mengakses n8n

Buka browser lalu akses:

    http://Your-IP-Server:5678

 atau  jika mengakses secara local bisagunakan 

    http://localhost:5678 