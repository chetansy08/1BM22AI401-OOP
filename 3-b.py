class CreditCard:
  __limit=150000

  def __init__(self,balance,pin):
    self.__balance=balance
    self.__pin=pin

  def get_balance(self):
    print("available balance:",self.__balance)

  def withdraw(self,amount):
    if amount<self.__balance and amount>0:
      self.__balance=self.__balance-amount
      print(f"Amount Rs{amount} withdrawn successfully")
      # print("remaianig balance",self.__balance)

    else:
      print("Insufficient balance so you can't withdraw")

  def deposite(self,amount):
    temp=self.__balance + amount
    if temp>CreditCard.__limit:
      print("can't deposite")

    else:
      balance=self.__balance + amount
      print("amount deposited successfully")
      # print(self.balance)

cc=CreditCard(50000,6090) 
cc.get_balance() 
cc.withdraw(10000)
cc.deposite(20000)
