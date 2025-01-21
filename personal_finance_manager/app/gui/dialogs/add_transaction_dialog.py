# app/gui/dialogs/add_transaction_dialog.py

from PyQt5 import QtWidgets, QtCore
from ..components.transaction_table import TransactionTable

class AddTransactionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Transaction")
        self.setGeometry(150, 150, 400, 200)

        layout = QtWidgets.QVBoxLayout()

        # Amount
        self.amount_input = QtWidgets.QLineEdit()
        layout.addWidget(QtWidgets.QLabel("Amount:"))
        layout.addWidget(self.amount_input)

        # Category
        self.category_input = QtWidgets.QComboBox()
        self.category_input.addItems(["Food", "Transportation", "Utilities", "Entertainment", "Other"])
        layout.addWidget(QtWidgets.QLabel("Category:"))
        layout.addWidget(self.category_input)

        # Description
        self.description_input = QtWidgets.QLineEdit()
        layout.addWidget(QtWidgets.QLabel("Description:"))
        layout.addWidget(self.description_input)

        # Date
        self.date_input = QtWidgets.QDateEdit(QtCore.QDate.currentDate())
        layout.addWidget(QtWidgets.QLabel("Date:"))
        layout.addWidget(self.date_input)

        # Buttons
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_data(self):
        amount = float(self.amount_input.text())
        category = self.category_input.currentText()
        description = self.description_input.text()
        date = self.date_input.date().toString("yyyy-MM-dd")
        return amount, category, description, date