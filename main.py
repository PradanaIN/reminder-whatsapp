import pywhatkit
import time
import pyautogui
import pyperclip
import datetime

# ID Grup WhatsApp
group_id = "JpJNKT3hZZZGg5LSvWh9FT"

# Pesan dengan emoji
message = """🌟 *PENGINGAT HARIANMU!* 🏡✨

🔔 Waktu untuk bersiap pulang, tetapi sebelum itu, periksa beberapa hal penting berikut:

📝 *Absen Pulang*
Jangan lupa untuk absen sebelum meninggalkan tempat kerja.

⚡ *Periksa Perangkat Elektronik*
Matikan semua perangkat yang tidak terpakai, seperti komputer, lampu, dan alat elektronik lainnya, untuk efisiensi energi.

_"Discipline is management action to enforce organization standards"_ — Keith Davis

Terima kasih atas kerja kerasmu hari ini. Sampai jumpa besok dengan semangat yang baru! 💪😊
"""

# Fungsi untuk mengirim pesan ke grup WhatsApp
def send_whatsapp_group_message():
    print("Mengirim pesan ke grup WhatsApp...")

    # Buka WhatsApp Web dengan `pywhatkit` pada waktu yang diinginkan (17:15 WITA)
    current_time = datetime.datetime.now()
    target_time = current_time.replace(hour=17, minute=38, second=0, microsecond=0)

    # Hitung selisih waktu jika target waktu sudah lewat
    if current_time > target_time:
        target_time += datetime.timedelta(days=1)  # Kirim pesan besok

    time_to_wait = (target_time - current_time).total_seconds()

    # Penghitung mundur (hanya satu kali loop)
    while time_to_wait > 0:
        hours, remainder = divmod(int(time_to_wait), 3600)  # Menghitung jam
        mins, secs = divmod(remainder, 60)  # Menghitung menit dan detik
        print(f"Waktu sampai pengiriman berikutnya: {hours} jam {mins} menit {secs} detik", end='\r')
        time.sleep(1)
        time_to_wait -= 1

    # Setelah waktu habis, kirim pesan
    # Gunakan `pyperclip` untuk menyalin teks dengan emoji ke clipboard
    pyperclip.copy(message)

    # Buka WhatsApp Web pada waktu yang ditentukan dan kirimkan pesan
    pywhatkit.sendwhatmsg_to_group_instantly(group_id, " ")  # Mengirim pesan kosong untuk membuka chat

    time.sleep(3)  # Tunggu agar WhatsApp Web terbuka

    # Gunakan `pyautogui` untuk menempelkan pesan
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # Tekan "Enter" untuk mengirim pesan
    pyautogui.press("enter")
    
    print("Pesan berhasil dikirim ke grup!")

# Fungsi utama untuk menjalankan program secara terus-menerus
def run_daily():
    while True:
        send_whatsapp_group_message()
        # Setelah mengirim pesan, tunggu 24 jam sebelum mengirim pesan berikutnya
        print("Pesan berhasil dikirim. Menunggu 24 jam hingga pengiriman pesan berikutnya...")

        # Hitung mundur selama 24 jam (86400 detik)
        time_to_wait = 86400  # 24 jam dalam detik
        while time_to_wait > 0:
            hours, remainder = divmod(int(time_to_wait), 3600)  # Menghitung jam
            mins, secs = divmod(remainder, 60)  # Menghitung menit dan detik
            print(f"Waktu sampai pengiriman berikutnya: {hours} jam {mins} menit {secs} detik", end='\r')
            time.sleep(1)
            time_to_wait -= 1

# Jalankan fungsi utama
run_daily()
