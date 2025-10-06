# Garuda Gear

Nama : Lessyarta Kamali Sopamena Pirade

NPM : 2406356643

Kelas : PBP C

Penjelasan shop: Garuda Gear adalah platform yang menawarkan perlengkapan sepak bola yang sepenuhnya diproduksi dan dibuat di Indonesia.

Link PWS: https://lessyarta-kamali-garudagear.pbp.cs.ui.ac.id

## Pertanyaan Tugas 2:

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

## Pertanyaan Tugas 3:

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Data delivery sangat penting karena sebuah platform dinamis perlu mengirimkan data dari satu stack ke stack lainnya. Dalam kasus Garuda Gear, ini berarti mengirimkan data dari backend (server Django dan database) ke frontend (browser user). Tanpa data delivery, Garuda Gear yang saya bangun hanya akan menjadi halaman HTML statis.
   Dengan data delivery, garuda gear dapat:
   1) Menampilkan katalog produk yang dijual, di mana saya menggunakan data delivery dalam format HTML untuk mengirimkan daftar produk dari database ke template main.html.
   2) Menyediakan data untuk platform lain, di mana saya  mengimplementasikan endpoint yang mengembalikan data dalam format XML dan JSON.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   Menurut saya, JSON lebih baik dan lebih modern untuk pengembangan web. Hal ini karena tampilan data di JSON lebih ringkas dan mudah saya baca. JSON lebih populer dibandingkan XML. Hal ini karena meskipun sintaks JSON berasal dari objek JavaScript dan JavaScript adalah bahasa dominan untuk frontend web. Hal ini membuat proses pengolahan data JSON di browser menjadi lebih natural. XML juga memerlukan proses parsing yang lebih rumit.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   Method is_valid() berfungsi sebagai lapisan validasi data. Sebelum data yang dikirim user dari form diizinkan untuk disimpan ke database, method is_valid() akan memeriksa apakah semua input sesuai dengan aturan yang ada di ProductForm dan Product model.
   Misalnya, semua field wajib sudah terisi dan semua tipe data sudah benar.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

   csrf_token adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya. 
   Jika saya tidak menambahkan csrf_token pada form tambah produk di Garuda Gear, maka form saya akan rentan terhadap serangan Cross-Site Request Forgery (CSRF). 
   Skenario yang dapat dimanfaatkan oleh penyerang:
   1) Saya login ke aplikasi Garuda Gear.
   2) Saya mengunjungi website lain yang sudah dimasuki penyerang.
   3) Webite tersebut memiliki kode yang secara diam-diam mengirimkan request POST ke URL tambah produk di aplikasi saya.
   4) Karena saya masih login, request jahat tersebut akan membawa cookie sesi saya yang valid.
   5) Tanpa csrf_token, server saya akan menganggap request tersebut sah dan akan memprosesnya (misalnya, menambahkan produk spam ke katalog saya) tanpa saya sadari.
   Jika saya mempunyai csrf_token, setiap request POST dari browser user harus menyertakan token unik yang cocok dengan yang ada di server. Penyerang tidak akan memiliki token ini, sehingga request dari penyerang akan ditolak dan serangan gagal.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   
   Pertama, saya menyiapkan 4 fungsi baru di views.py, yaitu def show_xml(request), def show_json(request), def show_xml_by_id(request, news_id), dan def show_json_by_id(request, news_id).
   Lalu saya memperbaiki bagian class Product dan category product dengan membuat class Product dengan field-field yang diperlukan: name, price, description, thumbnail, category, is_featured, stock, brand, dan menggunakan CATEGORY_CHOICES untuk memberikan pilihan kategori produk
   Setelah itu saya membuat class ProductForm yang inherit dari ModelForm.

   Saya menambahkan 2 file html baru:
   1) Template add_product.html yang menyediakan tombol submit untuk menambahkan produk
   2) Template product_detail.html yang bekerja untuk menampilkan detail lengkap produk termasuk nama, kategori, brand, stok, dan status bestseller, menampilkan gambar produk jika tersedia dan menampilkan tombol back untuk kembali ke daftar produk
   
   Kemudian, saya membuat fungsi add_product(request) di views.py yang jika valid akan menyimpan data ke database dan redirect ke halaman utama.
   Saya juga membuat fungsi show_product(request, id) di views.py untuk menangani kasus produk tidak ditemukan dengan mengembalikan 404 dan mengirim data produk ke template product_detail.html
   
   Lalu, menambahkan 4 fungsi views baru di views.py, yaitu def show_xml(request) yang mengkonversi data ke format XML, def show_json(request) yang mengkonversi data ke format JSON, def show_xml_by_id(request, news_id) yang mengambil produk berdasarkan ID dan mengkonversi hasil ke format XML, serta def show_json_by_id(request, news_id) yang mengambil satu produk berdasarkan ID dan mengkonversi hasil ke format JSON dan mengembalikan HttpResponse.
   
   Saya juga membuat URL routing dengan menambahkan URL patterns di urls.py.
   Setelah implementasi selesai, saya melakukan testing untuk melihat semua produk dalam format XML dan JSON, serta melihat produk tertentu dalam format XML dan JSON

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
   Tutorial 2 sangat jelas dan membantu dalam Tugas 3 PBP ini. Terima kasih banyak tim asisten dosen!

Screenshot Postman:
![All Products by XML](screenshots/PostmanXML.png)
![All Products by JSON](screenshots/PostmanJSON.png)
![XML by Product ID](screenshots/PostmanIDXML.png)
![JSON by Product ID](screenshots/PostmanIDJSON.png)

## Pertanyaan Tugas 4:

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
  
   Django AuthenticationForm adalah sebuah form bawaan dari Django yang dirancang untuk memverifikasi identitas user saat login. Form ini memiliki 2 field utama: username dan password. Tugas utamanya adalah mengambil input dari user, lalu memeriksa ke database apakah ada user dengan kombinasi username dan password tersebut yang aktif. 
   
   Kelebihan:
   - AuthenticationForm dilengkapi dengan mekanisme keamanan bawaan Django yang tidak hanya mencocokkan username dan password, tetapi juga memastikan password yang dimasukkan di-hash dengan benar sebelum dibandingkan dengan hash di database, serta memeriksa status user (apakah akun aktif atau tidak) sebelum mengizinkan login. 
   - Form memvalidasi input dengan memastikan kedua field terisi dan memberikan pesan error jika input salah.
   
   Kekurangan:
   - Form hanya menerima username. Jika ingin login dengan alamat email, harus membuat class form baru yang inherit dari AuthenticationForm.
   - Tampilan yang dihasilkan sangat standar. Jika ingin mendapatkan tampilan sesuai keinginan, harus me-render setiap field secara manual di dalam HTML dan menatanya dengan CSS.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

   Perbedaan:
   - Autentikasi: Proses verifikasi user. Contohnya adalah saat memasukkan username dan password. Jika input user cocok dengan data di database, sistem berhasil mengautentikasi user.
   - Otorisasi: Proses menentukan hak akses atau izin yang dimiliki oleh user yang sudah terautentikasi. Contohnya adalah ketika ada admin dan user biasa yang sama-sama berhasil log in, namun hanya admin yang dapat menghapus data, sedangkan user biasa tidak.

   Implementasi di Django:
   - Autentikasi: 
   1) Django menyediakan model User bawaan yang memiliki field esensial seperti username, password (disimpan dalam bentuk hash), email, first_name, dan last_name.
   2) Django menyediakan fungsi seperti authenticate() untuk memeriksa kredensial user dan login() untuk membuat sesi bagi user yang berhasil diautentikasi.
   3) Django juga menyediakan form seperti AuthenticationForm dan UserCreationForm untuk mempermudah proses login dan registrasi.

   - Otorisasi:
   1) Menggunakan decorator @login_required adalah cara paling sederhana untuk otorisasi. Decorator ini digunakan pada sebuah view untuk memeriksa apakah seorang user sudah terautentikasi atau belum. Jika belum, akses ke halaman tersebut akan ditolak dan user akan diarahkan ke halaman login. 
   2) Django memiliki sistem izin yang lebih canggih. Kita bisa menentukan izin spesifik untuk model tertentu dan memberikannya kepada user atau grup.
   3) Model User bawaan Django memiliki flag seperti is_staff atau is_superuser yang bisa digunakan untuk memberikan hak akses khusus. Misalnya, hanya user dengan is_staff=True yang dapat mengakses halaman admin Django.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

   Cookies:
   - Kelebihan:
   1) Data disimpan di browser user, sehingga tidak membebani penyimpanan di server.
   2) Cookies dapat diatur agar memiliki masa kedaluwarsa yang panjang, sehingga tetap ada bahkan ketika browser ditutup.
   - Kekurangan:
   1) Data cookies disimpan sebagai teks biasa di komputer, sehingga siapapun yang mengakses komputer tersebut dapat melihatnya.
   2) Kapasitas penyimpanan cookies sangat kecil (sekitar 4 KB), sehingga tidak cocok untuk menyimpan data yang besar.
   3) User dapat mematikan fitur cookies di browser, sehingga aplikasi tidak berfungsi dengan benar.

   Session:
   - Kelebihan:
   1) Data session disimpan di sisi server. Browser client hanya menyimpan Session ID (sebuah token acak) di dalam cookie. Ini jauh lebih aman karena data sensitif tidak pernah meninggalkan server.
   2) Ukuran tidak dibatasi oleh limit 4 KB seperti cookies.
   - Kekurangan:
   1) Setiap sesi user aktif akan memakan memori di server. Jika ada ribuan user yang aktif bersamaan, ini dapat mnejadi beban.
   2) Mekanisme session masih membutuhkan cookie untuk menyimpan Session ID di client. Jika cookies dimatikan, session juga tidak akan berfungsi.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
   
   Tidak, penggunaan cookies tidak aman secara default. Cookie pada dasarnya adalah file teks yang disimpan di komputer user, sehingga rentan untuk dibaca atau dimanipulasi.

   Risiko potensial yang harus diwaspadai:

   - Pencurian sesi: Jika seorang penyerang berhasil mendapatkan cookie sesi (misalnya, sessionid Django), mereka dapat menggunakannya untuk meniru user dan masuk ke akun mereka tanpa memerlukan password.
   - Cross-Site Scripting (XSS), di mana penyerang dapat menyuntikkan skrip berbahaya ke dalam situs web. Jika tidak ditangani dengan benar, skrip ini dapat dieksekusi oleh browser user lain dan digunakan untuk mencuri cookies mereka.
   - Cross-Site Request Forgery (CSRF), yaitu serangan di mana penyerang menipu user yang sudah login untuk tanpa sadar mengirimkan request berbahaya ke aplikasi web. Misalnya, membuat user tanpa sadar mentransfer uang atau mengubah kata sandi mereka.
   
   Bagaimana Django Menanganinya:
   
   Django dirancang dengan prinsip "secure by default" dan menyediakan beberapa lapisan perlindungan yang kuat untuk mengatasi risiko-risiko ini.

   1) Django tidak menyimpan data sensitif di dalam cookie, hanya menyimpan sebuah sessionid acak. Data sesi yang sebenarnya disimpan dengan aman di database server.
   2) Untuk setiap form yang menggunakan metode POST, Django mewajibkan adanya {% csrf_token %}. Token ini adalah nilai rahasia unik yang dihasilkan untuk setiap sesi user. Saat form dikirim, Django memverifikasi token ini. Jika token tidak ada atau tidak cocok, request akan ditolak. Ini secara efektif mencegah serangan CSRF.
   3) Django secara otomatis mengamankan halaman web dengan melakukan escaping atau menetralkan karakter-karakter HTML khusus dari variabel yang akan ditampilkan. Ini berarti, jika seorang user mencoba memasukkan kode JavaScript berbahaya ke dalam sebuah field, simbol-simbol pemicu kode seperti < dan > akan diubah menjadi teks biasa yang tidak berbahaya. Hasilnya, kode tersebut hanya akan ditampilkan sebagai tulisan di layar dan tidak akan dieksekusi oleh browser, sehingga melindungi dari serangan XSS.
   4) Flag pengaman cookie:
   - HttpOnly: Django secara default mengatur cookie sessionid dengan flag HttpOnly. Flag ini memberitahu browser untuk tidak mengizinkan JavaScript mengakses cookie tersebut, sehingga sangat efektif memitigasi risiko pencurian cookie melalui serangan XSS.
   - Secure: Jika aplikasi berjalan di atas HTTPS, Django dapat dikonfigurasi dengan SESSION_COOKIE_SECURE = True  untuk menambahkan flag Secure pada cookies. Ini memastikan browser hanya akan mengirim cookie melalui koneksi yang terenkripsi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   Pertama, saya membuat sistem registrasi user dengan menambahkan import UserCreationForm dan messages di file views.py untuk membuat formulir pendaftaran user di aplikasi web dengan mudah. Lalu, saya menambahkan function register di file tersebut untuk menghasilkan formulir registrasi dan membuat akun user baru ketika data sudah diisi dan di-submit oleh user.
   
   Kemudian, saya membuat file register.html untuk membuat tampilan form registrasi. Saya juga menambahkan {% csrf_token %} untuk keamanan. Saya menambahkan path /register/ di urls.py untuk registrasi agar aplikasi Django tahu fungsi view mana yang harus dijalankan ketika seorang user mengunjungi URL tersebut.
   
   Setelah itu, saya membuat fungsi login dan logout dengan menambahkan import authenticate, login, AuthenticationForm, dan logout. Langkah selanjutnya mirip dengan langkah pembuatan form registrasi sebelumnya yaitu dengan membuat function login_user dan logout_user di views.py, serta login.html dan menambahkan button untuk logout di main.html.
   
   Ketika akun user sudah di-register, user dapat melakukan login di halaman login. Ketika ingin logout, user dapat menekan button logout.
   
   Langkah selanjutnya adalah menambahkan import decorator login_required pada views.py dan mengaplikasikannya untuk fungsi show_main dan show_product agar hanya dapat diakses oleh user yang sudah login (terautentikasi). Hal ini saya lakukan untuk memastikan bahwa hanya user yang sudah login yang dapat mengakses halaman tertentu (otorisasi).

   Saya juga menyimpan cookie saat login di function login_user dengan menggunakan response.set_cookie('last_login', ...) dan mengambil data cookie di show_main pada views.py menggunakan request.COOKIES.get('last_login', 'Never') dan memasukkannya ke dalam context. Kemudian di main.html, saya menampilkannya dengan {{ last_login }}. Saat logout, cookie akan terhapus karena di function logout_user saya memanggil response.delete_cookie('last_login').
   
   Di models.py, saya menambahkan sebuah field ForeignKey ke model Product yang merujuk ke model User bawaan Django. Ini menciptakan hubungan many-to-one (banyak produk dimiliki oleh satu user). Di function add_product pada views.py, saya menggunakan form.save(commit=False) agar objek dibuat di memori tanpa disimpan ke database. Ini memberi saya waktu untuk mengatur product.user = request.user sebelum akhirnya memanggil product.save().

   Terakhir, saya menambahkan tombol filter My dan All pada halaman main.html untuk melihat produk yang saya jual sebagai penjual dan semua produk yang dijual oleh semua penjual yang terdaftar di aplikasi Garuda Gear.

## Pertanyaan Tugas 5:
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
   Urutan:
   1) Inline Style = ditulis langsung dalam HTML. Contoh: h1 style="color: pink;"
   2) ID Selector = menggunakan atribut id. Contoh: #navbar
   3) Class Selector = menggunakan class atau pseudo-class. Contoh: .test, :hover
   4) Attribute Selector = menggunakan atribut. Contoh: [type="text"]
   5) Element Selector = hanya berdasarkan nama elemen. Contoh: h1, p, div

   Aturan tambahan:
   - Jika ada 2 aturan dengan spesifitas yang sama, aturan terakhir yang ditulis akan menang
   
   Contoh:
   
   h1 {background-color: yellow;}
   
   h1 {background-color: red;}
   
   Tampilan: background-color akan red.
   
   - Selector ID lebih kuat dibanding selector atribut
   
   div#myDiv {background-color: green;}
   
   #myDiv {background-color: yellow;}
   
   div[id=myDiv] {background-color: blue;}
   
   Tampilan: hasil background-color akan green karena lebih spesifik.
   
   - Class selector lebih kuat daripada banyak element selector
   
   Contoh: 
   
   .intro {background-color: yellow;}
   
   h1 {background-color: red;}
   
   Tampilan: background-color: yellow, karena class lebih spesifik.
   
   - Selector universal (*) dan nilai yang diwarisi tidak mempengaruhi spesifisitas
   
   Contoh: * {background-color: yellow;}
   
   h1 {background-color: red;}
   
   Tampilan: background-color: red; karena element selector (h1) lebih spesifik daripada *.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
   
   Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena bertujuan agar tampilan sebuah web dapat terlihat baik dan fungsional di semua jenis perangkat, mulai dari desktop dengan layar lebar, tablet, hingga smartphone dengan layar kecil. Sebuah aplikasi web harus bisa beradaptasi untuk memberi pengalaman user (UX) yang konsisten dan nyaman. 
   
   Contoh aplikasi yang sudah menerapkan responsive design:
   - Website PBP: https://pbp-fasilkom-ui.github.io/ganjil-2026. Ketika mencoba toggle device mode (Ctrl + Shift + I lalu Ctrl + Shift + M), layar otomatis berubah menjadi tampilan lebih kecil, namun tampilan menyesuaikan dengan lebar layar.
   
   Contoh aplikasi yang belum menerapkan responsive design:
   - Space Jam: https://www.spacejam.com/1996/. Ketika mencoba toggle device mode, layar semakin kecil namun tampilan tetap sama sehingga user perlu melakukan zoom untuk melihat tampilan.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
   Margin, border, dan padding adalah bagian dari CSS Box Model.
   
   Perbedaan:
   - Margin: mengosongkan area di sekitar border (transparan)
   - Border: garis tepian yang membungkus konten dan padding-nya
   - Padding: mengosongkan area di sekitar konten (transparan)

   Cara implementasi di CSS:
   
   .card-yay {
      
         /* padding 20px di semua sisi (atas, kanan, bawah, kiri) */
         
         padding: 20px;
         
         /* border solid setebal 1px dengan warna abu-abu */
         
         border: 1px solid #cccccc;

         
         /* margin 15px di semua sisi untuk memberi jarak dengan elemen lain */
         
         margin: 15px;

   }

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   1) Flexbox:
   Digunakan untuk mengatur tata letak elemen dalam satu dimensi (baik secara horizontal dalam satu baris, atau vertikal dalam satu kolom). Digunakan untuk komponen seperti navbar atau item kartu yang berjajar.
   
   Implementasi di Tugas 5: 
   
   Pada navbar.html, kelas flex, items-center, dan justify-between digunakan.
   - flex: Mengaktifkan layout Flexbox.
   - items-center: Menyejajarkan item secara vertikal di tengah.
   - justify-between: Memberi jarak merata antar item (logo di kiri, menu di tengah, tombol login di kanan).
   
   2) Grid layout:
   Digunakan untuk mengatur tata letak elemen dalam dua dimensi (baris dan kolom). Mirip seperti tabel atau spreadsheet.
   
   Implementasi di Tugas 5: 
   
   Pada main.html, kelas grid, grid-cols-1, md:grid-cols-2, dan lg:grid-cols-3 digunakan untuk menampilkan daftar berita.
   - grid: Mengaktifkan layout Grid.
   - grid-cols-1: Secara default (di layar kecil), berita ditampilkan dalam 1 kolom.
   - md:grid-cols-2: Pada layar ukuran medium (medium), tata letaknya berubah menjadi 2 kolom.
   - lg:grid-cols-3: Pada layar besar (large), tata letaknya menjadi 3 kolom.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

      Pertama, saya menambahkan Tailwind ke aplikasi. Lalu mengimplementasikan fitur Edit Product dan Delete Product, di mana masing-masing mempunyai function di views.py. Kemudian, saya membuat navigation bar yang berisi nama toko, home, add product, about us, username, dan logout button.

      Saya mengkonfigurasi Static Files pada aplikasi dan menambahkan global.css, di mana saya memilih warna-warna dasar dari web saya. Saya menghubungkan file global.css dengan base.html dan menambahkan font Poppins pada base.html ini.

      Setelah itu, saya melakukan styling untuk main.html, navbar.html, edit_product.html, register.html, login.html, product_detail.html. Agar produk nyaman dilihat, saya menambahkan card_product.html yang menampilkan produk dalam bentuk kartu. Kartu ini dirancang dengan rasio 3:4 untuk thumbnail dan menampilkan informasi seperti nama, harga, dan kategori. Pada setiap kartu, saya mengimplementasikan efek "pop" agar lebih interaktif. Saat pengguna mengarahkan kursor ke sebuah kartu, kartu tersebut akan sedikit membesar (hover:scale-105) dan menampilkan bayangan (hover:shadow-xl). Awalnya, efek bayangan terpotong karena adanya kelas overflow-hidden pada elemen pembungkus. Kartu juga saya bentuk dengan rounded edge.
      
      Saya juga menambahkan about.html yang menampilkan informasi mengenai Garuda Gear. about.html ini dapat diakses melalui navigation bar.

      Terakhir, saya mengimplementasikan sistem Pagination. Di views.py, saya menggunakan Paginator bawaan Django untuk membagi daftar produk menjadi beberapa halaman, dengan masing-masing halaman menampilkan maksimal 9 produk. Di main.html, saya menambahkan komponen navigasi halaman yang dinamis. Komponen ini secara otomatis menampilkan nomor halaman yang benar, menonaktifkan tombol "Previous" atau "Next" jika tidak diperlukan, dan menunjukkan nomor halaman yang sedang aktif.

## Pertanyaan Tugas 6:
1. Apa perbedaan antara synchronous request dan asynchronous request?

   Pada synchronous request, user harus menunggu ketika halaman load (click, wait, refresh).

   Pada asynchronous request, user masih bisa berinteraksi dengan halaman website walaupun data sedang di-load.

   Awalnya, website Garuda Gear bekerja secara synchronous. Ini berarti ketika user menghapus produk (delete product), browser akan berhenti total. Browser mengirim permintaan ke server, lalu user harus menunggu sampai server selesai menghapus produk dan mengirim kembali halaman utama yang baru untuk lanjut menggunakan website. Selama proses menunggu itu, halaman menjadi tidak responsif. 

   Sekarang, setelah mengimplementasi AJAX, Garuda Gear bekerja secara asynchronous. Ketika user menghapus produk, permintaan penghapusan dikirim di latar belakang. User tidak perlu menunggu. Halaman tetap bisa di-scroll dan digunakan. Saat server selesai, ia hanya memberitahu browser bahwa sudah selesai lalu JavaScript di browser bertugas memperbarui tampilan (menghilangkan kartu produk dan menampilkan toast).

2. Bagaimana AJAX bekerja di Django (alur request–response)?

   Di Tugas 6 ini, alur kerja AJAX yang kita buat adalah sebagai berikut:

   Pertama, user menekan tombol "Edit" pada salah satu kartu produk di halaman utama. Lalu, fungsi JavaScript showEditModal(productId) yang terpasang pada tombol tersebut dijalankan. Ini mencegah browser pindah halaman. Fungsi showEditModal kemudian melakukan fetch ke URL spesifik yang telah dibuat, misalnya /edit-product-ajax/123/. Permintaan ini dikirim secara asynchronous di latar belakang untuk mengambil data produk yang akan diedit. urls.py di sisi server mencocokkan URL /edit-product-ajax/123/ dengan view edit_product_ajax.
   
   View edit_product_ajax mengambil data produk dari database, mengubahnya menjadi format JSON, lalu mengirimkannya kembali sebagai JsonResponse. Fetch di frontend menerima data JSON tersebut dan menggunakannya untuk mengisi field-field di dalam form modal. Setelah selesai mengedit dan menekan "Save", fetch kembali mengirim data form ke view yang sama (tapi dengan metode POST). Setelah mendapat balasan JsonResponse yang berisi status sukses, JavaScript kemudian memanggil showToast() dan fetchProducts() untuk memperbarui daftar produk di halaman utama tanpa reload.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

   - Halaman tidak pernah berhenti atau freeze. Saat data produk di-load, ada loading spinner, tapi sisa halaman seperti navbar tetap bisa digunakan. Ini lebih nyaman untuk user.
   - Daripada server harus merender ulang seluruh HTML setiap kali user filter atau hapus produk, dengan AJAX server hanya mengirimkan data JSON yang ukurannya jauh lebih kecil. Ini menghemat bandwidth dan mempercepat waktu.
   - User bisa menambah produk baru tanpa meninggalkan halaman utama. Alur kerja tidak terputus.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

   - Dengan CSRF (Cross-Site Request Forgery) Protection. Setiap permintaan POST yang user kirim (untuk login, register, tambah produk, dll.) selalu menyertakan CSRF Token. Di Garuda Gear, saya membuat fungsi JavaScript getCookie('csrftoken') untuk mengambil token dari cookie, lalu menyertakannya dalam header permintaan fetch. Ini membuktikan kepada Django bahwa permintaan tersebut sah dan berasal dari website saya sendiri, bukan dari situs lain yang mencoba meniru aksi user.
   - Semua data yang dikirim melalui AJAX tetap divalidasi oleh form Django di backend (UserCreationForm untuk register, ProductForm untuk produk). Jika ada data yang tidak valid (misalnya, username sudah ada), view akan mengembalikan JsonResponse yang berisi pesan error, dan JavaScript akan menampilkannya kepada user.
   - Untuk proses otentikasi, view AJAX tetap memanggil fungsi authenticate() dan login() bawaan Django.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

   - Website terasa modern dan cepat. Menghapus produk dan melihatnya langsung hilang dari daftar, atau filter dan melihat hasilnya muncul seketika.
   - User tidak perlu lagi menunggu halaman reload setiap kali melakukan aksi kecil. Proses seperti mengisi form yang salah tidak lagi "menghukum" pengguna dengan me-reload halaman dan mungkin mengosongkan semua field. Error muncul di tempat, dan bisa langsung diperbaiki.
   - Jika user sedang melihat-lihat produk di halaman 3, lalu ingin menambahkan produk baru, user bisa melakukannya lewat modal dan setelah selesai tetap berada di halaman 3.
   - Dengan kombinasi loading spinner, pesan error di form, dan notifikasi toast, user selalu tahu apa yang sedang terjadi. Jika sistem sedang bekerja, berhasil, atau error, semua  itu diberitahu secara visual.