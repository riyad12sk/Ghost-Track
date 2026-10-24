import re
from datetime import datetime

# সেফলি ডিএনএস রেজোলভার ইমপোর্ট (যদি dnspython লাইব্রেরি ইনস্টল না থাকে)
try:
    from dns import resolver
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# সঠিক মডিউল এবং ডিকশনারি নাম দিয়ে ইমপোর্ট করা
from .provider_mail import PROVIDER_MAIL

class EmailProcessor:
    def __init__(self):
        self.providers = PROVIDER_MAIL

    def analyze_email(self, email):
        """Analisis detail email dengan aman"""
        try:
            email = str(email).strip().lower()
            
            # ভ্যালিড ফরম্যাট চেক
            if not self.validate_format(email):
                return {"error": "Invalid email format"}

            username, domain = email.split('@', 1)

            # Cek provider
            provider_info = self.get_provider_info(domain)

            # Cek MX records
            mx_records = self.check_mx_records(domain)

            return {
                "timestamp": datetime.now().isoformat(),
                "email": email,
                "username": username,
                "domain": domain,
                "provider_info": provider_info,
                "format_valid": True,
                "mx_records": mx_records,
                "disposable": self.check_if_disposable(domain)
            }
        except Exception as e:
            return {"error": f"Failed to analyze email: {str(e)}"}

    def validate_format(self, email):
        """Validasi format email"""
        try:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return bool(re.match(pattern, str(email).strip()))
        except Exception:
            return False

    def get_provider_info(self, domain):
        """Dapatkan informasi provider email dengan aman"""
        try:
            domain = domain.lower().strip()
            
            # ১. সরাসরি ডোমেইন মিলে গেলে (যেমন: gmail.com, gov.bd)
            if domain in self.providers:
                return self.providers[domain]

            # ২. সাব-ডোমেইন বা এক্সটেনশন চেক নিরাপদ উপায়ে করা
            parts = domain.split('.')
            if len(parts) >= 2:
                tld = f"{parts[-2]}.{parts[-1]}"
                if tld in self.providers:
                    return self.providers[tld]

            return {"name": "Custom / Private Domain", "type": "Private", "country": "Unknown"}
        except Exception:
            return {"name": "Unknown", "type": "Unknown", "country": "Unknown"}

    def check_mx_records(self, domain):
        """Cek MX records domain dengan penanganan error"""
        if not DNS_AVAILABLE:
            return ["DNS resolver module (dnspython) not available"]
            
        try:
            mx_records = resolver.resolve(domain, 'MX')
            return [str(mx.exchange).rstrip('.') for mx in mx_records]
        except Exception:
            return []

    def check_if_disposable(self, domain):
        """Cek apakah email disposable (Temporary Mail)"""
        try:
            disposable_domains = [
                "tempmail.com", "10minutemail.com", "throwawaymail.com",
                "guerrillamail.com", "mailinator.com", "trashmail.com",
                "yopmail.com", "dispostable.com"
            ]
            return domain.lower().strip() in disposable_domains
        except Exception:
            return False
