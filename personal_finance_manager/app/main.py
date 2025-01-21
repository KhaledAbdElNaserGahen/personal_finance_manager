# app/main.py

import sys
from PyQt5 import QtWidgets
from .gui.main_window import MainWindow
from .models.database import init_db

def main():
    # Initialize the database
    init_db()

    # Initialize the application
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # You can choose other styles like 'Windows', 'Macintosh', etc.

    # Set up the main window
    window = MainWindow()
    window.show()

    # Start the application
    sys.exit(app.exec_())