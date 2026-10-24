import requests
import json
import os
import socket
from datetime import datetime

class WebProcessor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def analyze_website(self, domain):
        """Analyze DNS records, server headers, and web security posture"""
        clean_domain = domain.strip().replace("https://", "").replace("http://", "").split("/")[0]
        if not clean_domain:
            return {"error": True, "message": "Invalid domain format."}

        # IP Resolution
        try:
            target_ip = socket.gethostbyname(clean_domain)
        except Exception:
            target_ip = "Unable to Resolve IP"

        # HTTP Header Analysis
        headers_found = {}
        server_info = "Unknown"
        status_code = "N/A"
        try:
            res = requests.get(f"https://{clean_domain}", headers=self.headers, timeout=6, allow_redirects=True)
            status_code = res.status_code
            server_info = res.headers.get("Server", "Hidden / Not Disclosed")
            headers_found = {
                "strict_transport_security": "Strict-Transport-Security" in res.headers,
                "x_frame_options": res.headers.get("X-Frame-Options", "Not Set"),
                "x_content_type_options": res.headers.get("X-Content-Type-Options", "Not Set")
            }
        except Exception as e:
            status_code = f"Error ({str(e)})"

        result = {
            "domain": clean_domain,
            "ip_address": target_ip,
            "http_status": status_code,
            "server": server_info,
            "security_headers": headers_found,
            "recon_links": {
                "whois_lookup": f"https://whois.domaintools.com/{clean_domain}",
                "dns_records": f"https://dnschecker.org/all-dns-records-of-domain.php?query={clean_domain}",
                "subdomain_finder": f"https://crt.sh/?q={clean_domain}"
            }
        }

        # Generate HTML Report
        report_file = self.generate_html_report(result)
        result["report_saved"] = report_file
        return result

    def generate_html_report(self, data):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/web_scan_{timestamp}.html"

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Website Recon Report - {data.get('domain')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                a {{ color: #38bdf8; text-decoration: none; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - Website Reconnaissance Report</h2>
                <p><strong>Target Domain:</strong> {data.get('domain')}</p>
                <p><strong>Resolved IP:</strong> {data.get('ip_address')}</p>
                <p><strong>HTTP Status:</strong> {data.get('http_status')}</p>
                <p><strong>Server Banner:</strong> {data.get('server')}</p>
                <p><strong>Scan Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            <div class="card">
                <h2>Recon & OSINT Links</h2>
                <table>
                    <tr><th>WHOIS Lookup</th><td><a href="{data.get('recon_links', {}).get('whois_lookup')}" target="_blank">View WHOIS Data</a></td></tr>
                    <tr><th>DNS Records</th><td><a href="{data.get('recon_links', {}).get('dns_records')}" target="_blank">Check All DNS Records</a></td></tr>
                    <tr><th>Subdomain Search (crt.sh)</th><td><a href="{data.get('recon_links', {}).get('subdomain_finder')}" target="_blank">Search Subdomains</a></td></tr>
                </table>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename
