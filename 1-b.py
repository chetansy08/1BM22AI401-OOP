class COMPLEX:
  def __init__(self,real_part,img_part):
    self.real_part=real_part
    self.img_part=img_part

  def __add__(self,other):
    result_real=self.real_part + other.real_part
    result_img=self.img_part + other.img_part
    return COMPLEX(result_real , result_img)

C1=COMPLEX(3,5)

C2=COMPLEX(2,7)

C3 = C1 + C2

print("C1:",C1.real_part,"+",C1.img_part,"i")
print("C2:",C2.real_part,"+",C2.img_part,"i")
print("C3= C1 + C2:",C3.real_part,"+",C3.img_part,"i")
