"""BudgetBuddy - a small spending/allowance tracker.

Run it with:  python main.py
"""

import storage
from features import core, reports


def show_menu():
    print()
    print("=== BudgetBuddy ===")
    print("1) Show balance")
    print("2) List transactions")
    print("3) Add a transaction")
    print("4) Filter by category")
    print("5) Show the last transaction")
    print("6) Category breakdown")
    print("7) Spending summary")
    print("8) Account summary")
    print("0) Quit")


def main():
    data = storage.load_data()
    while True:
        show_menu()
        try:
            choice = input("Pick an option: ").strip()
        except EOFError:
            print()
            break
        if choice == "0":
            print("See you next session!")
            break
        elif choice == "1":
            print("Balance: $" + str(core.balance(data)))
        elif choice == "2":
            core.list_transactions(core.get_transactions(data))
        elif choice == "3":
            try:
                description = input("Description: ")
                amount = float(input("Amount (negative for an expense): "))
                category = input("Category [general]: ")
                core.add_transaction(data, description, amount, category)
            except ValueError as error:
                print("Transaction not added: " + str(error))
                continue
            except EOFError:
                print("\nTransaction cancelled.")
                break
            storage.save_data(data)
            print("Transaction added.")
        elif choice == "4":
            try:
                category = input("Category: ").strip()
            except EOFError:
                print()
                break
            matches = core.transactions_by_category(core.get_transactions(data), category)
            if not matches:
                print("No transactions in this category.")
            for t in matches:
                print("- " + t["description"])
        elif choice == "5":
            transaction = core.last_transaction(core.get_transactions(data))
            print(transaction["description"] if transaction else "No transactions yet.")
        elif choice == "6":
            totals = reports.category_report(data)
            if not totals:
                print("No transactions yet.")
            for category, amount in sorted(totals.items()):
                print(category + ": $" + format(amount, ".2f"))
        elif choice == "7":
            txns = core.get_transactions(data)
            print("Spent $" + str(core.total_spent(txns)) + " over " + str(len(txns)) +
                  " transactions (avg $" + str(core.average_transaction(txns)) + ").")
        elif choice == "8":
            print(reports.account_summary(data))
        else:
            print("Please pick a number from the menu.")


if __name__ == "__main__":
    main()
