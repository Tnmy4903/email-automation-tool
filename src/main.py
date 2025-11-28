import argparse
import time
from pathlib import Path
from typing import Optional

from .config import load_settings
from .templates import render_subject, render_body
from .mailer import Mailer
from .utils import setup_logger, read_contacts, validate_email_address, remove_contact_from_csv

def run(csv_path: Path, resume_path: Path, delay_sec: float, dry_run: bool):
    logger = setup_logger()

    if not resume_path.exists():
        raise FileNotFoundError(f"Resume not found at: {resume_path}")

    settings = load_settings()
    mailer = Mailer(settings, logger)

    total = sent = skipped = 0

    for row in read_contacts(csv_path):
        total += 1
        name, email, company = row["name"], row["email"], row["company"]

        if not (name and email and company and validate_email_address(email)):
            skipped += 1
            logger.error(f"Skipping row (invalid/missing data): {row}")
            continue

        subject = render_subject(name, company)
        body = render_body(name, company)

        if dry_run:
            logger.info(f"[DRY-RUN] Would send to {email} | Subject: {subject}")
        else:
            try:
                mailer.send_one(
                    to_email=email,
                    subject=subject,
                    body=body,
                    attachment_path=resume_path
                )
                sent += 1
                logger.info(f"Sent to {email} ({name} @ {company})")
                remove_contact_from_csv(csv_path, email)
            except Exception as e:
                skipped += 1
                logger.exception(f"Failed to send to {email}: {e}")

            time.sleep(delay_sec)
            if sent >= 300:
                logger.info("Reached daily limit of 450 emails. Stopping automatically.")
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Personalized HR email sender")
    parser.add_argument("--csv", type=Path, default=Path("data/hr_contacts.csv"), help="Path to CSV file")
    parser.add_argument("--resume", type=Path, default=Path("assets/Tanmay_Resume.pdf"), help="Path to resume PDF")
    parser.add_argument("--delay", type=float, default=1.5, help="Delay (seconds) between emails")
    parser.add_argument("--send", action="store_true", help="Actually send emails (omit to dry-run)")
    args = parser.parse_args()

    run(csv_path=args.csv, resume_path=args.resume, delay_sec=args.delay, dry_run=not args.send)
