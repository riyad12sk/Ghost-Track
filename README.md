# 🛡️ SK BLACK - OSINT & Personal Security Toolkit

<p align="center">
  <b>Ultimate personal security & monitoring toolkit. Track devices, analyze telecom data, monitor digital footprints, inspect network endpoints, and run security scripts. Modular, private, and fully deployable on Linux servers or Termux. Built for seamless, ethical, and flexible personal digital protection.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-cyan?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Server-orange?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/Target-Bangladesh%20%7C%20Global-green?style=for-the-badge" alt="Target">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
</p>

---

## 🌟 Key Features

- **🔍 Advanced OSINT Modules:** Username tracking, social media presence scanning, and dark web/data breach lookup wrappers.
- **📱 Telecom & Regional Localization:** Specifically configured for Bangladesh (`+880` country code, local divisions, and mobile operators: Grameenphone, Robi, Banglalink, Airtel, Teletalk).
- **🌐 Network Reconnaissance:** Robust port scanning, service detection, IP geolocation, reverse DNS, and network topology analysis.
- **📁 File & Metadata Analysis:** Detailed EXIF data extraction from images, document metadata analysis, and image steganography detection.
- **🔐 Encryption & Security:** Safe SQLite logging, automatic update checking, and resilient, exception-hardened runtime execution.
- **📱 Termux & Server Ready:** Optimized to run smoothly on Android via Termux or on Linux VPS/Dedicated servers.

---

## 📂 Project Architecture

```text
sk-black/
│
├── config/             # Configuration and local database storage
├── output/             # JSON scan reports and analysis logs
├── tools/
│   ├── darkweb/        # Dark web scanning & breach checks
│   ├── file/           # IP, Email, Phone processors & BD region codes
│   ├── metafile/       # Image & document metadata extractors
│   ├── network/        # Network, WiFi, and port scanning modules
│   ├── osint/          # Sherlock, Holehe, and Maigret CLI wrappers
│   ├── social/         # Social media profiling and username checks
│   ├── stego/          # Image steganography analyzer
│   └── utils/          # Core utilities (Logger, DB, API, Updater, Config)
│
├── main.py             # Main interactive application entry point
├── requirements.txt    # Required Python dependencies
└── README.md           # Project documentation


📲 Termux Installation Guide (Step-by-Step)
​Android ফোনে Termux অ্যাপে প্রজেক্টটি ইনস্টল ও ব্যবহার করার পূর্ণাঙ্গ নিয়ম:
​১. টার্মেক্স প্যাকেজ আপডেট ও বেসিক টুলস ইনস্টল করুন:
pkg update && pkg upgrade -y
pkg install git python python-pip nmap libjpeg-turbo zlib -y

২. গিটহাব থেকে প্রজেক্ট ক্লোন করুন:
git clone [https://github.com/riyad12sk/sk-black.git](https://github.com/riyad12sk/sk-black.git)
cd sk-black
৩. পাইথন ডিপেন্ডেন্সি ইনস্টল করুন:
pip install --upgrade pip
pip install -r requirements.txt
৪. টুলটি রান করুন:
python main.py

🖥️ Linux Server / VPS Setup
​উবুন্টু বা লিনাক্স সার্ভারে সেটআপের জন্য:
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pip nmap -y
git clone [https://github.com/riyad12sk/sk-black.git](https://github.com/riyad12sk/sk-black.git)
cd sk-black
pip3 install -r requirements.txt
python3 main.py

🛠️ Required Dependencies
​Python 3.8+
​requests, beautifulsoup4, scapy, python-nmap, phonenumbers, Pillow, opencv-python, cryptography, rich, dnspython
​🚀 Pushing Updates to GitHub
​টার্মেক্স বা আপনার পিসি থেকে প্রজেক্টে কোনো নতুন পরিবর্তন গিটহাবে পাঠানোর জন্য:
git add .
git commit -m "Update and stabilize SK BLACK modules"
git branch -M main
git push -u origin main

👨‍💻 Author & Contact
​GitHub: @riyad12sk
​Telegram: @SK_SHORIF_12
​⚠️ Disclaimer
​Ethical Use Only: This toolkit is created for security research, personal digital defense, and educational purposes only. The user assumes full responsibility for any actions performed using this software. Unauthorized scanning or testing is strictly discouraged.
​<p align="center">
<b>Developed with ❤️ by Riyad Sk</b>
</p>
