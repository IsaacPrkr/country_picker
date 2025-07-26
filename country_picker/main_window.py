# country_picker/main_window.py

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel
)

class MainWindow(QMainWindow):
    def __init__(self, preselect_country=None):
        super().__init__()

        self.setWindowTitle("Country Picker")

        # Create UI elements
        self.combo_box = QComboBox()
        self.label = QLabel("")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect signals
        self.combo_box.currentTextChanged.connect(self.update_label)

        # Store preselect value for future use
        self.preselect_country = preselect_country

    def update_label(self, text: str):
        self.label.setText(f"Selected: {text}")

def start_app(preselect_country=None):
    app = QApplication(sys.argv)
    window = MainWindow(preselect_country)
    window.show()
    sys.exit(app.exec())
