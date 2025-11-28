from dataclasses import dataclass
import os
from dotenv import load_dotenv

@dataclass(frozen=True)
class Settings:
    email_host: str
    email_port: int
    email_address: str
    email_password: str
    use_tls: bool = True  # STARTTLS on port 587 by default

def load_settings() -> Settings:
    load_dotenv()
    host = os.getenv("EMAIL_HOST", "").strip()
    port = int(os.getenv("EMAIL_PORT", "587"))
    address = os.getenv("EMAIL_ADDRESS", "").strip()
    password = os.getenv("EMAIL_PASSWORD", "")
    if not all([host, port, address, password]):
        raise ValueError("Missing one or more required SMTP env vars.")
    return Settings(
        email_host=host,
        email_port=port,
        email_address=address,
        email_password=password,
        use_tls=True
    )
