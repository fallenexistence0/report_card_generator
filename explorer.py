from tkinter import *
from tkinter import filedialog
import tkinter as tk



class FileExplorer():

    @staticmethod
    def browseFiles():
        csv_file_path = filedialog.askopenfilename(
            initialdir="~/Downloads",
            title="Select a file",
            filetypes=(
                ("Text files", "*.csv"),
                ("All files", "*.*"))
        )

        return csv_file_path



        #label_file_explorer.configure(text="File Opened: "+filename)
