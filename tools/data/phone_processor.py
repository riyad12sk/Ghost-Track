import requests
import re
import json
import os
from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

class PhoneProcessor:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        self.gemini_models = [
            "gemini-2.5-flash",
            "gemini-1.5-flash",
            "gemini-pro"
        ]

    def get_ai_osint_analysis(self, phone_data):
        if not self.gemini_api_key:
            return "Note: AI Intelligence module is running in offline fallback mode (GEMINI_API_KEY not set)."

        prompt = f"""
        You are an expert OSINT Investigator for the Ghost-Track security suite.
        Analyze the following phone number scan data and provide a brief threat assessment and investigator recommendations in Bengali:
        
        Data:
        {json.dumps(phone_data, indent=2)}
        """

        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        headers = {
            "Content-Type": "application/json"
        }

        for model in self.gemini_models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.gemini_api_key}"
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=8)
                if response.status_code == 200:
                    res_data = response.json()
                    if 'candidates' in res_data and len(res_data['candidates']) > 0:
                        text = res_data['candidates'][0]['content']['parts'][0]['text'].strip()
                        return f"[{model}] \n{text}"
            except Exception:
                continue

        return "Note: AI Intelligence module is currently running in offline fallback mode."

    def check_whatsapp(self, phone_number):
        clean_num = re.sub(r'[^0-9]', '', phone_number)
        url = f"https://api.whatsapp.com/send/?phone={clean_num}"
        try:
            res = requests.get(url, headers=self.headers, timeout=5)
            if "WhatsApp Web" in res.text or "send" in res.url:
                return {"status": "Likely Active", "link": f"https://wa.me/{clean_num}"}
            return {"status": "Unknown / Not Found", "link": None}
        except Exception:
            return {"status": "Check Failed", "link": None}

    def check_telegram(self, phone_number):
        clean_num = re.sub(r'[^0-9]', '', phone_number)
        url = f"https://t.me/+{clean_num}"
        try:
            res = requests.get(url, headers=self.headers, timeout=5)
            if res.status_code == 200 and "Telegram: Contact" in res.text:
                return {"status": "Registered / Public Contact", "link": url}
            return {"status": "Not Public / Not Found", "link": None}
        except Exception:
            return {"status": "Check Failed", "link": None}

    def generate_html_report(self, data):
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/phone_scan_{timestamp}.html"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Phone OSINT Report - {data.get('nomor')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-bottom: 20px; }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                .status-ok {{ color: #4ade80; font-weight: bold; }}
                .ai-box {{ background: #0f2942; border-left: 4px solid #38bdf8; padding: 15px; margin-top: 10px; border-radius: 4px; line-height: 1.6; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - Phone OSINT Analysis Report</h2>
                <p><strong>Target Number:</strong> {data.get('nomor')}</p>
                <p><strong>Generated At:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            <div class="card">
                <h2>Basic & Carrier Info</h2>
                <table>
                    <tr><th>Carrier / Provider</th><td>{data.get('provider')}</td></tr>
                    <tr><th>Type</th><td>{data.get('tipe')}</td></tr>
                    <tr><th>Country</th><td>{data.get('negara')}</td></tr>
                    <tr><th>International Format</th><td>{data.get('format', {}).get('internasional')}</td></tr>
                </table>
            </div>
            <div class="card">
                <h2>App Presence Check</h2>
                <table>
                    <tr><th>WhatsApp</th><td class="status-ok">{data.get('app_presence', {}).get('whatsapp', {}).get('status')}</td></tr>
                    <tr><th>Telegram</th><td class="status-ok">{data.get('app_presence', {}).get('telegram', {}).get('status')}</td></tr>
                </table>
            </div>
            <div class="card">
                <h2>AI Intelligence Assessment</h2>
                <div class="ai-box">
                    <pre style="white-space: pre-wrap; font-family: inherit;">{data.get('ai_analysis')}</pre>
                </div>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filename

    def analyze_phone(self, phone_number):
        try:
            if not phone_number.startswith('+'):
                if phone_number.startswith('01'):
                    parsed_num = phonenumbers.parse(phone_number, "BD")
                else:
                    parsed_num = phonenumbers.parse("+" + phone_number)
            else:
                parsed_num = phonenumbers.parse(phone_number)

            is_valid = phonenumbers.is_valid_number(parsed_num)
            is_possible = phonenumbers.is_possible_number(parsed_num)
            
            carrier_name = carrier.name_for_number(parsed_num, "en") or "Unknown"
            country_name = geocoder.description_for_number(parsed_num, "en") or "Unknown"
            timezones = list(timezone.time_zones_for_number(parsed_num))

            formatted_e164 = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.E164)
            formatted_nat = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.NATIONAL)
            formatted_int = phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

            wa_result = self.check_whatsapp(formatted_e164)
            tg_result = self.check_telegram(formatted_e164)

            result = {
                'nomor': phone_number,
                'valid': is_valid,
                'possible': is_possible,
                'provider': carrier_name,
                'tipe': 'Mobile' if phonenumbers.number_type(parsed_num) == phonenumbers.PhoneNumberType.MOBILE else 'Fixed/Other',
                'negara': country_name,
                'timezone': timezones,
                'format': {
                    'nasional': formatted_nat,
                    'internasional': formatted_int,
                    'E164': formatted_e164
                },
                'app_presence': {
                    'whatsapp': wa_result,
                    'telegram': tg_result
                }
            }

            result['ai_analysis'] = self.get_ai_osint_analysis(result)
            report_file = self.generate_html_report(result)
            result['report_saved'] = report_file

            return result

        except Exception as e:
            return {
                'error': True,
                'message': str(e),
                'nomor': phone_number
            }
