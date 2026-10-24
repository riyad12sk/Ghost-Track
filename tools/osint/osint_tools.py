import requests
import json
import subprocess
from datetime import datetime
import os

class OSINTTools:
    def __init__(self, tools_dir="tools/osint/bin"):
        self.tools_dir = tools_dir
        self.setup_tools()

    def setup_tools(self):
        """Setup OSINT tools dengan pembuatan direktori otomatis"""
        try:
            os.makedirs(self.tools_dir, exist_ok=True)
        except Exception:
            pass

    def run_sherlock(self, username):
        """Run Sherlock untuk username search dengan penanganan error yang aman"""
        username = str(username).strip()
        try:
            sherlock_path = f"{self.tools_dir}/sherlock/sherlock.py"
            if os.path.exists(sherlock_path):
                cmd = ["python", sherlock_path, username, "--json"]
            else:
                # যদি লোকাল পাথ না থাকে, গ্লোবাল কমান্ড ট্রাই করা
                cmd = ["sherlock", username, "--json"]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and result.stdout:
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError:
                    return {"status": "success", "output": result.stdout}
            else:
                return {
                    "status": "error",
                    "message": "Sherlock execution failed or tool not installed.",
                    "details": result.stderr or "No output"
                }
        except FileNotFoundError:
            return {
                "status": "simulated",
                "username": username,
                "message": "Sherlock CLI not found. Running in safe fallback mode.",
                "platforms": {"github": f"https://github.com/{username}", "twitter": f"https://twitter.com/{username}"}
            }
        except Exception as e:
            return {"error": str(e)}

    def run_holehe(self, email):
        """Run Holehe untuk email check dengan aman"""
        email = str(email).strip()
        try:
            cmd = ["holehe", email, "--json"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0 and result.stdout:
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError:
                    return {"status": "success", "output": result.stdout}
            else:
                return {
                    "status": "error",
                    "message": "Holehe execution failed or tool not installed.",
                    "details": result.stderr or "No output"
                }
        except FileNotFoundError:
            return {
                "status": "simulated",
                "email": email,
                "message": "Holehe CLI not found in environment. Simulated check completed.",
                "found_on": []
            }
        except Exception as e:
            return {"error": str(e)}

    def run_maigret(self, username):
        """Run Maigret untuk social media search dengan aman"""
        username = str(username).strip()
        try:
            cmd = ["maigret", username, "--json"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
            
            if result.returncode == 0 and result.stdout:
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError:
                    return {"status": "success", "output": result.stdout}
            else:
                return {
                    "status": "error",
                    "message": "Maigret execution failed or tool not installed.",
                    "details": result.stderr or "No output"
                }
        except FileNotFoundError:
            return {
                "status": "simulated",
                "username": username,
                "message": "Maigret CLI not found. Running in safe fallback mode.",
                "profile_links": {
                    "facebook": f"https://facebook.com/{username}",
                    "instagram": f"https://instagram.com/{username}",
                    "telegram": f"https://t.me/{username}"
                }
            }
        except Exception as e:
            return {"error": str(e)}
