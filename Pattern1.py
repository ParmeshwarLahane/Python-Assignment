# Write a program which accept one nuber and diplay the below patter
# Output ---
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print("\nProgram is for print star pattern in scure formate")

def main():
    No = int(input("Enter number : "))
    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()

if __name__=="__main__":
    main()

# Write a program which accept one nuber and diplay the below patter
# Output ---
# * * * * *
# * * * * 
# * * * 
# * * 
# * 
print("\nProgram is for print star pattern in scure formate")

def main():
    No = int(input("Enter number : "))
    for i in range(No):
        for j in range(No-i):
            print("*",end=" ")
        print()

if __name__=="__main__":
    main()


# Write a program which accept one nuber and diplay the below patter
# Output ---
# *
# * *
# * * *
# * * * *
# * * * * *

def main():
    No = int(input("Enter number : "))
    for i in range(No):
        for j in range(i+1):
            print("*",end=" ")
        print()

if __name__=="__main__":
    main()


# Write a program which accept one nuber and diplay the below patter
# Output ---
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def main():
    No = int(input("Enter number : "))
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

if __name__=="__main__":
    main()
