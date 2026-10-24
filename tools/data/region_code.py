# Bangladeshi Administrative Divisions & Region Mapping
BANGLADESH_REGIONS = {
    "30": "Dhaka Division",
    "20": "Chittagong Division",
    "50": "Rajshahi Division",
    "40": "Khulna Division",
    "70": "Sylhet Division",
    "60": "Rangpur Division",
    "10": "Barisal Division",
    "80": "Mymensingh Division"
}

# মোবাইল অপারেটর প্রিফিক্স (বাংলাদেশি নম্বর যাচাইয়ের জন্য অতিরিক্ত সুবিধা)
BD_OPERATORS = {
    "013": "Grameenphone",
    "017": "Grameenphone",
    "018": "Robi",
    "019": "Banglalink",
    "014": "Banglalink",
    "016": "Airtel",
    "015": "Teletalk"
}

def get_region_name(code):
    """কোড অনুযায়ী রিজিওন বা বিভাগ বের করার নিরাপদ ফাংশন"""
    try:
        code = str(code).strip()
        return BANGLADESH_REGIONS.get(code, "Unknown / International Region")
    except Exception:
        return "Unknown Region"

def get_operator_name(phone_number):
    """নম্বরের প্রিফিক্স দেখে মোবাইল অপারেটর শনাক্ত করার ফাংশন"""
    try:
        phone_number = str(phone_number).strip()
        if phone_number.startswith("+880"):
            phone_number = "0" + phone_number[4:]
        
        prefix = phone_number[:3]
        return BD_OPERATORS.get(prefix, "Unknown Operator")
    except Exception:
        return "Unknown Operator"
