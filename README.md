# 👻 Ghost-Track — Phone & OSINT Toolkit

**A Python command-line toolkit for basic phone-number metadata, email/domain checks, IP geolocation, public-profile URL checks, website reconnaissance, and local scan reports.**  
**বাংলা:** Ghost-Track একটি Python-ভিত্তিক Command Line Toolkit। এতে ফোন নম্বরের সাধারণ metadata, ইমেইল/ডোমেইন পরীক্ষা, IP geolocation, public profile link check, website reconnaissance এবং scan report সংরক্ষণের সুবিধা রয়েছে।

> **Important / গুরুত্বপূর্ণ:** This README documents the code currently present in this repository. Some modules are demo, simulated, incomplete, or not connected to the main menu. Do not treat their output as verified personal information or a security verdict.  
> এই README-তে Repository-তে বর্তমানে থাকা কোড অনুযায়ী তথ্য দেওয়া হয়েছে। কিছু Module Demo/Simulated/অসম্পূর্ণ অথবা Main Menu-তে যুক্ত নয়। কোনো ফলাফলকে নিশ্চিত ব্যক্তিগত তথ্য বা চূড়ান্ত Security Verdict হিসেবে ধরবেন না।

---

## 📚 Contents / সূচিপত্র

- [Features / সুবিধাসমূহ](#-features--সুবিধাসমূহ)
- [Requirements / যা লাগবে](#-requirements--যা-লাগবে)
- [Install on Termux / Termux-এ ইনস্টল](#-install-on-termux--termux-এ-ইনস্টল)
- [Run / চালু করা](#-run--চালু-করা)
- [Main Menu Guide / মেনু ব্যবহার](#-main-menu-guide--মেনু-ব্যবহার)
- [Project Files / ফাইল পরিচিতি](#-project-files--ফাইল-পরিচিতি)
- [Optional Modules / অতিরিক্ত মডিউল](#-optional-modules--অতিরিক্ত-মডিউল)
- [Configuration / কনফিগারেশন](#-configuration--কনফিগারেশন)
- [Reports and Logs / রিপোর্ট ও লগ](#-reports-and-logs--রিপোর্ট-ও-লগ)
- [Known Limitations / সীমাবদ্ধতা](#-known-limitations--সীমাবদ্ধতা)
- [Troubleshooting / সমস্যা সমাধান](#-troubleshooting--সমস্যা-সমাধান)
- [Privacy and Responsible Use / গোপনীয়তা ও দায়িত্বশীল ব্যবহার](#-privacy-and-responsible-use--গোপনীয়তা-ও-দায়িত্বশীল-ব্যবহার)
- [License](#-license)

---

## ✨ Features / সুবিধাসমূহ

The main application currently exposes these menu options:

| Menu | English | বাংলা |
|---|---|---|
| 1 | NID format/demo report | NID ফরম্যাট পরীক্ষা ও Demo রিপোর্ট |
| 2 | Phone number metadata and basic WhatsApp/Telegram link checks | ফোন নম্বরের metadata এবং WhatsApp/Telegram link check |
| 3 | Email format/domain reachability and search links | ইমেইল ফরম্যাট, ডোমেইন reachability ও search link |
| 4 | Public IP geolocation and ISP information | Public IP-এর অবস্থান ও ISP তথ্য |
| 5 | Public username/profile URL checks on 9 platforms | ৯টি প্ল্যাটফর্মে Public username/profile URL check |
| 6 | Limited breach-status request and public search links | সীমিত breach-status request ও public search link |
| 7 | Website DNS/IP/HTTP and security-header checks | Website-এর DNS/IP/HTTP ও security-header পরীক্ষা |
| 8 | List previously generated HTML reports | আগে তৈরি HTML রিপোর্টের তালিকা |
| 9 | Settings and optional Gemini API key for phone analysis | Settings ও Phone analysis-এর ঐচ্ছিক Gemini API key |
| 0 | Exit | বন্ধ করা |

---

## 🧰 Requirements / যা লাগবে

- Android with [Termux](https://termux.dev/) or a Linux/macOS/Windows terminal.
- Python 3.
- Git.
- Internet connection for modules that query public websites or APIs.
- The dependencies listed in `requirements.txt`.

**Termux note:** Install Termux from a trusted source and keep it updated. Some optional modules need native system packages or hardware permissions and may not work on a standard Android device.

**বাংলা:** Termux, Python 3, Git এবং Internet connection লাগবে। `requirements.txt`-এ থাকা Python package ইনস্টল করতে হবে। অতিরিক্ত কিছু Module-এর জন্য আলাদা System Package, Permission বা Hardware প্রয়োজন হতে পারে।

---

## 📲 Install on Termux / Termux-এ ইনস্টল

Open Termux and run these commands one by one:

**Step 1 — Update Termux packages / Termux আপডেট করুন**

```bash
pkg update && pkg upgrade -y
```

**Step 2 — Install Git and Python / Git ও Python ইনস্টল করুন**

```bash
pkg install git python -y
```

**Step 3 — Clone this repository / Repository ডাউনলোড করুন**

```bash
git clone https://github.com/riyad12sk/Ghost-Track.git
```

**Step 4 — Enter the project folder / Project folder-এ যান**

```bash
cd Ghost-Track
```

**Step 5 — Update pip tools / pip tools আপডেট করুন**

```bash
python -m pip install --upgrade pip setuptools wheel
```

**Step 6 — Install project dependencies / প্রয়োজনীয় package ইনস্টল করুন**

```bash
pip install -r requirements.txt
```

If installation of the full requirements file fails on your Android/Python version, the main menu's core imports can be installed separately with:

```bash
pip install rich==13.3.1 requests==2.31.0 phonenumbers==8.13.11
```

The separate command above is only for the main menu's core imports; it does not install dependencies for every optional utility.

**বাংলা:** উপরের Command-গুলো ধারাবাহিকভাবে চালালে Repository Termux-এ Clone হবে এবং Python package ইনস্টল হবে। Full requirements ইনস্টল না হলে Core package-এর Command ব্যবহার করতে পারেন; তবে এতে সব Optional Module-এর dependency ইনস্টল হবে না।

---

## ▶️ Run / চালু করা

From inside the `Ghost-Track` directory, run:

```bash
python saint_final.py
```

The main menu is launched by **`saint_final.py`**. There is no `main.py` entry point in the current repository.

**বাংলা:** `cd Ghost-Track` করার পর `python saint_final.py` চালান। এই ফাইল থেকেই মূল Menu চালু হয়।

To stop the application, select `0` in the menu. If the terminal is waiting for input, follow the on-screen prompt.

---

## 🧭 Main Menu Guide / মেনু ব্যবহার

### 1 — NID Scanner

- Enter a value containing digits; the current processor accepts lengths of 10, 13, or 17 digits as a valid *format*.
- It prints a Rich table and saves JSON, TXT, and HTML reports in `output/`.
- **Critical limitation:** The personal details in the current `tools/data/nid_processor.py` are hard-coded demo values (including a sample name pattern, date, gender, blood group and address). They are **not fetched from Bangladesh NID records and are not real identity data**.

**বাংলা:** NID নম্বরের দৈর্ঘ্য/ফরম্যাট পরীক্ষা করে Demo রিপোর্ট তৈরি করে। এখানে দেখানো নাম, জন্মতারিখ, ঠিকানা, রক্তের গ্রুপ ইত্যাদি বাস্তব NID Database থেকে আসে না—কোডে Demo হিসেবে নির্ধারিত। এগুলো বিশ্বাস বা ব্যবহার করবেন না।

### 2 — Phone Number Analysis

- Enter a Bangladesh number such as `017XXXXXXXX` or an international number such as `+88017XXXXXXXX`.
- Uses the `phonenumbers` package for number validity/possibility, country/region description, carrier metadata, number type and time zones.
- Performs basic HTTP checks against WhatsApp and Telegram public URLs; these checks do **not** reliably prove that a number is registered or that an account belongs to a person.
- Creates an HTML report in `output/`.
- If `GEMINI_API_KEY` is configured, the code sends the phone-analysis data to Google's Gemini API for a Bengali text assessment. Do not submit someone else's personal number without a lawful reason and permission.

**বাংলা:** `017XXXXXXXX` অথবা `+88017XXXXXXXX` ফরম্যাটে নম্বর দিন। Package থেকে নম্বরের format, সম্ভাব্য validity, carrier/region ও timezone metadata পাওয়া যায়। WhatsApp/Telegram check কেবল সাধারণ URL response দেখে—এটি account registration-এর নিশ্চিত প্রমাণ নয়। Gemini key দিলে নম্বর-সংক্রান্ত analysis data Google Gemini API-তে পাঠানো হয়।

### 3 — Email Investigation

- Enter an email address.
- Checks basic email syntax and attempts to open the email domain over HTTPS.
- Produces Google/GitHub/public breach-search links and an HTML report.
- The main-menu processor does **not** perform a verified breach-database lookup. A reachable website does not prove that an email inbox exists.

**বাংলা:** ইমেইলের basic format ও domain-এর HTTPS reachability পরীক্ষা করে এবং Search Link-সহ HTML রিপোর্ট বানায়। এটি inbox আছে কি না বা email কোনো breach-এ নিশ্চিতভাবে আছে কি না—তা যাচাই করে না।

### 4 — IP Address Analysis

- Enter an IP address, for example `8.8.8.8`.
- Queries the external `ip-api.com` service for country, region, city, coordinates, timezone, ISP/organization, ASN and proxy/hosting flags.
- Saves an HTML report in `output/`.
- Results are approximate network geolocation, not a person's exact home address. The IP is sent to the third-party lookup service.

**বাংলা:** IP address দিলে `ip-api.com` থেকে দেশ, অঞ্চল, শহর, আনুমানিক coordinates, timezone ও ISP-সংক্রান্ত তথ্য আনে। এটি কোনো ব্যক্তির সঠিক বাসার ঠিকানা নয়। Lookup করার সময় IP তৃতীয় পক্ষের Service-এ পাঠানো হয়।

### 5 — Social Media Analysis

- Enter a public username (with or without `@`).
- Checks profile URLs on GitHub, X, Instagram, Reddit, Pinterest, Telegram, TikTok, Medium and Dev.to.
- Uses HTTP response codes to label results and saves an HTML report.
- A HTTP 200 response may be a login, challenge or generic page; it is not conclusive proof of an account. A 404 or request failure can also be misleading.

**বাংলা:** Public username দিয়ে ৯টি Platform-এর Profile URL check করে। শুধু HTTP status code দেখে ফলাফল দেয়; তাই কোনো Profile নিশ্চিতভাবে আছে/নেই—এমন সিদ্ধান্ত নেওয়া যাবে না।

### 6 — Dark Web Scan

- Enter a query only when you have a lawful reason to check your own or an authorized organization's exposure.
- The main-menu processor makes a request to a public breach-search URL and creates links to public search services.
- Its current `leak_detected` result is based on a simple HTTP status check, not on parsing and validating confirmed breach records.
- This is **not** a full dark-web crawler or a verified dark-web scan.

**বাংলা:** নিজের বা অনুমোদিত প্রতিষ্ঠানের exposure পরীক্ষা করার বৈধ প্রয়োজন থাকলেই query দিন। বর্তমান কোড সাধারণ HTTP status দেখে ফলাফল নির্ধারণ করে এবং কিছু Public Search Link তৈরি করে। এটি পূর্ণাঙ্গ Dark Web Scanner নয় এবং ফলাফল নিশ্চিত breach evidence নয়।

### 7 — Website Reconnaissance

- Enter a domain you own or are authorized to assess, for example `example.com`.
- Resolves the domain to an IP, requests its HTTPS page, reads the HTTP status and server header, and checks a few security headers.
- Adds public WHOIS, DNS and certificate-transparency search links to the HTML report.
- This is a basic informational check, not a penetration test.

**বাংলা:** নিজের বা অনুমতিপ্রাপ্ত Website-এর Domain দিন। এটি DNS থেকে IP resolve, HTTPS request, HTTP status, Server header এবং কয়েকটি Security Header পরীক্ষা করে। এটি Penetration Test নয়।

### 8 — View Scan History

Lists HTML report files in `output/`, newest first. It does not search every JSON/TXT file or the SQLite database.

**বাংলা:** `output/` Folder-এর HTML রিপোর্টগুলো নতুন থেকে পুরোনো ক্রমে দেখায়। JSON/TXT বা Database-এর সব তথ্য দেখায় না।

### 9 — Settings

- Option 1: Displays Python version, output path and whether `GEMINI_API_KEY` exists.
- Option 2: Sets `GEMINI_API_KEY` for the current process only. It is not saved permanently.
- Option 3: After confirmation, deletes **all regular files** directly inside `output/` (not only HTML reports). Back up anything important first.
- Option 0: Returns to the main menu.

**বাংলা:** Option 1-এ System/API key status, Option 2-এ বর্তমান Session-এর জন্য Gemini key সেট করা যায়, Option 3-এ Confirm করলে `output/`-এর সব regular file মুছে যায়—শুধু HTML নয়। তাই আগে Backup রাখুন।

---

## 🗂️ Project Files / ফাইল পরিচিতি

### Root files / মূল ফাইল

| File | Purpose / কাজ |
|---|---|
| `saint_final.py` | Main CLI entry point; creates processors and displays the 0–9 menu. / মূল Menu ও Processor চালায়। |
| `requirements.txt` | Pinned Python dependencies. / Python package তালিকা। |
| `set.py` | Optional setup script; creates folders and overwrites `config/security.key` and `config/settings.json`, then asks for API keys. It is not required to start the main menu. / Setup script; চালালে Key ও Config ফাইল overwrite করে। |
| `fix_menu.py` | A patch helper that attempts to rewrite `saint_final.py`. **Do not run it** if you want to keep source code unchanged. / এটি `saint_final.py` পরিবর্তনের চেষ্টা করে; চালাবেন না। |
| `.gitignore` | Git ignore patterns; currently contains only generic object/Ada patterns. / Git ignore নিয়ম। |
| `LICENSE` | MIT License. / MIT লাইসেন্স। |
| `README.md` | This bilingual documentation. / এই বাংলা-ইংরেজি নির্দেশিকা। |

### Main menu processors / মূল Menu-র Processor

| File | Purpose / কাজ |
|---|---|
| `tools/data/nid_processor.py` | NID format check, demo data, Rich table, JSON/TXT/HTML report. / NID Demo রিপোর্ট। |
| `tools/data/phone_processor.py` | Phone parsing, carrier/region/timezone metadata, basic WhatsApp/Telegram checks, optional Gemini analysis, HTML report. / Phone metadata ও রিপোর্ট। |
| `tools/data/email_processor.py` | Email syntax, domain HTTPS check and public search links, HTML report. / Email ও Domain check। |
| `tools/data/ip_processor.py` | IP geolocation lookup through ip-api.com and HTML report. / IP তথ্য ও রিপোর্ট। |
| `tools/data/social_processor.py` | Public profile URL checks across nine platforms and HTML report. / Social profile link check। |
| `tools/data/darkweb_processor.py` | Limited public breach-search request and search links, HTML report. / সীমিত breach-search ও রিপোর্ট। |
| `tools/data/web_processor.py` | DNS resolution, HTTPS response/header checks, public recon links, HTML report. / Website basic recon। |
| `tools/data/history_processor.py` | Lists HTML reports in `output/`. / HTML রিপোর্টের History। |
| `tools/data/settings_processor.py` | Gemini environment-key status/update and output-file clearing menu. / Settings Menu। |
| `tools/data/provider_mail.py` | Email-domain/provider mapping helper. / Email provider mapping। |
| `tools/data/providers_phone.py` | Bangladesh mobile prefix/operator mapping helper. / মোবাইল Operator mapping। |
| `tools/data/region_code.py` | Bangladesh division/operator lookup helper. / Division ও Operator lookup helper। |
| `tools/data/email_proci.py` | Alternate email processor with MX lookup and disposable-domain list; not imported by the main menu. / বিকল্প Email Processor। |
| `tools/data/ip_proci.py` | Alternate IPv4/IPv6 validation, reverse-DNS and geolocation helper; not imported by the main menu. / বিকল্প IP Processor। |
| `tools/data/phone_proci.py` | Alternate phone metadata processor using provider mapping; not imported by the main menu. / বিকল্প Phone Processor। |

### Utility modules / সহায়ক Module

| File | Purpose / কাজ |
|---|---|
| `tools/utils/api_handler.py` | Generic HTTP API request helper with logging. / API Request helper। |
| `tools/utils/common.py` | Phone/email/IPv4 validation, JSON save and Rich table helpers. / Validation ও display helper। |
| `tools/utils/config_manager.py` | Read/write JSON configuration and API-key settings. / Config read/write। |
| `tools/utils/db_handler.py` | SQLite schema and scan-history read/write helpers. / SQLite Database helper। |
| `tools/utils/encryption.py` | Fernet encryption/decryption helper. / Data encryption helper। |
| `tools/utils/logger.py` | Writes application activity to `logs/` and terminal. / Logging helper। |
| `tools/utils/report_generator.py` | Generic JSON/TXT/HTML report generator. / Report তৈরি helper। |
| `tools/utils/updater.py` | Release-check/download helper currently pointing to a different GitHub repository (`Mj-user/saint-pegasus`); not used by the main menu. Do not rely on it for Ghost-Track updates. / এটি অন্য Repository-তে নির্দেশ করে; Ghost-Track update হিসেবে ব্যবহার করবেন না। |

### Other standalone / experimental tools / অন্যান্য আলাদা Tool

| File or folder | Purpose / কাজ |
|---|---|
| `tools/darkweb_scan.py` | Older Dark Web scanner stub; returns simulated/disabled results. / Simulated পুরোনো Scanner। |
| `tools/darkweb/darkweb_scanner.py` | Experimental scanner configured with `api.darkweb.local` placeholder endpoints; not a working live service. / Placeholder API-সহ Experimental Module। |
| `tools/investig_email.py` | Alternate email investigator; WHOIS domain info, but breach/social checks are disabled. / বিকল্প Email Investigator। |
| `tools/nik_scan.py` | NIK/NID demo parser with generated sample data; not a real NID lookup. / Demo NID Parser। |
| `tools/osint/osint_tools.py` | Optional wrappers for external Sherlock and Holehe command-line tools; not connected to the main menu. / External CLI Tool wrapper। |
| `tools/network/network_scan.py` | Optional Nmap-based basic/full/vulnerability scan wrapper; not connected to the main menu. / Nmap wrapper। |
| `tools/social/analyz_social.py` | Alternate public social-profile page parser. / বিকল্প Social Analyzer। |
| `tools/social/social_analyzer.py` | Same content as `analyz_social.py` in the current tree. / একই কোডের duplicate। |
| `tools/social/social_tracker.py` and `tools/track_social.py` | Simulated profile-link tracker; does not make live profile checks in its current implementation. / Simulated Tracker। |
| `tools/stego/stego_analyz.py` | Image metadata/statistical/LSB/edge analysis; suspicious-region result is a placeholder. / Image steganography indicator analysis। |
| `tools/metafile/metafile.py` | Image EXIF and PDF metadata extraction; other file types receive only basic attributes. / File metadata extraction। |
| `tools/web/web_recon.py` | Alternate WHOIS, DNS, SSL certificate, HTTP-header and technology checks. / Advanced/alternate Website recon helper। |
| `tools/wireles/wifi_scanner.py` | Scapy beacon-frame Wi-Fi discovery and simulated vulnerability result; requires compatible wireless hardware/permissions. / Wi-Fi beacon discovery। |

### Duplicate folders and stored files / Duplicate ও সংরক্ষিত ফাইল

- `tools/file/` contains copies of several processors also present under `tools/data/`. The main menu imports from `tools/data/`, not `tools/file/`.
- `tools/__init__.py` and subfolder `__init__.py` files mark Python packages; most are intentionally empty.
- `tools/**/__pycache__/` contains generated Python bytecode (`.pyc`) and is not source code.
- `config/settings.json` stores basic configuration. A second directory whose name begins with an invisible zero-width character also contains a settings file; it is not referenced by the main menu.
- `logs/` contains log output. `output/` contains previously generated scan reports (HTML/JSON/TXT). These are data artifacts, not program modules.

---

## ⚙️ Configuration / কনফিগারেশন

### Optional Gemini API key

Only the phone-analysis processor reads `GEMINI_API_KEY`. Without it, the AI section returns an offline/fallback note. The main menu does not require this key.

For the current Termux session:

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
python saint_final.py
```

To load it in future Termux sessions, add the export line to your shell startup file (for example `~/.bashrc`) and reload that file. Keep your real key private; never commit it to GitHub.

**বাংলা:** Gemini API Key ঐচ্ছিক। Key না দিলেও Main Menu চলবে; শুধু Phone analysis-এর AI অংশ Fallback message দেখাবে। Key দিলে Phone analysis-এর তথ্য Google Gemini-তে পাঠানো হয়। নিজের Key Public Repository-তে রাখবেন না।

### Existing config and encryption key

- `config/settings.json` currently contains basic version/author/log/API-key fields.
- The main menu's current processors do not read the API keys stored in that JSON file.
- `config/security.key` is tracked in the repository. Treat a committed encryption key as exposed; do not use it to protect new sensitive data. Key rotation/removal is a separate maintenance task and has **not** been performed as part of this README-only update.
- Running `python set.py` rewrites the security key and settings file. It is not needed for the normal launch.

**বাংলা:** `config/security.key` GitHub-এ আছে, তাই এটিকে নিরাপদ Secret ধরে নেওয়া যাবে না। `set.py` চালালে Key ও Settings overwrite হবে—সাধারণভাবে Bot/Tool চালু করতে এটি প্রয়োজন নেই।

---

## 📄 Reports and Logs / রিপোর্ট ও লগ

The main processors create reports under `output/`. Depending on the selected menu option, reports may be HTML, JSON and/or TXT. Open an HTML report in a browser:

```bash
termux-open output
```

If `termux-open` is unavailable, use your Android file manager to open the project folder and then open a report file.

Logs are stored under `logs/`. Do not publish reports or logs that contain personal identifiers, IP addresses, email addresses or other private information.

**বাংলা:** Scan শেষে `output/` Folder-এ রিপোর্ট তৈরি হয়। HTML রিপোর্ট Browser-এ খুলতে পারেন। রিপোর্ট বা Log-এ ব্যক্তিগত তথ্য থাকলে Public করবেন না।

---

## 🧩 Optional Modules / অতিরিক্ত মডিউল

These modules are not required for the main menu and their dependencies are not all included in `requirements.txt`.

| Module | Additional dependency / requirement |
|---|---|
| `tools/web/web_recon.py`, `tools/data/email_proci.py` | `dnspython` for DNS resolver; `python-whois` for WHOIS. |
| `tools/stego/stego_analyz.py` | Pillow, NumPy, SciPy and OpenCV (`cv2`). |
| `tools/metafile/metafile.py` | Pillow; PyPDF2 for PDF metadata; optional python-magic plus system libmagic. |
| `tools/network/network_scan.py` | Nmap system binary and `python-nmap`. |
| `tools/wireles/wifi_scanner.py` | Scapy, a compatible Wi-Fi interface, monitor-mode support and appropriate OS permissions. Standard Android/Termux devices may not support this. |
| `tools/osint/osint_tools.py` | Sherlock and Holehe command-line programs installed separately. |

Install optional Python packages only when you intend to use the relevant module. Example:

```bash
pip install dnspython Pillow numpy scipy PyPDF2 python-magic python-nmap scapy
```

This example does not install native tools such as Nmap or libmagic, nor external CLI tools such as Sherlock/Holehe. OpenCV installation can be difficult on Termux and may require a compatible build.

**বাংলা:** এগুলো Main Menu-র জন্য বাধ্যতামূলক নয়। যে Optional Module ব্যবহার করবেন, তার প্রয়োজনীয় Package/Native Tool আলাদাভাবে ইনস্টল করতে হবে। Termux-এ সব Native/Hardware Module কাজ করবে—এমন নিশ্চয়তা নেই।

---

## ⚠️ Known Limitations / সীমাবদ্ধতা

1. **NID output is mock data.** The current NID processor does not connect to an official NID database.
2. **Dark-web features are incomplete.** Some endpoints are placeholders or disabled; a simple HTTP status is not proof of a leak.
3. **Social and messaging checks are heuristic.** HTTP status or public links cannot establish account ownership or registration with certainty.
4. **IP geolocation is approximate.** It usually describes a network exit/provider, not a precise person location.
5. **Optional tools are not wired into the main menu.** Having a Python file does not mean the feature is available from the numbered menu.
6. **Dependency list is incomplete for optional modules.** See the optional-module table.
7. **Updater points to another project.** Do not use its update URL as the official Ghost-Track source.
8. **`fix_menu.py` changes source code.** Do not execute it if the intention is to keep all source files unchanged.

**বাংলা:** NID তথ্য Demo; Dark Web endpoint-এর কিছু অংশ Placeholder/Disabled; Social ও Messaging check নিশ্চিত নয়; IP location আনুমানিক; Optional Tool Main Menu-তে যুক্ত নয়; কিছু dependency requirements-এ নেই; Updater অন্য Repository-তে নির্দেশ করে; এবং `fix_menu.py` চালালে মূল Python ফাইল পরিবর্তনের চেষ্টা করে।

---

## 🛠️ Troubleshooting / সমস্যা সমাধান

### `ModuleNotFoundError`

Install the missing package. For the main menu, retry:

```bash
pip install -r requirements.txt
```

If a missing module belongs to an optional utility, install the corresponding optional dependency listed above.

### `python: command not found`

```bash
pkg install python -y
```

### Repository folder not found

Check your current directory:

```bash
pwd
ls
cd Ghost-Track
```

### Network/API request fails

Check your internet connection. Public services may rate-limit, block automated requests, change their pages, or be temporarily unavailable. A failed request does not prove that a profile, email or service does not exist.

### Report folder missing

The report-generating processors create `output/` when they save a report. If needed:

```bash
mkdir -p output logs
```

### Exit and restart

Choose `0` to exit, then run:

```bash
python saint_final.py
```

---

## 🔐 Privacy and Responsible Use / গোপনীয়তা ও দায়িত্বশীল ব্যবহার

- Use the toolkit only for your own information, systems you own, or targets for which you have clear authorization.
- Do not use it to harass, stalk, dox, impersonate, or access another person's private information.
- Do not enter real NID numbers, private phone numbers, private email addresses or confidential identifiers unless you have a lawful basis and permission.
- Phone analysis may send its input data to Google Gemini when `GEMINI_API_KEY` is configured. IP lookup sends the IP address to ip-api.com. Website/social/email modules contact third-party sites.
- Store reports securely and remove sensitive reports from shared/public locations.
- Follow applicable laws, platform terms and rate limits.

**বাংলা:** শুধু নিজের তথ্য, নিজের System অথবা স্পষ্ট অনুমতিপ্রাপ্ত Target-এ ব্যবহার করুন। কাউকে হয়রানি, Stalking, Doxxing বা ব্যক্তিগত তথ্য সংগ্রহের জন্য ব্যবহার করবেন না। Gemini Key থাকলে Phone analysis-এর data Google-এ এবং IP lookup-এর IP ip-api.com-এ পাঠানো হয়। রিপোর্ট নিরাপদে রাখুন এবং আইন ও Platform-এর নিয়ম মেনে চলুন।

---

## 📜 License

This project includes an MIT License. See [LICENSE](LICENSE) for the full terms.

---

## 👨‍💻 Repository

- **GitHub:** https://github.com/riyad12sk/Ghost-Track
- **Main launcher:** `saint_final.py`
- **Current documented version string in the banner:** `1.0.0`

If you find a bug, verify it against the actual implementation before relying on a scan result. Contributions should clearly distinguish working features from simulated or experimental modules.
