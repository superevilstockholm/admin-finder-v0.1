# Admin Finder v0.1

Admin Finder adalah sebuah tool yang digunakan untuk mencari direktori admin pada sebuah website dengan menggunakan metode HTTP request asinkron. Tool ini sangat efisien dalam melakukan pencarian karena hanya memerlukan satu thread untuk menjalankan seluruh proses pencarian, berkat penggunaan library `aiohttp` dan `asyncio`. 

## Fitur

- **Pencarian Cepat dan Efisien:** Admin Finder menggunakan teknik asinkron dengan `aiohttp` untuk melakukan request HTTP ke banyak URL sekaligus, tetapi hanya memerlukan satu thread untuk menjalankannya. Ini membuatnya lebih ringan dan cepat dibandingkan metode pencarian tradisional yang menggunakan banyak thread.
  
- **Penggunaan User-Agent Acak:** Setiap kali melakukan request ke server, Admin Finder akan memilih User-Agent secara acak dari file `useragent.json`. Hal ini untuk memastikan bahwa tool ini dapat menghindari pemblokiran yang mungkin terjadi jika terlalu banyak request menggunakan User-Agent yang sama.

- **Mudah Digunakan:** Anda hanya perlu memasukkan URL utama dari situs yang ingin Anda cari, dan tool ini akan otomatis mencoba berbagai direktori admin yang ada dalam `adminFinder.txt` untuk mencari tahu apakah ada yang berhasil ditemukan.

## Keunggulan

- **Menggunakan Satu Thread:** Meskipun memeriksa banyak URL, Admin Finder hanya menggunakan satu thread berkat penggunaan `aiohttp` dan `asyncio`. Ini membuatnya jauh lebih efisien dibandingkan tool lain yang mungkin menggunakan banyak thread atau proses untuk melakukan pencarian serupa.

- **Mudah Diintegrasikan dan Dikonfigurasi:** Tool ini mudah diintegrasikan dengan proyek lain dan Anda dapat dengan mudah mengganti wordlist (`adminFinder.txt`) atau daftar User-Agent (`useragent.json`) sesuai dengan kebutuhan Anda.

- **Pengelolaan User-Agent Dinamis:** Tool ini secara otomatis mengubah User-Agent setelah setiap request yang gagal, yang membantu menghindari pemblokiran atau pembatasan dari server.

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/superevilstockholm/admin-finder-v0.1.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan script Python:
   ```bash
   python adminFinder.py
   ```
4. Masukkan URL yang ingin Anda periksa.
5. Admin Finder akan mencoba berbagai URL dan menampilkan hasilnya jika ditemukan direktori admin yang valid (status code 200).

## Contoh:
   ```bash
   Insert URL: http://example.com
   Found [200]: http://example.com/admin
   Found [200]: http://example.com/administrator
   Url yang berhasil: ['http://example.com/admin', 'http://example.com/administrator']
   ```
