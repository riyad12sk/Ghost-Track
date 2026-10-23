import os
import json
import sys
from rich.console import Console
from rich.prompt import Prompt
from cryptography.fernet import Fernet

console = Console()

def setup_environment():
    """Setup lingkungan aplikasi"""
    try:
        # Buat direktori
        directories = ['config', 'tools', 'logs', 'output']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            console.print(f"[green]✓[/green] Creating directory {directory}")

        # Generate kunci enkripsi
        key = Fernet.generate_key()
        with open('config/security.key', 'wb') as f:
            f.write(key)
        console.print("[green]✓[/green] Generating encryption key")

        # Setup konfigurasi
        setup_config()

        console.print("\n[bold green]Setup Successful![/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error during setup: {str(e)}[/bold red]")
        sys.exit(1)

def setup_config():
    """Setup file konfigurasi"""
    config = {
        "version": "1.0.0",
        "author": "SK BLACK",  # <-- এখানে আপনার নাম দেওয়া হলো
        "max_login_attempts": 3,
        "log_level": "INFO",
        "api_keys": {}
    }

    # Tanya API keys
    console.print("\n[bold]Setup API Keys (Bangladesh +880 Compatible)[/bold]")
    apis = ["truecaller", "ipapi", "shodan"]
    for api in apis:
        key = Prompt.ask(f"Enter API key for {api} (Leave blank if none)")
        if key:
            config["api_keys"][api] = key

    # Simpan konfigurasi
    with open('config/settings.json', 'w') as f:
        json.dump(config, f, indent=4)
    console.print("[green]✓[/green] Saving configuration")

if __name__ == "__main__":
    console.print("[bold]🦄 SK-BLACK-Track-Ultimate Setup[/bold]")  # <-- এখানে আপনার নাম দেওয়া হলো
    setup_environment()
