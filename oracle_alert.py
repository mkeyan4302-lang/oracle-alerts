import requests, datetime

TOKEN   = "8701503237:AAHhvESJpBRb6cmEL19iZvfvMSCKOcmc1AU"   # from BotFather
CHAT_ID = "1384968439"     # from Step 2

def build_message():
    now = datetime.datetime.now().strftime("%d %b %Y, %I:%M %p IST")
    return f"""
🔔 *ORACLE Alert — {now}*

📊 *6-Hour Portfolio Check*
Open ORACLE and run Market Pulse for live signals.

⚡ *Your 12-Framework Rules*
• Gold/Silver at ATH → Do NOT add SIP
• Equity dip → Great SIP opportunity  
• India VIX > 20 → Stay calm, keep SIP running
• Never stop SIP during a market crash (Graham's rule)

📌 *Pending Actions*
⚠️  Exit ABSL Silver ETF FOF (−8.23%)
✅  Nifty 50 Index SIP ₹1,000/mo — start if not done
✅  ABSL Smallcap 50 SIP → Resume at ₹300/mo
⏸  Pause Motilal Gold+Silver SIP

📚 *Lesson of the day*
"The stock market is a device for transferring money
from the impatient to the patient." — Warren Buffett
    """

def send_alert():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": build_message(),
        "parse_mode": "Markdown"
    })

if __name__ == "__main__":
    send_alert()
    print("Alert sent!")
