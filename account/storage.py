import csv
from account.entity import Account

class DataStorage:
    
    def __init__(self, filename: str = "accounts_data.csv"):
        self.filename = filename

    def save_accounts(self, accounts: list[Account]) -> None:
        if not accounts: return
        fields = ["acc_no", "name", "phone", "pin", "balance", "status"]
        try:
            with open(self.filename, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                # convert each Account object to dict and write to csv
                writer.writerows([acc.to_dict() for acc in accounts])
            print(f"\n[System] Data saved to {self.filename}")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_accounts(self) -> list[Account]:
        accounts = []
        try:
            with open(self.filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    acc = Account(
                        int(row["acc_no"]), 
                        row["name"], 
                        row["phone"], 
                        row["pin"], 
                        float(row["balance"])
                    )
                    acc.status = row["status"]
                    accounts.append(acc)
        except FileNotFoundError:
            print("[System] Starting with fresh data.")
        return accounts
    def save_transaction(self, entry: dict, filename: str = "transaction_history.csv") -> None:
        
        try:
            with open(filename, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["timestamp", "acc_no", "type", "amount"])
                if f.tell() == 0:  
                    writer.writeheader()
                writer.writerow(entry)
        except Exception as e:
            print(f"Error saving transaction: {e}")

    def load_transactions(self, filename: str = "transaction_history.csv") -> list[dict]:
        transactions = []
        try:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    transactions.append({
                        "timestamp": row["timestamp"],
                        "acc_no": int(row["acc_no"]),
                        "type": row["type"],
                        "amount": float(row["amount"])
                    })
        except FileNotFoundError:
            print("[System] No previous transaction history found.")
        except Exception as e:
            print(f"Error loading transactions: {e}")

        return transactions