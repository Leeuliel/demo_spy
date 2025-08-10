"""
Main entry point for the PyQt5 application.
"""

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout,QScrollArea
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


# Individual collapsible section
class CollapseSection(QWidget):
    def __init__(self, label_text: str, content_widget: QWidget):
        super().__init__()
        self.collapsed = False

        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(8)

        self.toggle_btn = QPushButton("−")
        self.toggle_btn.setFixedWidth(28)
        self.toggle_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.toggle_btn.setStyleSheet("background: #e0e0e0; border-radius: 6px;")
        self.toggle_btn.clicked.connect(self.toggle_collapse)

        self.label = QLabel(label_text)
        self.label.setFont(QFont("Segoe UI", 14, QFont.Bold))

        header_layout.addWidget(self.toggle_btn)
        header_layout.addWidget(self.label)
        header_layout.addStretch()

        self.content_widget = content_widget
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.content_widget)
        self.setLayout(main_layout)

    def toggle_collapse(self):
        self.collapsed = not self.collapsed
        self.content_widget.setVisible(not self.collapsed)
        self.toggle_btn.setText("+" if self.collapsed else "−")

# Manager for all sections and the collapse/expand all button
class CollapseAllSections(QWidget):
    def __init__(self, sections):
        super().__init__()
        self.sections = sections
        layout = QVBoxLayout()
        layout.setSpacing(24)
        layout.setContentsMargins(32, 32, 32, 32)

        button_layout = QHBoxLayout()
        self.collapse_all_btn = QPushButton("Collapse All")
        self.collapse_all_btn.setFixedWidth(120)
        self.collapse_all_btn.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.collapse_all_btn.setStyleSheet("background: #e0e0e0; border-radius: 6px;")
        self.collapse_all_btn.clicked.connect(self.toggle_all_sections)
        button_layout.addWidget(self.collapse_all_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        for section in self.sections:
            layout.addWidget(section)

        self.setLayout(layout)

    def toggle_all_sections(self):
        any_expanded = any(not s.collapsed for s in self.sections)
        for s in self.sections:
            s.collapsed = any_expanded
            s.text_area.setVisible(not s.collapsed)
            s.toggle_btn.setText("+" if s.collapsed else "−")
        self.collapse_all_btn.setText("Expand All" if any_expanded else "Collapse All")

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
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Initialize sections in MainWindow
        self.sections = []
        for i in range(1, 11):
            # Example: use QTextEdit as content, but you can pass any QWidget (e.g., PvTraceViewer)
            text_widget = QTextEdit()
            text_widget.setReadOnly(True)
            text_widget.setFont(QFont("Segoe UI", 12))
            text_widget.setText(f"Section {i} text area\nLine 1 for section {i}\nLine 2 for section {i}\nLine 3 for section {i}\nLine 4 for section {i}\nLine 5 for section {i}\nLine 6 for section {i}\nLine 7 for section {i}\nLine 8 for section {i}\nLine 9 for section {i}\nLine 10 for section {i}")
            text_widget.setStyleSheet("background: #f5f5f5; border-radius: 8px;")
            text_widget.setLineWrapMode(QTextEdit.NoWrap)
            section = CollapseSection(f"Section {i}", text_widget)
            self.sections.append(section)

        self.collapse_all_widget = CollapseAllSections(self.sections)
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.collapse_all_widget)
        central_widget.setLayout(central_layout)
        scroll_area.setWidget(central_widget)
        self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
