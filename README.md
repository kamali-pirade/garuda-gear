# Tugas 2 PBP: Garuda Gear

Nama: Lessyarta Kamali Sopamena Pirade

NPM: 2406356643

Kelas: PBP C

Penjelasan shop: Garuda Gear adalah platform yang menawarkan perlengkapan sepak bola yang sepenuhnya diproduksi dan dibuat di Indonesia.

Link PWS: https://lessyarta-kamali-garudagear.pbp.cs.ui.ac.id/

Pertanyaan:

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Langkah-langkah pengerjaan sesuai checklist:
   Langkah 1: Membuat sebuah proyek Django baru.
   Membuat direktori garuda-gear, lalu membuat virtual environment dan mengaktifkannya. Setelah itu, saya menyiapkan dependencies di requirements.txt dan menginstallnya.
   Buat proyek Django bernama garuda_gear.
   Konfigurasi environtment variables dengan membuat .env dan .env.prod. Di dalam file .env, atur PRODUCTION=False agar aplikasi menggunakan database SQLite yang simpel untuk pengerjaan pada laptop saya. Di dalam .env.prod ada PRODUCTION=True dan kredensial saya agar dapat berjalan di PWS saat online.
   Lalu, saya modifikasi settings.py agar dapat membaca environment variables dari file .env.
   Melakukan migrasi database dan run server. Memeriksa aplikasi di http://localhost:8000 pada browser.

   Langkah 2: Membuat aplikasi dengan nama main pada proyek tersebut, membuat model pada aplikasi main, membuat fungsi pada views.py, membuat routing pada urls.py.
   Setelah membuat proyek baru, saya membuat aplikasi main yang terdiri dari model untuk struktur database, view untuk logika, dan template untuk tampilan. Saya mendaftarkan aplikasi main di dalam file settings.py agar diakui oleh proyek, lalu memasukkan nama aplikasi, nama pembuat, dan kelas di views.py agar dapat digunakan pada main.html dengan placeholder {{...}}. Kemudian, saya melakukan routing dua tingkat di urls.py, baik di level proyek, maupun di level aplikasi.

   Langkah 3: Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
   Saya melakukan direct push, namun gagal pada awalnya. Ketika saya periksa di log build, kegagalan ini ternyata diakibatkan oleh tidak ditemukannya file requirements.txt. Saya kemudian melakukan pip freeze lalu add file requirements.txt kembali. Setelah itu, deployment ke PWS sukses dan dapat diakses di https://lessyarta-kamali-garudagear.pbp.cs.ui.ac.id/

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   Browser user -> Django -> urls.py -> views.py -> models.py -> views.py -> berkas html -> Response (HTML) -> Browser user
   Saat user mengunjungi URL aplikasi, Django pertama-tama memeriksa urls.py yang berfungsi sebagai peta jalan dan menentukan fungsi mana di dalam views.py yang harus dieksekusi. Fungsi di views.py ini berkomunikasi dengan models.py untuk mengambil data dari database. Setelah mendapatkan data yang diperlukan, view akan menggabungkan data tersebut dengan berkas html yang berfungsi sebagai template visual. Hasilnya adalah sebuah halaman HTML lengkap yang dikirim kembali sebagai respons ke browser user, sehingga menampilkan halaman web yang utuh.

3. Jelaskan peran settings.py dalam proyek Django!
   Dalam proyek Django, settings.py berfungsi sebagai pusat konfigurasi utama dari sebuah aplikasi.

   Sesuai dengan yang saya lakukan dalam pembuatan Tugas 2 PBP ini, perannya sebagai berikut:

   - Menambahkan 'main' ke daftar INSTALLED_APPS agar proyek Django mengenali dan mengelola aplikasi main yang sudah saya buat.
   - Mengatur database agar aplikasi bisa secara cerdas beralih antara menggunakan database SQLite saat pengembangan di laptop saya, dan menggunakan database PostgreSQL saat di-deploy ke PWS dengan cara membaca environment variables.
   - File settings.py menyimpan SECRET_KEY unik proyek saya dan ALLOWED_HOSTS, yaitu daftar domain yang diizinkan untuk mengakses aplikasi saya.

4. Bagaimana cara kerja migrasi database di Django?
   Migrasi adalah cara memastikan database proyek yang sedang dibuat selalu cocok dengan rancangan yang saya tulis di file models.py. Pertama menjalankan perintah makemigrations di mana Django akan melihat perubahan yang baru dibuat pada model dan secara otomatis membuat sebuah file "rencana kerja". Kemudian, saat menjalankan migrate di mana Django akan membaca "rencana kerja" tersebut dan membangun atau mengubah tabel Product di dalam database. Setiap kali ada perubahan di models.py, migrasi harus dilakukan.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Menurut saya, Django baik untuk pemula karena menyediakan banyak fitur penting secara bawaan sehingga tidak akan sulit untuk memilih library tambahan. Contohnya, fitur ORM (Object-Relational Mapper) memungkinkan interaksi dengan database menggunakan Python tanpa perlu menulis SQL, dan Admin Panel yang dibuat secara otomatis memberikan antarmuka siap pakai untuk mengelola data secara visual. Selain itu, strukturnya dengan pola Model-View-Template (MVT) juga memudahkan pemula untuk menulis kode yang rapi dan memisahkan antara logika, data, dan tampilan.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
   Tutorial 1 sangat membantu dan mudah dimengerti. Terima kasih banyak tim asisten dosen!
