import math
x1 = int(input("Enter the x1 : "))
x2 = int(input("Enter the x2 : "))
y1 = int(input("Enter the y1 : "))
y2 = int(input("Enter the y2 : "))

d1 = (x2-x1)*(x2-x1)
d2 = (y2-y1)*(y2-y1)

res = math.sqrt(d1+d2)
print("Distance between two points is : ",res)