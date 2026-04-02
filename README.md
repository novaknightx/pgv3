# 🛡️ PhishGuard — Smart Phishing Detection Tool

## 📌 Overview

PhishGuard is a lightweight, browser-based tool designed to detect phishing emails and malicious URLs in real time. It works without requiring any API keys and performs analysis directly in the user’s browser, making it fast, private, and easy to use.

The main goal of this project is to help users identify suspicious links and emails before they fall victim to cyber attacks.

---

## 🚀 Features

* Detects phishing emails and URLs instantly
* Uses multiple heuristic checks for better accuracy
* Identifies typosquatting (e.g., paypa1 instead of paypal)
* Detects suspicious domains and fake structures
* Works completely offline for basic analysis
* No login or API key required

---

## 🧠 How It Works

PhishGuard analyzes inputs using a combination of techniques:

* **Heuristic Analysis** → Checks patterns commonly used in phishing
* **String Similarity (Levenshtein Distance)** → Detects fake domains
* **Entropy Calculation** → Identifies random or auto-generated domains
* **DNS & Domain Checks** → Verifies domain validity
* **Blacklist Matching** → Detects disposable or risky domains

Each factor contributes to a risk score, which determines whether the input is:

* Legitimate
* Suspicious
* Phishing

---

## 💻 Tech Stack

* HTML, CSS, JavaScript (Frontend)
* Python (optional local server)
* Public APIs (DNS, RDAP)

---

## 📂 Project Structure

```
phishguard/
├── index.html      # Main application
├── 404.html        # Error page
├── _config.yml     # GitHub Pages config
├── README.md       # Project documentation
├── server.py       # Optional local server
```

---

## ▶️ How to Run

### Option 1 — Directly in Browser

Simply open `index.html` in any browser.

### Option 2 — Using Local Server (Recommended)

```bash
python server.py
```

Then open:

```
http://localhost:8080
```

---

## 🌐 Live Demo

Once hosted on GitHub Pages:

```
https://your-username.github.io/phishguard
```

---

## 🎯 Purpose of the Project

This project was built to demonstrate practical implementation of cybersecurity concepts using simple web technologies. It focuses on real-world phishing detection techniques that are commonly used in modern security systems.

---

## 🔐 Privacy

All analysis is performed locally in the browser. No personal data is stored or sent to external servers.

---

## 📌 Future Improvements

* Machine learning-based detection model
* Browser extension integration
* Real-time threat intelligence APIs
* Improved UI/UX and dashboard

---

## 👤 Author

Dude Aravind
B.Tech AI & ML

---

## ⭐ Final Note

PhishGuard is a simple but effective tool that shows how intelligent detection systems can be built without heavy infrastructure. It focuses on practical usability and real-world application rather than complexity.
