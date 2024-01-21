class Student:
  pass

class Marks:
  pass

obj1=Student()
obj2=Marks()

print(f"IS OBJ1 AN INSTANCE OF STUDENT: {isinstance(obj1,Student)}")
print(f"IS OBJ2 AN INSTANCE OF MARKS: {isinstance(obj2,Marks)}")

print(f"IS STUDENT AN SUBCLASS OF STUDENT:{issubclass(Student,Student)}")
print(f"IS STUDENT AN SUBCLASS OF STUDENT:{issubclass(Student,Student)}")
