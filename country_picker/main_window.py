# country_picker/main_window.py

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel
)

from .data_fetcher import fetch_country_data

class MainWindow(QMainWindow):
    def __init__(self, preselect_country=None):
        super().__init__()

        self.setWindowTitle("Country Picker")

        # UI setup
        self.combo_box = QComboBox()
        self.label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect signal
        self.combo_box.currentTextChanged.connect(self.update_label)

        # Preselect setup
        self.preselect_country = preselect_country

        # Load data
        self.load_countries()

    def load_countries(self):
        countries = fetch_country_data()
        countries.sort()
        self.combo_box.addItems(countries)

        # Apply pre-selection if needed
        if self.preselect_country and self.preselect_country in countries:
            index = self.combo_box.findText(self.preselect_country)
            if index != -1:
                self.combo_box.setCurrentIndex(index)

    def update_label(self, text: str):
        self.label.setText(f"Selected: {text}")

def start_app(preselect_country=None):
    app = QApplication(sys.argv)
    window = MainWindow(preselect_country)
    window.show()
    sys.exit(app.exec())
