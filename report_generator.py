import pandas as pd
from playwright.sync_api import sync_playwright
import pathlib
import os

from datetime import date

from tkinter import *

from threading import Thread

import uuid


from pathlib import Path

output_directory = Path.home() / "Documents" / "Jefferson Academy Reports"

output_directory.mkdir(
    parents=True,
    exist_ok=True
)



def display_message(message):
    print(f"status: {message}")

def generate_reports(csv_file, progress_callback=print):

    unique_ID = uuid.uuid4()

    # gets current date, which is used in the name of the PDF that is outputed.
    current_time = date.today()

    progress_callback(f"Starting process")


    current_directory = os.path.dirname(os.path.abspath(__file__))
    progress_callback(f"current directory set")
    print(current_directory)

    #csv_file_path = os.path.join(current_directory, 'data.csv')
    #print("file path sucess")
    
    
    progress_callback(f"CSV file path: {csv_file}")

    progress_callback(f"Checking for index.html")
    html_path = os.path.join(current_directory, 'index.html')
    progress_callback(f"index.html path: {html_path}")


    all_reports_html = ""
    def html_to_pdf(html_content, pdf_filename):
        HTML(string=html_content).write_pdf(pdf_filename)

    df = pd.read_csv(csv_file)

    # Read HTML template outside the loop
    with open(html_path, 'r', encoding="UTF-8") as html_file:
        html_template = html_file.read()


    required_columns = {
        'student_name', 
        'current_class', 
        'class_teacher', 
        'school_year', 
        'class_quizzes', 
        'speaking', 
        'final_exam', 
        'overall_grade'
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        progress_callback(f"Invalid csv file structure. Missing necessary columns: {missing_columns}")
        return

    for i, row in df.iterrows():
        try:
        # Extract values from the current row
            student_name = row['student_name']
            current_class = row['current_class']
            class_teacher = row['class_teacher']
            school_year = row['school_year']
            class_quizzes = row['class_quizzes']
            speaking = row['speaking']
            final_exam = row['final_exam']
            overall_grade = row['overall_grade'] if 'overall_grade' in row else ''

        except KeyError as error:
            print(f"Missing column: {error}")
            return

        progress_callback(f"Processing report for {student_name}")

        progress_callback(f"Processing reports...")

        modified_html = html_template

        modified_html = modified_html.replace('{student_name}', str(student_name))
        modified_html = modified_html.replace('{class_teacher}', str(class_teacher))
        modified_html = modified_html.replace('{current_class}', str(current_class))
        modified_html = modified_html.replace('{school_year}', str(school_year))
        modified_html = modified_html.replace('{class_quizzes}', str(class_quizzes))
        modified_html = modified_html.replace('{speaking}', str(speaking))
        modified_html = modified_html.replace('{final_exam}', str(final_exam))
        modified_html = modified_html.replace('{overall_grade}', str(overall_grade))

        # Print the modified HTML content (for debugging purposes)
        progress_callback(f"Modified HTML content:")
        #print(modified_html)

        filePath = os.path.abspath("./report_card_automation")
        fileUrl = pathlib.Path(filePath).as_uri()


        # <----- Uncomment this section if you want each page to be generated seperatly in a pdf. ----->
        # with sync_playwright() as p:
        #     browser = p.chromium.launch()
        #     page = browser.new_page()
        #     page.set_content(modified_html)
        #     page.emulate_media(media="screen")
        #     page.pdf(path=f"./report_{student_name}.pdf", format="A4",
        #              landscape=True, margin={"top": "2cm"})
        #     browser.close()

        all_reports_html += modified_html

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chromium", headless=True)

        progress_callback("Browser launched successfully")
        page = browser.new_page()
        progress_callback("Page created successfully")

        page.set_content(all_reports_html)

        progress_callback("HTML content set")
        page.emulate_media(media="screen")

        progress_callback("Generating PDF...")
        page.pdf(path=f"{output_directory}/report_card_for_{unique_ID}_{current_time}.pdf", format="A4",
                landscape=True, margin={"top": "2cm"})
        browser.close()

    progress_callback(f"PDF conversion complete.")