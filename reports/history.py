from tabulate import tabulate
from datetime import datetime


def log_transaction(history_list: list[dict], acc_no: int, txn_type: str, amount: float) -> None:
    entry = {
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "acc_no": acc_no,
        "type": txn_type,
        "amount": amount
    }
    history_list.append(entry)

class HistoryManager:
   
    def view_history(self, history_list: list[dict], acc_no: int) -> None:
        user_history = [txn for txn in history_list if txn["acc_no"] == acc_no]
        if not user_history:
            print(f"\n[!] No transactions found for Account: {acc_no}")
            return

        table_data = []
        for txn in user_history:
            table_data.append([txn["timestamp"], txn["type"], f"{txn['amount']:.2f} BDT"])
        
        print(f"\n--- TRANSACTION HISTORY (ACC: {acc_no}) ---")
        print(tabulate(table_data, headers=["Date & Time", "Type", "Amount"], tablefmt="fancy_grid"))