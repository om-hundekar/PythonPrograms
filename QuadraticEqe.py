import math
a=int(input("Enter the coeficient of x2"))
b=int(input("Enter the coeficient of x"))
c=int(input("Enter the coeficient of term"))
dis=(b*b)-(4*a*c)
print("Discriminant=",dis)
if dis==0:
    print("Both roots are equal")
    r1=r2=(-b +math.sqrt(dis))/(2*a)
    print("Root 1:",r1,"Root 2:",r2)
elif dis>0:
    print("Both roots are real")
    r1=(-b + math.sqrt(dis))/(2*a)
    r2=(-b - math.sqrt(dis))/(2*a)
    print("Root 1:",r1,"Root 2:",r2)
else:
    print("Both roots are complex")

    
