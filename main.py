import datetime
import pytz
import asyncio
from timer import countdown_timer
from sender import send_messages_to_all
from scheduler import scheduler

# Zona waktu Asia/Makassar
TIMEZONE = pytz.timezone("Asia/Makassar")

async def send_whatsapp_messages():
    print("Mengirim pesan ke kontak WhatsApp...")
    send_messages_to_all()  # Kirim pesan ke semua kontak satu per satu
    print("✅ Selesai mengirim semua pesan.")

async def run_daily():
    while True:
        now = datetime.datetime.now(TIMEZONE)
        weekday = now.weekday()  # Senin = 0, Selasa = 1, ..., Jumat = 4

        if scheduler():  # Cek apakah hari ini adalah hari kerja
            # Tentukan jam pengiriman berdasarkan hari
            if weekday in [0, 1, 2, 3]:  # Senin - Kamis
                target_time = now.replace(hour=15, minute=58, second=0, microsecond=0)
            elif weekday == 4:  # Jumat
                target_time = now.replace(hour=16, minute=28, second=0, microsecond=0)
            else:
                print("Hari ini bukan hari kerja. Tidak mengirim pesan.")
                await asyncio.sleep(72000)  # Tunggu 20 jam sebelum memeriksa ulang
                continue

            # Tunggu sampai waktu pengiriman
            await countdown_timer(target_time)
            await send_whatsapp_messages()

        else:
            print("Hari ini bukan hari kerja. Tidak mengirim pesan.")

        # Tambahkan log bahwa program masih berjalan
        print("⏳ Program masih berjalan, menunggu proses berikutnya dalam 20 jam...")

        # Tunggu hingga keesokan harinya sebelum menjalankan loop lagi
        await asyncio.sleep(72000)  # Tunggu 20 jam sebelum mengirim pesan lagi

if __name__ == "__main__":
    asyncio.run(run_daily())
