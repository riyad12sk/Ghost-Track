import html
import json
import os
import re
from datetime import datetime

from rich.console import Console
from rich.table import Table

console = Console()


class NIDProcessor:
    """Perform local NID input-format checks only.

    This class does not access Bangladesh Election Commission systems or
    retrieve identity, demographic, address, or family information.
    """

    ACCEPTED_LENGTHS = (10, 13, 17)

    def analyze_nid(self, nid_number):
        raw_value = str(nid_number or "").strip()
        digits = re.sub(r"\D", "", raw_value)

        if not digits or not raw_value:
            return {"error": True, "message": "Enter a NID number containing digits."}

        only_digits = bool(re.fullmatch(r"[0-9\s-]+", raw_value))
        recognized_length = len(digits) in self.ACCEPTED_LENGTHS
        masked_nid = ("*" * max(0, len(digits) - 4)) + digits[-4:]

        timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
        result = {
            "timestamp": timestamp,
            "target_nid": masked_nid,
            "status": "Format check completed",
            "checks": {
                "digits_only": only_digits,
                "digit_count": len(digits),
                "recognized_common_length": recognized_length,
                "format_result": (
                    "Length matches a commonly used Bangladesh NID format; "
                    "this does not verify that the number exists or is genuine."
                    if only_digits and recognized_length
                    else "Input does not match the expected digit-only/common-length pattern."
                ),
                "identity_verified": False,
                "verification_method": "Local format check only; no government database/API queried."
            },
            "notice": (
                "This tool cannot retrieve or verify a person's name, date of birth, "
                "parents, blood group, photograph, or address. Use only an official "
                "Election Commission verification service with authorized access."
            )
        }

        table = Table(title="NID Format Check", show_header=True, header_style="bold cyan")
        table.add_column("Field", style="bold")
        table.add_column("Result")
        table.add_row("Masked NID", masked_nid)
        table.add_row("Digit count", str(len(digits)))
        table.add_row("Digits-only input", "Yes" if only_digits else "No")
        table.add_row("Common length", "Recognized" if recognized_length else "Not recognized")
        table.add_row("Identity verified", "No")
        console.print(table)

        os.makedirs("output", exist_ok=True)
        filename_stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        base_path = os.path.join("output", f"nid_format_{filename_stamp}")
        json_file = base_path + ".json"
        txt_file = base_path + ".txt"
        html_file = base_path + ".html"

        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=2, ensure_ascii=False)

        with open(txt_file, "w", encoding="utf-8") as file:
            file.write("Ghost-Track NID Format Check\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Masked NID: {masked_nid}\n")
            file.write(f"Digit count: {len(digits)}\n")
            file.write(f"Digits only: {only_digits}\n")
            file.write(f"Common length recognized: {recognized_length}\n")
            file.write("Identity verified: No\n")
            file.write(result["notice"] + "\n")

        safe_result = html.escape(json.dumps(result, indent=2, ensure_ascii=False))
        html_content = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ghost-Track NID Format Check</title>
<style>
body{{font-family:Arial,sans-serif;background:#0f172a;color:#f8fafc;padding:24px}}
main{{max-width:850px;margin:auto;background:#1e293b;padding:24px;border-radius:12px}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#0b1220;padding:16px;border-radius:8px}}
.notice{{color:#fbbf24}}
</style>
</head>
<body><main>
<h1>Ghost-Track — NID Format Check</h1>
<p>Masked NID: <strong>{html.escape(masked_nid)}</strong></p>
<p class="notice">Format checking only. This report does not verify identity or retrieve government records.</p>
<pre>{safe_result}</pre>
</main></body></html>"""
        with open(html_file, "w", encoding="utf-8") as file:
            file.write(html_content)

        result["report_saved"] = html_file
        result["reports"] = {"json": json_file, "txt": txt_file, "html": html_file}
        console.print(f"\n[green]Reports saved:[/green] {json_file}, {txt_file}, {html_file}")
        return result

    def generate_html_report(self, data, filename):
        """Write a safe HTML report for a supplied NID format-check result."""
        safe_data = html.escape(json.dumps(data, indent=2, ensure_ascii=False))
        with open(filename, "w", encoding="utf-8") as file:
            file.write(
                "<!doctype html><html lang='en'><meta charset='utf-8'>"
                "<title>NID Format Check</title><body>"
                "<h1>NID Format Check — identity not verified</h1>"
                f"<pre>{safe_data}</pre></body></html>"
            )
