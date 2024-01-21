class Dog:
  def __init__(self,name,size,breed='unknown',dob='unknown'):
    self.set_name(name)
    self.size=size
    self.breed=breed
    self.dob=dob

  def Bark(self):
    print("Woof!")

  def get_name(self):
    print("Dog name:",self.name)

  def set_name(self,name):
    if 2 <= len(name) <=30 and name.isalpha():
      self.name=name.title()

    else:
        raise ValueError("invalid name , name shld be bet 2 and 30 ")

  def dog_years(self):
    self.dob=(2023 - int(self.dob))*7
    print("dog age:",self.dob)

obj=Dog("bob",'med','huskey','2020')
obj.Bark()
obj.get_name()
obj.dog_years()
