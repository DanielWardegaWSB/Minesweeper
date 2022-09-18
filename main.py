import sys

from PyQt6.QtWidgets import QApplication

from gui import MainWidget

# Starting the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    w.setWindowTitle("Minesweeper")
    w.show()
    sys.exit(app.exec())
