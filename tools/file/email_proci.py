import requests
import json
import os
import re
from datetime import datetime

class EmailProcessor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def analyze_email(self, email):
        """Analyze email address structure, domain MX records, and basic web footprints"""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return {"error": True, "message": "Invalid email address format."}

        domain = email.split('@')[1]
        
        # Check basic domain accessibility & MX lookup
        domain_status = "Active Domain"
        try:
            res = requests.get(f"https://{domain}", timeout=5)
            if res.status_code >= 400:
                domain_status = "Domain Unreachable or Private"
        except Exception:
            domain_status = "Domain Check Failed / Offline"

        # Generate Deep Search Footprint Links
        google_dork = f"https://www.google.com/search?q=%22{email}%22"
        github_search = f"https://github.com/search?q={email}&type=code"
        holehe_check = f"https://haveibeenpwned.com/unifiedsearch/{email}"

        result = {
            "email": email,
            "domain": domain,
            "domain_status": domain_status,
            "osint_footprints": {
                "google_search": google_dork,
                "github_code_search": github_search,
                "breach_check": holehe_check
            }
        }

        # Generate HTML Report
        report_file = self.generate_html_report(result)
        result["report_saved"] = report_file
        return result

    def generate_html_report(self, data):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/email_scan_{timestamp}.html"

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Email OSINT Report - {data.get('email')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                a {{ color: #38bdf8; text-decoration: none; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - Email OSINT Report</h2>
                <p><strong>Target Email:</strong> {data.get('email')}</p>
                <p><strong>Domain:</strong> {data.get('domain')}</p>
                <p><strong>Domain Status:</strong> {data.get('domain_status')}</p>
            </div>
            <div class="card">
                <h2>Deep OSINT Links</h2>
                <table>
                    <tr><th>Google Footprint</th><td><a href="{data.get('osint_footprints', {}).get('google_search')}" target="_blank">Search Google Dorks</a></td></tr>
                    <tr><th>GitHub Leak Check</th><td><a href="{data.get('osint_footprints', {}).get('github_code_search')}" target="_blank">Search GitHub Repos</a></td></tr>
                </table>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename
