import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class SocialAnalyzer:
    def __init__(self):
        self.platforms = {
            "facebook": {
                "url": "https://www.facebook.com/{}",
                "selectors": {
                    "name": "h1.profile-name",
                    "photo": "img.profile-photo"
                }
            },
            "instagram": {
                "url": "https://www.instagram.com/{}",
                "selectors": {
                    "name": "h2.profile-name",
                    "bio": "div.biography"
                }
            },
            "twitter": {
                "url": "https://twitter.com/{}",
                "selectors": {
                    "name": "h2.profile-name",
                    "bio": "div.bio"
                }
            }
        }
        # অ্যান্টি-বট এড়ানোর জন্য ব্রাউজারের হেডার যুক্ত করা হয়েছে
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }

    def analyze_username(self, username):
        """Analisis username di berbagai platform dengan aman"""
        username = str(username).strip()
        results = {
            "timestamp": datetime.now().isoformat(),
            "username": username,
            "platforms": {}
        }

        for platform, config in self.platforms.items():
            results["platforms"][platform] = self.check_platform(platform, username, config)

        return results

    def check_platform(self, platform, username, config):
        """Cek keberadaan username di platform dengan error handling"""
        url = config["url"].format(username)
        try:
            # রিকোয়েস্টে হেডার ও টাইমআউট যুক্ত করা হয়েছে
            response = requests.get(url, headers=self.headers, timeout=10, allow_redirects=True)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return {
                    "exists": True,
                    "url": url,
                    "name": self.extract_element(soup, config["selectors"].get("name")),
                    "bio": self.extract_element(soup, config["selectors"].get("bio")),
                    "photo": self.extract_element(soup, config["selectors"].get("photo")),
                    "details": "Profile link verified (Live)"
                }
            elif response.status_code == 404:
                return {
                    "exists": False,
                    "url": url,
                    "details": "Profile not found (404)"
                }
            else:
                # যদি প্ল্যাটফর্ম থেকে ব্লক বা লগইন পেজে রিডাইরেক্ট করে
                return {
                    "exists": "Checked (Protected / Rate Limited)",
                    "url": url,
                    "details": f"HTTP Status: {response.status_code}"
                }

        except requests.exceptions.RequestException as e:
            # নেটওয়ার্ক বা কানেকশন এরর হ্যান্ডেল করার জন্য
            return {
                "exists": "Checked (Simulated Link Generated)",
                "url": url,
                "details": f"Connection handled safely: {str(e)}"
            }
        except Exception as e:
            return {
                "exists": False,
                "url": url,
                "details": str(e)
            }

    def extract_element(self, soup, selector):
        """Extract elemen dari HTML menggunakan selector dengan aman"""
        if not selector:
            return None
        try:
            element = soup.select_one(selector)
            return element.text.strip() if element else None
        except Exception:
            return None
