import re
import json
import hashlib
import os
from datetime import datetime
from rich.table import Table
from rich.console import Console

console = Console()

def validate_phone(phone):
    """Validasi format nomor telepon (Mendukung format Bangladesh +880 / 01...)"""
    phone = str(phone).strip()
    # Bangladeshi mobile numbers format (+8801... or 01...)
    pattern = r'^(\+880|880)?0?1[3-9][0-9]{8}$'
    return bool(re.match(pattern, phone))

def validate_email(email):
    """Validasi format email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_ip(ip):
    """Validasi format IP address"""
    pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, ip))

def save_result(data, category, identifier):
    """Simpan hasil ke file JSON dengan aman"""
    try:
        # ফোল্ডার না থাকলে স্বয়ংক্রিয়ভাবে তৈরি করা
        os.makedirs("output", exist_ok=True)
        filename = f"output/{category}_{identifier}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return filename
    except Exception as e:
        return None

def display_result_table(data, title):
    """Tampilkan hasil dalam format tabel dengan aman"""
    table = Table(title=title, show_header=True, header_style="bold cyan")
    table.add_column("Informasi", style="cyan", no_wrap=True)
    table.add_column("Detail", style="yellow")

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value, indent=2, ensure_ascii=False)
            table.add_row(str(key), str(value))
    else:
        table.add_row("Data", str(data))

    console.print(table)
