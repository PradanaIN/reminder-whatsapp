import pywhatkit
import pyautogui
import pyperclip
import time
from config import group_id, message

def copy_message_to_clipboard():
    # Menyalin pesan ke clipboard 
    pyperclip.copy(message)

def send_whatsapp_message():
    # Mengirim pesan ke WhatsApp Web
    pywhatkit.sendwhatmsg_to_group_instantly(group_id, " ")  # Mengirim pesan kosong untuk membuka chat
    time.sleep(1)  # Tunggu agar WhatsApp Web terbuka
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("enter")
    print("Pesan berhasil dikirim ke grup!")
