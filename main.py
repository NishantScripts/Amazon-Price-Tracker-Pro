"""
Amazon Price Monitoring System
Author: Nishant Walse
Description: An automated Python script to monitor Amazon product prices
             and send secure email alerts when the price drops below a target threshold.
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time
from email.message import EmailMessage

class AmazonPriceMonitor:
    """
    A robust web scraper and automation tool designed to bypass standard 
    bot-detection and track e-commerce pricing in real-time.
    """

    def __init__(self, product_url, target_budget):
        self.url = product_url
        self.budget = target_budget
        
        # ==========================================
        # SECURITY NOTICE: NEVER HARDCODE REAL PASSWORDS ON GITHUB
        # Replace these placeholders with your actual details on your local machine only.
        # ==========================================
        self.EMAIL_USER = "YOUR_EMAIL@gmail.com" 
        self.EMAIL_PASS = "YOUR_16_DIGIT_APP_PASSWORD" 
        
        # Advanced Headers to simulate a real user session
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        self.session = requests.Session()

    def fetch_market_data(self):
        """Scrapes the target URL and extracts the product name and current price."""
        try:
            # Human-like delay to prevent IP blocking
            time.sleep(2)
            response = self.session.get(self.url, headers=self.headers, timeout=30)
            
            if response.status_code != 200:
                return None

            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract Product Title
            title_node = soup.find(id="productTitle") or soup.find("h1")
            product_name = " ".join(title_node.get_text().strip().split()[:5]) if title_node else "Unknown Product"

            # Extract and Clean Price
            price = None
            price_selectors = [
                ("span", {"class": "a-price-whole"}), 
                ("span", {"class": "a-offscreen"})
            ]
            
            for tag, attr in price_selectors:
                element = soup.find(tag, attr)
                if element:
                    digits = "".join(filter(str.isdigit, element.get_text()))
                    if digits:
                        price = int(digits)
                        break
            
            return {"name": product_name, "price": price} if price else None
            
        except Exception as e:
            print(f"[SYSTEM ERROR] Data retrieval failed: {e}")
            return None

    def dispatch_alert(self, name, current_price):
        """Constructs and dispatches an SMTP email notification."""
        msg = EmailMessage()
        msg['Subject'] = f"📈 PRICE DROP ALERT: {name}"
        msg['From'] = self.EMAIL_USER
        msg['To'] = self.EMAIL_USER
        
        email_body = (
            f"Automated System Alert: Target threshold breached!\n\n"
            f"Product: {name}\n"
            f"Current Market Price: ₹{current_price:,}\n"
            f"Your Budget: ₹{self.budget:,}\n\n"
            f"Purchase Link: {self.url}\n\n"
            f"Maintained by Nishant's Python Automation Service."
        )
        msg.set_content(email_body)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.EMAIL_USER, self.EMAIL_PASS)
                server.send_message(msg)
            print(f"[SUCCESS] Alert dispatched successfully at {time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"[FAILURE] SMTP Authentication failed. Please check credentials. Error: {e}")

    def execute_tracking_loop(self):
        """Initializes the infinite background loop for 24/7 tracking."""
        print("\n" + "="*55)
        print("🟢 AUTOMATED PRICE MONITORING SYSTEM ACTIVE")
        print("="*55)
        
        while True:
            data = self.fetch_market_data()
            
            if data:
                print(f"[{time.strftime('%H:%M:%S')}] {data['name']} : ₹{data['price']:,}")
                
                if data['price'] <= self.budget:
                    print("[ACTION] Target criteria met. Executing alert protocol...")
                    self.dispatch_alert(data['name'], data['price'])
                else:
                    gap = data['price'] - self.budget
                    print(f"[{time.strftime('%H:%M:%S')}] Status: Holding. Price is ₹{gap:,} above budget.")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] [WARNING] Connection intercepted by host. Retrying later...")

            # Sleep interval set to 1 hour (3600 seconds) for production use
            print("💤 System pausing for 60 minutes...\n")
            time.sleep(3600)

# --- SYSTEM INITIALIZATION ---
if __name__ == "__main__":
    # Configure Target Product
    PRODUCT_URL = "https://www.amazon.in/dp/B0CHX1W1XY" 
    TARGET_BUDGET = 60000 
    
    tracker = AmazonPriceMonitor(PRODUCT_URL, TARGET_BUDGET)
    tracker.execute_tracking_loop()
          
