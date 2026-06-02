# 🔍 Phase 2 — AI-Powered Reconnaissance & OSINT

> **"Know thy enemy"** — Recon mein jitna time lagao, exploitation utna easy hoga.
> Ab AI tools ke saath recon 10x fast aur accurate hai.

---

## 🤖 AI-Powered Recon — The New Way

### Using AI for Recon (Game Changer!)

```
┌─────────────────────────────────────────────────────────┐
│  OLD WAY: Manual Google dorking, one tool at a time     │
│  NEW WAY: AI + automated pipelines + smart analysis     │
└─────────────────────────────────────────────────────────┘
```

### How to Use ChatGPT/Claude for Hacking

```
PROMPT EXAMPLES (Ask AI these questions):

1. RECON PLANNING:
   "I'm doing an authorized pentest on a web application running 
   Apache 2.4.49 on Ubuntu. What vulnerabilities should I check 
   for? Give me specific CVEs and exploit methods."

2. EXPLOIT RESEARCH:
   "Explain CVE-2021-41773 step by step. Show me the HTTP request 
   to exploit Apache path traversal."

3. SCRIPT GENERATION:
   "Write a Python script that enumerates subdomains using 
   certificate transparency logs from crt.sh API"

4. PAYLOAD CRAFTING:
   "Generate 20 different XSS payloads that bypass common WAF 
   filters like Cloudflare and ModSecurity"

5. REPORT WRITING:
   "I found an SQL injection in the login form at /api/login. 
   Write a professional pentest finding report with CVSS score, 
   description, steps to reproduce, impact, and remediation."

6. LOG ANALYSIS:
   "Analyze these Apache access logs and identify potential 
   attack patterns: [paste logs]"

7. CODE REVIEW:
   "Review this PHP code for security vulnerabilities: [paste code]"
```

### AI Recon Tools (Install in Kali)

```bash
# ═══════════════════════════════════════════════
# ReconFTW — All-in-one recon automation
# ═══════════════════════════════════════════════
git clone https://github.com/six2dez/reconftw.git
cd reconftw
./install.sh
# Usage:
./reconftw.sh -d target.com -r

# ═══════════════════════════════════════════════
# Nuclei — AI-powered vulnerability scanner
# ═══════════════════════════════════════════════
sudo apt install -y nuclei
# Or:
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Scan for ALL known vulnerabilities
nuclei -u https://target.com -t /root/nuclei-templates/
nuclei -u https://target.com -tags cve          # only CVE checks
nuclei -u https://target.com -tags xss,sqli     # specific vuln types
nuclei -l urls.txt -t /root/nuclei-templates/   # bulk scan

# ═══════════════════════════════════════════════
# Subfinder — Fast subdomain discovery
# ═══════════════════════════════════════════════
sudo apt install -y subfinder
subfinder -d target.com -o subdomains.txt
subfinder -d target.com -all                    # use all sources

# ═══════════════════════════════════════════════
# httpx — Probe for live web servers
# ═══════════════════════════════════════════════
sudo apt install -y httpx-toolkit
cat subdomains.txt | httpx -sc -title -tech-detect -o live_hosts.txt

# ═══════════════════════════════════════════════
# FULL AUTOMATED PIPELINE
# ═══════════════════════════════════════════════
# Subdomain → Live hosts → Vulnerability scan
subfinder -d target.com -silent | httpx -silent | nuclei -t /root/nuclei-templates/
```

---

## 🕵️ OSINT — Digital Footprinting

### Person OSINT (Social Media, Emails, etc.)

```bash
# ═══════════════════════════════════════════════
# Sherlock — Find username across 400+ sites
# ═══════════════════════════════════════════════
sudo apt install -y sherlock
sherlock target_username --timeout 10 --output results.txt

# ═══════════════════════════════════════════════
# Maigret — Better than Sherlock (more sites!)
# ═══════════════════════════════════════════════
pip3 install maigret
maigret target_username --all-sites

# ═══════════════════════════════════════════════
# Holehe — Check if email is registered on sites
# ═══════════════════════════════════════════════
pip3 install holehe
holehe target@email.com

# ═══════════════════════════════════════════════
# PhoneInfoga — Phone number OSINT
# ═══════════════════════════════════════════════
# Install
git clone https://github.com/sundowndev/phoneinfoga.git
cd phoneinfoga
# Or download binary from releases

phoneinfoga scan -n "+911234567890"
phoneinfoga serve                    # web interface

# ═══════════════════════════════════════════════
# GHunt — Google Account OSINT
# ═══════════════════════════════════════════════
pip3 install ghunt
ghunt email target@gmail.com

# ═══════════════════════════════════════════════
# Maltego — Visual OSINT (GUI — pre-installed in Kali)
# ═══════════════════════════════════════════════
maltego
# Create "New Graph" → Drag entities → Run transforms
```

### Online OSINT Resources

```
PEOPLE SEARCH:
├── https://www.social-searcher.com/    — Social media search
├── https://thatsthem.com/              — People search (US)
├── https://www.peekyou.com/            — Social profiles
├── https://namechk.com/                — Username availability
└── https://whatsmyname.app/            — Username search

EMAIL OSINT:
├── https://hunter.io/                  — Find company emails
├── https://haveibeenpwned.com/         — Check breached accounts
├── https://epieos.com/                 — Email to social accounts
├── https://tools.emailhippo.com/      — Email validation
└── https://phonebook.cz/              — Breach data search

DOMAIN/IP OSINT:
├── https://shodan.io/                  — IoT/server search engine
├── https://censys.io/                  — Internet scanning data
├── https://crt.sh/                     — Certificate transparency
├── https://securitytrails.com/         — DNS history
├── https://dnsdumpster.com/            — DNS recon
├── https://viewdns.info/              — Reverse IP, DNS tools
├── https://web.archive.org/           — Wayback Machine
├── https://builtwith.com/             — Technology detection
└── https://wigle.net/                 — WiFi network map

IMAGE/MEDIA OSINT:
├── https://images.google.com/         — Reverse image search
├── https://tineye.com/                — Reverse image search
├── https://fotoforensics.com/         — Image forensics
└── https://exifdata.com/              — Image metadata
```

### Google Dorking — Advanced

```
# ═══════════════════════════════════════════════
# FIND VULNERABLE SYSTEMS (Google Hacking DB)
# ═══════════════════════════════════════════════

# Login pages
inurl:"/admin/login" site:target.com
inurl:"/wp-admin" site:target.com
inurl:"/user/login" site:target.com
intitle:"admin panel" site:target.com

# Exposed sensitive files  
site:target.com filetype:env               # .env files (DB creds!)
site:target.com filetype:sql               # SQL dumps
site:target.com filetype:log               # Log files
site:target.com filetype:bak               # Backup files
site:target.com filetype:conf              # Config files
site:target.com filetype:pem               # SSL keys!
site:target.com "DB_PASSWORD" | "DB_HOST"  # Hardcoded creds

# Directory listings (misconfigured servers)
intitle:"index of" site:target.com
intitle:"index of" "parent directory" site:target.com
intitle:"index of" ".git" site:target.com   # Exposed git repos!
intitle:"index of" "wp-content/uploads" site:target.com

# Error messages (info disclosure)
site:target.com "mysql error" | "sql syntax"
site:target.com "PHP Warning" | "PHP Error"
site:target.com "Stack Trace" | "Internal Server Error"
site:target.com "ORA-" | "PLS-"            # Oracle errors

# Exposed APIs & dashboards
site:target.com inurl:"/api/" | inurl:"/swagger"
site:target.com intitle:"Kibana" | intitle:"Grafana"
site:target.com intitle:"phpMyAdmin"
site:target.com intitle:"Jenkins" inurl:"/manage"

# Cameras & IoT
inurl:"/view.shtml"                         # IP cameras
intitle:"webcamXP" | intitle:"webcam 7"
inurl:"/admin/default.asp"                  # Router admin panels

# Bug Bounty Dorking
site:target.com inurl:"/api/v1/" | inurl:"/api/v2/"
site:target.com ext:json | ext:xml | ext:yaml
site:target.com "api_key" | "apikey" | "api-key"

# Full Google Hacking Database:
# https://www.exploit-db.com/google-hacking-database
```

---

## 🔍 Network Reconnaissance

### Nmap — AI-Enhanced Scanning

```bash
# ═══════════════════════════════════════════════
# DISCOVERY
# ═══════════════════════════════════════════════
# Find all alive hosts
sudo nmap -sn 192.168.1.0/24 -oG - | grep Up | awk '{print $2}' > alive.txt

# ═══════════════════════════════════════════════
# COMPREHENSIVE SCAN (Copy-paste this for CTFs!)
# ═══════════════════════════════════════════════
sudo nmap -sS -sV -sC -O -A -p- -T4 --min-rate=1000 \
  --script=vuln,default,discovery \
  -oA full_scan TARGET_IP

# ═══════════════════════════════════════════════
# STEALTH SCAN (Avoid detection)
# ═══════════════════════════════════════════════
sudo nmap -sS -T2 --randomize-hosts --data-length 50 \
  -D RND:5 --source-port 53 TARGET_IP
# -D RND:5 = add 5 random decoy IPs
# --source-port 53 = pretend to be DNS traffic

# ═══════════════════════════════════════════════
# SPECIFIC SERVICE ENUMERATION
# ═══════════════════════════════════════════════
# SMB (Windows file sharing)
nmap -p 445 --script=smb-vuln*,smb-enum-shares,smb-enum-users TARGET
# HTTP
nmap -p 80,443 --script=http-title,http-methods,http-enum TARGET
# SSH
nmap -p 22 --script=ssh-brute,ssh-auth-methods TARGET
# FTP
nmap -p 21 --script=ftp-anon,ftp-brute TARGET
# MySQL
nmap -p 3306 --script=mysql-info,mysql-enum TARGET

# ═══════════════════════════════════════════════
# AI TRICK: Paste Nmap output to ChatGPT!
# ═══════════════════════════════════════════════
# "Analyze this Nmap scan result and suggest:
#  1. Potential attack vectors for each open port
#  2. Known CVEs for the detected service versions  
#  3. Priority order for exploitation
#  [paste nmap output]"
```

### Automated Recon Script

```bash
#!/bin/bash
# recon_auto.sh — Automated recon pipeline
# Usage: ./recon_auto.sh target.com

TARGET=$1
OUTPUT_DIR="recon_$TARGET_$(date +%Y%m%d)"
mkdir -p $OUTPUT_DIR

echo "═══════════════════════════════════════"
echo "  AUTOMATED RECON: $TARGET"
echo "  Output: $OUTPUT_DIR"
echo "═══════════════════════════════════════"

# Step 1: Subdomain enumeration
echo "[*] Phase 1: Subdomain enumeration..."
subfinder -d $TARGET -silent -o $OUTPUT_DIR/subdomains.txt 2>/dev/null
amass enum -passive -d $TARGET -o $OUTPUT_DIR/amass_subs.txt 2>/dev/null
cat $OUTPUT_DIR/subdomains.txt $OUTPUT_DIR/amass_subs.txt 2>/dev/null | sort -u > $OUTPUT_DIR/all_subs.txt
echo "[+] Found $(wc -l < $OUTPUT_DIR/all_subs.txt) unique subdomains"

# Step 2: Probe for live hosts
echo "[*] Phase 2: Probing live hosts..."
cat $OUTPUT_DIR/all_subs.txt | httpx -silent -sc -title -tech-detect -o $OUTPUT_DIR/live_hosts.txt 2>/dev/null
echo "[+] Found $(wc -l < $OUTPUT_DIR/live_hosts.txt) live hosts"

# Step 3: Port scan on live IPs
echo "[*] Phase 3: Port scanning..."
cat $OUTPUT_DIR/all_subs.txt | while read sub; do
    ip=$(dig +short $sub | head -1)
    if [ ! -z "$ip" ]; then
        echo "$ip" >> $OUTPUT_DIR/ips.txt
    fi
done
sort -u $OUTPUT_DIR/ips.txt -o $OUTPUT_DIR/ips.txt 2>/dev/null
nmap -sS -sV -T4 --top-ports 1000 -iL $OUTPUT_DIR/ips.txt -oA $OUTPUT_DIR/nmap_scan 2>/dev/null

# Step 4: Vulnerability scan
echo "[*] Phase 4: Vulnerability scanning..."
nuclei -l $OUTPUT_DIR/live_hosts.txt -severity critical,high -o $OUTPUT_DIR/vulns.txt 2>/dev/null
echo "[+] Found $(wc -l < $OUTPUT_DIR/vulns.txt 2>/dev/null || echo 0) potential vulnerabilities"

# Step 5: Directory enumeration on web servers
echo "[*] Phase 5: Directory enumeration..."
cat $OUTPUT_DIR/live_hosts.txt | while read url; do
    echo "[*] Scanning: $url"
    gobuster dir -u "$url" -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 50 -q >> $OUTPUT_DIR/directories.txt 2>/dev/null
done

echo ""
echo "═══════════════════════════════════════"
echo "  RECON COMPLETE!"
echo "  Results in: $OUTPUT_DIR/"
echo "═══════════════════════════════════════"
ls -la $OUTPUT_DIR/
```

---

## 📸 Screenshot & Evidence Collection

```bash
# ═══════════════════════════════════════════════
# Eyewitness — Automated screenshot of websites
# ═══════════════════════════════════════════════
sudo apt install -y eyewitness
eyewitness --web -f live_hosts.txt --timeout 10 -d screenshots/

# ═══════════════════════════════════════════════
# Aquatone — Another screenshot tool
# ═══════════════════════════════════════════════
cat live_hosts.txt | aquatone -out screenshots/

# ═══════════════════════════════════════════════
# Gowitness — Screenshot + tech detection
# ═══════════════════════════════════════════════
gowitness file -f live_hosts.txt
```

---

## 🎥 Phase 2 Videos

```
1. "OSINT Full Course" — TCM Security (FREE, 4+ hours)
   https://www.youtube.com/watch?v=qwA6MmbeGNo

2. "Google Dorking Full Tutorial" — NetworkChuck
   https://www.youtube.com/watch?v=u_gOnwWEXiA

3. "Nmap Full Tutorial" — HackerSploit
   https://www.youtube.com/watch?v=4t4kBkMsDbQ

4. "Shodan Tutorial" — David Bombal  
   https://www.youtube.com/watch?v=R3wKTxnQmPU

5. "Bug Bounty Recon" — Nahamsec
   https://www.youtube.com/watch?v=MIujSpuDtFY

6. "Automated Recon with Nuclei" — ProjectDiscovery
   https://www.youtube.com/watch?v=o33YbSOV-KM
```

---

## ✅ Phase 2 Checklist

```
AI RECON
[ ] Can use AI to plan and accelerate recon
[ ] Can generate custom scripts with AI
[ ] Can analyze scan results with AI

OSINT
[ ] Can find person's digital footprint (username, email, phone)
[ ] Can use Sherlock, Maigret, Holehe
[ ] Know 10+ OSINT websites
[ ] Can use Google dorking effectively

NETWORK RECON
[ ] Master all Nmap scan types
[ ] Can use automated recon pipeline
[ ] Can enumerate specific services (SMB, HTTP, FTP)
[ ] Can take screenshots with Eyewitness

DOCUMENTATION
[ ] Can organize and document recon findings
[ ] Can prioritize targets based on recon
```

---

> **Phase 2 done? → [Phase 3 — Network Attacks](./Phase3_Network_Attacks.md)** 🌐
