"""
SweetDreamzProcessor
GUI Module
"""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, ttk

from config import Config
from utils.logger import get_logger
from processor.workbook import WorkbookManager


class SweetDreamzApp:
    """Main GUI application."""

    def __init__(self) -> None:
        self.logger = get_logger(__name__)
        self.workbook = WorkbookManager()

        self.root = tk.Tk()
        self.root.title(Config.TITLE)
        self.root.geometry(
            f"{Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT}"
        )

        self.selected_file: Path | None = None

        self.create_widgets()

    def create_widgets(self) -> None:

        title = tk.Label(
            self.root,
            text=Config.APP_NAME,
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=15)

        self.file_label = tk.Label(
            self.root,
            text="No workbook selected.",
            fg="blue"
        )

        self.file_label.pack()

        browse_btn = ttk.Button(
            self.root,
            text="Browse Workbook",
            command=self.browse_workbook
        )

        browse_btn.pack(pady=10)

        self.progress = ttk.Progressbar(
            self.root,
            length=600,
            mode="determinate"
        )

        self.progress.pack(pady=10)

        tk.Label(
            self.root,
            text="Application Log"
        ).pack()

        self.log_box = tk.Text(
            self.root,
            width=110,
            height=20
        )

        self.log_box.pack(padx=10, pady=10)

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=15)

        self.process_btn = ttk.Button(
            button_frame,
            text="Process Workbook",
            state="disabled"
        )

        self.process_btn.grid(row=0, column=0, padx=10)

        ttk.Button(
            button_frame,
            text="Exit",
            command=self.root.destroy
        ).grid(row=0, column=1)

        self.log("Application Started.")

    def browse_workbook(self) -> None:
        """Browse and load an Excel workbook."""

        filename = filedialog.askopenfilename(
            title="Select Workbook",
            filetypes=[
                ("Excel Workbook", "*.xlsx *.xlsm")
            ]
        )

        if not filename:
            return

        try:
            self.workbook.load(filename)

            info = self.workbook.information()

            self.selected_file = Path(filename)

            self.file_label.config(
                text=info["filename"]
            )

            self.process_btn.config(state="normal")

            self.log("Workbook Loaded Successfully")
            self.log(f'Worksheets : {info["worksheets"]}')
            self.log(f'Rows : {info["rows"]}')
            self.log(f'Columns : {info["columns"]}')
            self.log(
                "Sheet Names : "
                + ", ".join(info["sheet_names"])
            )

        except Exception as e:
            self.log(f"ERROR: {e}")

    def log(self, message: str) -> None:

        self.logger.info(message)

        self.log_box.insert(
            tk.END,
            message + "\n"
        )

        self.log_box.see(tk.END)

    def run(self) -> None:
        """Start GUI."""
        self.root.mainloop()