# 📧 Automated HR Outreach Email Sender

This project sends **personalized job inquiry emails** to HR contacts listed in a CSV file.
Each email is sent **individually** with:

* Custom **name** and **company**
* Your own **resume attached**
* A professional template included
* Automatic logging + CSV auto-clean feature

---

## ✨ Features

| Feature             | Description                          |
| ------------------- | ------------------------------------ |
| Personalized emails | `{name}` and `{company}` auto-filled |
| CSV based sending   | Just update `data/hr_contacts.csv`   |
| Attach resume       | Sends your resume with every email   |
| Safe sending        | Delay + auto-stop limit              |
| Auto-clean CSV      | Removes row after successful send    |

---

## 🛠 Folder Structure

```
email-broadcast/
├─ assets/
│  └─ YOUR_RESUME.pdf
├─ data/
│  └─ hr_contacts.csv
├─ logs/
├─ src/
│  ├─ config.py
│  ├─ templates.py      ← Edit body text & signature here
│  ├─ mailer.py
│  ├─ utils.py
│  └─ main.py
├─ .env
└─ requirements.txt
```

---

## 📄 Step 1 — Prepare Your Resume

Place your resume in:

```
assets/YOUR_RESUME.pdf
```

**Rename it to exactly**:

```
YOUR_RESUME.pdf
```

---

## 📝 Step 2 — Edit Email Template (Your Name, Email, Phone, Links)

Open:

```
src/templates.py
```

Replace inside the email body:

```
Warm regards,
Your Name Here
your_email@example.com

Your Phone Number
Your LinkedIn Profile or Portfolio Link
```

Example:

```
Warm regards,
Rohit Sharma
rohit.sharma1999@gmail.com

+91 98765 43210
linkedin.com/in/rohitsharma/
```

---

## 🧾 Step 3 — CSV Format

File location:

```
data/hr_contacts.csv
```

Must contain:

```
sno,name,email,title,company
1,Akanksha Puri,akanksha.puri@sourcefuse.com,Associate Director HR,SourceFuse Technologies
```

> `title` ignored automatically.

---

## 🔐 Step 4 — Setup `.env`

Create `.env` file in root:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### How to Get App Password (Mandatory)

1. Turn on **2-Step Verification**
2. Open: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Generate new password for **Mail**
4. Copy it into `EMAIL_PASSWORD`

> **DO NOT USE NORMAL GMAIL PASSWORD**

---

## 💻 Step 5 — Install Required Packages

```bash
python -m venv .venv
.\.venv\Scripts\Activate    # Windows
# OR
source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

---

## 🚀 Step 6 — Run the Script

### Dry Run (No Emails Sent)

```bash
python -m src.main
```

### Send Emails (2 seconds delay)

```bash
python -m src.main --send --delay 2
```

### Auto Stop Limit

The script **automatically stops after ~450 emails/day** (safe limit).

---

## 🔄 Automatic CSV Cleanup Behavior

| Result                      | CSV Action                          |
| --------------------------- | ----------------------------------- |
| **Email sent successfully** | That row is **removed** immediately |
| **Failed to send**          | Row **stays** for retry             |

---

## 🗂 Logs

```
logs/sent.log     ← Successful sends
logs/errors.log   ← Failed sends
```

---

## ✅ Summary for User

| Step        | What to Edit                                                          |
| ----------- | --------------------------------------------------------------------- |
| Resume      | Replace `YOUR_RESUME.pdf`                                             |
| Template    | Open `src/templates.py` and update **your name, email, phone, links** |
| Credentials | Fill `.env` with **your email + app password**                        |
| Contacts    | Add HR list to `data/hr_contacts.csv`                                 |

---