import logging
from datetime import datetime
import os

class PegasusLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        self.setup_logger()

    def setup_logger(self):
        """Setup logging configuration dengan pembuatan direktori otomatis"""
        # ফোল্ডার না থাকলে স্বয়ংক্রিয়ভাবে তৈরি করার ব্যবস্থা
        os.makedirs(self.log_dir, exist_ok=True)
        
        log_file = f"{self.log_dir}/sk_black_{datetime.now().strftime('%Y%m%d')}.log"

        # আগের কোনো হ্যান্ডলার থাকলে তা পরিষ্কার করা যাতে ডুপ্লিকেট লগ না হয়
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger('SKBlackToolkit')

    def log_activity(self, user, activity, status="success", details=None):
        """Log aktivitas pengguna"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "activity": activity,
            "status": status,
            "details": details
        }

        if status == "success":
            self.logger.info(f"User [{user}] -> {activity}")
        else:
            self.logger.error(f"User [{user}] -> {activity} | Details: {details}")
