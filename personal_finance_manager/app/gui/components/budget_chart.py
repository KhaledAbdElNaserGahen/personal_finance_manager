# app/gui/components/budget_chart.py

from PyQt5 import QtWidgets, QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class BudgetChart(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.load_data()

    def load_data(self):
        from ..models.database import get_budgets, get_total_spent
        budgets = get_budgets()
        spent = get_total_spent()

        categories = [budget[0] for budget in budgets]
        budget_amounts = [budget[1] for budget in budgets]
        spent_amounts = [spent.get(category, 0) for category in categories]

        self.ax.clear()
        self.ax.bar(categories, budget_amounts, label='Budget', color='skyblue')
        self.ax.bar(categories, spent_amounts, label='Spent', color='orange')
        self.ax.set_ylabel('Amount')
        self.ax.set_title('Budget vs Spent')
        self.ax.legend()
        self.draw()