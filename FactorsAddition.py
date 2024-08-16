# Write a program which accept one number from user and return addition of factors.

print("\nProgram is to find Factors and its addition ")
def main():
    # Variable creation 
    Temp1 = 0
    No = int(input("\nEnter number : ")) # Value of No - User input

    # Loop start point - 1, end point - half value of No and + 1, step (move) - 1
    for i in range(1,int(No/2)+1,1):   # Here we have reduced the loop initialization to (No/2)

        if (No%i) == 0:
            print(i,end=",")

            Temp1 = Temp1 + i

    print(f"\nAddition of Factors : {Temp1}\n")

if __name__=="__main__":
    main()