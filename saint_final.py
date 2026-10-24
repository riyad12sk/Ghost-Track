import os
import sys
from rich.console import Console
from rich.panel import Panel

# Import processors
from tools.data.nid_processor import NIDProcessor
from tools.data.phone_processor import PhoneProcessor
from tools.data.email_processor import EmailProcessor
from tools.data.ip_processor import IPProcessor
from tools.data.social_processor import SocialProcessor
from tools.data.darkweb_processor import DarkWebProcessor
from tools.data.web_processor import WebProcessor
from tools.data.history_processor import HistoryProcessor
from tools.data.settings_processor import SettingsProcessor

console = Console()

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    banner = r"""
   / __ \/  _/\ \/ /   |  / __ \   /_  __/ __ \/  | / ____/ //_/
Phone & OSINT Toolkit | Developed by: SK BLACK | Version: 1.0.0
    """
    console.print(f"[bold cyan]{banner}[/bold cyan]")

def main_menu():
    nid_proc = NIDProcessor()
    phone_proc = PhoneProcessor()
    email_proc = EmailProcessor()
    ip_proc = IPProcessor()
    social_proc = SocialProcessor()
    darkweb_proc = DarkWebProcessor()
    web_proc = WebProcessor()
    history_proc = HistoryProcessor()
    settings_proc = SettingsProcessor()

    while True:
        show_banner()
        print("[1] NID Scanner")
        print("[2] Phone Number Analysis")
        print("[3] Email Investigation")
        print("[4] IP Address Analysis")
        print("[5] Social Media Analysis")
        print("[6] Dark Web Scan")
        print("[7] Website Reconnaissance")
        print("[8] View Scan History")
        print("[9] Settings")
        print("[0] Exit\n")
        
        choice = input("Select an option [1/2/3/4/5/6/7/8/9/0]: ").strip()

        if choice == "1":
            print("\n--- NID Scanner ---")
            nid_input = input("Enter NID: ").strip()
            if nid_input:
                nid_proc.analyze_nid(nid_input)
            input("\nPress Enter to continue...")

        elif choice == "2":
            print("\n--- Phone Number Analysis ---")
            num = input("Enter phone number (format: +880xxx): ").strip()
            if num:
                phone_proc.analyze_phone(num)
            input("\nPress Enter to continue...")

        elif choice == "3":
            print("\n--- Email Investigation ---")
            email = input("Enter email address: ").strip()
            if email:
                email_proc.analyze_email(email)
            input("\nPress Enter to continue...")

        elif choice == "4":
            print("\n--- IP Address Analysis ---")
            ip = input("Enter IP Address (e.g., 8.8.8.8): ").strip()
            if ip:
                ip_proc.analyze_ip(ip)
            input("\nPress Enter to continue...")

        elif choice == "5":
            print("\n--- Social Media Analysis ---")
            user = input("Enter Target Username (e.g., riyad12sk): ").strip()
            if user:
                social_proc.analyze_social(user)
            input("\nPress Enter to continue...")

        elif choice == "6":
            print("\n--- Dark Web Scan ---")
            query = input("Enter Target Email/Username/Keyword to scan: ").strip()
            if query:
                darkweb_proc.analyze_darkweb(query)
            input("\nPress Enter to continue...")

        elif choice == "7":
            print("\n--- Website Reconnaissance ---")
            domain = input("Enter Target Domain (e.g., github.com): ").strip()
            if domain:
                web_proc.analyze_website(domain)
            input("\nPress Enter to continue...")

        elif choice == "8":
            print("\n--- View Scan History ---")
            history_proc.view_history()
            input("\nPress Enter to continue...")

        elif choice == "9":
            settings_proc.manage_settings()

        elif choice == "0":
            print("\n[+] Exiting Ghost-Track... Stay Safe!")
            sys.exit(0)

        else:
            print("\n[-] Option not fully configured yet.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
