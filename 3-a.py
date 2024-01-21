class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.__salary=salary

  def Work(self):
    print("WORKING AS A TRANIEE")

  def show(self):
    print(f"EMPLOYEE NAME:,{self.name}")
    print(f"employee salary:{self.__salary}")

  def get_name(self):
    print(self.name)

  def set_salary(self,x):
    self.__salary=x



emp=Employee("chetan","20000")
emp.Work()

emp.set_salary(30000)
emp.show()
# print("employee salary",emp.salary)

#name manggling
print("Employee-salary",emp._Employee__salary)
