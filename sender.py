import pywhatkit
import pyautogui
import pyperclip
import time
import json
from config import message
from logger import setup_logger

logger = setup_logger("app_log")

# Load daftar kontak dari file JSON
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"Error membaca kontak: {e}")
        return []

def send_whatsapp_message(number, name, first_time=False):
    try:
        personalized_message = f"Halo, selamat sore {name}!\n\n" + message
        pyperclip.copy(personalized_message)

        if first_time:
            # Hanya buka WhatsApp Web sekali
            pywhatkit.sendwhatmsg_instantly(number, " ")
            time.sleep(5)  # Tunggu WhatsApp Web terbuka
        else:
            # Buka search bar
            pyautogui.hotkey("ctrl", "alt", "/")
            time.sleep(1)

            # Ketik nomor atau nama kontak
            pyautogui.write(number)
            time.sleep(1)

            # Pilih kontak yang muncul pertama
            pyautogui.press("enter")
            time.sleep(1)

        # Paste & kirim pesan
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

        logger.info(f"Pesan berhasil dikirim ke {name} ({number})!")
    except Exception as e:
        logger.error(f"Terjadi kesalahan saat mengirim ke {name}: {e}")

def close_whatsapp_tabs():
    logger.info("Menutup tab WhatsApp Web...")
    pyautogui.hotkey("ctrl", "w")  # Menutup tab saat ini

def send_messages_to_all():
    contacts = load_contacts()
    if not contacts:
        logger.error("Tidak ada kontak yang ditemukan.")
        return

    first_time = True
    for contact in contacts:
        send_whatsapp_message(contact["number"], contact["name"], first_time)
        first_time = False  
        time.sleep(1.5)  # Jeda singkat untuk menghindari spam

    close_whatsapp_tabs()  # **Tutup WhatsApp Web setelah selesai**