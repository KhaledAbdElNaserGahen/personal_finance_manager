# app/gui/dialogs/set_goal_dialog.py

from PyQt5 import QtWidgets, QtCore

class SetGoalDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Goal")
        self.setGeometry(150, 150, 400, 200)

        layout = QtWidgets.QVBoxLayout()

        # Goal Name
        self.goal_name_input = QtWidgets.QLineEdit()
        layout.addWidget(QtWidgets.QLabel("Goal Name:"))
        layout.addWidget(self.goal_name_input)

        # Target Amount
        self.target_amount_input = QtWidgets.QLineEdit()
        layout.addWidget(QtWidgets.QLabel("Target Amount:"))
        layout.addWidget(self.target_amount_input)

        # Target Date
        self.target_date_input = QtWidgets.QDateEdit(QtCore.QDate.currentDate())
        layout.addWidget(QtWidgets.QLabel("Target Date:"))
        layout.addWidget(self.target_date_input)

        # Buttons
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_data(self):
        goal_name = self.goal_name_input.text()
        target_amount = float(self.target_amount_input.text())
        target_date = self.target_date_input.date().toString("yyyy-MM-dd")
        return goal_name, target_amount, target_date