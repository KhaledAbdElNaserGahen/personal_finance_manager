# tests/test_services.py

import unittest
from ..app.services.api_integration import fetch_transactions

class TestServices(unittest.TestCase):
    def test_fetch_transactions(self):
        transactions = fetch_transactions("api_key", "account_id")
        self.assertIsNotNone(transactions)