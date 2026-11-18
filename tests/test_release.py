"""Regression coverage for the release's reports and interactive input."""

import copy
import io
import unittest
from unittest.mock import patch

import main
from features import core, reports


class TestCategoryReport(unittest.TestCase):
    def test_signed_totals_and_every_transaction_counted_once(self):
        data = {"transactions": [
            {"category": "food", "amount": -6.75},
            {"category": "income", "amount": 20},
            {"category": "food", "amount": -3.25},
            {"category": "food", "amount": 2},
            {"category": "fun", "amount": 0},
        ]}
        original = copy.deepcopy(data)
        self.assertEqual(reports.category_report(data), {"food": -8, "income": 20, "fun": 0})
        self.assertEqual(data, original)

    def test_empty_account(self):
        self.assertEqual(reports.category_report({"transactions": []}), {})

    def test_rounds_after_adding_all_amounts(self):
        data = {"transactions": [{"category": "food", "amount": -0.005}] * 3}
        self.assertEqual(reports.category_report(data), {"food": -0.02})


class TestTransactionValidation(unittest.TestCase):
    def test_empty_description_leaves_data_unchanged(self):
        data = {"transactions": []}
        with self.assertRaises(ValueError):
            core.add_transaction(data, "  ", -5)
        self.assertEqual(data["transactions"], [])

    def test_non_finite_amounts_leave_data_unchanged(self):
        for amount in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(amount=amount):
                data = {"transactions": []}
                with self.assertRaises(ValueError):
                    core.add_transaction(data, "Lunch", amount)
                self.assertEqual(data["transactions"], [])

    def test_category_and_description_are_trimmed(self):
        data = {"transactions": []}
        tx = core.add_transaction(data, " Lunch ", -5, " food ")
        self.assertEqual(tx, {"id": 1, "description": "Lunch", "amount": -5, "category": "food"})
        self.assertEqual(core.add_transaction(data, "Bus", -2, " ")["category"], "general")

    def test_empty_latest_transaction(self):
        self.assertIsNone(core.last_transaction([]))

    def test_latest_transaction_uses_last_entry(self):
        transactions = [{"description": "First"}, {"description": "Last"}]
        self.assertEqual(core.last_transaction(transactions), transactions[-1])


class TestCLI(unittest.TestCase):
    def run_menu(self, inputs, transactions=None):
        data = {"account_name": "Test", "starting_balance": 50,
                "transactions": [] if transactions is None else transactions}
        with patch("main.storage.load_data", return_value=data), \
                patch("main.storage.save_data") as save, \
                patch("builtins.input", side_effect=inputs), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            main.main()
        return data, save, output.getvalue()

    def test_invalid_amount_returns_to_menu_without_saving(self):
        data, save, output = self.run_menu(["3", "Lunch", "oops", "1", "0"])
        save.assert_not_called()
        self.assertEqual(data["transactions"], [])
        self.assertIn("Transaction not added", output)
        self.assertIn("Balance: $50", output)

    def test_non_finite_amount_does_not_save(self):
        for amount in ("nan", "inf", "-inf"):
            with self.subTest(amount=amount):
                data, save, output = self.run_menu(["3", "Lunch", amount, "food", "0"])
                save.assert_not_called()
                self.assertEqual(data["transactions"], [])
                self.assertIn("finite number", output)

    def test_adding_an_expense_saves_and_updates_the_balance_and_report(self):
        data, save, output = self.run_menu(["3", "Lunch", "-5.25", "food", "1", "6", "0"])
        save.assert_called_once_with(data)
        self.assertIn("Balance: $44.75", output)
        self.assertIn("food: $-5.25", output)

    def test_empty_latest_and_report_are_safe(self):
        _, save, output = self.run_menu(["5", "6", "0"])
        save.assert_not_called()
        self.assertEqual(output.count("No transactions yet."), 2)

    def test_end_of_input_cancels_without_saving(self):
        for inputs in ([EOFError()], ["3", EOFError()],
                       ["3", "Lunch", EOFError()],
                       ["3", "Lunch", "-5", EOFError()], ["4", EOFError()]):
            with self.subTest(inputs=inputs):
                data, save, _ = self.run_menu(inputs)
                save.assert_not_called()
                self.assertEqual(data["transactions"], [])

    def test_missing_category_shows_empty_message(self):
        _, _, output = self.run_menu(["4", "missing", "0"])
        self.assertIn("No transactions in this category.", output)


if __name__ == "__main__":
    unittest.main()
