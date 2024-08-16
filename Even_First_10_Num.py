# Write a program which display first 10 even number on screen

print("\nThis Application is to find even number")

def main():

    No = int(input("\nEnter Count : ")) 
    
    for i in range(2,(No+1)*2,2):
        
        print(i)
if __name__=="__main__":
    main()