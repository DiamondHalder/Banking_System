from utils import prompt_non_empty, prompt_int, clean_name
from account.entity import Account
from reports.history import log_transaction

class AccountManager:
    def __init__(self, accounts: list[Account]):
        self.accounts = accounts

    def generate_acc_no(self) -> int:
        if not self.accounts: return 1001
        return self.accounts[-1].acc_no + 1

    def add_new_account(self, history_list: list[dict]) -> None:
        print("\n" + "="*30 + "\n   CREATE NEW ACCOUNT \n" + "="*30)
        name = clean_name(prompt_non_empty("Enter Customer Name: "))
        while True:
            phone = prompt_non_empty("Enter Phone Number: ")
            if phone.isdigit() and len(phone) == 11:
                break
            print("Error: Phone number must be numeric and contain exactly 11 digits.")
        
        for acc in self.accounts:
            if acc.phone == phone:
                print("Error: This phone number is already linked!")
                return

        while True:
            pin = prompt_non_empty("Set 4-Digit Security PIN: ")
            if pin.isdigit() and len(pin) == 4:
                 break
            print("Error: PIN must be exactly 4 digits.")
        balance = float(prompt_int("Initial Deposit Amount (Min 500): ", min_val=500))

        new_acc = Account(self.generate_acc_no(), name, phone, pin, balance)
        self.accounts.append(new_acc)
        log_transaction(history_list, new_acc.acc_no, "Initial Dep", balance)
        print(f"\nSuccess! Account Number: {new_acc.acc_no}")

    def find_account(self, acc_no: int) -> Account | None:
        for acc in self.accounts:
            if acc.acc_no == acc_no: return acc
        return None

    def update_profile(self) -> None:
        acc_no = prompt_int("Enter Account Number to Update: ")
        acc = self.find_account(acc_no)
        if acc:
            new_name = input("New Name (Enter to skip): ").strip()
            if new_name: acc.name = clean_name(new_name)
            new_phone = input("New Phone (Enter to skip): ").strip()
            if new_phone: acc.phone = new_phone
            print("Profile updated!")
        else: print("Error: Account not found!")

    def close_account(self, history_list: list[dict]) -> None:
         
        acc_no = prompt_int("Enter Account Number to Delete: ")
        acc = self.find_account(acc_no)
    
        if not acc:
            print("Error: Account not found!")
            return
    
        if acc.balance > 0:
         print(f"Error: Account balance must be 0 BDT to close (Current: {acc.balance:.2f} BDT)")
         return

        pin = prompt_non_empty("Enter your PIN to confirm: ")
        if pin != acc.pin:
          print("Error: Invalid PIN. Cannot close account.")
          return

     
        log_transaction(history_list, acc.acc_no, "Account Closed", 0)
    
        self.accounts.remove(acc)
        print(f"Account {acc.acc_no} ({acc.name}) has been successfully closed.")