from cryptography.fernet import Fernet
import os

class PegasusEncryption:
    def __init__(self, key_file="config/security.key"):
        self.key_file = key_file
        self.load_or_generate_key()

    def load_or_generate_key(self):
        """Load atau generate kunci enkripsi dengan aman"""
        try:
            # ডিরেক্টরি পাথ চেক করে ফোল্ডার তৈরি করা (ক্র্যাশ এড়ানোর জন্য)
            dir_name = os.path.dirname(self.key_file)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)

            if os.path.exists(self.key_file):
                with open(self.key_file, 'rb') as f:
                    self.key = f.read()
            else:
                self.key = Fernet.generate_key()
                with open(self.key_file, 'wb') as f:
                    f.write(self.key)

            self.cipher_suite = Fernet(self.key)
        except Exception as e:
            # ফলব্যাক মেকানিজম যাতে কোড ক্র্যাশ না করে
            self.key = Fernet.generate_key()
            self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        """Enkripsi data (mendukung string dan bytes)"""
        try:
            if isinstance(data, str):
                data = data.encode('utf-8')
            return self.cipher_suite.encrypt(data)
        except Exception as e:
            return None

    def decrypt(self, encrypted_data, decode_str=True):
        """Dekripsi data dengan penanganan error yang aman"""
        try:
            if isinstance(encrypted_data, str):
                encrypted_data = encrypted_data.encode('utf-8')
                
            decrypted_bytes = self.cipher_suite.decrypt(encrypted_data)
            
            if decode_str:
                try:
                    return decrypted_bytes.decode('utf-8')
                except UnicodeDecodeError:
                    return decrypted_bytes
            return decrypted_bytes
        except Exception as e:
            return None
