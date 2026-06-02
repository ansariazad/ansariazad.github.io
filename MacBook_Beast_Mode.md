# 🖥️ MacBook Air M3 — Beast Mode Setup Guide

> Tere MacBook ko premium, fast, aur hacker-level dikhana hai.
> Har step mein bataya hai kya hoga, kaise hoga, aur kyun karna hai.

---

## ⚡ TERA CURRENT SYSTEM

```
Model:    MacBook Air M3
RAM:      8 GB
macOS:    26.4.1 (Tahoe)
Shell:    Zsh (default)
Dock:     Auto-hide ON, Magnification ON, Size 34
```

---

## 📋 KYA KARENGE (Summary)

| # | Category | Kya Hoga | Time |
|---|----------|----------|------|
| 1 | Terminal Makeover | Hacker-style terminal with colors, icons, suggestions | 5 min |
| 2 | Dock & Desktop | Clean, minimal, premium dock | 2 min |
| 3 | System Speed | Faster animations, smooth experience | 2 min |
| 4 | Hot Corners | Mouse corners pe smart actions | 1 min |
| 5 | Finder Upgrade | Better file browsing experience | 2 min |
| 6 | Screenshots | Better screenshot settings | 1 min |
| 7 | Trackpad & Keyboard | Pro-level gestures & shortcuts | 2 min |
| 8 | Must-Have Apps | Free apps jo MacBook level up karein | 5 min |
| 9 | Menu Bar | Clean, useful menu bar | 2 min |
| 10 | Wallpaper & Theme | Dark mode + premium look | 1 min |

**Total: ~25 minutes mein MacBook transform!**

---

# STEP 1: 🖥️ TERMINAL MAKEOVER

### What We'll Install

```
Oh My Zsh          → Zsh framework (themes + plugins)
Powerlevel10k      → Premium theme (icons, git status, time, errors)
zsh-autosuggestions → Type karte waqt grey suggestions dikhega
zsh-syntax-highlighting → Sahi command = GREEN, galat = RED
Nerd Font          → Terminal mein icons dikhenge (folders, git, etc.)
```

### Before vs After

```
BEFORE (boring default):
azad@MacBook ~ %

AFTER (beast mode):
  ~/Desktop/Modify    main ✓  3.14  11:30
❯ 

Features:
├── Folder icon + path
├── Git branch + status (✓ = clean, ✗ = changes)  
├── Python version shown
├── Time on right side
├── Error indicator (red ✗ if last command failed)
├── Auto-suggestions in grey as you type
└── Commands color-coded (green=valid, red=invalid)
```

### Commands to Run

```bash
# 1. Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 2. Install Powerlevel10k theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# 3. Install plugins
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# 4. Install Nerd Font (for icons in terminal)
brew install --cask font-meslo-lg-nerd-font

# 5. Update ~/.zshrc
# Change these lines:
#   ZSH_THEME="powerlevel10k/powerlevel10k"
#   plugins=(git zsh-autosuggestions zsh-syntax-highlighting web-search sudo copypath)

# 6. Restart terminal → Powerlevel10k wizard will start
# Choose your style!

# 7. Set terminal font
# Terminal.app → Settings → Profiles → Font → "MesloLGS NF" size 13
# OR
# iTerm2 → Preferences → Profiles → Text → Font → "MesloLGS NF"
```

### Useful Zsh Aliases to Add

```bash
# Add these to ~/.zshrc at the bottom:

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'

# Quick opens
alias o='open .'                    # open current folder in Finder
alias c='clear'
alias h='history'
alias p='python3'

# Git shortcuts
alias gs='git status'
alias ga='git add .'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline -20'

# System
alias ip='curl -s ifconfig.me'     # show public IP
alias localip='ipconfig getifaddr en0'
alias ports='lsof -i -P -n | grep LISTEN'
alias cpu='top -l 1 | head -5'
alias mem='vm_stat | head -5'
alias battery='pmset -g batt'
alias wifi='networksetup -getairportnetwork en0'

# Cleanup
alias cleanup='find . -name ".DS_Store" -delete'
alias emptytrash='rm -rf ~/.Trash/*'

# Fun
alias matrix='cmatrix'             # needs: brew install cmatrix
alias weather='curl wttr.in'       # weather in terminal!
alias moon='curl wttr.in/Moon'     # moon phase
```

---

# STEP 2: 🎨 DOCK & DESKTOP

### What Changes

```
BEFORE: Big dock, lots of apps, bouncing icons, slow animations
AFTER:  Small sleek dock, only essential apps, smooth & fast
```

### Commands

```bash
# ═══════════════════════════════════════════════
# DOCK — Premium Look
# ═══════════════════════════════════════════════

# Dock size (36 = perfect balance)
defaults write com.apple.dock tilesize -int 36

# Magnification on hover (bigger when you hover)
defaults write com.apple.dock magnification -bool true
defaults write com.apple.dock largesize -int 54

# Auto-hide dock (more screen space!)
defaults write com.apple.dock autohide -bool true

# Remove auto-hide delay (INSTANT show/hide!)
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.3

# Minimize effect: "scale" is cleaner than "genie"
defaults write com.apple.dock mineffect -string "scale"

# Don't show recent apps in dock (cleaner!)
defaults write com.apple.dock show-recents -bool false

# Don't animate opening apps (no bouncing!)
defaults write com.apple.dock launchanim -bool false

# Show indicator dots for open apps
defaults write com.apple.dock show-process-indicators -bool true

# Add spacers in dock (organize sections)
# Small spacer:
defaults write com.apple.dock persistent-apps -array-add '{"tile-type"="small-spacer-tile";}'

# ═══════════════════════════════════════════════
# Apply dock changes
# ═══════════════════════════════════════════════
killall Dock
```

### Recommended Dock Apps (Remove rest!)

```
Keep ONLY these in dock:
1. Finder
2. Safari / Chrome
3. Terminal / iTerm2
4. VS Code / your editor
5. Notes
6. Settings
7. Files (Downloads folder as stack)

Remove everything else → access from Launchpad (F4)
```

---

# STEP 3: ⚡ SYSTEM SPEED TWEAKS

### What Changes

```
BEFORE: Smooth but slow animations, delays everywhere
AFTER:  Snappy, instant response, feels 2x faster
```

### Commands

```bash
# ═══════════════════════════════════════════════
# SPEED UP ANIMATIONS
# ═══════════════════════════════════════════════

# Faster window resize animations
defaults write NSGlobalDomain NSWindowResizeTime -float 0.1

# Speed up Mission Control animation
defaults write com.apple.dock expose-animation-duration -float 0.12

# Faster Launchpad animations
defaults write com.apple.dock springboard-show-duration -float 0.1
defaults write com.apple.dock springboard-hide-duration -float 0.1

# Disable window opening animation
defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false

# Speed up dialog boxes
defaults write NSGlobalDomain NSWindowResizeTime 0.1

# ═══════════════════════════════════════════════
# KEYBOARD — FASTER TYPING
# ═══════════════════════════════════════════════

# Fastest key repeat rate (hold a key = fast repeating)
defaults write NSGlobalDomain KeyRepeat -int 1
defaults write NSGlobalDomain InitialKeyRepeat -int 10

# Disable auto-correct (annoying for coders!)
defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false

# Disable auto-capitalization
defaults write NSGlobalDomain NSAutomaticCapitalizationEnabled -bool false

# Disable smart quotes & dashes (breaks code!)
defaults write NSGlobalDomain NSAutomaticQuoteSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticDashSubstitutionEnabled -bool false

# ═══════════════════════════════════════════════
# SCROLLING
# ═══════════════════════════════════════════════

# Smooth scrolling
defaults write NSGlobalDomain NSScrollAnimationEnabled -bool true

# Show scroll bars: Always / WhenScrolling / Automatic
defaults write NSGlobalDomain AppleShowScrollBars -string "WhenScrolling"
```

---

# STEP 4: 🔲 HOT CORNERS

### What Are Hot Corners?

```
Move mouse to screen corner → action triggers!

Recommended Setup:
┌─────────────────────────────────┐
│ Mission Control    Quick Note   │
│ (top-left)         (top-right)  │
│                                 │
│                                 │
│ Desktop            Lock Screen  │
│ (bottom-left)      (bottom-right)│
└─────────────────────────────────┘
```

### How to Set

```
System Settings → Desktop & Dock → scroll down → Hot Corners...

Set:
- Top Left:      Mission Control (see all windows)
- Top Right:     Quick Note (instant notes)
- Bottom Left:   Desktop (show desktop instantly)
- Bottom Right:  Lock Screen (security!)
```

### Or via Terminal

```bash
# Top Left → Mission Control (2)
defaults write com.apple.dock wvous-tl-corner -int 2
defaults write com.apple.dock wvous-tl-modifier -int 0

# Top Right → Quick Note (14) 
defaults write com.apple.dock wvous-tr-corner -int 14
defaults write com.apple.dock wvous-tr-modifier -int 0

# Bottom Left → Desktop (4)
defaults write com.apple.dock wvous-bl-corner -int 4
defaults write com.apple.dock wvous-bl-modifier -int 0

# Bottom Right → Lock Screen (13)
defaults write com.apple.dock wvous-br-corner -int 13
defaults write com.apple.dock wvous-br-modifier -int 0

killall Dock
```

---

# STEP 5: 📁 FINDER UPGRADE

### Commands

```bash
# ═══════════════════════════════════════════════
# FINDER — Make it Actually Useful
# ═══════════════════════════════════════════════

# Show file extensions
defaults write NSGlobalDomain AppleShowAllExtensions -bool true

# Show hidden files (dotfiles)
defaults write com.apple.finder AppleShowAllFiles -bool true

# Show path bar at bottom
defaults write com.apple.finder ShowPathbar -bool true

# Show status bar (file count & size)
defaults write com.apple.finder ShowStatusBar -bool true

# Show full path in title bar
defaults write com.apple.finder _FXShowPosixPathInTitle -bool true

# Default to list view (cleanest!)
defaults write com.apple.finder FXPreferredViewStyle -string "Nlsv"

# Search current folder by default (not entire Mac)
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"

# Don't create .DS_Store on USB/network drives
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true

# New Finder window opens Home folder
defaults write com.apple.finder NewWindowTarget -string "PfHm"

# Apply
killall Finder
```

### Finder Keyboard Shortcuts

```
Cmd + Shift + .     → Show/hide hidden files
Cmd + Shift + G     → Go to folder (type path)
Cmd + I             → Get Info
Cmd + Shift + N     → New folder
Space               → Quick Look (preview file)
Cmd + Delete        → Move to Trash
Cmd + Shift + Delete → Empty Trash
```

---

# STEP 6: 📸 SCREENSHOT SETTINGS

### Commands

```bash
# ═══════════════════════════════════════════════
# SCREENSHOTS — Better Defaults
# ═══════════════════════════════════════════════

# Save screenshots to a dedicated folder
mkdir -p ~/Desktop/Screenshots
defaults write com.apple.screencapture location -string "~/Desktop/Screenshots"

# Save as PNG (best quality) — or "jpg" for smaller
defaults write com.apple.screencapture type -string "png"

# Remove shadow from window screenshots
defaults write com.apple.screencapture disable-shadow -bool true

# Don't show floating thumbnail after screenshot
defaults write com.apple.screencapture show-thumbnail -bool false

# Apply
killall SystemUIServer
```

### Screenshot Shortcuts

```
Cmd + Shift + 3     → Full screen screenshot
Cmd + Shift + 4     → Select area screenshot
Cmd + Shift + 4 + Space → Window screenshot
Cmd + Shift + 5     → Screenshot toolbar (record too!)
```

---

# STEP 7: 🖱️ TRACKPAD & KEYBOARD

### Trackpad Settings (System Settings → Trackpad)

```
ENABLE THESE:
✅ Tap to Click (tap instead of press — way faster!)
✅ Three-finger drag (Settings → Accessibility → Pointer → Trackpad Options)
✅ Swipe between pages (2 fingers)
✅ Swipe between desktops (3 fingers)
✅ Mission Control (3 fingers up)
✅ App Exposé (3 fingers down)
✅ Pinch to zoom
✅ Smart zoom (double-tap with 2 fingers)
✅ Rotate

TRACKING SPEED:
→ Set to 7-8 out of 10 (fast!)
```

### Terminal Commands

```bash
# Enable tap to click
defaults write com.apple.AppleMultitouchTrackpad Clicking -bool true

# Fastest tracking speed (0-3, 3 = fastest)
defaults write NSGlobalDomain com.apple.trackpad.scaling -float 2.5

# Enable three-finger drag
defaults write com.apple.AppleMultitouchTrackpad TrackpadThreeFingerDrag -bool true
```

### Essential Keyboard Shortcuts

```
MUST KNOW:
Cmd + Space         → Spotlight (or Raycast)
Cmd + Tab           → Switch apps
Cmd + `             → Switch windows of same app
Cmd + Q             → Quit app
Cmd + W             → Close window/tab
Cmd + T             → New tab
Cmd + N             → New window
Cmd + ,             → App preferences
Cmd + H             → Hide app
Cmd + M             → Minimize window
Cmd + Ctrl + F      → Full screen toggle
Cmd + Option + Esc  → Force quit

PRO:
Ctrl + Space        → Switch input language
Ctrl + Cmd + Space  → Emoji picker 😎
Cmd + Shift + 5     → Screenshot/record toolbar
Cmd + L (in browser)→ Jump to URL bar
```

---

# STEP 8: 📦 MUST-HAVE APPS (All FREE!)

### 1. Rectangle — Window Management ⭐⭐⭐

```
WHAT: Snap windows to half/quarter screen with keyboard shortcuts
WHY:  macOS default window management sucks, this fixes it

Install: brew install --cask rectangle

Shortcuts:
Ctrl + Option + ←     → Left half
Ctrl + Option + →     → Right half
Ctrl + Option + ↑     → Top half  
Ctrl + Option + ↓     → Bottom half
Ctrl + Option + Enter → Full screen
Ctrl + Option + U     → Top-left quarter
Ctrl + Option + I     → Top-right quarter
Ctrl + Option + J     → Bottom-left quarter
Ctrl + Option + K     → Bottom-right quarter
Ctrl + Option + C     → Center window
```

### 2. AltTab — Better App Switcher

```
WHAT: Windows-style Alt+Tab with window previews
WHY:  Default Cmd+Tab only shows app icons, not windows

Install: brew install --cask alt-tab

After install: Shows actual window previews when switching!
```

### 3. Stats — System Monitor in Menu Bar

```
WHAT: Shows CPU, RAM, Network, Battery, Disk in menu bar
WHY:  Always know what your Mac is doing

Install: brew install --cask stats

Shows: CPU %, RAM usage, Network speed, Battery health, Temperature
```

### 4. Raycast — Spotlight Replacement

```
WHAT: 10x better than Spotlight
WHY:  Calculator, clipboard history, snippets, window management, AI

Install: brew install --cask raycast

Features:
- File search (faster than Spotlight)
- Calculator (type "34 * 56" directly)
- Clipboard history (see everything you copied!)
- Snippets (type shortcuts → expand to full text)
- Window management built-in
- App launcher
- Web search shortcuts

Replace Spotlight:
System Settings → Keyboard → Keyboard Shortcuts → Spotlight → OFF
Raycast → Settings → Hotkey → Cmd + Space
```

### 5. iTerm2 — Better Terminal (Optional)

```
WHAT: Terminal replacement with split panes, search, profiles
WHY:  More features than default Terminal.app

Install: brew install --cask iterm2

Best settings:
- Theme: "Minimal" (Settings → Appearance → Theme)
- Font: "MesloLGS NF" 13pt
- Color scheme: "Solarized Dark" or "Dracula"
- Transparency: 5-10%
- Blur: ON
```

### 6. Hidden Bar — Menu Bar Cleanup

```
WHAT: Hide menu bar icons you don't need
WHY:  Clean, minimal menu bar

Install: brew install --cask hiddenbar

Usage: Drag icons left/right of the divider to show/hide
```

### 7. IINA — Best Video Player

```
WHAT: Beautiful modern video player (replaces VLC)
WHY:  Native macOS design, plays everything

Install: brew install --cask iina
```

### 8. AppCleaner — Uninstall Apps Properly

```
WHAT: Drag app to trash → deletes ALL related files
WHY:  Normal delete leaves junk files behind

Install: brew install --cask appcleaner
```

### Install All at Once

```bash
brew install --cask rectangle alt-tab stats raycast hiddenbar iina appcleaner
```

---

# STEP 9: 📊 MENU BAR

### Clean Menu Bar Setup

```
LEFT SIDE (Apple keeps):
 Apple menu → Notch → App name

RIGHT SIDE (your control):
 Hidden Bar | Stats (CPU/RAM) | WiFi | Battery | Time | Control Center

HIDE these (drag into Hidden Bar):
- Siri
- Spotlight (if using Raycast)
- Any app icons you don't need
```

### Battery Percentage

```bash
# Show battery percentage in menu bar
defaults write com.apple.menuextra.battery ShowPercent -string "YES"
```

### Clock Format

```
System Settings → Control Center → Clock → 
- Show date: Always
- Show day of week: ON
- Time format: 24-hour or 12-hour (your choice)
```

---

# STEP 10: 🎨 DARK MODE & WALLPAPER

### Dark Mode

```
System Settings → Appearance → Dark

OR auto switch:
System Settings → Appearance → Auto
(Light during day, dark at night)
```

### Accent Color

```
System Settings → Appearance → Accent color
Recommended: Multicolor (changes per app) or Graphite (minimal)
```

### Premium Wallpapers (FREE)

```
Wallpaper Sources:
├── Built-in: System Settings → Wallpaper → Dynamic Desktop
│   → "Sequoia" and "Tahoe" look amazing!
│
├── Unsplash: https://unsplash.com/wallpapers/desktop/mac
│   → Search: "dark minimal", "abstract", "gradient"
│
├── Wallhaven: https://wallhaven.cc
│   → Best wallpaper site, filter by resolution
│
├── Dynamic Wallpapers (change with time):
│   → https://dynamicwallpaper.club (free downloads)
│
└── Hacker Aesthetic:
    → Search: "cyberpunk wallpaper 4k", "dark code wallpaper"
```

---

# 🚀 QUICK INSTALL — ALL IN ONE SCRIPT

```bash
#!/bin/bash
echo "=== MacBook Beast Mode Activated ==="

# ── DOCK ──
defaults write com.apple.dock tilesize -int 36
defaults write com.apple.dock magnification -bool true
defaults write com.apple.dock largesize -int 54
defaults write com.apple.dock autohide -bool true
defaults write com.apple.dock autohide-delay -float 0
defaults write com.apple.dock autohide-time-modifier -float 0.3
defaults write com.apple.dock mineffect -string "scale"
defaults write com.apple.dock show-recents -bool false
defaults write com.apple.dock launchanim -bool false

# ── HOT CORNERS ──
defaults write com.apple.dock wvous-tl-corner -int 2
defaults write com.apple.dock wvous-tl-modifier -int 0
defaults write com.apple.dock wvous-tr-corner -int 14
defaults write com.apple.dock wvous-tr-modifier -int 0
defaults write com.apple.dock wvous-bl-corner -int 4
defaults write com.apple.dock wvous-bl-modifier -int 0
defaults write com.apple.dock wvous-br-corner -int 13
defaults write com.apple.dock wvous-br-modifier -int 0

# ── SPEED ──
defaults write com.apple.dock expose-animation-duration -float 0.12
defaults write com.apple.dock springboard-show-duration -float 0.1
defaults write com.apple.dock springboard-hide-duration -float 0.1
defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false
defaults write NSGlobalDomain NSWindowResizeTime -float 0.1
defaults write NSGlobalDomain KeyRepeat -int 1
defaults write NSGlobalDomain InitialKeyRepeat -int 10

# ── TYPING ──
defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticCapitalizationEnabled -bool false
defaults write NSGlobalDomain NSAutomaticQuoteSubstitutionEnabled -bool false
defaults write NSGlobalDomain NSAutomaticDashSubstitutionEnabled -bool false

# ── FINDER ──
defaults write NSGlobalDomain AppleShowAllExtensions -bool true
defaults write com.apple.finder AppleShowAllFiles -bool true
defaults write com.apple.finder ShowPathbar -bool true
defaults write com.apple.finder ShowStatusBar -bool true
defaults write com.apple.finder FXPreferredViewStyle -string "Nlsv"
defaults write com.apple.finder FXDefaultSearchScope -string "SCcf"
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true
defaults write com.apple.desktopservices DSDontWriteUSBStores -bool true

# ── SCREENSHOTS ──
mkdir -p ~/Desktop/Screenshots
defaults write com.apple.screencapture location -string "~/Desktop/Screenshots"
defaults write com.apple.screencapture type -string "png"
defaults write com.apple.screencapture disable-shadow -bool true

# ── TRACKPAD ──
defaults write com.apple.AppleMultitouchTrackpad Clicking -bool true

# ── APPLY ALL ──
killall Dock
killall Finder
killall SystemUIServer

echo ""
echo "=== DONE! MacBook is now in Beast Mode! ==="
echo ""
echo "Next steps:"
echo "1. Install apps: brew install --cask rectangle alt-tab stats raycast hiddenbar iina appcleaner"
echo "2. Install Oh My Zsh: sh -c \"\$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\""
echo "3. Restart your Mac for all changes to take effect"
```

---

# ⚡ KEYBOARD SHORTCUTS CHEATSHEET

```
WINDOW MANAGEMENT (after Rectangle install):
Ctrl+Opt+←    Left half         Ctrl+Opt+→    Right half
Ctrl+Opt+↑    Top half          Ctrl+Opt+↓    Bottom half
Ctrl+Opt+Enter Fullscreen       Ctrl+Opt+C    Center
Ctrl+Opt+U    Top-left          Ctrl+Opt+I    Top-right
Ctrl+Opt+J    Bottom-left       Ctrl+Opt+K    Bottom-right

SYSTEM:
Cmd+Space     Spotlight/Raycast  Cmd+Tab      Switch apps
Cmd+Q         Quit app          Cmd+W        Close window
Cmd+H         Hide app          Cmd+M        Minimize
Cmd+,         Preferences       Cmd+Ctrl+F   Full screen
Cmd+Opt+Esc   Force Quit        Ctrl+Cmd+Q   Lock screen

SCREENSHOTS:
Cmd+Shift+3   Full screen       Cmd+Shift+4   Select area
Cmd+Shift+4+Space  Window       Cmd+Shift+5   Toolbar

FINDER:
Cmd+Shift+.   Show hidden       Space         Quick Look
Cmd+Shift+G   Go to path        Cmd+Delete    Move to trash

TERMINAL:
Cmd+T         New tab           Cmd+D         Split pane (iTerm)
Ctrl+C        Cancel command    Ctrl+R        Search history
Tab           Auto-complete     Ctrl+L        Clear screen
```

---

> **Guide padh liya? Bol "implement" toh sab run kar dunga!** 🚀
> Main pehle system settings karunga, phir apps install, phir terminal setup.
