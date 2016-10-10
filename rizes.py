import math
a=int(input("Enter the first factor of the equation:"))
b=int(input("Enter the second factor of the equation:"))
c=int(input("Enter the second factor of the equation:"))
if (b**2-4*a*c<0):
    print("No real valued solutions exist")
else:
    riza=math.sqrt(b**2-4*a*c)
    x1=(-b+riza)/2*a
    x2=(-b-riza)/2*a
    if (x1==x2):
        print("The double solution of the equation is:",x1)
    else:
        print("The first solution of the equation is", x1, "and the second solution of the equation is", x2)
        
