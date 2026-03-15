# 🛒 Amazon Price Monitoring System (Pro)
**An automated Python-based scraping tool built to track high-value e-commerce items and dispatch real-time email alerts.**

---

### 📖 Project Overview
This project is an intelligent, console-based monitoring system designed to track dynamic product prices on Amazon India. It focuses on core automation principles: **Web Scraping**, **Anti-Bot Evasion**, and **Automated Communication**. It allows users to set a target budget and securely pushes notifications when the market price drops.

### 🛠️ Tech Stack & Skills
* **Language:** Python 3
* **Libraries:** `requests`, `BeautifulSoup4` (bs4), `smtplib`, `email.message`
* **Network Security:** Custom Header injection and Session management to bypass server-side bot detection algorithms.
* **Communication:** SMTP Protocol integration for secure, real-time email dispatch.

### 🚀 Key Technical Features
* **24/7 Background Tracking:** Implements an infinite execution loop with strategic time intervals to monitor prices around the clock without overloading the server.
* **Anti-Detection Mechanics:** Utilizes advanced browser headers (User-Agent, Accept-Encoding) and persistent HTTP sessions to mimic real human traffic and avoid IP blocks.
* **Robust Data Parsing:** Engineered with multi-layered CSS selectors (fallback mechanism) to ensure data extraction even if the website's HTML layout changes dynamically.
* **Real-Time SMTP Alerts:** Automatically authenticates with Google's SMTP servers to format and push detailed price-drop alerts directly to the user's inbox.

---

### 🛠️ How to Run
1. **Clone the Repository:**
   `git clone https://github.com/NishantScripts/Amazon-Price-Tracker-Pro.git`
2. **Install Dependencies:**
   Ensure you have Python installed, then run: `pip install requests beautifulsoup4`
3. **Configure the Script:**
   Open `main.py` and replace the placeholder credentials (`YOUR_EMAIL` and `YOUR_APP_PASSWORD`) with your actual Gmail and 16-digit App Password. Set your desired `PRODUCT_URL` and `TARGET_BUDGET`.
4. **Execute:**
   Run the script using the terminal: `python main.py`

---
*Developed by [NishantScripts](https://github.com/NishantScripts)*
