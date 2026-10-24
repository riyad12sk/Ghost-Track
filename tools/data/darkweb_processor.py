import requests
import json
import os
from datetime import datetime

class DarkWebProcessor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def analyze_darkweb(self, query):
        """Analyze leaks, paste sites, and darkweb index footprints for a target query"""
        clean_query = query.strip()
        if not clean_query:
            return {"error": True, "message": "Invalid query provided."}

        # Query public leak search & paste index endpoints safely
        leak_found = False
        paste_sources = []
        
        # Check HaveIBeenPwned unified database footprint endpoint
        try:
            hibp_url = f"https://haveibeenpwned.com/unifiedsearch/{clean_query}"
            res = requests.get(hibp_url, headers=self.headers, timeout=6)
            if res.status_code == 200:
                leak_found = True
        except Exception:
            pass

        # Generate Dark Web OSINT Intelligence Links
        ahmia_search = f"https://ahmia.fi/search/?q={clean_query}"
        pastebin_dork = f"https://www.google.com/search?q=site:pastebin.com+%22{clean_query}%22"
        intelx_search = f"https://intelx.io/?s={clean_query}"

        result = {
            "query": clean_query,
            "leak_detected": leak_found,
            "threat_level": "HIGH / Potential Data Leak" if leak_found else "LOW / No Instant Leak Found",
            "darkweb_sources": {
                "ahmia_onion_index": ahmia_search,
                "pastebin_leak_dork": pastebin_dork,
                "intelx_footprints": intelx_search
            }
        }

        # Generate HTML Report
        report_file = self.generate_html_report(result)
        result["report_saved"] = report_file
        return result

    def generate_html_report(self, data):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/darkweb_scan_{timestamp}.html"

        threat_class = "status-bad" if data.get("leak_detected") else "status-ok"

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dark Web Intelligence Report - {data.get('query')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                .status-bad {{ color: #f87171; font-weight: bold; }}
                .status-ok {{ color: #4ade80; font-weight: bold; }}
                a {{ color: #38bdf8; text-decoration: none; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - Dark Web Intelligence Report</h2>
                <p><strong>Target Query:</strong> {data.get('query')}</p>
                <p><strong>Threat Assessment:</strong> <span class="{threat_class}">{data.get('threat_level')}</span></p>
                <p><strong>Scan Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            <div class="card">
                <h2>Darknet & Paste Index Sources</h2>
                <table>
                    <tr><th>Ahmia Onion Search</th><td><a href="{data.get('darkweb_sources', {}).get('ahmia_onion_index')}" target="_blank">Search Onion Indexes</a></td></tr>
                    <tr><th>Pastebin Leak Dork</th><td><a href="{data.get('darkweb_sources', {}).get('pastebin_leak_dork')}" target="_blank">View Pastebin Dorks</a></td></tr>
                    <tr><th>Intelligence X Footprints</th><td><a href="{data.get('darkweb_sources', {}).get('intelx_footprints')}" target="_blank">Search IntelX Data</a></td></tr>
                </table>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename
