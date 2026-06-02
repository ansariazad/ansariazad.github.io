# 🌍 Phase 10 — Real World: Bug Bounty, CTFs & Career

> Ab tu sab seekh chuka hai. Ab **real world** mein apply kar aur **paisa kama!**

---

## 💰 Bug Bounty — Legal Hacking for Money!

### What is Bug Bounty?

```
Companies PAY YOU to find security bugs in their systems!

Average Bug Bounty Payouts:
├── Critical (RCE, Auth Bypass)     → $5,000 - $100,000+
├── High (SQLi, IDOR, SSRF)        → $1,000 - $10,000
├── Medium (XSS, CSRF)             → $250 - $2,000
├── Low (Info Disclosure)            → $50 - $500
└── Some companies pay more!

Top earners make $500K+ per year!
Indian bug bounty hunters regularly earn ₹10-50 lakhs/year
```

### Bug Bounty Platforms

```
PLATFORMS (Sign up on ALL of these!):

1. HackerOne — https://hackerone.com
   → Largest platform, 2000+ programs
   → Companies: Google, Microsoft, Uber, PayPal, etc.

2. Bugcrowd — https://bugcrowd.com
   → Second largest, good for beginners
   → University program available

3. Intigriti — https://intigriti.com
   → European platform, growing fast
   → Good payouts

4. YesWeHack — https://yeswehack.com
   → European, good programs

5. Open Bug Bounty — https://openbugbounty.org
   → XSS focused, great for beginners!

6. Google VRP — https://bughunters.google.com/
   → Google's own program

7. GitHub Security Lab — https://securitylab.github.com/
   → Find bugs in open source
```

### Bug Bounty Methodology

```bash
# ═══════════════════════════════════════════════
# STEP-BY-STEP BUG BOUNTY WORKFLOW
# ═══════════════════════════════════════════════

# STEP 1: CHOOSE A PROGRAM
# Start with programs that have large scope
# Look for: *.company.com (wildcard scope)
# Avoid: Very popular targets (too competitive)
# Focus on: New programs, less-known companies

# STEP 2: RECON (Most important step!)
subfinder -d target.com -o subs.txt
cat subs.txt | httpx -sc -title -tech-detect -o live.txt
nuclei -l live.txt -severity critical,high -o vulns.txt

# STEP 3: MANUAL TESTING
# Focus on:
# - Authentication (login, register, password reset)
# - Authorization (IDOR, access control)
# - Input validation (SQLi, XSS, command injection)
# - Business logic (price manipulation, race conditions)
# - API endpoints (hidden/undocumented)
# - File upload
# - SSRF
# - Subdomain takeover

# STEP 4: WRITE REPORT
# Good report = faster fix = faster payment!

# STEP 5: SUBMIT & WAIT
# Be patient, professional, and responsive
```

### Bug Bounty Report Template

```markdown
## Title
[Vulnerability Type] in [Location] allows [Impact]

## Severity
Critical / High / Medium / Low
CVSS Score: X.X

## Description
A brief description of what the vulnerability is.

## Steps to Reproduce
1. Go to https://target.com/endpoint
2. Intercept the request with Burp Suite
3. Modify parameter X to Y
4. Observe that Z happens

## Proof of Concept
[Screenshots, video, HTTP requests/responses]

## Impact
Explain what an attacker could do:
- Read other users' data
- Modify account settings
- Execute arbitrary code
- Access admin panel

## Remediation
Suggest how to fix:
- Input validation
- Parameterized queries
- Access control checks
- Rate limiting

## References
- OWASP link
- CWE number
- Similar CVEs
```

### Subdomain Takeover (Easy Bug Bounty Win!)

```bash
# ═══════════════════════════════════════════════
# Subdomain takeover = unused subdomain pointing to 
# expired service (Heroku, S3, GitHub Pages, etc.)
# You claim the service = you control the subdomain!
# ═══════════════════════════════════════════════

# Tool: Subjack
go install github.com/haccer/subjack@latest
subjack -w subdomains.txt -t 100 -timeout 30 -ssl -a

# Tool: Nuclei with takeover templates
nuclei -l subdomains.txt -t /root/nuclei-templates/takeovers/

# What to look for:
# - CNAME pointing to unregistered service
# - "There isn't a GitHub Pages site here"
# - "NoSuchBucket" (AWS S3)
# - "No such app" (Heroku)
# - "Domain not found" (Shopify)

# This is typically a Medium-High severity finding
# Easy money: $200-$2000 per takeover!
```

---

## 🏆 CTF Mastery

### CTF Strategy

```
CTF CATEGORIES:
├── Web          → SQLi, XSS, SSRF, deserialization
├── Pwn/Binary   → Buffer overflow, ROP chains
├── Reverse      → Reverse engineering binaries
├── Crypto       → Cryptography challenges
├── Forensics    → Disk/memory/network forensics
├── OSINT        → Open source intelligence
├── Misc         → Everything else
└── Hardware     → IoT, embedded systems

BEGINNER STRATEGY:
1. Start with Web + OSINT (easiest)
2. Learn Forensics (fun and useful)
3. Pick up Crypto basics
4. Eventually learn Pwn (hardest but most rewarding)
```

### CTF Platforms & Resources

```
PRACTICE PLATFORMS:
├── PicoCTF        → https://picoctf.org (BEST for beginners!)
├── OverTheWire    → https://overthewire.org (Linux basics)
├── TryHackMe      → https://tryhackme.com (guided labs)
├── HackTheBox     → https://hackthebox.com (machines)
├── RootMe         → https://root-me.org (challenges)
├── CryptoHack     → https://cryptohack.org (crypto)
├── Pwnable.kr     → https://pwnable.kr (binary exploitation)
└── CTFtime        → https://ctftime.org (upcoming competitions)

WRITEUP SITES (Learn from others!):
├── https://0xdf.gitlab.io/          → HTB writeups
├── https://ippsec.rocks/            → Search IppSec videos
├── https://ctftime.org/writeups     → CTF competition writeups
└── Medium/blogs                      → Search: "CTF writeup [challenge name]"
```

### Must-Do CTF Progression

```
LEVEL 1 — ABSOLUTE BEGINNER:
1. OverTheWire Bandit (30 levels) — Linux basics
2. PicoCTF — Web and Forensics categories
3. TryHackMe "Complete Beginner" path

LEVEL 2 — BEGINNER:
4. TryHackMe: Blue, Ice, Vulnversity, Kenobi
5. HackTheBox "Starting Point" machines
6. VulnHub: Kioptrix, Mr. Robot, DC-1

LEVEL 3 — INTERMEDIATE:
7. HackTheBox Easy machines (retired)
8. TryHackMe: Overpass, Skynet, Internal
9. PortSwigger Web Security Academy (all labs!)

LEVEL 4 — ADVANCED:
10. HackTheBox Medium machines
11. Real CTF competitions (CTFtime.org)
12. OSCP-like machines (Proving Grounds)

LEVEL 5 — EXPERT:
13. HackTheBox Hard/Insane machines
14. Pro Labs (HackTheBox, OSCP)
15. Red team engagements
```

---

## 📜 Certifications Roadmap

```
CERTIFICATION PATH (Priority Order):

┌─────────────────────────────────────────────────┐
│  BEGINNER (0-6 months)                           │
├─────────────────────────────────────────────────┤
│  1. CompTIA Security+           → $392          │
│     → Foundation, most recognized               │
│     → Study: Professor Messer (FREE YouTube)     │
│                                                  │
│  2. eJPT (INE)                  → $249          │
│     → Practical exam, beginner-friendly          │
│     → Best value for money!                      │
│     → Study: INE free tier + TCM Academy         │
├─────────────────────────────────────────────────┤
│  INTERMEDIATE (6-12 months)                      │
├─────────────────────────────────────────────────┤
│  3. CEH (EC-Council)            → $1,199        │
│     → Industry standard, HR loves it             │
│     → Mostly theoretical                         │
│                                                  │
│  4. PNPT (TCM Security)        → $399           │
│     → Practical, affordable, respected           │
│     → Study: TCM Academy courses                 │
│                                                  │
│  5. CompTIA PenTest+            → $392          │
│     → Practical + knowledge-based               │
├─────────────────────────────────────────────────┤
│  ADVANCED (12+ months)                           │
├─────────────────────────────────────────────────┤
│  6. OSCP (Offensive Security)   → $1,649        │
│     → GOLD STANDARD in pentesting               │
│     → 24-hour practical exam                     │
│     → Study: 6-12 months prep needed            │
│                                                  │
│  7. CRTP/CRTO                   → $400-500      │
│     → Active Directory focused                   │
│     → Red team operations                        │
│                                                  │
│  8. OSWE/OSED/OSEP              → $1,649 each   │
│     → Advanced OffSec certs                      │
└─────────────────────────────────────────────────┘

RECOMMENDED ORDER FOR INDIA:
1. eJPT (affordable, practical, fast)
2. CompTIA Security+ (job requirement)
3. PNPT (great practical cert)
4. OSCP (career milestone)
```

---

## 💼 Career Paths in Cybersecurity

```
JOB ROLES & SALARIES (India):

ENTRY LEVEL (0-2 years):
├── SOC Analyst (L1)              → ₹4-8 LPA
├── Junior Penetration Tester     → ₹5-10 LPA
├── Security Analyst              → ₹5-8 LPA
├── Vulnerability Analyst         → ₹5-9 LPA
└── IT Security Associate        → ₹4-7 LPA

MID LEVEL (2-5 years):
├── Penetration Tester            → ₹10-20 LPA
├── SOC Analyst (L2/L3)           → ₹8-15 LPA
├── Security Engineer             → ₹12-25 LPA
├── Threat Hunter                 → ₹12-20 LPA
├── Incident Responder            → ₹10-18 LPA
└── Bug Bounty Hunter             → ₹10-50+ LPA

SENIOR LEVEL (5+ years):
├── Senior Pentester              → ₹20-40 LPA
├── Red Team Lead                 → ₹25-50 LPA
├── Security Architect            → ₹25-45 LPA
├── CISO                          → ₹40-1Cr+ LPA
└── Security Consultant           → ₹20-60 LPA

FREELANCE/REMOTE:
├── Bug Bounty (top hunters)      → $100K-500K+/year
├── Freelance Pentester           → $100-300/hour
└── Security Consultant           → $150-500/hour

TOP COMPANIES HIRING IN INDIA:
Deloitte, EY, KPMG, PwC, Accenture, IBM,
TCS, Infosys, Wipro, HCL, Cognizant,
CrowdStrike, Palo Alto, Fortinet, Cisco,
Amazon (AWS Security), Microsoft, Google,
Paytm, Razorpay, CRED, Flipkart
```

### How to Get Your First Job

```
1. BUILD YOUR PROFILE:
   - HackTheBox rank (at least Hacker level)
   - TryHackMe badges (complete learning paths)
   - Bug bounty hall of fame entries
   - CTF competition rankings
   - GitHub with security tools/scripts
   - Blog with writeups

2. GET CERTIFIED:
   - Start with eJPT or Security+
   - Certifications open doors for interviews

3. NETWORKING:
   - Join cybersecurity communities (Discord, Reddit)
   - Attend meetups and conferences (nullcon, c0c0n, BSides)
   - Follow security researchers on Twitter/LinkedIn
   - Contribute to open-source security projects

4. APPLY:
   - LinkedIn (search: "penetration tester", "security analyst")
   - Naukri.com
   - Indeed
   - Company career pages directly
   - Referrals from community connections

5. INTERVIEW PREP:
   - Practice explaining your methodology
   - Be ready to do live hacking demos
   - Know OWASP Top 10 inside out
   - Understand compliance (PCI DSS, ISO 27001, GDPR)
```

---

## 🎥 Phase 10 Videos

```
1. "Bug Bounty Hunting Course" — Nahamsec (Full Course FREE)
   https://www.youtube.com/watch?v=OVQhAL3MOwA

2. "How I Made $10,000 Bug Bounty" — STÖK
   https://www.youtube.com/watch?v=8I-3gR9C1K8

3. "Getting Started in Bug Bounty" — InsiderPhD
   https://www.youtube.com/watch?v=CU9Iacev-Og

4. "Cybersecurity Career Guide" — NetworkChuck
   https://www.youtube.com/watch?v=qMcyErvirTY

5. "OSCP Preparation Guide" — John Hammond
   https://www.youtube.com/watch?v=wjTt-5mfyhY

6. "How to Write Bug Bounty Reports" — Nahamsec
   https://www.youtube.com/watch?v=dkWkrSFUJp4

7. "Indian Hackers Success Stories" — Search on YouTube
   → Many Indian bug bounty hunters share their journey!
```

---

## 🎉 YOU MADE IT!

```
FROM ZERO → HACKER

What you now know:
✅ Linux mastery & bash scripting
✅ Python for hacking & automation
✅ Network attacks (MITM, WiFi, sniffing)
✅ Web exploitation (SQLi, XSS, SSRF, etc.)
✅ System hacking (Metasploit, priv esc)
✅ USB & physical attacks
✅ Mobile hacking (Android)
✅ Social engineering & phishing
✅ Malware analysis & C2 frameworks
✅ Bug bounty methodology
✅ Career path & certifications

WHAT TO DO NEXT:
1. 🏆 Join HackerOne & Bugcrowd — start hunting bugs
2. 📜 Get eJPT certification
3. 💻 Do 1 HackTheBox machine per week
4. 📝 Write CTF writeups on a blog
5. 🌐 Build your online presence (Twitter, LinkedIn)
6. 🤝 Join a security community
7. 💼 Apply for security jobs
8. 📚 Never stop learning!

Remember: ALWAYS hack ETHICALLY.
Use your powers for good. Be the white hat the world needs! 🏴‍☠️✅
```

---

> **The journey never ends. Keep learning, keep hacking, keep growing! 🚀**
