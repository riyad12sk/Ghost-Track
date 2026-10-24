# Bangladeshi Phone Operators Prefix Mapping
PROVIDERS_PHONE = {
    # Grameenphone
    "017": "Grameenphone",
    "013": "Grameenphone",
    
    # Robi
    "018": "Robi",
    
    # Banglalink
    "019": "Banglalink",
    "014": "Banglalink",
    
    # Airtel
    "016": "Airtel",
    
    # Teletalk
    "015": "Teletalk"
}

def get_phone_provider(phone_number):
    """নম্বর বা প্রিফিক্স থেকে মোবাইল অপারেটর শনাক্ত করার নিরাপদ ফাংশন"""
    try:
        phone_number = str(phone_number).strip()
        
        # যদি আন্তর্জাতিক কোড (+880 বা 880) থাকে তবে সেটিকে লোকাল ফরম্যাটে (01...) রূপান্তর করা
        if phone_number.startswith("+880"):
            phone_number = "0" + phone_number[4:]
        elif phone_number.startswith("880"):
            phone_number = "0" + phone_number[3:]
        
        # প্রথম ৩ ডিজিট (যেমন: 017, 018) আলাদা করা
        if len(phone_number) >= 3:
            prefix = phone_number[:3]
            return PROVIDERS_PHONE.get(prefix, "Unknown / International Operator")
        
        return "Invalid Number Format"
    except Exception as e:
        return f"Error: {str(e)}"
