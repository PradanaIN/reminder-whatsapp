import datetime
import pytz
from timer import countdown_timer
from sender import send_whatsapp_message, copy_message_to_clipboard
from scheduler import scheduler  
import asyncio  # Pastikan asyncio diimport

async def send_whatsapp_group_message():
    # Fungsi utama untuk mengirim pesan ke grup WhatsApp
    print("Mengirim pesan ke grup WhatsApp...")
    current_time = datetime.datetime.now(pytz.timezone("Asia/Makassar"))
    target_time = current_time.replace(hour=17, minute=45, second=0, microsecond=0)

    await countdown_timer(target_time)  # Menunggu hingga waktu target tercapai
    
    copy_message_to_clipboard()
    send_whatsapp_message()

async def run_daily():
    # Menjalankan pengiriman pesan harian secara terus-menerus
    while True:
        if scheduler():  # Memanggil fungsi scheduler untuk pengecekan
            await send_whatsapp_group_message()  # Panggil fungsi async dengan await
            print("Pesan berhasil dikirim. Menunggu 24 jam hingga pengiriman pesan berikutnya...")
        else:
            print("Pesan tidak dikirim hari ini. Menunggu 24 jam...")
        
        await countdown_timer(datetime.datetime.now() + datetime.timedelta(days=1))  # Tunggu selama 24 jam

# Jalankan fungsi utama
if __name__ == "__main__":
    asyncio.run(run_daily())  # Menjalankan fungsi async dengan asyncio.run
