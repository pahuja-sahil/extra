# Import required libraries
import os
from twilio.rest import Client
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Twilio API credentials
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

# Create a Twilio client
try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
except Exception as e:
    logger.error(f"Failed to create Twilio client: {e}")
    raise

def send_sms(to, body):
    """
    Send an SMS message using Twilio.

    Args:
        to (str): The recipient's phone number.
        body (str): The message body.

    Returns:
        The SID of the sent message.
    """
    try:
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        logger.info(f"Sent SMS to {to}: {body}")
        return message.sid
    except Exception as e:
        logger.error(f"Failed to send SMS: {e}")
        raise

def receive_sms():
    """
    Receive an SMS message using Twilio.

    Returns:
        A list of received messages.
    """
    try:
        messages = client.messages.list(from_=TWILIO_PHONE_NUMBER)
        logger.info(f"Received {len(messages)} SMS messages")
        return messages
    except Exception as e:
        logger.error(f"Failed to receive SMS: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    to = "+1234567890"
    body = "Hello from Twilio!"
    send_sms(to, body)
    receive_sms()