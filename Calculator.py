while True:
    a=int(input("Enter first number "))
    b=int(input("Enter second number "))

    operation = int(input("choose operation (Add Subtract Multiply Divide or Exponential or Remainder) Enter as 1,2,3,4,5,6 "))
    if operation == 1:
        print(a+b)
    elif operation == 2:
        print(a-b)
    elif operation == 3:
        print(a*b)
    elif operation == 4:
        print(a/b)
    elif operation == 5:
        print(a**b)
    elif operation ==6:
        print(a%b)
    else:
        print("Not an operation")
    Continue = input("Do you want to continue? Yes/no ")
    if Continue == "yes":
        print("ok")
    else:
        print("Goodbye!")
        break
        
