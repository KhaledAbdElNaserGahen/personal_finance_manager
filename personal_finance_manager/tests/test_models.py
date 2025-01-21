# tests/test_models.py

import unittest
from ..app.models.database import init_db, add_transaction, set_budget, set_goal, get_transactions, get_budgets, get_goals

class TestModels(unittest.TestCase):
    def setUp(self):
        init_db()
        add_transaction(100, "Food", "Lunch", "2025-01-21")
        set_budget("Food", 500)
        set_goal("Save Money", 1000, "2025-12-31")

    def test_get_transactions(self):
        transactions = get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][1], "Food")

    def test_set_budget(self):
        budgets = get_budgets()
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0][1], 500)

    def test_set_goal(self):
        goals = get_goals()
        self.assertEqual(len(goals), 1)
        self.assertEqual(goals[0][1], "Save Money")
        self.assertEqual(goals[0][2], 1000)