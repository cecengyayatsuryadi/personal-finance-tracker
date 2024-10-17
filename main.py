import logging
from src.finance_tracker import FinanceTracker
from src.report_generator import ReportGenerator
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATA_FILE_PATH = 'data/transactions.csv'

def load_data(tracker):
    try:
        tracker.load_data(DATA_FILE_PATH)
        logging.info("Data loaded successfully.")
        return True
    except FileNotFoundError:
        logging.warning("Data file not found. Starting with an empty dataset.")
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")
    return False

def save_data(tracker):
    try:
        tracker.save_data(DATA_FILE_PATH)
        logging.info("Data saved successfully.")
    except Exception as e:
        logging.error(f"An error occurred while saving data: {e}")

def get_user_input():
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        pd.to_datetime(date)
    except ValueError:
        logging.error("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return None

    amount = input("Enter the amount: ")
    try:
        amount = float(amount)
    except ValueError:
        logging.error("Invalid amount entered. Please enter a numeric value.")
        return None

    category = input("Enter the category: ")
    description = input("Enter the description: ")

    return date, amount, category, description

def view_transactions(tracker):
    transactions = tracker.read_transactions()
    if transactions:
        for transaction in transactions:
            logging.info(transaction)
    else:
        logging.info("No transactions found.")

def delete_transaction(tracker):
    transaction_id = input("Enter the transaction ID to delete: ")
    try:
        tracker.delete_transaction(transaction_id)
        save_data(tracker)
        logging.info("Transaction with ID %s deleted successfully.", transaction_id)
    except Exception as e:
        logging.error("An error occurred while deleting transaction: %s", e)

def edit_transaction(tracker):
    transaction_id = input("Enter the transaction ID to edit: ")
    print("\nSelect the field to edit:")
    print("1. Date")
    print("2. Amount")
    print("3. Category")
    print("4. Description")
    choice = input("Enter your choice: ")

    # Initialize the fields with None
    date, amount, category, description = None, None, None, None

    if choice == '1':
        date = input("Enter the new date (YYYY-MM-DD): ")
    elif choice == '2':
        amount = input("Enter the new amount: ")
        try:
            amount = float(amount)
        except ValueError:
            logging.error("Invalid amount entered. Please enter a numeric value.")
            return
    elif choice == '3':
        category = input("Enter the new category: ")
    elif choice == '4':
        description = input("Enter the new description: ")
    else:
        logging.error("Invalid choice. Please try again.")
        return

    try:
        tracker.edit_transaction(transaction_id, date=date, amount=amount, category=category, description=description)
        save_data(tracker)
        logging.info("Transaction with ID %s edited successfully.", transaction_id)
    except Exception as e:
        logging.error("An error occurred while editing transaction: %s", e)

def add_transaction(tracker):
    user_input = get_user_input()
    if user_input:
        date, amount, category, description = user_input
        tracker.add_transaction(date, amount, category, description)
        save_data(tracker)

def generate_report(tracker):
    report = ReportGenerator(tracker.transactions)
    monthly_report = report.generate_monthly_report()
    logging.info("\nMonthly Report:\n%s", monthly_report)

def generate_annual_report(tracker):
    report = ReportGenerator(tracker.transactions)
    annual_report = report.generate_annual_report()
    logging.info("\nAnnual Report:\n%s", annual_report)

def generate_category_report(tracker):
    report = ReportGenerator(tracker.transactions)
    category_report = report.generate_category_report()
    logging.info("\nCategory Report:\n%s", category_report)

def search_transactions(tracker):
    search_term = input("Enter search term (category, date, or amount): ")
    results = [t for t in tracker.transactions if search_term.lower() in str(t).lower()]
    if results:
        for result in results:
            logging.info(result)
    else:
        logging.info("No transactions found matching the search term.")

def main():
    tracker = FinanceTracker()
    if load_data(tracker):
        save_data(tracker)

    menu_options = {
        '1': view_transactions,
        '2': add_transaction,
        '3': delete_transaction,
        '4': edit_transaction,
        '5': generate_report,
        '6': generate_annual_report,
        '7': generate_category_report,
        '8': search_transactions,
        '9': exit
    }

    while True:
        print("\nMenu:")
        print("1. View Transactions")
        print("2. Add Transaction")
        print("3. Delete Transaction")
        print("4. Edit Transaction")
        print("5. Generate Monthly Report")
        print("6. Generate Annual Report")
        print("7. Generate Category Report")
        print("8. Search Transactions")
        print("9. Exit")
        choice = input("Enter your choice: ")

        action = menu_options.get(choice)
        if action:
            action(tracker)
        else:
            logging.error("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()