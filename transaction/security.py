from utils import prompt_non_empty, prompt_int
from account.entity import Account

class SecurityManager:
    
    
    @staticmethod
    def login(accounts: list[Account]) -> Account | None:
        print("\n" + "-"*25)
        print("   SECURE USER LOGIN")
        print("-"*25)
        acc_no = prompt_int("Account Number: ")
        pin = prompt_non_empty("PIN: ")

        for acc in accounts:
        
            if acc.acc_no == acc_no and acc.pin == pin:
                print(f"\nWelcome back, {acc.name}!")
                return acc
        
        print("\nError: Invalid credentials!")
        return None

    @staticmethod
    def change_pin(current_user: Account) -> None:
        print("\n--- Change Security PIN ---")
        old_pin = prompt_non_empty("Enter Current PIN: ")
        if old_pin == current_user.pin:
            current_user.pin = prompt_non_empty("Enter New 4-Digit PIN: ")
            print("Success: PIN updated successfully.")
        else:
            print("Error: Authentication failed.")