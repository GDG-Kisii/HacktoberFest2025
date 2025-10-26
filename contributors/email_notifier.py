import jwt
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecret")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = 587

class EmailNotifier:
    def generate_verification_token(self, email, username):
        payload = {
            "email": email,
            "username": username,
            "type": "verification",
            "exp": datetime.utcnow() + timedelta(hours=24)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
        return token

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            return True, payload
        except jwt.ExpiredSignatureError:
            return False, "Token expired"
        except jwt.InvalidTokenError:
            return False, "Invalid token"

    def send_email(self, recipient_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False
