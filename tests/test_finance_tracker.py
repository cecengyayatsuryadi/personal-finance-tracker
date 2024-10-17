import unittest
from src.finance_tracker import FinanceTracker

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FinanceTracker()

    def test_add_transaction(self):
        self.tracker.add_transaction('2023-10-01', 50, 'Food', 'Groceries')
        self.assertEqual(len(self.tracker.transactions), 1)

    def test_delete_transaction(self):
        self.tracker.add_transaction('2023-10-01', 50, 'Food', 'Groceries')
        self.tracker.delete_transaction(1)
        self.assertEqual(len(self.tracker.transactions), 0)

    def test_edit_transaction(self):
        self.tracker.add_transaction('2023-10-01', 50, 'Food', 'Groceries')
        self.tracker.edit_transaction(1, amount=100)
        self.assertEqual(self.tracker.transactions[0]['amount'], 100)

if __name__ == '__main__':
    unittest.main()