"""Regression tests for the four Lesson 13 Bug Bash issues."""

import json
import unittest
from unittest.mock import mock_open, patch

import main
import storage
from features import core, reports


class TestBugBash(unittest.TestCase):
    def test_balance_includes_starting_balance(self):
        data = {"starting_balance": 50.0, "transactions": [
            {"amount": -2.5}, {"amount": 20.0}, {"amount": -6.75},
            {"amount": -12.0}, {"amount": -3.25}, {"amount": 15.0},
        ]}
        self.assertEqual(core.balance(data), 60.5)

    def test_account_summary_uses_account_name(self):
        data = {"account_name": "My Allowance", "transactions": [{}, {}]}
        self.assertEqual(reports.account_summary(data), "My Allowance: 2 transactions")

    def test_save_data_opens_file_for_writing(self):
        data = {"account_name": "Test", "transactions": []}
        file_mock = mock_open()
        with patch("builtins.open", file_mock):
            storage.save_data(data, path="test-budgetbuddy.json")
        file_mock.assert_called_once_with("test-budgetbuddy.json", "w", encoding="utf-8")
        chunks = [call.args[0] for call in file_mock().write.call_args_list]
        self.assertEqual(json.loads("".join(chunks)), data)

    def test_spending_summary_uses_correct_amount_and_count(self):
        data = {"starting_balance": 50.0, "transactions": [
            {"amount": -2.5}, {"amount": 20.0}, {"amount": -6.75},
            {"amount": -12.0}, {"amount": -3.25}, {"amount": 15.0},
        ]}
        with patch.object(storage, "load_data", return_value=data), \
             patch("builtins.input", side_effect=["7", "0"]), \
             patch("builtins.print") as output:
            main.main()
        lines = [str(call.args[0]) for call in output.call_args_list if call.args]
        self.assertTrue(any("Spent $24.5 over 6 transactions" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
