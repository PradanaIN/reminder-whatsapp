import datetime
from logger import setup_logger

# Setup logger
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

def scheduler():
    # Fungsi untuk memeriksa apakah hari ini adalah hari kerja dan bukan hari libur atau cuti bersama.
    today = datetime.datetime.now()
    today_str = today.strftime("%Y-%m-%d")

    logger.info(f"Checking if today ({today_str}) is a workday.")

    # Cek apakah hari ini adalah Sabtu (5) atau Minggu (6)
    if today.weekday() >= 5:  # Sabtu (5) atau Minggu (6)
        logger.info("Hari ini adalah akhir pekan. Tidak mengirim pesan.")
        return False

    # Cek apakah hari ini adalah salah satu hari libur nasional
    if today_str in LIBURAN:
        logger.info(f"Hari ini adalah hari libur nasional ({today_str}). Tidak mengirim pesan.")
        return False

    # Cek apakah hari ini adalah salah satu hari cuti bersama
    if today_str in CUTI_BERSAMA:
        logger.info(f"Hari ini adalah cuti bersama ({today_str}). Tidak mengirim pesan.")
        return False

    # Jika hari kerja dan bukan libur
    logger.info(f"Hari ini adalah hari kerja. Pesan akan dikirim.")
    return True