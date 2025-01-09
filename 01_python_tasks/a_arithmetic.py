# Basic Arithmetic Operations

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

print(f"Addition        :   {num1} + {num2} = {num1 + num2} ")
print(f"Subtraction     :   {num1} - {num2} = {num1 - num2} ")
print(f"Multiplication  :   {num1} X {num2} = {num1 * num2} ")
def division(num1,num2):
    if(num2==0):
        print(f"Division        :   {num1} / {num2} = Division by zero is not allowed")
    else:
        print(f"Division        :   {num1} / {num2} = {num1 / num2} ")
division(num1,num2)

        

'''

Output:

Enter a first number: 12
Enter a second number: 6
Addition        :   12 + 6 = 18
Subtraction     :   12 - 6 = 6
Multiplication  :   12 X 6 = 72
Division        :   12 / 6 = 2.0


Enter a first number: 12
Enter a second number: 0
Addition        :   12 + 0 = 12
Subtraction     :   12 - 0 = 12
Multiplication  :   12 X 0 = 0
Division        :   12 / 0 = Division by zero is not allowed

'''
      
