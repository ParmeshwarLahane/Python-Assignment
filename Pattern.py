# Write a program which acccept number from user and print that number of "*" on screen

print("\nProgram to print Stat on screen ")

def main():
    
    No = int(input("Enter number : "))

    for i in range(No):
        print("*",end=" ")

main()
