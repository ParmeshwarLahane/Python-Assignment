# Write a program which display number to reverse order, like 10 to 1 on screen

def main():

    print("\nThis program will print the numbers in reverse order..")

    No = int(input("\nEnter number : "))

    for i in range(No,0,-1):
        print(i,end=" ")
        
    print("\n")

main()