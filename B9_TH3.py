"""" Program make a simple a calculator that can add, subtract,multiply and divide using functions"""
# This function add two numbers
def add(x,y):
    return x+y
# This function subtracts two numbers
def subtract(x,y):
    return x-y
# This function multiplies twon numbers
def multiply(x,y):
    return x*y
# This function diviedes two numbers
def divide(x,y):
    return x/y
print(" Select operetion.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice=input(" Enter choice(1/2/3/4):")
num1=int(input("Enter fist number:"))
num2=int(input("Enter second number: "))

if choice=='1':
    print(num1,"+","=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")
