"""
Basic test for the DemoSpy PyQt5 main window.
"""
import pytest
from PyQt5.QtWidgets import QApplication
from main import MainWindow
import sys

@pytest.fixture(scope="module")
def app():
    app = QApplication(sys.argv)
    yield app
    app.quit()

def test_main_window_components(app):
    window = MainWindow()
    window.show()
    # Check window title
    assert window.windowTitle() == "DemoSpy - Modern PyQt5 App"
    # Check central widget and layout
    central = window.centralWidget()
    layout = central.layout()
    assert layout.count() == 4  # 2 labels + 2 text areas
    # Check labels and text areas
    assert central.layout().itemAt(0).widget().text() == "Section 1"
    assert central.layout().itemAt(2).widget().text() == "Section 2"
    assert central.layout().itemAt(1).widget().isReadOnly()
    assert central.layout().itemAt(3).widget().isReadOnly()
