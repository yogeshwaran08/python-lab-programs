try:
    a = int(input("Enter the num 1 : "))
    b = int(input("Enter the num 2 :"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Zero error")
except ValueError:
    print("Number only")
finally:
    print("Exception handling works correctly")