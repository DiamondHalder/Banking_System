class Account:
    
    
    def __init__(self, acc_no: int, name: str, phone: str, pin: str, balance: float):
        self.acc_no = acc_no
        self.name = name
        self.phone = phone
        self.pin = pin
        self.balance = balance
        self.status = "Active"

    def to_dict(self):
        
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "phone": self.phone,
            "pin": self.pin,
            "balance": self.balance,
            "status": self.status
        }