class WrongAge(Exception):
  pass 

class AgeInvalid(Exception):
  pass

class Father:
  def __init__(self,age):
    if age<0:
      raise WrongAge("age cannot be negative")

    self.age=age

class Son(Father):
  def __init__(self,father_age,son_age):
    super().__init__(father_age)
    if son_age>=father_age:
      raise AgeInvalid("son's age shld be less den father's age")

    self.son_age=son_age

try:
  father_age=int(input("Enter the father's age"))
  son_age=int(input("Enter the son's age"))
  obj=Son(father_age,son_age)

  print("father age:",father_age)
  print("son age:",son_age)

except WrongAge as e:
  print("Error",e)

except AgeInvalid as e:
  print("Error",e)

except ValueError:
  print("please enter valid age as integer")

