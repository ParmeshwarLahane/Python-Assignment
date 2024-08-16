# Write a program which accept number from user and check whether that number is positive or negative number

def main():

    print("\nThis application is to check the entered number is positive or negative :")

    No = float(input("Enter number : "))

    if No == 0:
        print(f"Input is Zero : {int(No)}\n")

    elif No > 0:
        print(f"Positive number : {No}\n")

    else:
        print(f"Negative number : {No}\n")

main()