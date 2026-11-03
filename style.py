from tkinter import *
import tkinter as tk

from report_generator import generate_reports

from tkinter import filedialog
from explorer import FileExplorer

from PIL import Image, ImageTk

class ReportCardGUI:


    def select_file(self):
        csv_file_path = FileExplorer.browseFiles()

        if not csv_file_path:
            return
            
        generate_reports(csv_file_path)

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
            column=0,
        )

        self.image = Image.open("assets/logos/jefferson_academy_logo_1.png")

        self.image_resized = self.image.resize((200, 150))

        self.photo = ImageTk.PhotoImage(self.image_resized)

        self.image_label = Label(self.window, image = self.photo)
        self.image_label.image = self.photo
        self.image_label.grid(
            row=0,
            column=0,
            sticky=NW   
        )
        self.window.title(
            "Jefferson Academy -Report Card Generator"
            )

        self.icon = tk.PhotoImage(
            file="assets/logos/jefferson_academy_logo_2.png"
            )

        self.window.iconphoto(True, self.icon)


        self.instructions = Label(
            self.button_frame,
            font=("Arial", 14, "bold"),
            text="Choose a valid csv file to generate a pdf of the reports:",
            fg="black",
            bg="#f7f7ff"
            )



        self.instructions.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        self.browse_files_button = tk.Button(
            self.button_frame, 
            text='Browse files',
            command=self.select_file,
            font=('Arial', 11, "bold"),
            bg='#2b3187',
            fg='#f7f7ff',
            width=20,
            height=2
            )


        self.browse_files_button.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        self.button_exit = Button(
            self.button_frame,
            font=('Arial', 11, "bold"),
            width=20,
            height=2,
            bg="#2b3187", 
            fg="#f7f7ff",
            text = "Exit",
            command = exit
            ) 

        self.button_exit.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )



    def click(self):
        self.FileExplorer()


    def run(self):
        self.window.mainloop()