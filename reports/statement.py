from tabulate import tabulate

class StatementGenerator:
   

    def print_receipt(self, acc_name: str, acc_no: int, txn_type: str, amount: float, current_balance: float) -> None:
        receipt_data = [
            ["Account Holder", acc_name],
            ["Account No", acc_no],
            ["Transaction Type", txn_type],
            ["Amount", f"{amount:.2f} BDT"],
            ["Current Balance", f"{current_balance:.2f} BDT"]
        ]
        
        print("\n" + "═"*40)
        print("        TRANSACTION SUCCESSFUL")
        print("═"*40)
        print(tabulate(receipt_data, tablefmt="plain"))
        print("═"*40)