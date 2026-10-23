import requests
import json
import os
from datetime import datetime

class PegasusUpdater:
    def __init__(self):
        self.current_version = "1.0.0"
        # আপনার গিটহাব ইউজারনেম ও রিপোজিটরির নাম এখানে যুক্ত করা হয়েছে
        self.update_url = "https://api.github.com/repos/Mj-user/saint-pegasus/releases/latest"

    def check_updates(self):
        """Cek pembaruan tersedia dengan aman"""
        try:
            response = requests.get(self.update_url, timeout=10)
            if response.status_code == 200:
                latest = response.json()
                tag_name = latest.get("tag_name", "v1.0.0")
                latest_version = tag_name.strip("v")
                
                # সেফ চেক: যদি কোনো অ্যাসেট বা রিলিজ ফাইল না থাকে
                download_url = ""
                assets = latest.get("assets", [])
                if assets and len(assets) > 0:
                    download_url = assets[0].get("browser_download_url", "")

                return {
                    "current_version": self.current_version,
                    "latest_version": latest_version,
                    "update_available": self.compare_versions(latest_version),
                    "release_notes": latest.get("body", "No release notes provided."),
                    "download_url": download_url
                }
            else:
                return {"error": f"GitHub API returned status code {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def compare_versions(self, latest):
        """Bandingkan versi secara aman"""
        try:
            current = [int(x) for x in self.current_version.split(".") if x.isdigit()]
            new = [int(x) for x in latest.split(".") if x.isdigit()]

            # লেংথ সমান না হলে শূন্য দিয়ে প্যাডিং করা
            max_len = max(len(current), len(new))
            current += [0] * (max_len - len(current))
            new += [0] * (max_len - len(new))

            for i in range(max_len):
                if new[i] > current[i]:
                    return True
                elif new[i] < current[i]:
                    return False
            return False
        except Exception:
            return False

    def download_update(self, url, target_path):
        """Download pembaruan dengan aman"""
        if not url:
            return False
        try:
            response = requests.get(url, stream=True, timeout=15)
            if response.status_code == 200:
                with open(target_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return True
            return False
        except Exception as e:
            return False
