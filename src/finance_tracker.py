import csv

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, amount, category, description):
        transaction_id = len(self.transactions) + 1
        self.transactions.append({
            'id': transaction_id,
            'date': date,
            'amount': float(amount),
            'category': category,
            'description': description
        })

    def read_transactions(self):
        return self.transactions

    def delete_transaction(self, transaction_id):
        self.transactions = [t for t in self.transactions if t['id'] != int(transaction_id)]

    def edit_transaction(self, transaction_id, date=None, amount=None, category=None, description=None):
        for transaction in self.transactions:
            if transaction['id'] == int(transaction_id):
                if date:
                    transaction['date'] = date
                if amount is not None:
                    transaction['amount'] = float(amount)
                if category:
                    transaction['category'] = category
                if description:
                    transaction['description'] = description
                break

    def load_data(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.add_transaction(row['date'], row['amount'], row['category'], row['description'])
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def save_data(self, file_path):
        try:
            with open(file_path, mode='w', newline='') as file:
                fieldnames = ['id', 'date', 'amount', 'category', 'description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for transaction in self.transactions:
                    writer.writerow(transaction)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")