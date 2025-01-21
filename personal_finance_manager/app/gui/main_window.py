# app/gui/main_window.py

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from .dialogs.add_transaction_dialog import AddTransactionDialog
from .dialogs.set_budget_dialog import SetBudgetDialog
from .dialogs.set_goal_dialog import SetGoalDialog
from .components.transaction_table import TransactionTable
from .components.budget_chart import BudgetChart
from .components.goal_progress_bar import GoalProgressBar
from ..services.notification_service import NotificationService

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal Finance Manager")
        self.setGeometry(100, 100, 1000, 800)

        # Initialize components
        self.transaction_table = TransactionTable(self)
        self.budget_chart = BudgetChart(self)
        self.goal_progress_bar = GoalProgressBar(self)
        self.notification_service = NotificationService()

        # Set up the central widget
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Tabs for different views
        tabs = QtWidgets.QTabWidget()
        tabs.addTab(self.transaction_table, "Transactions")
        tabs.addTab(self.budget_chart, "Budgets")
        tabs.addTab(self.goal_progress_bar, "Goals")

        layout.addWidget(tabs)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set up the menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        add_transaction_action = QtWidgets.QAction("Add Transaction", self)
        add_transaction_action.triggered.connect(self.open_add_transaction_dialog)
        file_menu.addAction(add_transaction_action)

        budget_menu = menubar.addMenu("&Budget")
        set_budget_action = QtWidgets.QAction("Set Budget", self)
        set_budget_action.triggered.connect(self.open_set_budget_dialog)
        budget_menu.addAction(set_budget_action)

        goal_menu = menubar.addMenu("&Goals")
        set_goal_action = QtWidgets.QAction("Set Goal", self)
        set_goal_action.triggered.connect(self.open_set_goal_dialog)
        goal_menu.addAction(set_goal_action)

        # Check budgets and send notifications
        self.notification_service.check_budgets()

    def open_add_transaction_dialog(self):
        dialog = AddTransactionDialog(self)
        dialog.exec_()

    def open_set_budget_dialog(self):
        dialog = SetBudgetDialog(self)
        dialog.exec_()

    def open_set_goal_dialog(self):
        dialog = SetGoalDialog(self)
        dialog.exec_()