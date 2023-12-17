import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
)


class MainForm(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        self.form1 = Form1(self)
        self.form2 = Form2(self)

        self.stacked_widget.addWidget(self.form1)
        self.stacked_widget.addWidget(self.form2)

        self.init_ui()

    def init_ui(self):
        # Create layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Set the layout for the main widget
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Form Switching Example")
        self.setGeometry(100, 100, 300, 150)

        # Connect signals
        self.form1.switch_form_signal.connect(self.switch_to_form2)
        self.form2.switch_form_signal.connect(self.switch_to_form1)

    def switch_to_form1(self):
        self.stacked_widget.setCurrentIndex(0)

    def switch_to_form2(self):
        self.stacked_widget.setCurrentIndex(1)


class Form1(QWidget):
    switch_form_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Create widgets for Form 1
        label_name = QLabel("Name (Form 1):")
        line_edit_name = QLineEdit()
        button_next = QPushButton("Next")

        # Connect button signal to slot
        button_next.clicked.connect(self.switch_to_form2)

        # Create layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(label_name)
        layout.addWidget(line_edit_name)
        layout.addWidget(button_next)

        # Set the layout for the form
        self.setLayout(layout)

    def switch_to_form2(self):
        self.switch_form_signal.emit()


class Form2(QWidget):
    switch_form_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Create widgets for Form 2
        label_info = QLabel("Additional Information (Form 2):")
        button_back = QPushButton("Back")

        # Connect button signal to slot
        button_back.clicked.connect(self.switch_to_form1)

        # Create layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(label_info)
        layout.addWidget(button_back)

        # Set the layout for the form
        self.setLayout(layout)

    def switch_to_form1(self):
        self.switch_form_signal.emit()


def main():
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
