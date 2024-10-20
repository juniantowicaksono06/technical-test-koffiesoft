## Tes KoffieSoft

Untuk menjalankan program ini silahkan install python terlebih dahulu, disini saya menggunakan python versi 3.10.6 dan sistem operasi Windows 11

Lalu bisa menginstall package python yang diperlukan dengan menjalankan perintah:

```bash
pip install -r requirements.txt
```

Jika sudah silahkan copy env berikut dan buat file .env dan paste ke file tersebut

```bash
DB_URL=mysql+pymysql://root:@localhost/app-1

JWT_SECRET_KEY=ABCD1234

PORT=8000
```

Sesuaikan dengan koneksi database anda, disini saya menggunakan MySQL

lalu bila sudah, silahkan menjalankan migrasi databasenya menggunakan perintah

```bash
alembic upgrade head
```

Lalu bisa menjalankan aplikasinya dengan menggunakan

```bash
python main.py
```

Kemudian bisa buka aplikasinya di browser dengan mengetikkan
```bash
http://localhost:8000/
```