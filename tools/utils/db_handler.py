import sqlite3
import json
from datetime import datetime
import os

class DatabaseHandler:
    def __init__(self, db_file="config/pegasus.db"):
        self.db_file = db_file
        self.setup_database()

    def setup_database(self):
        """Setup database dan tabel dengan aman"""
        try:
            # ডিরেক্টরি পাথ চেক করে ফোল্ডার তৈরি করা (ক্র্যাশ এড়ানোর জন্য)
            dir_name = os.path.dirname(self.db_file)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)

            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()

            # Buat tabel untuk menyimpan hasil scan
            c.execute('''
                CREATE TABLE IF NOT EXISTS scan_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    scan_type TEXT,
                    target TEXT,
                    result_data TEXT,
                    status TEXT
                )
            ''')

            # Buat tabel untuk log aktivitas
            c.execute('''
                CREATE TABLE IF NOT EXISTS activity_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    user TEXT,
                    activity TEXT,
                    details TEXT
                )
            ''')

            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database setup error: {e}")

    def save_scan_result(self, scan_type, target, result_data, status="success"):
        """Simpan hasil scan ke database dengan aman"""
        try:
            if not isinstance(result_data, (dict, list)):
                result_data = {"data": str(result_data)}
            
            json_data = json.dumps(result_data, ensure_ascii=False)

            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()

            c.execute('''
                INSERT INTO scan_results (timestamp, scan_type, target, result_data, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                scan_type,
                str(target),
                json_data,
                status
            ))

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            return False

    def get_scan_history(self, scan_type=None, limit=50):
        """Ambil riwayat scan dengan penanganan error yang aman"""
        try:
            conn = sqlite3.connect(self.db_file)
            c = conn.cursor()

            if scan_type:
                c.execute('''
                    SELECT * FROM scan_results 
                    WHERE scan_type = ? 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (scan_type, limit))
            else:
                c.execute('''
                    SELECT * FROM scan_results 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (limit,))

            results = c.fetchall()
            conn.close()

            parsed_results = []
            for r in results:
                try:
                    res_data = json.loads(r[4])
                except:
                    res_data = {"raw_data": r[4]}

                parsed_results.append({
                    "id": r[0],
                    "timestamp": r[1],
                    "scan_type": r[2],
                    "target": r[3],
                    "result_data": res_data,
                    "status": r[5]
                })
            return parsed_results
        except Exception as e:
            return []
