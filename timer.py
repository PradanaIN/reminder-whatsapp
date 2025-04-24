import asyncio
import datetime
import pytz  # Tambahkan pustaka pytz untuk timezone

async def countdown_timer(target_time: datetime.datetime):
    tz = pytz.timezone("Asia/Makassar")  # Sesuaikan dengan zona waktu yang digunakan di main.py
    current_time = datetime.datetime.now(tz)  # Pastikan menggunakan timezone yang sama

    if current_time > target_time:
        target_time += datetime.timedelta(days=1)
    
    time_to_wait = (target_time - current_time).total_seconds()

    while time_to_wait > 0:
        hours, remainder = divmod(int(time_to_wait), 3600)
        mins, secs = divmod(remainder, 60)
        print(f"Waktu sampai pengiriman berikutnya: {hours} jam {mins} menit {secs} detik", end='\r')
        await asyncio.sleep(1)
        time_to_wait -= 1
