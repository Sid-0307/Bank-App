class Bank:
    count=0
    def __init__(self,initial):
        self.money=initial
        
    def deposit(self,amount):
        try:
            amount=float(amount)
            self.money=self.money+amount
            self.log_transaction(f"Deposited:{amount}\tBalance:{self.money}")
            print("\nDeposition successful")
        except ValueError:
            print("Enter a valid number!!!")
        
    def withdraw(self,amount):
        try:
            amount=float(amount)
            if(amount>self.money):
                print("Not enough money to be withdraw!!!")
            else:
                self.money=self.money-amount
                self.log_transaction(f"Withdrew:{amount}\tBalance:{self.money}")
                print("\nWithdrawal successful")
        except ValueError:
            print("Enter a valid number!!!")
        
    def log_transaction(self,string):
        self.count=self.count+1
        if(self.count==1):
            with open("transactions.txt","w") as file:
                file.write(f"{string}\n")
        else:
            with open("transactions.txt","a") as file:
                file.write(f"{string}\n")
            
    
init=int(input("Enter initial balance in bank:"))
account=Bank(init)
while True:
    work=int(input("\n\n*** Menu ***\n1.Deposit\n2.Withdraw\n3.Check Transaction history\n4.Exit\nEnter your choice:"))
    if(work==1):
        amt=input("Enter amount to be deposited:")
        account.deposit(amt)
    elif(work==2):
        amt=input("Enter amount to be withdrew:")
        account.withdraw(amt)
    elif(work==3):
        print("\n\n*** Transaction history ***")
        with open("transactions.txt","r") as file:
            line=file.read()
            print(line)
    elif(work==4):
        break
    else:
        print("Enter a valid work")
        