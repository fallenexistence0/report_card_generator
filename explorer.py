from tkinter import *
from tkinter import filedialog
import tkinter as tk

from pathlib import Path


default_path = Path.home() / "Downloads"

class FileExplorer():


    @staticmethod
    def browseFiles():
        csv_file_path = filedialog.askopenfilename(
            initialdir=str(default_path),
            title="Select a file",
            filetypes=(
                ("Text files", "*.csv"),
                ("All files", "*.*"))
        )

        return csv_file_path


        #label_file_explorer.configure(text="File Opened: "+filename)
