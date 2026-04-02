# 🛡️ PhishGuard — GitHub Pages Hosting Guide

## How to host PhishGuard for FREE on GitHub Pages
Your app will be live at: `https://YOUR-USERNAME.github.io/phishguard`

---

## Step 1 — Create a GitHub account (if you don't have one)
1. Go to https://github.com
2. Click "Sign up"
3. Choose a username, enter email and password
4. Verify your email

---

## Step 2 — Create a new repository
1. Click the **+** button (top right) → "New repository"
2. Repository name: `phishguard`
3. Make it **Public** (required for free GitHub Pages)
4. Check "Add a README file"
5. Click **Create repository**

---

## Step 3 — Upload your files

### Option A — Upload via browser (easiest, no Git needed)
1. Inside your new repository, click **"Add file"** → **"Upload files"**
2. Drag and drop ALL these files from the phishguard folder:
   - index.html
   - 404.html
   - _config.yml
   - README.md
3. Scroll down, click **"Commit changes"**

### Option B — Using Git in terminal
```bash
cd path/to/phishguard

git init
git add .
git commit -m "Initial commit — PhishGuard v5"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/phishguard.git
git push -u origin main
```

---

## Step 4 — Enable GitHub Pages
1. In your repository, click **Settings** (top menu)
2. Click **Pages** in the left sidebar
3. Under "Source" → select **Deploy from a branch**
4. Branch: **main** | Folder: **/ (root)**
5. Click **Save**

Wait about 60 seconds. Your site is now live at:
**https://YOUR-USERNAME.github.io/phishguard**

---

## Step 5 — Test it
Open your browser and go to your URL. Try:
- `support@google.com` → should be SAFE (whitelist match)
- `paypa1-verify@secure-login.xyz` → should be PHISHING
- `sunnyy@gmail.com` → should be DOMAIN NOT FOUND
- `https://bit.ly/3xyz` → should flag as URL shortener

---

## How to update after making changes
```bash
git add index.html
git commit -m "Update: what you changed"
git push
```
GitHub Pages auto-rebuilds within 60 seconds.

---

## Limitations on GitHub Pages

| Feature | Status on GitHub Pages |
|---|---|
| All heuristic checks | Works perfectly |
| Google DNS (dns.google) | Works |
| crt.sh cert transparency | Works |
| ML scoring & feedback | Works (localStorage) |
| RDAP domain age | May be blocked by CORS |
| ip-api.com geolocation | Blocked (uses HTTP not HTTPS) |
| Redirect probe | Blocked by CORS |

The app gives strong results even without these — heuristics + DNS + ML cover the most important signals.

---

## Troubleshooting

**Site shows 404** — Wait 2-3 min after enabling Pages. Check repo is Public and index.html is in root.

**Changes not showing** — Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac). Pages can cache up to 10 minutes.

**"Page build failed" email** — Delete _config.yml, the site works fine without it.
