from dotenv import load_dotenv
import os

load_dotenv()

group_id = os.getenv("GROUP_ID", "DEFAULT_GROUP_ID")  # Fallback jika tidak ditemukan
message = os.getenv("MESSAGE", "Pesan default jika tidak ada di .env")
