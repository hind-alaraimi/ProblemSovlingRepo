def divide_number(n1,n2):
    try:
        Div = int(n1) / int(n2)
        
    except ValueError:
        print("Invalid Input, please enter only a number!")
    except ZeroDivisionError:
        print("You can't divide by zero!")
        
    finally:
        print("Calculation Completed!")
    #return Div

num1 = input("Enter First Number: ")
num2 = input("Enter First Number: ")

print(divide_number(num1,num2))