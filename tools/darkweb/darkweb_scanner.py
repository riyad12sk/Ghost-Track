import requests
import json
from datetime import datetime
import hashlib

class DarkWebScanner:
    def __init__(self, api_key=None, use_proxy=False, proxy_url="socks5://127.0.0.1:9050"):
        self.api_key = api_key
        self.use_proxy = use_proxy
        self.proxy_url = proxy_url
        # ডামি এন্ডপয়েন্টগুলো কনফিগার করা আছে, পরবর্তীতে রিয়েল এপিআই বা অনিয়ন রাউটিং লিংক বসানো যাবে
        self.endpoints = {
            "breach": "https://api.darkweb.local/breach",
            "paste": "https://api.darkweb.local/paste",
            "market": "https://api.darkweb.local/market"
        }

    def scan_target(self, target_type, target_value):
        """Scan target di dark web dengan aman"""
        try:
            target_value = str(target_value).strip()
            target_type = str(target_type).strip()

            # সেফলি হ্যাশ জেনারেট করা
            try:
                target_hash = hashlib.sha256(target_value.encode('utf-8')).hexdigest()
            except Exception:
                target_hash = "unknown_hash"

            results = {
                "timestamp": datetime.now().isoformat(),
                "target_type": target_type,
                "target_value": target_value,
                "hash": target_hash,
                "findings": {
                    "breaches": self.check_breaches(target_value),
                    "pastes": self.check_pastes(target_value),
                    "markets": self.check_markets(target_value)
                }
            }
            return results
        except Exception as e:
            return {"error": f"DarkWeb scan failed: {str(e)}"}

    def check_breaches(self, target):
        """Cek kebocoran data dengan aman"""
        try:
            response = self.make_request(
                self.endpoints["breach"],
                params={"target": target}
            )
            if isinstance(response, dict):
                return response.get("breaches", [])
            return []
        except Exception:
            return []

    def check_pastes(self, target):
        """Cek di paste sites dengan aman"""
        try:
            response = self.make_request(
                self.endpoints["paste"],
                params={"target": target}
            )
            if isinstance(response, dict):
                return response.get("pastes", [])
            return []
        except Exception:
            return []

    def check_markets(self, target):
        """Cek di dark markets dengan aman"""
        try:
            response = self.make_request(
                self.endpoints["market"],
                params={"target": target}
            )
            if isinstance(response, dict):
                return response.get("listings", [])
            return []
        except Exception:
            return []

    def make_request(self, url, params=None):
        """Buat HTTP request dengan API key dan penanganan error"""
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            
            # প্রক্সি সাপোর্ট (যদি ডার্কওয়েব অনিয়ন সাইট বা প্রক্সি প্রয়োজন হয়)
            proxies = {"http": self.proxy_url, "https": self.proxy_url} if self.use_proxy else None

            response = requests.get(url, headers=headers, params=params, proxies=proxies, timeout=15)
            
            if response.status_code == 200:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    return {"status": "success", "raw_text": response.text}
            else:
                return {"status": "error", "code": response.status_code}

        except requests.exceptions.RequestException:
            # যেহেতু এন্ডপয়েন্টটি ডামি/লোকাল, তাই কানেকশন ফেইল করলে সেফ ফলব্যাক ডেটা রিটার্ন করবে
            return {
                "status": "simulated",
                "message": "Darkweb API endpoint unreachable. Running in offline/fallback mode.",
                "breaches": [],
                "pastes": [],
                "listings": []
            }
        except Exception as e:
            return {"error": str(e)}
