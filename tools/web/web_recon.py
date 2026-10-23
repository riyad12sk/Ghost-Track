import requests
from bs4 import BeautifulSoup
import whois
import dns.resolver
import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse

class WebRecon:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def clean_domain(self, domain):
        """URL থেকে শুধু ক্লিন ডোমেইন বের করার ফাংশন"""
        domain = domain.strip()
        if "://" in domain:
            parsed_url = urlparse(domain)
            domain = parsed_url.netloc or parsed_url.path
        return domain.split('/')[0]

    def analyze_website(self, domain):
        """Analisis website secara menyeluruh"""
        domain = self.clean_domain(domain)
        results = {
            "timestamp": datetime.now().isoformat(),
            "domain": domain,
            "whois": self.get_whois_info(domain),
            "dns": self.get_dns_info(domain),
            "ssl": self.check_ssl(domain),
            "headers": self.check_headers(domain),
            "technologies": self.detect_technologies(domain),
            "security_headers": self.check_security_headers(domain)
        }
        return results

    def get_whois_info(self, domain):
        """Dapatkan informasi WHOIS"""
        try:
            w = whois.whois(domain)
            return {
                "registrar": w.registrar,
                "creation_date": str(w.creation_date),
                "expiration_date": str(w.expiration_date),
                "name_servers": w.name_servers
            }
        except Exception as e:
            return {"error": str(e)}

    def get_dns_info(self, domain):
        """Dapatkan informasi DNS"""
        records = {}
        try:
            for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']:
                try:
                    answers = dns.resolver.resolve(domain, record_type)
                    records[record_type] = [str(rdata) for rdata in answers]
                except:
                    records[record_type] = []
            return records
        except Exception as e:
            return {"error": str(e)}

    def check_ssl(self, domain):
        """Cek sertifikat SSL"""
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    return {
                        "issuer": dict(x[0] for x in cert.get('issuer', [])),
                        "subject": dict(x[0] for x in cert.get('subject', [])),
                        "version": cert.get('version'),
                        "valid_from": cert.get('notBefore'),
                        "valid_until": cert.get('notAfter')
                    }
        except Exception as e:
            return {"error": str(e)}

    def check_headers(self, domain):
        """Cek HTTP Response Headers"""
        try:
            url = f"https://{domain}"
            response = requests.get(url, headers=self.headers, timeout=5)
            return dict(response.headers)
        except Exception as e:
            return {"error": str(e)}

    def detect_technologies(self, domain):
        """Deteksi teknologi website (Simulated/Basic)"""
        try:
            url = f"https://{domain}"
            response = requests.get(url, headers=self.headers, timeout=5)
            server = response.headers.get("Server", "Unknown")
            return {
                "server": server,
                "powered_by": response.headers.get("X-Powered-By", "Not Disclosed")
            }
        except Exception as e:
            return {"error": str(e)}

    def check_security_headers(self, domain):
        """Cek keamanan HTTP Headers"""
        try:
            url = f"https://{domain}"
            response = requests.get(url, headers=self.headers, timeout=5)
            sec_headers = ['Content-Security-Policy', 'X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security']
            results = {}
            for h in sec_headers:
                results[h] = response.headers.get(h, "Not Implemented")
            return results
        except Exception as e:
            return {"error": str(e)}

    def recon_website(self, domain):
        """Main wrapper method untuk kompatibilitas menu"""
        return self.analyze_website(domain)
