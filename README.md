## WhatsApp Daily Reminder

WhatsApp Daily Reminder is a Python script that sends daily reminders to a specified WhatsApp group. The script calculates the time left until the next reminder is scheduled and sends a message once a day. The message includes important reminders and quotes, and the script automatically waits for 24 hours before sending the next reminder. It also takes into account holidays and weekends to ensure reminders are sent only on workdays.

**How it works** :

- The script checks if today is a workday and ensures that the date is not a weekend or holiday.
- At the scheduled time, the message will be sent to the specified WhatsApp group.
- After sending the message, the script waits for 24 hours before sending the next reminder.

### Requirements

To run the script, make sure you have the following Python libraries installed:

- **`pywhatkit`**: For sending WhatsApp messages.
- **`pyautogui`**: For automating keyboard actions.
- **`pyperclip`**: For clipboard management.

* **`python-dotenv`** : For managing environment variables such as WhatsApp group ID and message content.
* **`pytz`** : For handling timezone conversion and getting the current time in the correct timezone (WITA in this case).
* **`asyncio`** : For running asynchronous tasks like waiting for the next scheduled message.

### Features

- Sends a daily reminder message to a specified WhatsApp group.
- Calculates the time left until the next scheduled reminder based on the current time and the target time.
- Ensures reminders are not sent on weekends, national holidays, or shared leave days.
- Uses `pywhatkit` to send messages via WhatsApp Web.
- Automatically waits for 24 hours before sending the next reminder.
- Allows for a customizable message with important reminders and motivational quotes.
- Supports the use of timezones (set to WITA - UTC+8).

### Usage

1. Create a `.env` file in your project directory and include the following:

   ```
   GROUP_ID=<your-whatsapp-group-id>
   MESSAGE=<your-custom-message-here>
   ```

   Make sure to replace `<your-whatsapp-group-id>` with your actual WhatsApp group ID and `<your-custom-message-here>` with the message you'd like to send.

2. Open `main.py` and set the desired time for the reminder in the script (e.g., 7:00 PM).
3. Replace the WhatsApp group ID and message with your own in the script.
4. Install the necessary dependencies by running the following command:

   ```bash
   pip install pywhatkit pyautogui pyperclip python-dotenv pytz
   ```

5. Run the script using Python:

   ```bash
    python main.py
   ```

### Client

    Badan Pusat Statistik Kabupaten Bulungan
