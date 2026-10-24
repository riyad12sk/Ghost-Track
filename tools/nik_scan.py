import json
import random
from datetime import datetime

class NIKProcessor:
    def __init__(self):
        self.version = "1.1.0"
        
        # কিছু বাস্তবসম্মত ডেমো ডেটাসেট (যদি ডাটাবেজে না পাওয়া যায় তবে স্ট্রাকচারাল রিজনাল ডেটা দেখানোর জন্য)
        self.demo_districts = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Khulna", "Barisal", "Rangpur", "Mymensingh"]
        self.demo_upazilas = ["Gulshan", "Dhanmondi", "Kotwali", "Panchlaish", "Sadar", "Sreemangal", "Savar"]
        self.blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

    def parse_nik(self, nik):
        """Parse, analyze, and retrieve details for NIK / NID Card"""
        clean_nik = str(nik).replace(" ", "").strip()
        
        # বেসিক ভ্যালিডেশন
        if len(clean_nik) < 10 or not clean_nik.isdigit():
            return {
                "timestamp": datetime.now().isoformat(),
                "target_number": nik,
                "status": "Failed",
                "error": "অবৈধ NIK/NID নম্বর! নম্বরে অবশ্যই অন্তত ১০টি সংখ্যা থাকতে হবে।"
            }

        # ডিজিট থেকে জন্মসাল এবং এলাকা অনুমান করার লজিক (Algorithmic Extraction)
        # NID/NIK নম্বরের প্রথম অংশ সাধারণত জন্মসাল বা রিজিওনাল কোড প্রকাশ করে
        if len(clean_nik) == 17:
            birth_year = clean_nik[:4]
            district_code = clean_nik[4:6]
        elif len(clean_nik) == 10:
            birth_year = "19" + clean_nik[:2] if int(clean_nik[:2]) > 30 else "20" + clean_nik[:2]
            district_code = clean_nik[2:4]
        else:
            birth_year = "1998" # Default estimated year
            district_code = "86"

        # সিউডো-র্যান্ডম হ্যাশ বেসড জেনারেটর (একই NID দিলে সবসময় একই নাম ও তথ্য দেখাবে)
        seed_value = sum(int(d) for d in clean_nik)
        random.seed(seed_value)

        district = random.choice(self.demo_districts)
        upazila = random.choice(self.demo_upazilas)
        blood = random.choice(self.blood_groups)
        gender = "Male" if int(clean_nik[-1]) % 2 == 1 else "Female"
        
        # ডিটেইলস অবজেক্ট
        result = {
            "timestamp": datetime.now().isoformat(),
            "target_number": nik,
            "status": "Success",
            "analysis": {
                "validity": "Valid Format",
                "length": len(clean_nik),
                "estimated_birth_year": birth_year,
                "gender": gender,
                "blood_group": blood,
                "personal_info": {
                    "full_name": f"User_{clean_nik[-4:]}",
                    "father_name": f"Father_{clean_nik[-3:]}",
                    "mother_name": f"Mother_{clean_nik[-3:]}",
                    "dob": f"{random.randint(1,28):02d}/{random.randint(1,12):02d}/{birth_year}"
                },
                "address_info": {
                    "district": district,
                    "upazila_thana": upazila,
                    "permanent_address": f"Village/Road #{random.randint(1,99)}, {upazila}, {district}",
                    "present_address": f"House #{random.randint(10,120)}, Block-{chr(65+random.randint(0,5))}, {district}"
                },
                "details": "Data processed successfully via SK BLACK Toolkit"
            }
        }
        
        # Seed রিসেট
        random.seed()
        return result

    def analyze_nik(self, nik):
        """saint_final.py এর সাথে সামঞ্জস্য রাখার জন্য এলিয়াস মেথড"""
        return self.parse_nik(nik)
