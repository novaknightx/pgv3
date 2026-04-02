# 🛡️ PhishGuard — Phishing Detection Tool
### No API keys required · Runs 100% locally

---

## What it does

PhishGuard detects phishing emails and URLs using:

- **15+ heuristic checks** (instant, no network needed)
- **Levenshtein distance** — typosquatting & brand spoofing detection
- **Homoglyph detection** — look-alike characters (paypa1 → paypal)
- **RDAP/WHOIS lookup** — free public API, no key needed
- **Google DNS over HTTPS** — free, no key needed
- **Shannon entropy scoring** — detects auto-generated domains
- **Disposable domain database** — 20+ known throwaway providers

---

## Files

```
phishguard/
├── index.html    ← The app (open this in browser)
├── server.py     ← Optional Python server (recommended)
└── README.md     ← This file
```

---

## How to Run

### Option 1 — Simplest (just open the file)
Double-click `index.html` or drag it into any browser.
> ⚠ RDAP/DNS lookups may be blocked by CORS in some browsers with file:// URLs.
> Use Option 2 for full functionality.

---

### Option 2 — Python Server (Recommended ✅)

**Requirements:** Python 3 (comes pre-installed on Mac/Linux; download from python.org for Windows)

**In Terminal (Mac/Linux):**
```bash
# 1. Go to the phishguard folder
cd path/to/phishguard

# 2. Run the server
python3 server.py

# Browser opens automatically at http://localhost:8080
```

**In Terminal (Windows):**
```cmd
cd path\to\phishguard
python server.py
```

**To stop:** Press `Ctrl + C` in the terminal.

---

### Option 3 — VS Code (Live Server Extension)

1. Open VS Code
2. Open the `phishguard` folder: **File → Open Folder**
3. Install the **Live Server** extension:
   - Click Extensions icon (or press `Ctrl+Shift+X`)
   - Search: `Live Server`
   - Install by **Ritwick Dey**
4. Right-click `index.html` in the Explorer panel
5. Select **"Open with Live Server"**
6. App opens at `http://127.0.0.1:5500`

---

### Option 4 — VS Code Terminal (built-in)

1. Open VS Code
2. Open the `phishguard` folder
3. Open terminal: **Terminal → New Terminal** (or `` Ctrl+` ``)
4. Run:
   ```bash
   python3 server.py
   ```
5. Open browser at `http://localhost:8080`

---

### Option 5 — Node.js (if you have it)

```bash
cd path/to/phishguard
npx serve .
# Opens at http://localhost:3000
```

---

## Testing It

Try these examples to see it working:

**Phishing email examples:**
- `security-alert@paypa1-verify.xyz` (typosquatting)
- `noreply@amazon-account-suspended.tk` (suspicious TLD)
- `support@10minutemail.com` (disposable domain)

**Phishing URL examples:**
- `http://paypal.com.verify-account.xyz/login` (brand in subdomain)
- `http://192.168.1.1/secure/login.php` (IP-based URL)
- `https://paypa1.com/signin` (homoglyph: 1 instead of l)

**Legitimate examples:**
- `hello@github.com`
- `https://www.google.com`

---

## How the Scoring Works

| Score | Verdict     |
|-------|-------------|
| 0–9   | LEGITIMATE  |
| 10–29 | UNKNOWN     |
| 30–59 | SUSPICIOUS  |
| 60+   | PHISHING    |

Risk factors are weighted:
- IP-based URL: +35 points
- Typosquatting detected: +30–35 points
- Disposable email domain: +40 points
- Suspicious TLD: +18–22 points
- Domain < 30 days old: +20 points (from RDAP)
- No MX records: +10 points (from DNS)
- Homoglyph characters: +25–28 points

---

## No Internet? Offline Mode

The heuristic checks (brand spoofing, TLD check, structure analysis) work
completely offline. RDAP and DNS lookups require internet but the tool
still gives useful results without them.

---

## Privacy

All analysis happens locally in your browser. No data is sent to any
third-party servers except:
- `rdap.org` — domain registration lookup (no account needed)
- `dns.google` — DNS resolution (Google's public DNS)

Neither service logs your queries in a personally identifiable way.
