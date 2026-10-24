import requests
import json
from datetime import datetime
import os
from .logger import PegasusLogger

class APIHandler:
    def __init__(self, config_file="config/settings.json"):
        self.config_file = config_file
        self.api_keys = {}
        self.load_config(config_file)
        self.logger = PegasusLogger()

    def load_config(self, config_file):
        """Load API keys dari config dengan aman"""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.api_keys = config.get('api_keys', {})
            else:
                self.api_keys = {}
        except Exception:
            self.api_keys = {}

    def make_request(self, url, method="GET", headers=None, params=None, data=None):
        """Buat HTTP request dengan error handling yang aman"""
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            
            # সেফলি JSON রেসপন্স পার্স করা (যদি রেসপন্স JSON না হয়)
            try:
                return response.json()
            except json.JSONDecodeError:
                return {
                    "status": "success",
                    "status_code": response.status_code,
                    "text": response.text
                }
                
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            try:
                self.logger.log_activity(
                    "system",
                    f"API Request Failed: {url}",
                    "error",
                    error_msg
                )
            except Exception:
                pass
                
            return {"error": error_msg}
