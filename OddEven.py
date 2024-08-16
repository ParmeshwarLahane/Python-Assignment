# Write a program which contains one function named as ChkNum(),
# Which accept one parameter as number, if number is even then it should diplay "Even number" otherwise diplay "Odd number" on console.

def ChkNum():

    print("\nThis program will check whether the entered number is odd or even :")

    No = int(input("\nEnter number : "))

    if No >= 0:

        if (No % 2) == 0:
            print(f"\nEven number: {No}\n")

        else:
            print(f"\nOdd number: {No}\n")

    else:
        print("\nInvalid input.... :\n")

if __name__=="__main__":
    ChkNum()



