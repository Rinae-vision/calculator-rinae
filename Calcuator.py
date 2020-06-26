#Python calculator
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b
print("select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice1/2/3/4")

num1 = input("enter a number :")

num2 = input("enter another  number :")

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
    
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid input")
    