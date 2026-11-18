"""Account summaries and signed category totals for BudgetBuddy."""

from decimal import Decimal


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    """Return signed totals by category, rounded to cents after summing."""
    report = {}
    for transaction in data["transactions"]:
        category = transaction["category"]
        report[category] = report.get(category, Decimal("0")) + Decimal(str(transaction["amount"]))
    return {category: float(round(total, 2)) for category, total in report.items()}
