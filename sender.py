import os
import json
import requests
from logger import setup_logger
from quotes import get_random_quote

logger = setup_logger("app_log")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

# Muat template pesan dari file
with open("message_template.txt", "r", encoding="utf-8") as f:
    message_template = f.read()

def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"❌ Gagal membaca file kontak: {e}")
        return []

def send_whatsapp_message(number: str, name: str):
    try:
        name = name.strip() if name else "Pengguna"
        quote = get_random_quote()

        # Masukkan nama dan quote ke dalam template
        personalized_message = message_template.format(name=name, quote=quote)

        url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {"body": personalized_message}
        }

        response = requests.post(url, headers=headers, json=payload)
        print("Status:", response.status_code)
        print("Response JSON:", response.json())

        if response.status_code == 200:
            logger.info(f"✅ Pesan berhasil dikirim ke {name} ({number})!")
        else:
            logger.error(f"❌ Gagal mengirim pesan ke {name} ({number}): {response.status_code} - {response.text}")

    except Exception as e:
        logger.error(f"⚠️ Terjadi kesalahan saat mengirim ke {name or number}: {e}")

def send_messages_to_all():
    contacts = load_contacts()
    if not contacts:
        logger.error("📭 Tidak ada kontak yang ditemukan.")
        return

    for contact in contacts:
        number = contact.get("number")
        name = contact.get("name", "Pengguna")
        if number:
            send_whatsapp_message(number, name)
        else:
            logger.warning(f"⚠️ Kontak tanpa nomor dilewati: {contact}")
