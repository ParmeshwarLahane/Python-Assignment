# Create on module named as Arithmetic which contains 4 function as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division.
# All functions accepts two parameters as number and perform the opeation.
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user

def Add(Value1, Value2):
    return Value1 + Value2

def Sub(Value1, Value2):
    return Value1 - Value2

def Mul(Value1, Value2):
    return Value1 * Value2

def Div(Value1, Value2):
    return Value1 / Value2

def main():
    print("\nThis application is for perform Basic Arithmetic operations..")

    No1 = int(input("\nEnter first number : "))
    Opertor = input("Opretor? ")
    No2 = int(input("Enter first number : "))

    if Opertor == "+":
        Ans = Add(No1,No2)
        print(Ans)

    elif Opertor == "-":
        Ans = Sub(No1,No2)
        print(Ans)


    elif Opertor == "*":
        Ans = Mul(No1,No2)
        print(Ans)

    elif Opertor == "/":
        Ans = Div(No1,No2)
        print(Ans)

    else:
        print("\nInvalid input.. \n  Addition : +\n  Subtraction : '-' \n  Multiplication : '*' \n  Division : '/' \ntry again 'Good luck!!'\n\n")


if __name__=="__main__":
    main()



# -----------------------------OR-----------------------------------

# def Operator(Value1,Simbole,Value2):

#     if Simbole == "+":
#         return Value1 + Value2

#     if Simbole == "-":
#         return Value1 - Value2

#     if Simbole == "*":
#         return Value1 * Value2

#     if Simbole == "/":
#         return Value1 / Value2

#     else:
#         print("\nInvalid input.. \n  Addition : +\n  Subtraction : '-' \n  Multiplication : '*' \n  Division : '/' \ntry again 'Good luck!!'\n\n")

# def main():
#     print("\nProgram is for perform math opration")

#     No1 = int(input("\nEnter first number : "))
#     Simbole = input("Opretor? ")
#     No2 = int(input("Enter first number : "))

#     Ans = Operator(No1,Simbole,No2)
#     print(Ans)

# if __name__=="__main__":
#     main()
