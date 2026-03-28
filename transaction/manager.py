from utils import prompt_int, prompt_non_empty
from account.entity import Account
from reports.history import log_transaction


class TransactionManager:
    def check_balance(self, current_user: Account) -> None:
        print("\n" + "="*30 + "\n      BALANCE INQUIRY\n" + "="*30)
        print(f"Holder: {current_user.name}\nAcc No: {current_user.acc_no}\nBalance: {current_user.balance:.2f} BDT")
        print("="*30)

    def deposit(self, current_user: Account) -> float:
        amount = float(prompt_int("\nEnter Deposit Amount: ", min_val=1))
        current_user.balance += amount
        print(f"Deposited {amount} BDT.")
        return amount

    def withdraw(self, current_user: Account) -> float:
        amount = float(prompt_int("\nEnter Withdrawal Amount: ", min_val=1))
        if amount > current_user.balance:
            print("Error: Insufficient funds!")
            return 0.0
        current_user.balance -= amount
        print(f"Withdrawn {amount} BDT.")
        return amount

    def transfer(self, current_user: Account, accounts: list[Account], history_list: list[dict]) -> None:
        target_id = prompt_int("\nEnter Receiver Acc No: ")
        receiver = next((acc for acc in accounts if acc.acc_no == target_id), None)
        
        if receiver and receiver != current_user:
            amount = float(prompt_int(f"Transfer to {receiver.name}. Amount: ", min_val=1))
            if amount <= current_user.balance:
                if prompt_non_empty("Enter PIN to confirm: ") == current_user.pin:
                    current_user.balance -= amount
                    receiver.balance += amount
                    log_transaction(history_list, current_user.acc_no, f"To {target_id}", amount)
                    log_transaction(history_list, receiver.acc_no, f"From {current_user.acc_no}", amount)
                    print("Transfer Successful!")
                else: print("Error: Invalid PIN.")
            else: print("Error: Insufficient balance.")
        else: print("Error: Receiver not found or self transfer.")