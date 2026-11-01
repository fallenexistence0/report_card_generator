
from style import ReportCardGUI
from explorer import FileExplorer
from report_generator import generate_reports

from threading import Thread




def main():
    gui = ReportCardGUI()
    script = generate_reports()

    """     worker = Thread(
        target=generate_reports,
        daemon=True
    )
    
    gui.window.after(100, worker.start) """

    gui.run()




if __name__ == "__main__":
    main()