# Write a program which display 10 time Hello World 

def main():
    
    print("\nThe purpose of the program is to display Hello World on the screen as per the input.")
    
    No = int(input("Enter number : "))      # Value of No Variable : User input

    # If start point and step of loop are not specified then it will take start point as 0 and step as 1 by default.
    for i in range(No):      # For loop Starting point - 0, End point - No Value, Steps - 1.       

        print("Hello world..")

if __name__=="__main__":   # Program starter
    main()