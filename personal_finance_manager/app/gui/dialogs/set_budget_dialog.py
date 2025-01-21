# app/gui/dialogs/set_budget_dialog.py

from PyQt5 import QtWidgets

class SetBudgetDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Budget")
        self.setGeometry(150, 150, 400, 150)

        layout = QtWidgets.QVBoxLayout()

        # Category and Amount
        self.category_input = QtWidgets.QComboBox()
        self.category_input.addItems(["Food", "Transportation", "Utilities", "Entertainment", "Other"])
        layout.addWidget(QtWidgets.QLabel("Category:"))
        layout.addWidget(self.category_input)

        self.amount_input = QtWidgets.QLineEdit()
        layout.addWidget(QtWidgets.QLabel("Amount:"))
        layout.addWidget(self.amount_input)

        # Buttons
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_data(self):
        category = self.category_input.currentText()
        amount = float(self.amount_input.text())
        return category, amount