# midterm_project_201610680
import logging
logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    logger.info(f'add({x}, {y})={x+y}')
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    logger.info(f'subtract({x}, {y})={x-y}')
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    logger.info(f'multiply({x}, {y})={x*y}')
    return x * y

#Need to define divide function.
def divide (x,y):
    logger.info(f'divide({x}, {y})={x/y}')
    return x/y

print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 
print("5.log")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))
            

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice =='4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1,num2))
        elif choice =='5':
            test = open('logfile.log','rt')
            fileLines = test.readlines()
            for line in fileLines:
                print(line)

            test.close()
            

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")



#commit test
