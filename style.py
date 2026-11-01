from tkinter import *
import tkinter as tk

from tkinter import filedialog
from explorer import FileExplorer

from PIL import Image, ImageTk

class ReportCardGUI:



    def __init__(self):
            
        self.window = tk.Tk()

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()


        self.window.geometry("%dx%d" % (width, height)) 

        
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)


        self.button_frame = tk.Frame(self.window)
        self.button_frame.grid(
            row=0,
            column=0
        )

        self.window.title(
            "Jefferson Academy -Report Card Generator"
            )

        self.icon = tk.PhotoImage(
            file="assets/logos/jefferson_academy_logo_2.png"
            )

        self.window.iconphoto(True, self.icon)

    



        self.browse_files_button = tk.Button(
            self.button_frame, 
            text='Browse files',
            command=FileExplorer.browseFiles,
            font=('Ink Free', 10, "bold"),
            bg='pink',
            fg='black',
            width=20,
            height=2
            )

        self.browse_files_button.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.button_exit = Button(
            self.button_frame,
            width=20,
            height=2,
            bg="yellow", 
            text = "Exit",
            command = exit
            ) 

        self.button_exit.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )



    def click(self):
        self.FileExplorer()


    def run(self):
        self.window.mainloop()