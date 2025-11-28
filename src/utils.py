import csv
import logging
from pathlib import Path
from typing import Dict, Iterable
from email_validator import validate_email, EmailNotValidError

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def setup_logger():
    logger = logging.getLogger("emailer")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(LOG_DIR / "sent.log", encoding="utf-8")
        fh.setLevel(logging.INFO)
        eh = logging.FileHandler(LOG_DIR / "errors.log", encoding="utf-8")
        eh.setLevel(logging.ERROR)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        fh.setFormatter(fmt)
        eh.setFormatter(fmt)
        ch.setFormatter(fmt)

        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)

    return logger

def read_contacts(csv_path: Path) -> Iterable[Dict[str, str]]:
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip()
            company = (row.get("company") or "").strip()
            if name and email and company:
                yield {"name": name, "email": email, "company": company}

def validate_email_address(addr: str) -> bool:
    try:
        validate_email(addr, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False

def remove_contact_from_csv(csv_path: Path, email: str):
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r.get("email", "").strip().lower() != email.lower().strip():
                rows.append(r)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["sno", "name", "email", "title", "company"])
        writer.writeheader()
        writer.writerows(rows)
