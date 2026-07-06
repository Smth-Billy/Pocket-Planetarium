# 🌌 Pocket Planetarium - 2 Hands Control

Pocket Planetarium adalah aplikasi tata surya interaktif berbasis web 3D menggunakan **Three.js** dan teknologi deteksi gestur tangan secara real-time menggunakan **MediaPipe Hands**. Aplikasi ini memungkinkan pengguna menjelajahi planet-planet hanya dengan menggunakan gerakan tangan di depan webcam tanpa perlu menyentuh layar atau keyboard.

Aplikasi ini juga dilengkapi dengan server backend sederhana menggunakan **Flask (Python)** untuk memudahkan proses menjalankan proyek secara lokal maupun dibagikan ke jaringan publik.

---

## 🛠️ Fitur Utama & Cara Kontrol Gestur

Aplikasi ini mendukung deteksi hingga **2 tangan secara bersamaan** dengan fungsi kontrol yang berbeda:

| Kontrol Tangan | Gerakan / Gestur | Fungsi |
| :--- | :--- | :--- |
| **Tangan 1 (Utama)** | ☝️ **Jari Telunjuk Terbuka** | Menggerakkan pointer biru untuk memilih/melihat detail planet. |
| **Tangan 1 (Utama)** | 👌 **Cubit (Pinch) Jempol + Telunjuk** | Melakukan **Zoom-In** fokus masuk ke planet yang sedang dipilih. |
| **Tangan 2 (Tambahan)**| ✊ **Mengepal (Fist)** | **Menjeda Waktu (Pause)** rotasi dan revolusi planet di tata surya. |
| **Dua Tangan** | 👐 **Merentangkan Kedua Tangan** | **Global Zoom** (Mendekatkan/menjauhkan jarak kamera global berdasarkan jarak kedua tanganmu). |

---

## 🚀 Cara Menjalankan Proyek di Lokal (Localhost)

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer/laptop kamu:

### 1. Prasyarat
Pastikan kamu sudah menginstal **Python 3** di komputermu.

### 2. Instalasi Flask
Buka terminal atau command prompt, lalu instal pustaka Flask dengan perintah:
bash
pip install flask"

3. Menjalankan Server

Pastikan file app.py dan planetarium.html berada dalam satu folder yang sama. Jalankan perintah berikut di dalam folder tersebut:
Bash

python app.py

Setelah muncul tulisan --- Server Berjalan! ---, buka browser favoritmu dan akses alamat berikut:
👉 http://127.0.0.1:5000

Jangan lupa berikan izin (allow) akses kamera/webcam pada browser saat diminta.
🌐 Cara Membagikan Proyek Agar Bisa Dicoba Banyak Orang (Menggunakan Ngrok)

Jika kamu ingin memamerkan proyek ini ke teman, dosen, atau banyak orang di internet tanpa perlu menyewa hosting, kamu bisa menggunakan Ngrok untuk membuat tunneling aman dari localhost-mu ke publik.

    Penting: Karena aplikasi ini membutuhkan akses kamera (getUserMedia), browser mewajibkan koneksi yang aman (HTTPS). Ngrok secara otomatis menyediakan tautan HTTPS gratis untuk kebutuhan ini.

Langkah-langkah menggunakan Ngrok:

    Unduh & Pasang Ngrok

        Download Ngrok sesuai OS-mu di ngrok.com.

        Ikuti instruksi di situsnya untuk menghubungkan akun/token Ngrok kamu setelah mendaftar (gratis).

    Jalankan Aplikasi Flask Kamu

        Pastikan server Flask lokalmu sudah berjalan terlebih dahulu di port 5000 (python app.py).

    Buka Tunnel Ngrok

        Buka terminal/command prompt baru, lalu jalankan perintah berikut:
    Bash

    ngrok http 5000

    Bagikan Link HTTPS

        Ngrok akan menampilkan informasi di terminal. Cari bagian Forwarding yang memiliki alamat berawalan https://... (contoh: https://xxxx-xxxx.ngrok-free.app).

        Salin link https tersebut dan bagikan ke teman-temanmu. Mereka bisa langsung membukanya dari laptop maupun smartphone mereka!

📚 Teknologi yang Digunakan

    HTML5 & CSS3 (Responsive Design)

    Three.js - Pembuatan grafis 3D tata surya.

    MediaPipe Hands - Deteksi rangka hand landmark secara real-time via webcam.

    Flask (Python) - Web server backend minimalis.
