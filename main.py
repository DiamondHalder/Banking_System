from tabulate import tabulate
from account.manager import AccountManager
from account.storage import DataStorage
from transaction.security import SecurityManager
from transaction.manager import TransactionManager
from reports.history import HistoryManager, log_transaction 
from reports.analytics import ReportManager
from reports.statement import StatementGenerator

def main():
    storage = DataStorage()
    accounts = storage.load_accounts()
    txn_history = []
    
    acc_mgr = AccountManager(accounts)
    trans_mgr = TransactionManager()
    sec_mgr = SecurityManager()
    rep_mgr = ReportManager()
    hist_mgr = HistoryManager()
    stmt_gen = StatementGenerator()

    while True:
        print("\n" + "="*45 + "\n      BANKING MANAGEMENT SYSTEM (OOP PRO)\n" + "="*45)
        menu = [["1", "Create Account"], ["2", "User Login"], ["3", "Analytics"], ["4", "Manage Profiles"], ["5", "Exit"]]
        print(tabulate(menu, headers=["Opt", "Description"], tablefmt="fancy_outline"))
        
        choice = input("\nChoice (1-5): ").strip()
        if choice == "1": acc_mgr.add_new_account(txn_history)
        elif choice == "2":
            user = sec_mgr.login(accounts)
            if user:
                while True:
                    print(f"\n>>> Active: {user.name}")
                    u_menu = [["1", "Balance"], ["2", "Deposit"], ["3", "Withdraw"], ["4", "Transfer"], ["5", "History"], ["6", "Logout"]]
                    print(tabulate(u_menu, tablefmt="plain"))
                    c = input("\nAction: ").strip()
                    if c == "1": trans_mgr.check_balance(user)
                    elif c == "2":
                        amt = trans_mgr.deposit(user)
                        log_transaction(txn_history, user.acc_no, "Deposit", amt)
                        stmt_gen.print_receipt(user.name, user.acc_no, "Deposit", amt, user.balance)
                    elif c == "3":
                        amt = trans_mgr.withdraw(user)
                        if amt > 0:
                            log_transaction(txn_history, user.acc_no, "Withdraw", amt)
                            stmt_gen.print_receipt(user.name, user.acc_no, "Withdraw", amt, user.balance)
                    elif c == "4": trans_mgr.transfer(user, accounts, txn_history)
                    elif c == "5": hist_mgr.view_history(txn_history, user.acc_no)
                    elif c == "6": break
        elif choice == "3":
            rep_mgr.show_bank_summary(accounts)
            rep_mgr.show_top_customers(accounts)
        elif choice == "4":
            acc_mgr.update_profile()
        elif choice == "5":
            storage.save_accounts(accounts)
            print("Goodbye!"); break

if __name__ == "__main__": main()