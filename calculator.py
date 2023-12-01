#calculater using function

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

x = int(input('Enter the number : '))
y = int(input('Enter the number : '))
print("1. Add\n2. Subract\n3. Multiplication\n4. Division")
choice = int(input('Enter your choice : '))
if(choice == 1):
    print(add(x,y))
elif(choice == 2):
    print(sub(x,y))
elif(choice == 3):
    print(mul(x,y))
elif(choice == 4):
    print(div(x,y))
else:
    print("Invalid choice")