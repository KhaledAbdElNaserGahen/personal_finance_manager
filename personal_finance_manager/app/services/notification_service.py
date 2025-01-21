# app/services/notification_service.py

from ..models.database import get_budgets, get_total_spent

class NotificationService:
    def check_budgets(self):
        budgets = get_budgets()
        spent = get_total_spent()
        alerts = []
        for budget in budgets:
            category, budget_amount = budget
            total_spent = spent.get(category, 0)
            if total_spent > budget_amount:
                alerts.append(f"Exceeded budget for {category}: Spent {total_spent}, Budget {budget_amount}")
        if alerts:
            self.show_alert(alerts)

    def show_alert(self, alerts):
        from PyQt5.QtWidgets import QMessageBox
        alert_message = "\n".join(alerts)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Budget Alert")
        msg_box.setText(alert_message)
        msg_box.exec_()