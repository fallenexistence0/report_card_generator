from tkinter import *
from tkinter import filedialog
import tkinter as tk



class FileExplorer():

    def browseFiles():
        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select a file",
            filetypes=(
                ("Text files", "*.csv"),
                ("All files", "*.*"))
        )

        #label_file_explorer.configure(text="File Opened: "+filename)







#explorer.mainloop()