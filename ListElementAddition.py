# Write a program which accept N numbers from user and store it into list. Return addition of all elements from that list.

def main():

    list1 = list()   # Creating Empty list
    Addition = 0        # Variable declaration 

    print("Enter your list element length")
    No = int(input())  # User numbers input for the length of list

    print("Put your list element and Enter, do this till value of No ")  # Display Massges to user how to give input for program
    for i in range(1,No+1):     # hare loop run for get input for list elements
        Addition += i          # Adding for loop i variable value with Addition like Addition = Addition + i

        Element = int(input())          # User input of list elements
        list1.append(Element)       # Adding list element in Empty list1

    # Display the list and addition of list elements
    print(f"Display the List : {list1},\nAddition of list element : {Addition}")

if __name__=="__main__":
    main()          # Program starter

"""
def ListAddition(Ans):
    Addition = 0
    for i in Ans:
        Addition += i
    return Addition        

def ListDisplay(Listlength):
    list1 = list()
    for i in range(1,Listlength+1):
        list1.append(i)

    return list1

def main():
    Listlength = int(input("Enter Listlength : "))
    Ans = ListDisplay(Listlength)
    Addition = ListAddition(Ans)
    
    print(f"List : {Ans}, \nAddition : {Addition}")


if __name__=="__main__":
    main()          # Program starter
"""