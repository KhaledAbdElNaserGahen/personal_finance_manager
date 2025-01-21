# app/gui/components/goal_progress_bar.py

from PyQt5 import QtWidgets, QtCore

class GoalProgressBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        self.progress_bars = []

        self.load_data()

        self.setLayout(layout)

    def load_data(self):
        from ..models.database import get_goals
        goals = get_goals()
        for goal in self.progress_bars:
            self.layout().removeWidget(goal)
            goal.deleteLater()
        self.progress_bars = []
        for goal in goals:
            name, target, date, progress = goal
            progress_bar = QtWidgets.QProgressBar()
            progress_bar.setValue(int(progress / target * 100))
            progress_bar.setOrientation(QtCore.Qt.Horizontal)
            progress_bar.setMaximum(100)
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(QtWidgets.QLabel(name))
            layout.addWidget(progress_bar)
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)
            self.layout().addWidget(widget)
            self.progress_bars.append(progress_bar)