## WhatsApp Daily Reminder

WhatsApp Daily Reminder is a Python script that sends daily reminders to specified WhatsApp contacts. The script calculates the time left until the next reminder is scheduled and sends messages individually to multiple recipients. The message includes important reminders and quotes, and the script automatically waits before sending the next reminder. It also takes into account holidays and weekends to ensure reminders are sent only on workdays.

### How it Works

- The script checks if today is a workday and ensures that the date is not a weekend or holiday.
- At the scheduled time, the message will be sent to each individual contact in the list.
- After sending all messages, the script ensures that unnecessary tabs are closed to optimize performance.
- The script waits for 20 hours before checking and sending the next batch of reminders.

### Requirements

To run the script, make sure you have the following Python libraries installed:

- **`pywhatkit`** : For sending WhatsApp messages.
- **`pyautogui`** : For automating keyboard actions.
- **`pyperclip`** : For clipboard management.
- **`python-dotenv`** : For managing environment variables such as WhatsApp contacts and message content.
- **`pytz`** : For handling timezone conversion and getting the current time in the correct timezone (WITA in this case).
- **`asyncio`** : For running asynchronous tasks like waiting for the next scheduled message.

### Features

- Sends a daily reminder message to multiple individual WhatsApp contacts.
- Calculates the time left until the next scheduled reminder based on the current time and the target time.
- Ensures reminders are not sent on weekends, national holidays, or shared leave days.
- Uses `pywhatkit` to send messages via WhatsApp Web without requiring manual intervention.
- Closes unnecessary WhatsApp Web tabs after sending messages to optimize performance.
- Automatically waits for 20 hours before sending the next reminder.
- Allows for a customizable message with important reminders and motivational quotes.
- Supports the use of timezones (set to WITA - UTC+8).

### Usage

1. Create a `contacts.json` file in your project directory and include the contacts in the following format:
   ```json
   [
     { "name": "Budi", "number": "+6281234567890" },
     { "name": "Ani", "number": "+6289876543210" }
   ]
   ```
2. Create a `.env` file and include the following:
   ```
   MESSAGE="\n\nSebelum meninggalkan tempat kerja, pastikan sudah memeriksa hal-hal berikut:\n\n📝 *Absen Pulang*\nJangan lupa absen sebelum pulang, ya!!!!\n\n⚡ *Periksa Perangkat Elektronik*\nPastikan komputer, lampu, dan perangkat lainnya sudah dimatikan untuk menghemat energi.\n\n> _\"Discipline is management action to enforce organization standards\"_ — Keith Davis\n\nTerima kasih atas kerja kerasmu hari ini. Sampai jumpa besok dengan semangat yang baru! 💪😊"
   ```
3. Install the necessary dependencies by running the following command:
   ```bash
   pip install pywhatkit pyautogui pyperclip python-dotenv pytz asyncio
   ```
4. Run the script using Python:
   ```bash
   python main.py
   ```

### Example Message

```
Halo, selamat sore Novanni Indi Pradana!

Sebelum meninggalkan tempat kerja, pastikan sudah memeriksa hal-hal berikut:

📝 Absen Pulang
Jangan lupa absen sebelum pulang, ya!!!!

⚡ Periksa Perangkat Elektronik
Pastikan komputer, lampu, dan perangkat lainnya sudah dimatikan untuk menghemat energi.

> "Discipline is management action to enforce organization standards" — Keith Davis

Terima kasih atas kerja kerasmu hari ini. Sampai jumpa besok dengan semangat yang baru! 💪😊
```

### Schedule

- **Monday - Thursday** : Messages are sent at **15:55 WITA** .
- **Friday** : Messages are sent at **16:25 WITA** .

### Client

Badan Pusat Statistik Kabupaten Bulungan
