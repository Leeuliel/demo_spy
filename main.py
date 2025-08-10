"""
Main entry point for the PyQt5 application.
"""

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class SectionWidget(QWidget):
    """
    A reusable section widget with a label, a collapse/uncollapse button, and a read-only text area.
    """
    def __init__(self, label_text: str, text_placeholder: str):
        super().__init__()
        self.collapsed = False

        # Layouts
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(8)

        # Collapse/uncollapse button
        self.toggle_btn = QPushButton("−")
        self.toggle_btn.setFixedWidth(28)
        self.toggle_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.toggle_btn.setStyleSheet("background: #e0e0e0; border-radius: 6px;")
        self.toggle_btn.clicked.connect(self.toggle_collapse)

        # Label
        self.label = QLabel(label_text)
        self.label.setFont(QFont("Segoe UI", 14, QFont.Bold))

        header_layout.addWidget(self.toggle_btn)
        header_layout.addWidget(self.label)
        header_layout.addStretch()

        # Read-only text area
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Segoe UI", 12))
        self.text_area.setPlaceholderText(text_placeholder)
        self.text_area.setStyleSheet("background: #f5f5f5; border-radius: 8px;")

        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.text_area)
        self.setLayout(main_layout)

    def toggle_collapse(self):
        self.collapsed = not self.collapsed
        self.text_area.setVisible(not self.collapsed)
        self.toggle_btn.setText("+" if self.collapsed else "−")

class MainWindow(QMainWindow):
    """
    Main application window for DemoSpy.

    Displays two vertically stacked sections, each with a label and a read-only text area.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DemoSpy - Modern PyQt5 App")
        self.resize(600, 400)

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(24)
        layout.setContentsMargins(32, 32, 32, 32)

        # Section 1 (collapsible)
        section1 = SectionWidget("Section 1", "Read-only display area 1\nThis area can be collapsed.\nYou can add more text here to see how it behaves.\nYou can also add more text to see how it behaves when the text area is expanded.")
        layout.addWidget(section1)

        # Section 2 (collapsible)
        section2 = SectionWidget("Section 2", "Read-only display area 2")
        layout.addWidget(section2)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
