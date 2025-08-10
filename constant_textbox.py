from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtGui import QFont
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Constant Size Text Box Example")
        self.setFixedSize(400, 200)

        text_box = QTextEdit()
        text_box.setReadOnly(True)
        text_box.setFont(QFont("Segoe UI", 12))
        text_box.setFixedHeight(100)
        text_box.setFixedWidth(380)

        # Fill with 10 lines
        lines = [f"Line {i+1}" for i in range(10)]
        text_box.setText("\n".join(lines))

        self.setCentralWidget(text_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
