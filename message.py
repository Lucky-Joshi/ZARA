import pywhatkit as kit
import time

def send_whatsapp_message(phone_number, message):
    try:
        # Send a message via WhatsApp Web
        kit.sendwhatmsg_instantly(phone_number, message, 15, True, 2)
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {str(e)}")


# List of phone numbers and message
contacts = ["+919716222967"]
message = "Hello! This is message is sent using Python."

for contact in contacts:
    send_whatsapp_message(contact, message)
    time.sleep(10)  # Wait for a while before sending the next message

print("All messages sent!")
