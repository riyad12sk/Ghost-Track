import socket
from datetime import datetime

try:
    import nmap
    NMAP_INSTALLED = True
except ImportError:
    NMAP_INSTALLED = False

class NetworkScanner:
    def __init__(self):
        self.nmap_available = NMAP_INSTALLED
        try:
            if self.nmap_available:
                self.nm = nmap.PortScanner()
            else:
                self.nm = None
        except Exception:
            self.nmap_available = False
            self.nm = None

    def scan_target(self, target, scan_type="basic"):
        """Scan target network/host dengan aman"""
        target = str(target).strip()
        results = {
            "timestamp": datetime.now().isoformat(),
            "target": target,
            "scan_type": scan_type,
            "results": {}
        }

        if not self.nmap_available or not self.nm:
            return {
                "timestamp": datetime.now().isoformat(),
                "target": target,
                "scan_type": scan_type,
                "results": {
                    "status": "simulated",
                    "message": "Nmap binary or python-nmap not installed. Running in safe fallback mode.",
                    "open_ports": [80, 443, 22, 8080] if scan_type != "vuln" else []
                }
            }

        try:
            if scan_type == "basic":
                results["results"] = self.basic_scan(target)
            elif scan_type == "full":
                results["results"] = self.full_scan(target)
            elif scan_type == "vuln":
                results["results"] = self.vulnerability_scan(target)
            else:
                results["results"] = self.basic_scan(target)

            return results
        except Exception as e:
            return {"error": str(e), "target": target}

    def basic_scan(self, target):
        """Basic port scan"""
        try:
            self.nm.scan(target, arguments="-F")
            return self._parse_scan_results()
        except Exception as e:
            return {"error": str(e)}

    def full_scan(self, target):
        """Full port scan dengan service detection (Aman untuk unprivileged user)"""
        try:
            # -sT (TCP Connect scan) ব্যবহার করা হয়েছে যাতে রুট পারমিশন ছাড়া ক্র্যাশ না করে
            self.nm.scan(target, arguments="-sT -sV")
            return self._parse_scan_results()
        except Exception as e:
            return {"error": str(e)}

    def vulnerability_scan(self, target):
        """Vulnerability scan"""
        try:
            self.nm.scan(target, arguments="-sV --script vuln")
            return self._parse_scan_results()
        except Exception as e:
            return {"error": str(e)}

    def _parse_scan_results(self):
        """Helper untuk parse data nmap ke format dictionary yang aman"""
        parsed = {}
        try:
            for host in self.nm.all_hosts():
                parsed[host] = {
                    "state": self.nm[host].state(),
                    "protocols": {}
                }
                for proto in self.nm[host].all_protocols():
                    parsed[host]["protocols"][proto] = {}
                    ports = self.nm[host][proto].keys()
                    for port in ports:
                        port_data = self.nm[host][proto][port]
                        parsed[host]["protocols"][proto][port] = {
                            "state": port_data.get("state"),
                            "name": port_data.get("name"),
                            "product": port_data.get("product"),
                            "version": port_data.get("version")
                        }
        except Exception as e:
            parsed["raw_error"] = str(e)
        return parsed
