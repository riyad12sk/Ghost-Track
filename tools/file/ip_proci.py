import socket
import requests
from ipaddress import ip_address, IPv4Address, IPv6Address

class IPProcessor:
    def __init__(self):
        # HTTP ব্যবহার করা নিরাপদ, তবে কিছু নেটওয়ার্কে HTTPS প্রিফার করে
        self.api_url = "http://ip-api.com/json/{}"

    def analyze_ip(self, ip):
        """Analisis detail IP address dengan aman"""
        try:
            ip = str(ip).strip()
            # Validasi IP (IPv4 atau IPv6)
            ip_obj = ip_address(ip)

            # Dapatkan info geolokasi (hanya untuk public IP atau secara umum)
            geo_info = self.get_geo_info(ip) if not ip_obj.is_private else {"status": "private_network"}

            return {
                "ip": ip,
                "version": "IPv4" if isinstance(ip_obj, IPv4Address) else "IPv6",
                "valid": True,
                "type": self.get_ip_type(ip_obj),
                "reverse_dns": self.get_reverse_dns(ip),
                "geolocation": geo_info,
                "is_private": ip_obj.is_private,
                "is_global": ip_obj.is_global,
                "exploded_format": ip_obj.exploded
            }
        except Exception as e:
            return {"error": f"Invalid IP format: {str(e)}"}

    def get_ip_type(self, ip_obj):
        """Tentukan tipe IP"""
        try:
            if ip_obj.is_private:
                return "Private"
            elif ip_obj.is_multicast:
                return "Multicast"
            elif ip_obj.is_loopback:
                return "Loopback"
            elif ip_obj.is_link_local:
                return "Link-local"
            elif ip_obj.is_reserved:
                return "Reserved"
            else:
                return "Public"
        except Exception:
            return "Unknown"

    def get_reverse_dns(self, ip):
        """Dapatkan reverse DNS dengan aman"""
        try:
            # Menggunakan socket dengan timeout singkat agar tidak blocking
            socket.setdefaulttimeout(3)
            return socket.gethostbyaddr(ip)[0]
        except Exception:
            return None

    def get_geo_info(self, ip):
        """Dapatkan informasi geolokasi dengan penanganan error"""
        try:
            response = requests.get(self.api_url.format(ip), timeout=8)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    return data
                else:
                    return {"status": "fail", "message": data.get("message", "Unknown error from API")}
            return {"status": "error", "code": response.status_code}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"Network error: {str(e)}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
