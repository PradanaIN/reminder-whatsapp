import datetime
import pytz
import asyncio
from timer import countdown_timer
from sender import send_messages_to_all
from scheduler import scheduler

TIMEZONE = pytz.timezone("Asia/Makassar")

async def send_whatsapp_messages():
    print("Mengirim pesan ke kontak WhatsApp...")
    send_messages_to_all()
    print("✅ Selesai mengirim semua pesan.")

async def run_daily():
    while True:
        now = datetime.datetime.now(TIMEZONE)
        weekday = now.weekday()  # Senin=0

        if await scheduler():
            if weekday in [0, 1, 2, 3]:  # Senin-Kamis
                target_time = now.replace(hour=21, minute=56, second=00, microsecond=0)
            elif weekday == 4:  # Jumat
                target_time = now.replace(hour=16, minute=58, second=30, microsecond=0)
            else:
                print("Hari ini bukan hari kerja. Tidak mengirim pesan.")
                await asyncio.sleep(72000)
                continue

            await countdown_timer(target_time)
            await send_whatsapp_messages()
        else:
            print("Hari ini bukan hari kerja. Tidak mengirim pesan.")

        print("⏳ Program masih berjalan, menunggu proses berikutnya dalam 20 jam...")
        await asyncio.sleep(72000)

if __name__ == "__main__":
    asyncio.run(run_daily())
