import tkinter as tk
import pika
import os
from dotenv import load_dotenv
from threading import Thread


# membuat fungsi koneksi server
def connect():
    credential = pika.PlainCredentials(os.getenv("user"), os.getenv("pass"))
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.getenv("host"),
        port=int(os.getenv("port")),
        virtual_host=os.getenv("vhost"),
        credentials=credential
    ))

    # properti GUI publisher
    txt_channel.config(state="normal")
    txt_pesan.config(state="normal")
    txt_tujuan.config(state="normal")
    btn_connect_pub.config(state="disabled")
    btn_pub.config(state="active")
    btn_disconnect_pub.config(state="active")
    lbl_status_pub.config(text="Connected!", state="active")
    lbl_channel.config(state="active")
    lbl_pesan.config(state="active")
    lbl_tujuan.config(state="active")
    lbl_list_pub.config(state="active")

    # properti GUI subscriber
    txt_channel_sub.config(state="normal")
    btn_sub.config(state="active")
    lbl_channel_sub.config(state="active")
    lbl_list_sub.config(state="active")

    return connection


# membuat fungsi kirim pesan
def kirim():
    channel = connect().channel()
    channel.queue_declare(
        queue=txt_channel.get(),
        durable=True,
        exclusive=False,
        auto_delete=False,
        arguments=None
    )
    channel.basic_publish(
        exchange='',
        routing_key=txt_tujuan.get(),  # nama queue
        body=txt_pesan.get(),  # isi pesan dari queue yang dikirim
        properties=None
    )

    # properti GUI publisher
    txt_list_pub.config(state="normal")
    txt_list_pub.insert(tk.INSERT, f""" [x] "{txt_pesan.get()}" sent to {txt_tujuan.get()}\n""")
    txt_list_pub.config(state="disabled")
    txt_pesan.delete(0, tk.END)


# membuat fungsi terima pesan
def terima():
    def subscriber():
        def callback(ch, method, properties, body):
            txt_list_sub.config(state="normal")
            txt_list_sub.insert(tk.INSERT, f""" [x] Received "{body.decode()}" from {txt_channel_sub.get()}\n""")
            txt_list_sub.config(state="disabled")

        channel = connect().channel()
        channel.queue_declare(
            queue=txt_channel_sub.get(),
            durable=True,
            exclusive=False,
            auto_delete=False,
            arguments=None
        )
        channel.basic_qos(prefetch_count=1)  # hanya akan memberikan satu tugas dulu sampe selesai
        channel.basic_consume(
            queue=txt_channel_sub.get(),  # nama queue
            on_message_callback=callback,  # memanggil fungsi callback
            auto_ack=True
        )
        channel.start_consuming()  # bersifat standby

    # properti GUI subscriber
    txt_list_sub.config(state="normal")
    txt_list_sub.insert(tk.INSERT, f"""Menunggu pesan masuk dari "{txt_channel_sub.get()}"...\n""")
    txt_list_sub.config(state="disabled")

    # mengatur threading
    terima_thread = Thread(target=subscriber)
    terima_thread.setDaemon(True)
    terima_thread.start()


# membuat fungsi disconnect
def disconnect():
    connect().close()  # menutup koneksi setelah mengirim pesan

    # properti GUI publisher
    txt_channel.delete(0, tk.END)
    txt_channel.config(state="disabled")
    txt_pesan.delete(0, tk.END)
    txt_pesan.config(state="disabled")
    txt_tujuan.delete(0, tk.END)
    txt_tujuan.config(state="disabled")
    txt_list_pub.config(state="normal")
    txt_list_pub.delete('1.0', tk.END)
    txt_list_pub.config(state="disabled")
    btn_connect_pub.config(state="active")
    btn_pub.config(state="disabled")
    btn_disconnect_pub.config(state="disabled")
    lbl_status_pub.config(text="Disconnected!", state="disabled")
    lbl_channel.config(state="disabled")
    lbl_pesan.config(state="disabled")
    lbl_tujuan.config(state="disabled")
    lbl_list_pub.config(state="disabled")

    # properti GUI subscriber
    txt_channel_sub.delete(0, tk.END)
    txt_channel_sub.config(state="disabled")
    txt_list_sub.config(state="normal")
    txt_list_sub.delete('1.0', tk.END)
    txt_list_sub.config(state="disabled")
    btn_sub.config(state="disabled")
    lbl_channel_sub.config(state="disabled")
    lbl_list_sub.config(state="disabled")


load_dotenv()
temp_exchange = None
temp_queue = None
temp_channel = None

# membuat window
app = tk.Tk()
app.geometry("875x610")
app.title("Aplikasi Publisher/Subscriber RabbitMQ")

# ******************************************************************************************************************** #
# GUI publisher                                                                                                        #
# ******************************************************************************************************************** #
# membuat label dan text channel
lbl_channel = tk.Label(text="Channel", state="disabled")
lbl_channel.place(x=10, y=60)
txt_channel = tk.Entry(state="disabled", )
txt_channel.place(x=10, y=85)

# membuat label dan text tujuan
lbl_tujuan = tk.Label(text="Tujuan", state="disabled")
lbl_tujuan.place(x=10, y=105)
txt_tujuan = tk.Entry(state="disabled", )
txt_tujuan.place(x=10, y=130)

# membuat label dan text pesan
lbl_pesan = tk.Label(text="Pesan", state="disabled")
lbl_pesan.place(x=150, y=105)
txt_pesan = tk.Entry(state="disabled", width=43)
txt_pesan.place(x=153, y=130)

# membuat label dan daftar pesan terkirim
lbl_list_pub = tk.Label(text="Daftar Pesan Terkirim", state="disabled")
lbl_list_pub.place(x=10, y=195)
txt_list_pub = tk.Text(height=20, width=50, state="disabled")
txt_list_pub.place(x=10, y=220)

# membuat status koneksi
lbl_status_pub = tk.Label(text="Disconnected!", state="disabled")
lbl_status_pub.place(x=70, y=20)

# membuat tombol connect
btn_connect_pub = tk.Button(text="Connect", command=connect)
btn_connect_pub.place(x=10, y=20)

# membuat tombol kirim data
btn_pub = tk.Button(text="Publish", command=kirim, state="disabled")
btn_pub.place(x=10, y=160)

# membuat tombol disconnect
btn_disconnect_pub = tk.Button(text="Disconnect", command=disconnect, state="disabled")
btn_disconnect_pub.place(x=10, y=565)

# ******************************************************************************************************************** #
# GUI Subscriber                                                                                                       #
# ******************************************************************************************************************** #
# membuat label dan text exchange
lbl_channel_sub = tk.Label(text="Channel", state="disabled")
lbl_channel_sub.place(x=10 + 450, y=60)
txt_channel_sub = tk.Entry(state="disabled", width=67)
txt_channel_sub.place(x=10 + 450, y=85)

# membuat label dan daftar pesan diterima
lbl_list_sub = tk.Label(text="Daftar Pesan Diterima", state="disabled")
lbl_list_sub.place(x=10 + 450, y=195)
txt_list_sub = tk.Text(height=20, width=50, state="disabled")
txt_list_sub.place(x=10 + 450, y=220)

# membuat tombol terima data
btn_sub = tk.Button(text="Subscribe", command=terima, state="disabled")
btn_sub.place(x=10 + 450, y=160)

# menjalankan window
app.mainloop()
