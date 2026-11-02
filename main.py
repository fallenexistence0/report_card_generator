
from style import ReportCardGUI
from explorer import FileExplorer
from report_generator import generate_reports

from threading import Thread




def main():
    gui = ReportCardGUI()

    gui.run()




if __name__ == "__main__":
    main()