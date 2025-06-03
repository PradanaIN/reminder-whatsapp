import datetime
from logger import setup_logger

logger = setup_logger("app_log")

LIBURAN = {
    "2025-01-01", "2025-01-27", "2025-01-29", "2025-03-29", "2025-03-31",
    "2025-04-01", "2025-04-18", "2025-04-20", "2025-05-01", "2025-05-12",
    "2025-05-29", "2025-06-01", "2025-06-06", "2025-06-27", "2025-08-17",
    "2025-09-05", "2025-12-25"
}
CUTI_BERSAMA = {
    "2025-01-28", "2025-03-28", "2025-04-02", "2025-04-03", "2025-04-04",
    "2025-04-07", "2025-05-13", "2025-05-30", "2025-06-09", "2025-12-26"
}

async def scheduler():
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    logger.info(f"Checking if today ({today_str}) is a workday.")

    if datetime.datetime.today().weekday() >= 5 or today_str in LIBURAN or today_str in CUTI_BERSAMA:
        logger.info(f"Hari ini ({today_str}) adalah hari libur atau cuti bersama. Tidak mengirim pesan.")
        return False

    logger.info(f"Hari ini adalah hari kerja. Pesan akan dikirim.")
    return True
