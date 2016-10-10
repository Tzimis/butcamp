import math
s_one=int(input("Write me the the first side:"))
s_two=int(input("Write me the the second side:"))
s_three=int(input("Write me the the third side:"))
a=s_one+s_two+s_three
b=-s_one+s_two+s_three
c=s_one-s_two+s_three
d=s_one+s_two-s_three
area=0.25*math.sqrt(a*b*c*d)
print("The area of the triange:",area)
