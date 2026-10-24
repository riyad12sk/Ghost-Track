import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.pretty import pprint

# Import processors
from tools.data.phone_processor import PhoneProcessor
from tools.data.email_processor import EmailProcessor
from tools.data.ip_processor import IPProcessor
from tools.data.social_processor import SocialProcessor

console = Console()

def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    banner = r"""
   / __ \/  _/\ \/ /   |  / __ \   /_  __/ __ \/  | / ____/ //_/
Phone & OSINT Toolkit | Developed by: SK BLACK | Version: 1.0.0
    """
    console.print(f"[bold cyan]{banner}[/bold cyan]")

def main_menu():
    phone_proc = PhoneProcessor()
    email_proc = EmailProcessor()
    ip_proc = IPProcessor()
    social_proc = SocialProcessor()

    while True:
        show_banner()
        print("[1] NIK Scanner")
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
            print("\n[!] NIK Scanner selected...")
            input("\nPress Enter to continue...")

        elif choice == "2":
            print("\n--- Phone Number Analysis ---")
            num = input("Enter phone number (format: +880xxx): ").strip()
            if num:
                res = phone_proc.analyze_phone(num)
                pprint(res)
            input("\nPress Enter to continue...")

        elif choice == "3":
            print("\n--- Email Investigation ---")
            email = input("Enter email address: ").strip()
            if email:
                res = email_proc.analyze_email(email)
                pprint(res)
            input("\nPress Enter to continue...")

        elif choice == "4":
            print("\n--- IP Address Analysis ---")
            ip = input("Enter IP Address (e.g., 8.8.8.8): ").strip()
            if ip:
                res = ip_proc.analyze_ip(ip)
                pprint(res)
            input("\nPress Enter to continue...")

        elif choice == "5":
            print("\n--- Social Media Analysis ---")
            user = input("Enter Target Username (e.g., riyad12sk): ").strip()
            if user:
                res = social_proc.analyze_social(user)
                pprint(res)
            input("\nPress Enter to continue...")

        elif choice == "0":
            print("\n[+] Exiting Ghost-Track... Stay Safe!")
            sys.exit(0)

        else:
            print("\n[-] Option not fully configured yet.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
