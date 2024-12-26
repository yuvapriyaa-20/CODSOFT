#Calculator
def calculator():
    print("Select an operation to perform:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    try:
        operation = int(input("Enter the number corresponding to the operation(1/2/3/4):"))
        if operation not in [1,2,3,4]:
            print("Invalid operation choice. Please try again.")
            return
        n1=int(input("Enter the first number:"))
        n2=int(input("Enter the second number:"))
        if operation ==1:
            result= n1 + n2
            print(f"The result of addition :{n1} + {n2} = {result}")
        elif operation==2:
            result=n1 - n2
            print(f"Ther result of subtraction : {n1} - {n2} = {result}")
        elif operation ==3:
            result= n1 * n2
            print(f"The result of muliplication: {n1} * {n2} = {result}")
        elif operation ==4:
            if n2==0:
                print(f"Error: Division by zero is not allowed.")
            else:
                result= n1 / n2
                print(f"The result of divison: {n1} / {n2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
calculator()
                
    
