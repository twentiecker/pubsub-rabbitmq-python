# Aplikasi Broadcast Data dengan RabbitMQ

## Setup Projects

Projects ini dibuat dengan menggunakan <b>PyCharm</b>. Untuk melakukan setup project cukup lakukan clone pada
menu <code>Git > Clone</code> pada aplikasi <b>PyCharm</b> yang anda gunakan. Kemudian masukkan link URL yang ada di
bawah ini.

```
https://github.com/twentiecker/broadcaster-rabbitmq-python.git
```

## Setup RabbitMQ libraries

```
pip install pika
```

Library ini digunakan untuk melakukan komunikasi dengan RabbitMQ melalui protocol <b>AMQP 0-9-1</b>. <br/>
Dokumentasi lengkap mengenai library <b>pika</b> dapat dilihat pada link berikut: https://pika.readthedocs.io/en/stable/

## Setup PyInstaller libraries

```
pip install pyinstaller
```

Library ini digunakan untuk membuat executable file dari file python yang sudah kita buat. <br/>
Dokumentasi lengkap mengenai library <b>pyinstaller</b> dapat dilihat pada link
berikut: https://pyinstaller.org/en/stable/

## Setup Local Environment

### Setup Dotenv libraries

```
pip install python-dotenv
```

Library ini digunakan untuk membaca file local environment yang ada pada source code. <br/>
Dokumentasi lengkap mengenai libray ini dapat dilihat pada link
berikut: https://github.com/theskumar/python-dotenv#getting-started

### Setup file .env

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