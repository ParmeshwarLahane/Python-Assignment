# Write a program which accept one number from user and return its factorial
print("\nProgram is for print Factorials : ")
def main():

    No = int(input("Enter number : "))     # User input
    Temp = 1            # Variable fixed on - 1

    if No >= 1:         # If number is greater than or equal to one. Then run the below loop.

        for i in range(1,No+1,1):      # For loop Starting point - 1, End point - Value of No, Steps - 1.
            Temp = Temp * i

        print(f"{Temp} Factores of Number : {No}\n\n")

if __name__=="__main__":
    main()