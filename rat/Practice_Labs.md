# 🧪 Practice Labs — Complete Lab Setup Guide

> Bina lab ke hacking seekhna = bina pani ke swimming seekhna.
> Yeh guide tere UTM Mac setup ke liye optimized hai.

---

## 🏗️ Lab Architecture

```
YOUR MAC (Host)
├── UTM
│   ├── 🐉 Kali Linux (Attack Machine) — YOUR main VM
│   ├── 🎯 Metasploitable 2 (Vulnerable Linux) — Practice target
│   ├── 🎯 Metasploitable 3 (Vulnerable Windows) — Advanced target
│   ├── 🕸️ DVWA/Juice Shop (Web App) — Web hacking practice
│   └── 🪟 Windows 10 (Optional) — Windows exploitation
│
├── Online Labs (No setup needed!)
│   ├── TryHackMe.com
│   ├── HackTheBox.com
│   ├── PortSwigger Academy
│   └── PicoCTF.org
│
└── Docker (On Kali)
    ├── Juice Shop
    ├── DVWA
    ├── Vulnerable APIs
    └── Custom vulnerable apps
```

---

## 🔧 Setting Up Your Attack VM (Kali Linux)

### First Boot Checklist

```bash
# ═══════════════════════════════════════════════
# RUN THESE COMMANDS IN ORDER!
# ═══════════════════════════════════════════════

# 1. Update everything
sudo apt update && sudo apt full-upgrade -y

# 2. Change default password
passwd
# Default was: kali/kali → Change it!

# 3. Set timezone
sudo timedatectl set-timezone Asia/Kolkata

# 4. Install extended toolset
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

# 6. Extract wordlists
sudo gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null

# 7. Install Python packages
pip3 install requests beautifulsoup4 scapy paramiko pwntools \
  flask impacket pycryptodome maigret holehe

# 8. Create workspace
mkdir -p ~/hacking/{recon,scans,exploits,payloads,reports,scripts,loot,ctf,tools,notes}

# 9. Set up aliases
cat >> ~/.zshrc << 'EOF'

# === HACKING ALIASES ===
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade -y'
alias myip='ip addr show | grep "inet " | grep -v 127'
alias ports='sudo ss -tulnp'
alias scan='sudo nmap -sV -sC -T4'
alias fullscan='sudo nmap -sS -sV -sC -O -p- -T4 --min-rate=1000'
alias serve='python3 -m http.server 8000'
alias listen='sudo nc -lvnp'
alias msf='sudo msfconsole -q'
alias msfdb='sudo systemctl start postgresql && sudo msfdb init'
alias webup='sudo systemctl start apache2 && echo "Apache started on port 80"'
alias dockerup='sudo systemctl start docker'
EOF
source ~/.zshrc

# 10. Set up Metasploit database
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo msfdb init
```

---

## 🎯 Vulnerable Machines — Download & Setup

### 1. Metasploitable 2 (MUST HAVE — Easiest target)

```
Download: https://sourceforge.net/projects/metasploitable/

UTM Setup:
1. Download ZIP → Extract → Find .vmdk file
2. UTM → Create New VM → Other
3. Skip ISO → Import VMDK as disk
4. RAM: 512 MB, CPU: 1 core
5. Network: Same as Kali (Bridged or Host-Only)
6. Boot → Login: msfadmin / msfadmin

What's vulnerable:
├── Port 21 — vsftpd 2.3.4 (backdoor!)
├── Port 22 — SSH (brute forceable)
├── Port 23 — Telnet (plaintext creds)
├── Port 80 — DVWA, Mutillidae, phpMyAdmin
├── Port 139/445 — Samba (username map exploit)
├── Port 1099 — Java RMI
├── Port 1524 — Bindshell backdoor
├── Port 2049 — NFS (misconfigured shares)
├── Port 3306 — MySQL (weak creds)
├── Port 5432 — PostgreSQL (weak creds)
├── Port 5900 — VNC (password: password)
├── Port 6000 — X11 (no auth!)
├── Port 6667 — IRC (backdoor)
├── Port 8180 — Tomcat (default creds)
└── Port 8787 — Ruby DRb RCE
```

### 2. Web Hacking Labs (Inside Kali — Docker)

```bash
# ═══════════════════════════════════════════════
# Start Docker
sudo systemctl start docker

# DVWA — Damn Vulnerable Web Application
sudo docker run -d -p 80:80 vulnerables/web-dvwa
# Access: http://localhost
# Login: admin / password

# OWASP Juice Shop — Modern web app
sudo docker run -d -p 3000:3000 bkimminich/juice-shop
# Access: http://localhost:3000

# OWASP WebGoat — Interactive lessons
sudo docker run -d -p 8080:8080 -p 9090:9090 webgoat/webgoat
# Access: http://localhost:8080/WebGoat

# Damn Vulnerable GraphQL — API hacking
sudo docker run -d -p 5013:5013 dolevf/dvga
# Access: http://localhost:5013

# Vulnerable API (OWASP crAPI)
# git clone https://github.com/OWASP/crAPI.git
# cd crAPI && docker-compose up -d

# NodeGoat — OWASP Node.js vulnerable app
sudo docker run -d -p 4000:4000 owasp/nodegoat
# Access: http://localhost:4000

# ═══════════════════════════════════════════════
# STOP ALL LABS
sudo docker stop $(sudo docker ps -q)

# START ALL LABS
sudo docker start $(sudo docker ps -aq)
```

### 3. VulnHub Machines (Download & Import to UTM)

```
BEGINNER:
├── Kioptrix Level 1
│   https://www.vulnhub.com/entry/kioptrix-level-1-1,22/
│   
├── Mr. Robot
│   https://www.vulnhub.com/entry/mr-robot-1,151/
│
├── DC-1 (and DC-2 through DC-9)
│   https://www.vulnhub.com/entry/dc-1,292/
│
├── Basic Pentesting 1
│   https://www.vulnhub.com/entry/basic-pentesting-1,216/
│
└── Stapler
    https://www.vulnhub.com/entry/stapler-1,150/

INTERMEDIATE:
├── Vulnix
├── SickOs
├── PwnLab
└── Brainpan

ADVANCED:
├── HackLAB: Vulnix
├── Raven
└── Wintermute
```

---

## 🌐 Online Lab Platforms

### TryHackMe — Best for Beginners! 🏆

```
FREE Rooms to Complete (in order):

COMPLETE BEGINNER PATH:
1. "Introduction to Cyber Security"
2. "Linux Fundamentals Part 1, 2, 3"
3. "Intro to Networking"
4. "Nmap"
5. "Network Services"
6. "Web Fundamentals"
7. "OWASP Top 10"

MUST-DO FREE ROOMS:
├── OhSINT         → OSINT challenge
├── Vulnversity    → Web exploitation
├── Basic Pentesting → Full methodology
├── Kenobi         → Samba + Linux priv esc
├── Blue           → Windows EternalBlue
├── Ice            → Windows exploitation
├── Pickle Rick    → Web + command injection
├── RootMe         → Web exploitation
├── Bounty Hacker  → FTP + SSH + priv esc
├── Overpass       → Web + cron exploitation
├── Skynet         → Samba + Linux
└── Internal       → Full pentest

https://tryhackme.com
→ Free tier gives access to many rooms
→ Premium ($10/month) for ALL rooms — WORTH IT!
```

### HackTheBox — For Intermediate+

```
GETTING STARTED:
1. Create account: https://hackthebox.com
2. Start with "Starting Point" machines (guided)
3. Then move to Easy retired machines
4. Watch IppSec videos for solutions!

RECOMMENDED EASY MACHINES:
├── Lame
├── Jerry
├── Nibbles
├── Bashed
├── Shocker
├── Mirai
├── Blocky
├── Blue
├── Optimum
└── Devel

PRO LABS (Paid — Advanced):
├── Dante
├── Offshore
├── RastaLabs
└── Cybernetics

https://hackthebox.com
→ Free tier for active machines
→ VIP ($14/month) for retired machines — recommended!
```

### PortSwigger Web Security Academy — Best for Web! 🕸️

```
100% FREE — Interactive labs!

COMPLETE THESE IN ORDER:
1. SQL Injection (all 18 labs)
2. Cross-site scripting (XSS) (all 30 labs)
3. CSRF (all 12 labs)
4. Clickjacking
5. CORS
6. SSRF (all 7 labs)
7. XXE injection
8. OS command injection
9. Directory traversal
10. Access control
11. Authentication
12. Business logic
13. Information disclosure
14. File upload vulnerabilities
15. Race conditions
16. Server-side template injection
17. Web cache poisoning
18. HTTP request smuggling
19. Prototype pollution
20. GraphQL vulnerabilities

https://portswigger.net/web-security
→ ALL FREE, no signup required for most labs
```

### Other Platforms

```
├── PicoCTF          → https://picoctf.org (beginner CTF)
├── OverTheWire      → https://overthewire.org (Linux wargames)
├── RootMe           → https://root-me.org (challenges)
├── CryptoHack       → https://cryptohack.org (crypto)
├── Pwnable.kr       → https://pwnable.kr (binary)
├── VulnHub          → https://vulnhub.com (downloadable VMs)
├── Proving Grounds  → https://portal.offsec.com (OSCP prep)
├── PentesterLab     → https://pentesterlab.com (web)
└── CTFtime          → https://ctftime.org (competitions)
```

---

## 📊 Lab Practice Schedule

```
DAILY ROUTINE (2-3 hours):
┌─────────────────────────────────────────────┐
│ Mon → TryHackMe room                        │
│ Tue → HackTheBox machine                    │
│ Wed → PortSwigger labs (2-3 labs)            │
│ Thu → VulnHub machine or Docker lab          │
│ Fri → CTF practice (PicoCTF/RootMe)         │
│ Sat → Full pentest on lab machine            │
│ Sun → Write up findings + review week        │
└─────────────────────────────────────────────┘
```

---

## ⚠️ Lab Safety Rules

```
1. NEVER attack systems outside your lab
2. Keep vulnerable VMs on isolated network
3. Take VM snapshots before experiments
4. Use VPN for online lab platforms
5. Don't store real personal data in VMs
6. Keep Kali updated
7. Document everything you learn
```

---

> **Lab ready? Start with Phase 1 → [Phase 1 Foundation](./Phase1_Foundation.md)** 🚀
