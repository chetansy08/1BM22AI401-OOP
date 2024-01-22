from abc import ABC, abstractmethod

class MathOperation(ABC):

  @abstractmethod
  def add(self,x,y):
    pass

  @abstractmethod
  def subtract(self,x,y):
    pass

  @abstractmethod
  def multiply(self,x,y):
    pass

  @abstractmethod
  def division(self,x,y):
    pass

class SimpleCalculator(MathOperation):
  def add(self,x,y):
    return x + y

  def subtract(self,x,y):
    return x - y

  def multiply(self,x,y):
    return x * y

  def division(self,x,y):
    if y == 0:
      raise ValueError("cannot divide by zero ")
    return x / y


calculator=SimpleCalculator()

res_add=calculator.subtract(5,4)
print(res_add)
