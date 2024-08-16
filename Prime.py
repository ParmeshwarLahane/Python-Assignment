# Write a program which accept one number from user and return is prime or not.

def main(No):
    
    if No <= 1:
        return False

    for i in range(2,int(No**0.5) + 1):
        if (No % i) == 0:
            return False
    return True

No = int(input("\nEnter number : "))
if main(No):
    print("Prime number \n")

else:
    print("This is not Prime number : \n")