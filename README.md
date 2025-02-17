## WhatsApp Daily Reminder

WhatsApp Daily Reminder is a Python script that sends daily reminders to a specified WhatsApp group. The script calculates the time left until the next reminder is scheduled and sends a message once a day. The message includes important reminders and quotes, and the script automatically waits for 24 hours before sending the next reminder.

### Requirements

To run the script, make sure you have the following Python libraries installed:

- **`pywhatkit`**: For sending WhatsApp messages.
- **`pyautogui`**: For automating keyboard actions.
- **`pyperclip`**: For clipboard management.

You can install these dependencies using the following command:
    ```bash
    pip install pywhatkit pyautogui pyperclip


### Features

- Sends a daily reminder message to a specified WhatsApp group.
- Calculates the time left until the next scheduled reminder.
- Uses `pywhatkit` for sending messages via WhatsApp Web.
- Automatically waits for 24 hours before sending the next reminder.
- Includes a quote and customized reminders with emojis.

### Usage

1. Set the desired time for the reminder in the script (e.g., 7:00 PM).
2. Replace the WhatsApp group ID and message with your own in the script.
3. Install the necessary dependencies by running the following command:
   ```bash
   pip install pywhatkit pyautogui pyperclip
4. Run the script using Python:
   ```bash
    python whatsapp_daily_reminder.py
5. The script will wait until the scheduled time (e.g., 7:00 PM) and then send the reminder message to the WhatsApp group.
6. After the message is sent, the script will wait for 24 hours before sending the next reminder.

### Example Message
    ```
      🌟 *PENGINGAT HARIANMU!* 🏡✨
      
      🔔 Waktu untuk bersiap pulang, tetapi sebelum itu, periksa beberapa hal penting berikut:
      
      📝 *Absen Pulang*
      Jangan lupa untuk absen sebelum meninggalkan tempat kerja.
      
      ⚡ *Periksa Perangkat Elektronik*
      Matikan semua perangkat yang tidak terpakai, seperti komputer, lampu, dan alat elektronik lainnya, untuk efisiensi energi.
      
      _"Discipline is management action to enforce organization standards"_ — Keith Davis
      
      Terima kasih atas kerja kerasmu hari ini. Sampai jumpa besok dengan semangat yang baru! 💪😊
    
    
### Client
    ```
    Badan Pusat Statistik Kabupaten Bulungan

