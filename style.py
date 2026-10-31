from tkinter import *
import tkinter as tk

from tkinter import filedialog
from explorer import FileExplorer

class ReportCardGUI:



    def __init__(self):
            
        
        self.window = tk.Tk()

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        self.window.geometry("%dx%d" % (width, height))

        self.window.title(
            "Jefferson Academy -Report Card Generator"
            )

        self.icon = tk.PhotoImage(
            file="assets/logos/jefferson_academy_logo_2.png"
            )

        self.window.iconphoto(True, self.icon)

        self.browse_files_button = tk.Button(
            self.window, 
            text='Browse files',
            command=self.click,
            font=('Ink Free', 10, "bold"),
            bg='white',
            fg='black',
            padx=20,
            pady=10
            )

        self.browse_files_button.place(
            relx=0.5,
            rely=0.5,
            anchor='center'
        )


        self.label_file_explorer = Label(
            self.window,
            text="File Explorer",
            width=100,
            height=5,
            fg="blue"
        )

        self.button_explore = Button(self.window, 
            text = "Browse Files",
            command = FileExplorer.browseFiles
            ) 

        self.button_exit = Button(self.window, 
            text = "Exit",
            command = exit) 

        self.label_file_explorer.grid(column = 1, row = 1)

        self.button_explore.grid(column = 1, row = 2)

        self.button_exit.grid(column = 1,row = 3)



    def click(self):
        self.FileExplorer()


    def run(self):
        self.window.mainloop()