import json
from datetime import datetime
import requests

class SocialTracker:
    def __init__(self):
        self.platforms = {
            "facebook": "https://www.facebook.com/{}",
            "instagram": "https://www.instagram.com/{}",
            "twitter": "https://twitter.com/{}",
            "linkedin": "https://www.linkedin.com/in/{}",
            "github": "https://github.com/{}"
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }

    def search_username(self, username):
        """Cari username di berbagai platform"""
        username = username.strip()
        result = {
            "timestamp": datetime.now().isoformat(),
            "username": username,
            "platforms": {}
        }

        for platform, url_template in self.platforms.items():
            result["platforms"][platform] = self.check_platform(platform, username)

        return result

    def check_platform(self, platform, username):
        """Cek keberadaan username di platform"""
        profile_url = self.platforms[platform].format(username)
        
        try:
            # চাইলে নিচের কমেন্ট সরিয়ে লাইভ রিকুয়েস্ট চেক করতে পারেন, তবে সাধারণত সাইটগুলো ব্লক করে দিতে পারে
            # response = requests.get(profile_url, headers=self.headers, timeout=5)
            # exists = True if response.status_code == 200 else False
            
            return {
                "exists": "Checked (Simulated)",
                "url": profile_url,
                "status": "Active / Profile Link Generated",
                "details": "Success"
            }
        except Exception as e:
            return {
                "exists": False,
                "url": profile_url,
                "details": str(e)
            }
