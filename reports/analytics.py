from tabulate import tabulate
from account.entity import Account

class ReportManager:
    

    def show_bank_summary(self, accounts: list[Account]) -> None:
        if not accounts:
            print("No accounts in the system.")
            return

        total_balance = sum(acc.balance for acc in accounts)
        total_users = len(accounts)
        
        summary_data = [
            ["Total Registered Users", f"{total_users} Persons"],
            ["Total Bank Assets", f"{total_balance:.2f} BDT"]
        ]
        print("\n" + "╔" + "═"*35 + "╗")
        print("║      GLOBAL BANK ANALYTICS        ║")
        print("╚" + "═"*35 + "╝")
        print(tabulate(summary_data, tablefmt="fancy_grid"))

    def show_top_customers(self, accounts: list[Account]) -> None:
        if not accounts:
            print("No accounts to display.")
            return

        
        sorted_acc = sorted(accounts, key=lambda x: x.balance, reverse=True)
        
        table_data = []
        
        for i, acc in enumerate(sorted_acc[:5], 1):
            table_data.append([i, acc.name, acc.acc_no, f"{acc.balance:.2f} BDT"])
        
        print("\n--- TOP 5 VALUABLE CUSTOMERS ---")
        print(tabulate(table_data, headers=["Rank", "Name", "Acc No", "Balance"], tablefmt="grid"))