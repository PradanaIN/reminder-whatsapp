from dotenv import load_dotenv
import os

load_dotenv()  # Memuat file .env

group_id = os.getenv("GROUP_ID")  # Mendapatkan variabel GROUP_ID
message = os.getenv("MESSAGE")    # Mendapatkan variabel MESSAGE
