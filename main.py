import pandas as pd
from playwright.sync_api import sync_playwright
import pathlib
import os

from datetime import date



# gets current date, which is used in the name of the PDF that is outputed.
current_time = date.today()

print("Starting process")
current_directory = os.path.dirname(os.path.abspath(__file__))
print("current directory set")
print(current_directory)
csv_file_path = os.path.join(current_directory, 'data.csv')
print("file path sucess")
print("CSV file path:", csv_file_path)

all_reports_html = ""
def html_to_pdf(html_content, pdf_filename):
    HTML(string=html_content).write_pdf(pdf_filename)

df = pd.read_csv(csv_file_path)
# Read HTML template outside the loop
with open('./index.html', 'r') as html_file:
    html_template = html_file.read()

for i, row in df.iterrows():
    # Extract values from the current row
    student_name = row['student_name']
    current_class = row['current_class']
    class_teacher = row['class_teacher']
    school_year = row['school_year']
    class_quizzes = row['class_quizzes']
    speaking = row['speaking']
    final_exam = row['final_exam']
    overall_grade = row['overall_grade'] if 'overall_grade' in row else ''

    print(f"Processing report for {student_name}")

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
    print("Modified HTML content:")
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
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(all_reports_html)
    page.emulate_media(media="screen")
    page.pdf(path=f"./report_card_for_{current_time}.pdf", format="A4",
            landscape=True, margin={"top": "2cm"})
    browser.close()

print("PDF conversion complete.")
