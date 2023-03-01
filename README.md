# Aplikasi Ping Pong Messanger dengan RabbitMQ

## # Setup Projects

Projects ini dibuat dengan menggunakan <b>PyCharm</b>. Untuk melakukan setup project cukup lakukan clone pada
menu <code>Git > Clone</code> pada aplikasi <b>PyCharm</b> yang anda gunakan. Kemudian masukkan link URL yang ada di
bawah ini.

```
https://github.com/twentiecker/pubsub-rabbitmq-python.git
```

## # Setup RabbitMQ Libraries

```
pip install pika
```

Library ini digunakan untuk melakukan komunikasi dengan RabbitMQ melalui protocol <b>AMQP 0-9-1</b>. <br/>
Dokumentasi lengkap mengenai library <b>pika</b> dapat dilihat pada link berikut: https://pika.readthedocs.io/en/stable/

## # Setup Build Application Module

### Setup PyInstaller Libraries

```
pip install pyinstaller
```

Library ini digunakan untuk membuat executable file dari file python yang sudah kita buat. <br/>
Dokumentasi lengkap mengenai library <b>pyinstaller</b> dapat dilihat pada link
berikut: https://pyinstaller.org/en/stable/

### Build Application

Proses build application bisa dilakukan dengan beberapa cara. Pada project ini akan disampaikan dua cara dalam melakukan
proses build application.

#### General Command

```
pyinstaller pubsub_uts.pyw
```

#### Single File Executable

```
pyinstaller -F pubsub_uts.pyw
```

File aplikasi yang berhasil digenerate oleh pyinstaller akan ditempatakan pada folder <code>dist</code>

## # Setup Local Environment

### Setup Dotenv Libraries

```
pip install python-dotenv
```

Library ini digunakan untuk membaca file local environment yang ada pada source code. <br/>
Dokumentasi lengkap mengenai libray ini dapat dilihat pada link
berikut: https://github.com/theskumar/python-dotenv#getting-started

### Setup File .env

```
# konfigurasi RabbitMQ
host=your_host
port=your_port
user=your_username
pass=your_password
vhost=your_virtual_host
```

Buatlah file baru di posisi root source code dengan nama <code>.env</code>. Kemudian copy kode di atas dan ganti
nilai <code>your_host</code>, <code>your_port</code>, <code>your_username</code>, <code>your_password</code>, dan <code>
your_virtual_host</code> sesuai dengan konfigurasi RabbitMQ yang akan digunakan.