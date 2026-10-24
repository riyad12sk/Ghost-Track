import requests
import json
import os
from datetime import datetime

class SocialProcessor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5'
        }
        self.platforms = {
            "GitHub": "https://github.com/{}",
            "Twitter / X": "https://x.com/{}",
            "Instagram": "https://www.instagram.com/{}/",
            "Reddit": "https://www.reddit.com/user/{}",
            "Pinterest": "https://www.pinterest.com/{}/",
            "Telegram": "https://t.me/{}",
            "TikTok": "https://www.tiktok.com/@{}",
            "Medium": "https://medium.com/@{}",
            "Dev.to": "https://dev.to/{}"
        }

    def analyze_social(self, username):
        """Check username availability across major social platforms"""
        clean_username = username.strip().replace("@", "")
        if not clean_username:
            return {"error": True, "message": "Invalid username provided."}

        results = {}
        found_count = 0

        for platform, url_template in self.platforms.items():
            profile_url = url_template.format(clean_username)
            try:
                res = requests.get(profile_url, headers=self.headers, timeout=5, allow_redirects=True)
                if res.status_code == 200:
                    results[platform] = {"status": "Found / Active", "url": profile_url}
                    found_count += 1
                elif res.status_code == 404:
                    results[platform] = {"status": "Not Found / Available", "url": None}
                else:
                    results[platform] = {"status": f"Protected / Unclear (HTTP {res.status_code})", "url": profile_url}
            except Exception:
                results[platform] = {"status": "Check Failed", "url": None}

        data = {
            "username": clean_username,
            "total_platforms_checked": len(self.platforms),
            "matches_found": found_count,
            "profiles": results
        }

        report_file = self.generate_html_report(data)
        data["report_saved"] = report_file
        return data

    def generate_html_report(self, data):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/social_scan_{timestamp}.html"

        rows = ""
        for platform, info in data.get("profiles", {}).items():
            status = info.get("status")
            url = info.get("url")
            status_class = "status-ok" if "Found" in status else "status-muted"
            link_html = f'<a href="{url}" target="_blank">{url}</a>' if url else 'N/A'
            rows += f'<tr><td>{platform}</td><td class="{status_class}">{status}</td><td>{link_html}</td></tr>'

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Social Media OSINT Report - {data.get('username')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                .status-ok {{ color: #4ade80; font-weight: bold; }}
                .status-muted {{ color: #64748b; }}
                a {{ color: #38bdf8; text-decoration: none; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - Social Media OSINT Report</h2>
                <p><strong>Target Username:</strong> @{data.get('username')}</p>
                <p><strong>Matches Found:</strong> {data.get('matches_found')} / {data.get('total_platforms_checked')}</p>
                <p><strong>Scan Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            <div class="card">
                <h2>Platform Analysis</h2>
                <table>
                    <tr><th>Platform</th><th>Status</th><th>Profile Link</th></tr>
                    {rows}
                </table>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename
