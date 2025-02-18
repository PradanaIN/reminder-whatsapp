import pywhatkit
import pyautogui
import pyperclip
import time
from config import group_id, message
from logger import setup_logger

# Setup logger
logger = setup_logger("app_log")

def copy_message_to_clipboard():
    # Menyalin pesan ke clipboard
    pyperclip.copy(message)
    logger.info("Pesan disalin ke clipboard.")

def send_whatsapp_message():
    try:
        # Mengirim pesan ke WhatsApp Web
        pywhatkit.sendwhatmsg_to_group_instantly(group_id, " ")  # Mengirim pesan kosong untuk membuka chat
        time.sleep(1)  # Tunggu agar WhatsApp Web terbuka
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
        logger.info("Pesan berhasil dikirim ke grup!")
    except pywhatkit.exceptions.PyWhatKitException as e:
        logger.error(f"PyWhatKit error: {e}")
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat mengirim pesan: {e}")

