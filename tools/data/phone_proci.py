import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from .providers_phone import PROVIDERS_PHONE

class PhoneProcessor:
    def __init__(self):
        self.providers = PROVIDERS_PHONE

    def analyze_number(self, phone_number):
        """Analisis detail nomor telepon (Disesuaikan untuk Bangladesh)"""
        try:
            phone_number = str(phone_number).strip()
            
            # Parse nomor telepon dengan default region "BD" (Bangladesh)
            # Jika diawali +, phonenumbers লাইব্রেরি নিজে থেকেই কান্ট্রি কোড ডিটেক্ট করবে
            if phone_number.startswith("+"):
                parsed = phonenumbers.parse(phone_number)
            else:
                parsed = phonenumbers.parse(phone_number, "BD")

            # Dapatkan provider berdasarkan 3 digit awal nasional number (misal: 017, 018)
            national_num_str = str(parsed.national_number)
            prefix = "0" + national_num_str[:3] if not national_num_str.startswith("0") else national_num_str[:3]
            
            # Fallback ke built-in carrier module jika tidak ada di dict
            provider = self.providers.get(prefix, None)
            if not provider:
                try:
                    provider = carrier.name_for_number(parsed, "en")
                except:
                    provider = "Unknown"

            return {
                "nomor": phone_number,
                "format": {
                    "nasional": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
                    "internasional": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                    "E164": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
                },
                "provider": provider if provider else "Unknown Operator",
                "tipe": "Mobile" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE else "Fixed Line",
                "negara": geocoder.description_for_number(parsed, "en"),
                "valid": phonenumbers.is_valid_number(parsed),
                "possible": phonenumbers.is_possible_number(parsed),
                "timezone": list(timezone.time_zones_for_number(parsed))
            }
        except Exception as e:
            return {"error": f"Invalid phone number format: {str(e)}"}

    def validate_number(self, phone_number):
        """Validasi format nomor telepon dengan aman"""
        try:
            phone_number = str(phone_number).strip()
            if phone_number.startswith("+"):
                parsed = phonenumbers.parse(phone_number)
            else:
                parsed = phonenumbers.parse(phone_number, "BD")
            return phonenumbers.is_valid_number(parsed)
        except:
            return False
