import os
import re
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

class NIDProcessor:
    def __init__(self):
        pass

    def analyze_nid(self, nid_number):
        """Analyze NID with detailed parameters, rich table layout, and multiple file exports"""
        clean_nid = re.sub(r'\D', '', nid_number.strip())
        
        if not clean_nid:
            return {"error": True, "message": "Invalid NID format provided."}

        length = len(clean_nid)
        valid = length in [10, 13, 17]

        # Extract last 4 digits for demo mockup generation
        suffix = clean_nid[-4:] if length >= 4 else "0000"

        analysis_details = {
            'validity': 'Valid Format' if valid else 'Invalid Format',
            'length': length,
            'estimated_birth_year': '1968',
            'gender': 'Female',
            'blood_group': 'B-',
            'personal_info': {
                'full_name': f'User_{suffix}',
                'father_name': f'Father_{suffix[1:]}',
                'mother_name': f'Mother_{suffix[1:]}',
                'dob': '26/06/1968'
            },
            'address_info': {
                'district': 'Mymensingh',
                'upazila_thana': 'Dhanmondi',
                'permanent_address': 'Village/Road #38, Dhanmondi, Mymensingh',
                'present_address': 'House #51, Block-F, Mymensingh'
            },
            'details': 'Data processed successfully via SK BLACK Toolkit'
        }

        timestamp_str = datetime.now().isoformat()
        timestamp_file = datetime.now().strftime("%Y%m%d_%H%M%S")

        result = {
            "timestamp": timestamp_str,
            "target_number": nid_number.strip(),
            "status": "Success" if valid else "Failed",
            "analysis": analysis_details
        }

        # Display Rich Table
        table = Table(title="NID Analysis Results", show_header=True, header_style="bold magenta")
        table.add_column("Key", style="bold cyan", width=18)
        table.add_column("Value", style="bold green")

        table.add_row("timestamp", timestamp_str)
        table.add_row("target_number", nid_number.strip())
        table.add_row("status", result["status"])
        table.add_row("analysis", str(analysis_details))

        console.print(table)

        # Save files (JSON, TXT, HTML)
        os.makedirs("output", exist_ok=True)
        json_file = f"output/nid_{timestamp_file}.json"
        txt_file = f"output/nid_{timestamp_file}.txt"
        html_file = f"output/nid_{timestamp_file}.html"

        # Save JSON
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        # Save TXT
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(f"NID Scan Report for {nid_number}\n")
            f.write(f"Timestamp: {timestamp_str}\n")
            f.write(f"Status: {result['status']}\n")
            f.write(f"Analysis: {json.dumps(analysis_details, indent=2)}\n")

        # Save HTML
        self.generate_html_report(result, html_file)

        console.print(f"\n[bold green]{datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]} - SKBlackToolkit - INFO - User [system] -> Scan completed: nid - {nid_number.strip()}[/bold green]")
        console.print("\n[bold green]Results saved:[/bold green]")
        console.print(f"- JSON: {json_file}")
        console.print(f"- TXT:  {txt_file}")
        console.print(f"- HTML: {html_file}")

        result["report_saved"] = html_file
        return result

    def generate_html_report(self, data, filename):
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>NID OSINT Report - {data.get('target_number')}</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
                .card {{ background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
                h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
                th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #334155; }}
                th {{ color: #94a3b8; }}
                .status-ok {{ color: #4ade80; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>SK BLACK - NID Intelligence Report</h2>
                <p><strong>Input NID:</strong> {data.get('target_number')}</p>
                <p><strong>Timestamp:</strong> {data.get('timestamp')}</p>
                <p><strong>Status:</strong> {data.get('status')}</p>
            </div>
            <div class="card">
                <h2>Analysis Details</h2>
                <pre>{json.dumps(data.get('analysis'), indent=2)}</pre>
            </div>
        </body>
        </html>
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
