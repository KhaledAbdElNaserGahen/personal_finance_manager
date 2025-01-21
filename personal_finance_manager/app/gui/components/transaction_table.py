# app/gui/components/transaction_table.py

from PyQt5 import QtWidgets, QtCore
import pandas as pd

class TransactionTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Amount", "Category", "Description", "Date"])
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.load_data()

    def load_data(self):
        from ..models.database import get_transactions
        transactions = get_transactions()
        self.setRowCount(len(transactions))
        for i, transaction in enumerate(transactions):
            amount, category, description, date = transaction
            self.setItem(i, 0, QtWidgets.QTableWidgetItem(str(amount)))
            self.setItem(i, 1, QtWidgets.QTableWidgetItem(category))
            self.setItem(i, 2, QtWidgets.QTableWidgetItem(description))
            self.setItem(i, 3, QtWidgets.QTableWidgetItem(date))
        self.resizeColumnsToContents()