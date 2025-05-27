def Addition(a,b):
    return a+b
    
def Subtration(a,b):
    return a-b
    
def Multiplicaton(a,b):
    return a*b
    
def Division(a,b):
    return a/b
    
def Modulus(a,b):
    return a%b
    
a=float(input("Enter a number: "))
b=float(input("Enter a number: "))
print("Choose operator: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. modulus")
choice=int(input("Enter your choice: "))
a=int(a)
b=int(b)
if choice==1:
    Addition=Addition(a,b)
    print(f"{a} + {b} =", Addition)

elif choice==2:
    Subtration=Subtration(a,b)
    print(f"{a} - {b} =", Subtration)

elif choice==3:
    Multiplicaton=Multiplicaton(a,b)
    print(f"{a} x {b} =", Multiplicaton)

elif choice==4:
    Division==Division(a,b)
    print(f"{a} / {b} =", Division)

elif choice==5:
    Modulus=Modulus(a,b)
    print(f"{a} % {b} =", Modulus)

else:
    print("Enter a valid operator")