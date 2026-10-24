# Bangladesh & Popular Global Email/Domain Providers Mapping
PROVIDER_MAIL = {
    # Bangladesh Government & Education Domains
    "gov.bd": {
        "name": "Bangladesh Government",
        "type": "Government",
        "country": "Bangladesh"
    },
    "edu.bd": {
        "name": "Bangladesh Educational Institution",
        "type": "Education",
        "country": "Bangladesh"
    },
    "mil.bd": {
        "name": "Bangladesh Armed Forces",
        "type": "Military",
        "country": "Bangladesh"
    },
    "ac.bd": {
        "name": "Bangladesh Academic/Research",
        "type": "Academic",
        "country": "Bangladesh"
    },
    "net.bd": {
        "name": "Bangladesh Network Provider",
        "type": "ISP",
        "country": "Bangladesh"
    },

    # Popular Global Email Services
    "gmail.com": {
        "name": "Google Gmail",
        "type": "Public",
        "country": "USA"
    },
    "yahoo.com": {
        "name": "Yahoo Mail",
        "type": "Public",
        "country": "USA"
    },
    "outlook.com": {
        "name": "Microsoft Outlook",
        "type": "Public",
        "country": "USA"
    },
    "hotmail.com": {
        "name": "Microsoft Hotmail",
        "type": "Public",
        "country": "USA"
    },
    "icloud.com": {
        "name": "Apple iCloud",
        "type": "Public",
        "country": "USA"
    },
    "proton.me": {
        "name": "ProtonMail",
        "type": "Encrypted Public",
        "country": "Switzerland"
    },
    "protonmail.com": {
        "name": "ProtonMail",
        "type": "Encrypted Public",
        "country": "Switzerland"
    }
}

def get_mail_provider(email_or_domain):
    """ইমেল অ্যাড্রেস বা ডোমেইন থেকে প্রোভাইডার তথ্য বের করার নিরাপদ ফাংশন"""
    try:
        val = str(email_or_domain).strip().lower()
        
        # যদি ফুল ইমেল ইনপুট দেওয়া হয় (যেমন: user@gmail.com), তবে ডোমেইন অংশ আলাদা করা
        if "@" in val:
            domain = val.split("@")[-1]
        else:
            domain = val
            
        # ১. সরাসরি ফুল ডোমেইন মিলে গেলে (যেমন: gmail.com)
        if domain in PROVIDER_MAIL:
            return PROVIDER_MAIL[domain]
            
        # ২. সাব-ডোমেইন বা এক্সটেনশন মিলে গেলে (যেমন: .gov.bd বা .edu.bd)
        for key, info in PROVIDER_MAIL.items():
            if domain.endswith(key):
                return info
                
        # যদি কোনোটার সাথেই না মিলে
        return {
            "name": "Custom / Private Domain",
            "type": "Private / Corporate",
            "country": "Unknown"
        }
    except Exception as e:
        return {"error": str(e)}
