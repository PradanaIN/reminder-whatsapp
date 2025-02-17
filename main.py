import datetime
import time
from timer import countdown_timer
from whatsapp import send_whatsapp_message, copy_message_to_clipboard
from config import message

def send_whatsapp_group_message():
    # Fungsi utama untuk mengirim pesan ke grup WhatsApp
    print("Mengirim pesan ke grup WhatsApp...")
    current_time = datetime.datetime.now()
    target_time = current_time.replace(hour=18, minute=34, second=0, microsecond=0)

    countdown_timer(target_time)
    
    copy_message_to_clipboard()
    send_whatsapp_message()

def run_daily():
    # Menjalankan pengiriman pesan harian secara terus-menerus
    while True:
        send_whatsapp_group_message()
        print("Pesan berhasil dikirim. Menunggu 24 jam hingga pengiriman pesan berikutnya...")
        countdown_timer(datetime.datetime.now() + datetime.timedelta(days=1))

# Jalankan fungsi utama
if __name__ == "__main__":
    run_daily()
