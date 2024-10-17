import pandas as pd

class ReportGenerator:
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_monthly_report(self):
        if not self.transactions:
            return "No transactions available to generate a report."

        df = pd.DataFrame(self.transactions)
        
        if 'date' not in df.columns:
            return "The 'date' column is missing in the transactions data."

        try:
            df['date'] = pd.to_datetime(df['date'])
            monthly_summary = df.groupby(df['date'].dt.to_period('M')).sum(numeric_only=True)
            
            report = "Monthly Report:\n"
            report += "-" * 30 + "\n"
            for period, row in monthly_summary.iterrows():
                report += f"{period.strftime('%B %Y')}:\n"
                for column, value in row.items():
                    report += f"  {column.capitalize()}: {value:.2f}\n"
                report += "-" * 30 + "\n"
            return report
        except Exception as e:
            return f"An error occurred while generating the report: {e}"

    def generate_annual_report(self):
        if not self.transactions:
            return "No transactions available to generate a report."

        df = pd.DataFrame(self.transactions)
        
        if 'date' not in df.columns:
            return "The 'date' column is missing in the transactions data."

        try:
            df['date'] = pd.to_datetime(df['date'])
            annual_summary = df.groupby(df['date'].dt.to_period('Y')).sum(numeric_only=True)
            
            report = "Annual Report:\n"
            report += "-" * 30 + "\n"
            for period, row in annual_summary.iterrows():
                report += f"{period.strftime('%Y')}:\n"
                for column, value in row.items():
                    report += f"  {column.capitalize()}: {value:.2f}\n"
                report += "-" * 30 + "\n"
            return report
        except Exception as e:
            return f"An error occurred while generating the report: {e}"

    def generate_category_report(self):
        if not self.transactions:
            return "No transactions available to generate a report."

        df = pd.DataFrame(self.transactions)
        
        if 'category' not in df.columns:
            return "The 'category' column is missing in the transactions data."

        try:
            category_summary = df.groupby('category').sum(numeric_only=True)
            
            report = "Category Report:\n"
            report += "-" * 30 + "\n"
            for category, row in category_summary.iterrows():
                report += f"{category}:\n"
                for column, value in row.items():
                    report += f"  {column.capitalize()}: {value:.2f}\n"
                report += "-" * 30 + "\n"
            return report
        except Exception as e:
            return f"An error occurred while generating the report: {e}"