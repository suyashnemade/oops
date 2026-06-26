class Atm:
    def __init__(self, pin= None , balance = 0):
        self.__pin = pin
        self.__banalce = balance

        self.menu()

    def get_pin(self):
        return self.__pin
        
    def set_pin(self, new_pin):
        self.__pin = new_pin
        return "pin changed"

    def get_balance(self):
        return self.__banalce

    def set_balance(self, new_balance):
        self.__banalce = new_balance
        return "balance changed"

    def menu(self):
        while True:
            user_input = input("""what would you like to do?
                            \n1. Enter 1 to create pin
                            \n2. Enter 2 to deposit
                            \n3. Enter 3 to withdraw
                            \n4. Enter 4 to check balance
                            \n5. Enter 5 to exit
        """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("exit")
                break
            else:
                print("invalid input")

    def create_pin(self):
        if self.__pin is None:
            self.__pin = input("Enter your 4 digit pin: ")
            print("PIN created successfully")
        else:
            print("PIN already exists")

    def deposit(self):
        temp = input("Enter your pin: ")  
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            self.__banalce += amount
            print("Amount deposited successfully")
        else:
            print("invalid pin")


    def withdraw(self):
        temp = input("enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.__banalce:
                self.__banalce -= amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("invalid pin")

    
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print("Your balance is", self.__banalce)

        else:
            print("invalid pin")