import asyncio
import datetime

async def countdown_timer(target_time: datetime.datetime):
    current_time = datetime.datetime.now()
    if current_time > target_time:
        target_time += datetime.timedelta(days=1)
    time_to_wait = (target_time - current_time).total_seconds()

    while time_to_wait > 0:
        hours, remainder = divmod(int(time_to_wait), 3600)
        mins, secs = divmod(remainder, 60)
        print(f"Waktu sampai pengiriman berikutnya: {hours} jam {mins} menit {secs} detik", end='\r')
        await asyncio.sleep(1)  # Menggunakan async sleep
        time_to_wait -= 1  # Pindahkan setelah sleep
