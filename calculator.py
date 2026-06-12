def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return"Denominator can't be zero"
    else:
        return a/b
def power(a,b):
    return a**b

while True:
    print("Simple Calculator")
    print("Select from the following option:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.Exit")

    choice=int(input(("Enter your choice:")))

    if choice==6:
        print("Exits from Calculator")
        break
    if choice not in [1,2,3,4,5,6]:
        print("Invalid Choice")
        continue

    num1=int(input("Enter your first number:"))
    num2=int(input("Enter your second number:"))

    if choice==1:
        result=add(num1,num2)
    elif choice==2:
        result=subtract(num1,num2)
    elif choice==3:
        result=multiply(num1,num2)
    elif choice==4:
        result=divide(num1,num2)
    elif choice==5:
        result=power(num1,num2)
    print(f"Result:{result}\n")
