class Bank:
    def __init__(self, name, initial_balance) -> None:
        self.name = name
        self.total_available_balace = initial_balance
        self.loan_feature = 'on'
        self.customer_list = {}
        self.total_loan_amount= 0
        

    def add_customer(self,customer):
        self.customer_list[customer.account_number] = customer

    def add_balance(self, amount):
        self.total_available_balace += amount
    
    def Loan_feature(self,laon_feature):
        self.loan_feature = laon_feature
    

    def transfer_balace(self,customer_num1,customer_num2,amount):
        if self.customer_list[customer_num1].available_balance >= amount:
            self.customer_list[customer_num2].available_balance += amount
            self.customer_list[customer_num1].available_balance -= amount
            dict = {}
            dict['transfer_balace'] = amount
            self.customer_list[customer_num1].hitrory.append(dict)

            dict = {}
            dict['recived_transfer_balace'] = amount
            self.customer_list[customer_num2].hitrory.append(dict)
        else:
            
            print('insufficient balance to transfer balance')
            print('--------------------------------------------')
            print('')
    

    def take_loan(self, customer,amount):
        if(self.loan_feature == 'on'):
            if 2*customer.available_balance < amount:
                print('A customer can not take loan grater than twice of his total amount')
                print('-----------------------------------------------------------------------')
                print('')
            else:
                if amount <= self.total_available_balace:
                    customer.available_balance += amount
                    self.total_available_balace -= amount
                    self.total_loan_amount += amount
                    dict = {}
                    dict['take_loan'] = amount
                    customer.hitrory.append(dict)
                else:
                    print("The bank has insuffient balance ")
        else:
            print('Loan feature currently Off')
            print('------------------------------')

    def Total_available_balace(self):
        print(f'Total available balance is: {self.total_available_balace}')

    def show_loan_amount(self):
        print(f'Total loan amount is: {self.total_loan_amount}')

    def customer_history(self):
        for key in self.customer_list.keys():
            print('')
            print(f'Hitrory of customer with account Number: {key} is:')
            print('')
            cust = self.customer_list[key]
            #print(cust.hitrory)
            custm = cust.hitrory
            for hit in custm:
                print(hit)

    

    def __repr__(self) -> str:
        print("================ customer list======================")
        for key in self.customer_list:
            print(f'customer email: {self.customer_list[key].email}, customer password: {self.customer_list[key].password}, customer account number: {self.customer_list[key].account_number}')
        
        print("")
        print('=================== available balance ==== provided_loan =======================')
        print(self.total_available_balace, self.total_loan_amount)

        print("")
        print('==========================all user available balance =================')

        for key in self.customer_list.keys():
            print(self.customer_list[key].available_balance)
        return ''

class User:
    def __init__(self,email,password) -> None:
        self.email = email
        self.password = password


class Customer(User):
    counter = 12345
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.account_number = Customer.genarate_account_number()
        self.hitrory = []
        self.available_balance = 0
        self.loan = 0

    @classmethod
    def genarate_account_number(self):
        self.counter += 1
        return self.counter
    
    def deposit_balance(self,amount,bank):
        self.available_balance += amount
        bank.add_balance(amount)
        dict = {}
        dict['depsit_balace'] = amount
        self.hitrory.append(dict)

    def withdrawal_balance(self,amount,bank):
        if amount <= self.available_balance:
            if bank.total_available_balace >= amount:
                self.available_balance -= amount
                bank.total_available_balace -= amount
                dict = {}
                dict['withdrawal_balace'] = amount
                self.hitrory.append(dict)
            else:
                print("The bank is bankrupt")
        else:
            print('The amount is grater than Your available balance')

    def show_balance(self):
        print(f'=================={self.account_number}-====================')
        print(f'available balance: {self.available_balance}')
        print('')
    


class Admin(User):
    id_count = 10000
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.id = Admin.id_genarator()

    @classmethod
    def id_genarator(self):
        self.id_count += 1
        return self.id_count 
    
    def show_available_balance(self,bank):
        bank.Total_available_balace()
    def show_loan_amount(self,bank):
        bank.show_loan_amount()

    def loan_feature(self,laon_feature,bank):
        bank.Loan_feature(laon_feature)
        
    
        



bank = Bank("banladesh Bank", 10)

customer1 = Customer("customer1@gmail.com", 1234)
bank.add_customer(customer1)

customer2 = Customer("customer2@gmail.com", 1235)
bank.add_customer(customer2)


customer3 = Customer("customer3@gmail.com", 1237)
bank.add_customer(customer3)


customer1.deposit_balance(2000,bank)
customer1.show_balance()

customer1.withdrawal_balance(10,bank)


# customer1.show_balance()

bank.transfer_balace(customer1.account_number, customer2.account_number, 30)

admin1 = Admin('admin1@gmail.com',45678)
admin1.loan_feature('off',bank)
bank.take_loan(customer1,300)

#print(bank)




#admin1.show_available_balance(bank)
#admin1.show_loan_amount(bank)
admin1.loan_feature('off',bank)

bank.customer_history()