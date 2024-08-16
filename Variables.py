# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that numbers

def Add():

    print("\nAddition of two number ")

    No1 = float(input("\nEnter First number : "))
    No2 = float(input("Enter Second number : "))
    
    Ans = No1 + No2

    print(f"\nAddition : {No1} + {No2} = {Ans}\n")

Add()