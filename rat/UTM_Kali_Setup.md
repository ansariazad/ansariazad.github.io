# 🖥️ UTM Kali Linux Setup Guide — Mac Optimization

> Tu UTM pe Kali Linux chala raha hai Mac pe. Yeh guide tera setup optimize karega.

---

## ⚙️ UTM Settings (Recommended)

### VM Configuration
```
CPU Cores:    4 (minimum 2)
RAM:          4 GB (minimum 2 GB, 8 GB ideal)
Storage:      40 GB+ (Kali takes ~20 GB with tools)
Display:      virtio-gpu-gl (best performance on Mac)
Network:      Shared Network (NAT) for internet
              OR Bridged for same network as host
```

### Network Modes

```
┌─────────────────────────────────────────────────┐
│  NAT (Shared Network) — DEFAULT                  │
│  ✅ Internet access                              │
│  ✅ Isolated from local network                  │
│  ❌ Can't scan local network devices             │
│  Best for: General use, online labs              │
├─────────────────────────────────────────────────┤
│  Bridged — Same network as Mac                   │
│  ✅ Gets its own IP on your network              │
│  ✅ Can scan local network devices               │
│  ✅ Other VMs can communicate                    │
│  Best for: Lab practice with other VMs           │
├─────────────────────────────────────────────────┤
│  Host-Only — Isolated network                    │
│  ✅ Only your Mac and VMs can communicate        │
│  ❌ No internet                                  │
│  Best for: Isolated lab (safest for practice)    │
└─────────────────────────────────────────────────┘
```

### Setting Up Lab Network

For best practice, use **multiple network interfaces**:
1. **NAT** — For internet (updates, downloads)
2. **Host-Only** — For lab communication with other VMs

---

## 🚀 First Things After Boot

### 1. Update Everything
```bash
sudo apt update && sudo apt full-upgrade -y
sudo apt autoremove -y
```

### 2. Change Default Password
```bash
# Default: kali / kali
passwd
# Enter new password
```

### 3. Set Timezone
```bash
sudo timedatectl set-timezone Asia/Kolkata
```

### 4. Install Essential Tools
```bash
# Extended Kali tools
sudo apt install -y kali-linux-large

# Or install specific categories:
sudo apt install -y kali-tools-web
sudo apt install -y kali-tools-passwords
sudo apt install -y kali-tools-information-gathering
sudo apt install -y kali-tools-vulnerability
sudo apt install -y kali-tools-exploitation

# Useful utilities
sudo apt install -y git curl wget tree htop net-tools terminator
sudo apt install -y python3-pip gobuster seclists wordlists
sudo apt install -y flameshot       # screenshot tool
```

### 5. Extract Wordlists
```bash
# rockyou.txt (most important wordlist)
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Install SecLists
sudo apt install -y seclists
```

### 6. Setup Aliases (Time savers!)
```bash
# Add to ~/.bashrc or ~/.zshrc
nano ~/.zshrc

# Add these lines:
alias ll='ls -la'
alias la='ls -A'
alias update='sudo apt update && sudo apt upgrade -y'
alias myip='ip addr show | grep "inet " | grep -v 127'
alias ports='sudo ss -tulnp'
alias scan='sudo nmap -sV -sC -T4'
alias fullscan='sudo nmap -sS -sV -sC -O -p- -T4'
alias serve='python3 -m http.server 8000'
alias listen='sudo nc -lvnp'
alias msf='sudo msfconsole -q'

# Apply changes
source ~/.zshrc
```

### 7. Configure Terminal (Terminator)
```bash
# Install Terminator (split terminal)
sudo apt install -y terminator

# Use Terminator instead of default terminal
# Ctrl+Shift+E → Split vertically
# Ctrl+Shift+O → Split horizontally
# Ctrl+Shift+W → Close pane
# Alt+Arrow    → Navigate panes
```

---

## 🧪 Setting Up Practice Lab VMs

### Metasploitable 2 (MUST HAVE!)
```
1. Download: https://sourceforge.net/projects/metasploitable/
2. Extract the ZIP file
3. In UTM: Create New VM → Other → Import VMDK
4. Settings:
   - CPU: 1 core
   - RAM: 512 MB
   - Network: Same network as Kali (Bridged or Host-Only)
5. Login: msfadmin / msfadmin
6. Find its IP: ifconfig (inside Metasploitable)
```

### DVWA (Inside Kali)
```bash
# Option 1: APT install
sudo apt install -y dvwa
# Access at: http://localhost/dvwa

# Option 2: Manual
cd /var/www/html
sudo git clone https://github.com/digininja/DVWA.git
sudo chmod -R 777 DVWA
sudo cp DVWA/config/config.inc.php.dist DVWA/config/config.inc.php
sudo nano DVWA/config/config.inc.php
# Change db_password to '' (empty) or your MySQL root password

sudo systemctl start apache2
sudo systemctl start mysql

# Setup MySQL:
sudo mysql -u root
CREATE DATABASE dvwa;
CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON dvwa.* TO 'dvwa'@'localhost';
FLUSH PRIVILEGES;
exit;

# Access: http://localhost/DVWA
# Login: admin / password
# Click "Create / Reset Database"
```

### OWASP Juice Shop
```bash
# Using Docker (recommended)
sudo apt install -y docker.io
sudo systemctl start docker
sudo docker pull bkimminich/juice-shop
sudo docker run -d -p 3000:3000 bkimminich/juice-shop
# Access: http://localhost:3000
```

### Other Vulnerable VMs (Download from VulnHub)
```
Beginner VMs:
- Kioptrix Level 1: https://www.vulnhub.com/entry/kioptrix-level-1-1,22/
- Mr. Robot: https://www.vulnhub.com/entry/mr-robot-1,151/
- DC-1: https://www.vulnhub.com/entry/dc-1,292/
- Basic Pentesting: https://www.vulnhub.com/entry/basic-pentesting-1,216/
```

---

## 🔧 Troubleshooting Common Issues

### No Internet in Kali VM
```bash
# Check network interface
ip a
# If no IP, try:
sudo dhclient eth0
# Or restart networking
sudo systemctl restart NetworkManager
# Check DNS
cat /etc/resolv.conf
# Add DNS if missing:
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

### Resolution / Display Issues
```bash
# Install SPICE tools (for better display)
sudo apt install -y spice-vdagent
sudo systemctl enable spice-vdagent
sudo systemctl start spice-vdagent

# Or use QXL driver
# In UTM: Display → Change to virtio-gpu-gl
```

### Slow Performance
```bash
# Allocate more RAM in UTM settings
# Use lightweight desktop: XFCE (default in Kali)
# Disable unnecessary services:
sudo systemctl disable bluetooth
sudo systemctl disable cups

# Use swap if low RAM:
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Can't Paste from Mac to Kali
```bash
# Install SPICE guest tools
sudo apt install -y spice-vdagent
sudo systemctl restart spice-vdagent

# If still not working, use shared folder:
# UTM → VM Settings → Sharing → Add shared directory
# Access in Kali at /mnt/shared
```

### USB WiFi Adapter Not Working
```
1. UTM → VM Settings → USB
2. Add your USB WiFi adapter
3. In Kali: iwconfig (check if detected)
4. If not detected, install drivers:
   sudo apt install -y realtek-rtl88xxau-dkms  # for Alfa adapters
   # Or:
   sudo apt install -y firmware-atheros        # for Atheros
```

---

## 📁 Recommended Folder Structure in Kali

```bash
# Create organized workspace
mkdir -p ~/hacking/{
    recon,
    scans,
    exploits,
    payloads,
    reports,
    scripts,
    wordlists,
    notes,
    ctf,
    tools
}

# Structure:
~/hacking/
├── recon/          → OSINT & recon results
├── scans/          → Nmap & vulnerability scans
├── exploits/       → Exploit code & PoCs
├── payloads/       → Generated payloads
├── reports/        → Pentest reports
├── scripts/        → Your custom scripts
├── wordlists/      → Custom wordlists
├── notes/          → Study notes
├── ctf/            → CTF challenges & writeups
└── tools/          → Downloaded tools
```

---

## 🔐 Security Best Practices for Your Lab

```
1. NEVER attack systems without permission
2. Keep lab VMs on isolated network (Host-Only)
3. Use VPN when doing online labs/CTFs
4. Don't store sensitive data in VMs
5. Take snapshots before experiments
6. Keep Kali updated
7. Use strong passwords
8. Don't expose your lab to the internet
```

### Taking VM Snapshots in UTM
```
1. Shut down the VM
2. Right-click VM in UTM sidebar
3. Click "Clone" or use snapshots
4. Take snapshot before risky operations
5. Revert if something breaks
```

---

> **Lab setup ho gaya? Ab [Week 1](./Week1_Linux_Basics.md) se shuru kar!** 🚀
