# Write a program which contains one function that accept one number from user and returns True if number is divisible by 5 otherwise return False.
def Check(No):

    if No > 0:

        if (No % 5) == 0:
            return True

        else:
            return False
    else:
        return "Input is Zero"

def main():

    print("\nThis app checks whether the entered number is divisible by 5 or not...")

    No = int(input("Enter number : "))
    Ans = Check(No)
    print(Ans)


    # if No > 0:
        
    #     if (No%5) == 0:
    #         print(True)

    #     else:
    #         print(False)
    
    # else:
    #     print("Input Zero")

    
main()