# Tugas 2 PBP: Garuda Gear

<<<<<<< HEAD
Nama : Lessyarta Kamali Sopamena Pirade
=======
Nama: Lessyarta Kamali Sopamena Pirade

NPM: 2406356643

Kelas: PBP C
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336

NPM : 2406356643

Kelas : PBP C

Penjelasan shop: Garuda Gear adalah platform yang menawarkan perlengkapan sepak bola yang sepenuhnya diproduksi dan dibuat di Indonesia.

Link PWS: https://lessyarta-kamali-garudagear.pbp.cs.ui.ac.id

Pertanyaan Tugas 2:

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

   Bagan: https://drive.google.com/file/d/14AcmpOH011RIrVKUiDqXNh1vQHa-Nrzh/view?usp=sharing

   Saat sebuah permintaan dari klien diterima, Django akan memeriksanya terlebih dahulu di urls.py level proyek. Jika pola URL cocok dan mengarah ke aplikasi main, permintaan akan diteruskan untuk diproses lebih lanjut oleh urls.py di level aplikasi. Di sini, pola URL yang lebih spesifik akan dicocokkan untuk menjalankan fungsi view yang dituju. Namun, jika tidak ada pola yang cocok sejak awal di level proyek, Django akan langsung mengembalikan respons 404 Not Found.

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

Pertanyaan Tugas 3:

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?


2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat 
dimanfaatkan oleh penyerang?

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
   Tutorial 2 sangat jelas dan membantu dalam Tugas 3 PBP ini. Terima kasih banyak tim asisten dosen!
