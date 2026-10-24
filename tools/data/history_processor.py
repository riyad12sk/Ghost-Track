import os
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

class HistoryProcessor:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir

    def view_history(self):
        """List all generated HTML scan reports in output directory"""
        if not os.path.exists(self.output_dir):
            return {"message": "No scan history found. The output directory is empty.", "reports": []}

        files = [f for f in os.listdir(self.output_dir) if f.endswith(".html")]
        if not files:
            return {"message": "No scan history reports generated yet.", "reports": []}

        # Sort files by last modified time (newest first)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(self.output_dir, x)), reverse=True)

        report_list = []
        table = Table(title="📊 Ghost-Track Scan History Logs", show_header=True, header_style="bold cyan")
        table.add_column("#", style="dim", width=4)
        table.add_column("Report File Name", style="bold green")
        table.add_column("File Size (KB)", justify="right")
        table.add_column("Created Date & Time", style="magenta")

        for idx, file in enumerate(files, start=1):
            file_path = os.path.join(self.output_dir, file)
            size_kb = round(os.path.getsize(file_path) / 1024, 2)
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')

            table.add_row(str(idx), file, f"{size_kb} KB", mtime)
            report_list.append({
                "file": file,
                "path": file_path,
                "size": f"{size_kb} KB",
                "modified": mtime
            })

        console.print(table)
        return {"total_reports": len(report_list), "reports": report_list}
