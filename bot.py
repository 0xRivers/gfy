import schedule
import time
from datetime import datetime

# Function to simulate sending a Nostr message using nos2x
# This assumes the nos2x extension is available in the browser environment where the user is logged in
# This script now only logs the action since nos2x cannot be directly invoked from Python

def send_nostr_message(message):
    try:
        # Simulate sending the event through a nos2x integration mechanism
        print(f"Sending event to nos2x: {message}")
        print("(nos2x would sign and send the event here)")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Define the behavior for weekdays and weekends
def post_message():
    today = datetime.now()
    if today.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        send_nostr_message("gfy fiatjaf")
    else:
        send_nostr_message("GM fiatjaf")

# Schedule the bot to run every other day
schedule.every(2).days.at("08:00").do(post_message)  # Adjust time as needed

# Keep the script running to execute scheduled tasks
print("Nostr bot is running with nos2x...")
while True:
    schedule.run_pending()
    time.sleep(1)
