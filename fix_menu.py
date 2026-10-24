with open('saint_final.py', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if 'def phone_scan_menu(self):' in line:
        skip = False
    # Check if we are inside phone_scan_menu
    if 'def phone_scan_menu(self):' in line:
        new_lines.append(line)
        continue
    
    # We will rewrite phone_scan_menu cleanly
    if 'def email_scan_menu(self):' in line:
        skip = False

# Let's do a cleaner approach: replace the phone_scan_menu definition entirely
content = "".join(lines)

old_target = """    def phone_scan_menu(self):
        \"\"\"Menu untuk analisis nomor telepon\"\"\"
        self.console.clear()
        self.console.print("[bold]Phone Number Analysis[/bold]")

        phone = Prompt.ask("[cyan]Enter phone number (format: +880xxx):[/cyan]")
        self.phone_processor.analyze_phone(phone)"""

new_target = """    def phone_scan_menu(self):
        \"\"\"Menu untuk analisis nomor telepon\"\"\"
        self.console.clear()
        self.console.print("[bold]Phone Number Analysis[/bold]")

        phone = Prompt.ask("[cyan]Enter phone number (format: +880xxx):[/cyan]")
        res = self.phone_processor.analyze_phone(phone)
        from rich.pretty import pprint
        pprint(res)
        input("\\nPress Enter to continue...")"""

if old_target in content:
    content = content.replace(old_target, new_target)
    with open('saint_final.py', 'w') as f:
        f.write(content)
    print("Successfully patched saint_final.py!")
else:
    print("Target block not found, checking alternatives...")
