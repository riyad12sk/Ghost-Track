import os
import sys
import shutil
from rich.console import Console
from rich.panel import Panel

console = Console()

class SettingsProcessor:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir

    def manage_settings(self):
        """Interactive settings manager for API Keys, Logs, and System info"""
        while True:
            console.print("\n[bold cyan]⚙️ Ghost-Track Settings & Configuration[/bold cyan]")
            print("[1] Check Environment & API Keys")
            print("[2] Set / Update GEMINI_API_KEY")
            print("[3] Clear Scan Reports History (output/)")
            print("[0] Back to Main Menu\n")

            choice = input("Select Settings Option [1/2/3/0]: ").strip()

            if choice == "1":
                gemini_key = os.getenv("GEMINI_API_KEY")
                key_status = "[bold green]Configured[/bold green]" if gemini_key else "[bold red]Not Set[/bold red]"
                
                info = f"""
[bold yellow]System Information:[/bold yellow]
• Python Version: {sys.version.split()[0]}
• Output Directory: {os.path.abspath(self.output_dir)}

[bold yellow]API Credentials Status:[/bold yellow]
• GEMINI_API_KEY: {key_status}
                """
                console.print(Panel(info.strip(), title="System & API Status", border_style="cyan"))
                input("\nPress Enter to continue...")

            elif choice == "2":
                new_key = input("\nEnter your GEMINI_API_KEY: ").strip()
                if new_key:
                    os.environ["GEMINI_API_KEY"] = new_key
                    console.print("[bold green][+] GEMINI_API_KEY updated for current session![/bold green]")
                    console.print("[dim]Tip: Add 'export GEMINI_API_KEY=your_key' to your ~/.bashrc or ~/.zshrc for permanent effect.[/dim]")
                else:
                    console.print("[yellow][!] No key entered.[/yellow]")
                input("\nPress Enter to continue...")

            elif choice == "3":
                confirm = input("\nAre you sure you want to delete ALL saved HTML scan reports? (y/N): ").strip().lower()
                if confirm == 'y':
                    if os.path.exists(self.output_dir):
                        for file in os.listdir(self.output_dir):
                            file_path = os.path.join(self.output_dir, file)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                        console.print("[bold green][+] All scan reports cleared successfully![/bold green]")
                    else:
                        console.print("[yellow][!] Output directory is already empty.[/yellow]")
                else:
                    console.print("[cyan][*] Action cancelled.[/cyan]")
                input("\nPress Enter to continue...")

            elif choice == "0":
                break
            else:
                console.print("[red][!] Invalid option. Please select 1, 2, 3, or 0.[/red]")
