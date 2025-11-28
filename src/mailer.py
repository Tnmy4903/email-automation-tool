import smtplib
from email.message import EmailMessage
from pathlib import Path
from typing import Optional
from .config import Settings

class Mailer:
    def __init__(self, settings: Settings, logger):
        self.settings = settings
        self.logger = logger

    def _connect(self):
        server = smtplib.SMTP(self.settings.email_host, self.settings.email_port, timeout=30)
        if self.settings.use_tls:
            server.starttls()
        server.login(self.settings.email_address, self.settings.email_password)
        return server

    def send_one(self, to_email: str, subject: str, body: str, attachment_path: Optional[Path] = None):
        msg = EmailMessage()
        msg["From"] = self.settings.email_address
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        if attachment_path:
            with open(attachment_path, "rb") as f:
                data = f.read()
            msg.add_attachment(
                data,
                maintype="application",
                subtype="pdf",
                filename=attachment_path.name
            )

        with self._connect() as server:
            server.send_message(msg)
