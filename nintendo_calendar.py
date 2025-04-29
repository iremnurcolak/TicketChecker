import requests
import time
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage

# CONFIGURATION
EMAIL_SENDER = "MS_GJopSq@test-pzkmgq77xzvl059v.mlsender.net"
EMAIL_RECEIVER_OGZ = "ogzugur@icloud.com"
EMAIL_RECEIVER_MK = "mertkose1745@gmail.com"
EMAIL_RECEIVER_IRM = "iremnurcolak34@gmail.com"
EMAIL_PASSWORD = "mssp.2h0AGNg.x2p0347oe3pgzdrn.brkH96I"

# Function to send email
def send_email(subject, body, receiver):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = receiver

    with smtplib.SMTP("smtp.mailersend.net", 587) as smtp:
        smtp.starttls()  # Upgrade to secure connection
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

url = "https://museum-tickets.nintendo.com/en/api/calendar?target_year=2025&target_month=6"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://museum-tickets.nintendo.com/en/calendar",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "eyJpdiI6Ik5nVFF6OE4ydTJUYnMvQVRCelgwOWc9PSIsInZhbHVlIjoiZ1hWUmZ0MWVFcFZXd0lLVEl4eXE2ajhlK3FFRExUOVpxNmtUNXNPSXBTMU9XMmJvREJzWGJsSUQxMXkzakY0MTdvZDlhVk92N3Jpc2prNXZxVTEveEIwS1M1ZHhNR3ZoZWNFVGpmUEFLRkpzQjUxQ1ZvQ0JRVXFDUm5oa2xReTgiLCJtYWMiOiJhYmQwZTA3YjRmNzM4MTgyOWI5ZWQzMGYwMGI4MTQxNjE3MzNhNDMxMGM1YTMyYjdhZjFlMTQ3NTY3MTg5MTk1IiwidGFnIjoiIn0="
}

cookies = {
    "XSRF-TOKEN": "eyJpdiI6Ik5nVFF6OE4ydTJUYnMvQVRCelgwOWc9PSIsInZhbHVlIjoiZ1hWUmZ0MWVFcFZXd0lLVEl4eXE2ajhlK3FFRExUOVpxNmtUNXNPSXBTMU9XMmJvREJzWGJsSUQxMXkzakY0MTdvZDlhVk92N3Jpc2prNXZxVTEveEIwS1M1ZHhNR3ZoZWNFVGpmUEFLRkpzQjUxQ1ZvQ0JRVXFDUm5oa2xReTgiLCJtYWMiOiJhYmQwZTA3YjRmNzM4MTgyOWI5ZWQzMGYwMGI4MTQxNjE3MzNhNDMxMGM1YTMyYjdhZjFlMTQ3NTY3MTg5MTk1IiwidGFnIjoiIn0="
}

start_date = datetime(2025, 6, 6)
end_date = datetime(2025, 6, 13)

while True:
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        data = response.json()

        calendar = data.get("data", {}).get("calendar", {})

        print(f"----------------------------------------")
        print(f"Checking tickets at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        for i in range((end_date - start_date).days + 1):
            current_date = start_date + timedelta(days=i)
            date_str = current_date.strftime("%Y-%m-%d")
            day_data = calendar.get(date_str)

            if day_data:
                sale_status = day_data.get("sale_status")
                open_status = day_data.get("open_status")

                if sale_status == 1 and open_status == 1:
                    print(f"{date_str}: Ticket is available. Sending e-mail...")
                    send_email(
                        subject="Nintendo Museum Ticket Available",
                        body=f"Tickets are available for {date_str}!",
                        receiver=EMAIL_RECEIVER_MK
                    )
                    send_email(
                        subject="Nintendo Museum Ticket Available",
                        body=f"Tickets are available for {date_str}!",
                        receiver=EMAIL_RECEIVER_OGZ
                    )
                    send_email(
                        subject="Nintendo Museum Ticket Available",
                        body=f"Tickets are available for {date_str}!",
                        receiver=EMAIL_RECEIVER_IRM
                    )
                else:
                    print(f"{date_str}: No ticket for sale")
            else:
                print(f"{date_str}: No data found for this date")
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")

    # Wait for 60 seconds before next check
    time.sleep(60)
