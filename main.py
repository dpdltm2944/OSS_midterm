# midterm_project_201610680
import function as f


print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 
print("5.log")
print("6.exit")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6'):
        

        if choice == '1':
           num1 = float(input("Enter first number: "))
           num2 = float(input("Enter second number: "))
           print(num1, "+", num2, "=", f.add(num1, num2))
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", f.subtract(num1, num2))
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", f.multiply(num1, num2))
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", f.divide(num1, num2))
        elif choice == '5':
            f.showlog()
        elif choice == '6':
            if f.exit() == False:
                break
            else:
                continue
            

        # check if user wants another calculation
        # break the while loop if answer is no
        if f.exit()==False:
            check = input("Do you want to exit? (yes/no): ")
            if check.lower() == "yes":
                break
            elif check.lower() == "no":
                continue


    else:
        f.invalid(choice)



#commit test
