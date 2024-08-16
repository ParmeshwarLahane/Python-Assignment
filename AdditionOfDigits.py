# Write a program which accept number from user and return addition of digits in that number.

print("This Python program is for addition of number series. : ")

def main():
    Ans = 0
    Numbers = input("\nEnter numbers : ")

    for digit in str(Numbers):
        Ans += int(digit)
        print(digit,end=" ")

    print(f"\nAddition of Number Series : {Ans}")

if __name__=="__main__":
    main()