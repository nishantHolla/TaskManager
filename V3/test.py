from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QCheckBox, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QListWidget
        self.list_widget = QListWidget(self)

        # Create items with checkboxes
        for i in range(1, 6):
            item_text = 'Item {}'.format(i)
            item = QListWidgetItem(item_text)

            # Create a checkbox
            checkbox = QCheckBox()
            checkbox.setChecked(True)  # Set the initial state if needed

            # Set the checkbox as the item widget
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, checkbox)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

        # Connect a slot to handle checkbox state changes
        self.list_widget.itemChanged.connect(self.handle_checkbox_change)

    def handle_checkbox_change(self, item):
        # Handle checkbox state changes here
        if item.checkState() == 2:  # 2 corresponds to checked state
            print("Checkbox Checked for:", item.text())
        else:
            print("Checkbox Unchecked for:", item.text())

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
