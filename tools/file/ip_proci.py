import requests
import json
import os
from datetime import datetime

class IPProcessor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def analyze_ip(self, ip_address):
        """Fetch geolocation, ISP, timezone, and security context for an IP address"""
        url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query,proxy,hosting"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=8)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'fail':
                    return {"error": True, "message": f"IP Analysis Failed: {data.get('message', 'Invalid IP')}"}

                result = {
                    'ip': data.get('query'),
                    'country': f"{data.get('country')} ({data.get('countryCode')})",
                    'region': data.get('regionName'),
                    'city': data.get('city'),
                    'zip': data.get('zip', 'N/A'),
                    'coordinates': f"{data.get('lat')}, {data.get('lon')}",
                    'timezone': data.get('timezone'),
                    'isp': data.get('isp'),
                    'org': data.get('org'),
                    'asn': data.get('as'),
                    'is_proxy_or_vpn': data.get('proxy', False),
                    'is_hosting_server': data.get('hosting', False)
                }

                # Generate HTML Report
                report_file = self.generate_html_report(result)
                result['report_saved'] = report_file
                return result
            else:
                return {"error": True, "message": f"API HTTP Error: {response.status_code}"}

        except Exception as e:
            return {"error": True, "message": f"IP Lookup Failed: {str(e)}"}

    def generate_html_report(self, data):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/ip_scan_{timestamp}.html"

        is_proxy = "Detected" if data.get('is_proxy_or_vpn') else "Not Detected"
        proxy_class = "status-bad" if data.get('is_proxy_or_vpn') else "status-ok"

        is_hosting = "Yes (Hosting IP)" if data.get('is_hosting_server') else "No (Residential/Mobile)"
        hosting_class = "status-bad" if data.get('is_hosting_server') else "status-ok"

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>IP OSINT Report - {data.get('ip')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                .status-bad {{ color: #f87171; font-weight: bold; }}
                .status-ok {{ color: #4ade80; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - IP OSINT Analysis Report</h2>
                <p><strong>Target IP:</strong> {data.get('ip')}</p>
                <p><strong>Scan Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            <div class="card">
                <h2>Geolocation Information</h2>
                <table>
                    <tr><th>Country</th><td>{data.get('country')}</td></tr>
                    <tr><th>Region & City</th><td>{data.get('region')}, {data.get('city')}</td></tr>
                    <tr><th>ZIP Code</th><td>{data.get('zip')}</td></tr>
                    <tr><th>Coordinates</th><td>{data.get('coordinates')}</td></tr>
                    <tr><th>Timezone</th><td>{data.get('timezone')}</td></tr>
                </table>
            </div>
            <div class="card">
                <h2>Network & ISP Info</h2>
                <table>
                    <tr><th>ISP</th><td>{data.get('isp')}</td></tr>
                    <tr><th>Organization</th><td>{data.get('org')}</td></tr>
                    <tr><th>ASN</th><td>{data.get('asn')}</td></tr>
                    <tr><th>Proxy / VPN / Tor</th><td class="{proxy_class}">{is_proxy}</td></tr>
                    <tr><th>Hosting / DataCenter</th><td class="{hosting_class}">{is_hosting}</td></tr>
                </table>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename
