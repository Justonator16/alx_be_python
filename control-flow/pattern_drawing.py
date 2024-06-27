integer = int(input("Enter the size of the pattern: "))

#ANother method
# for i in range(integer):
#     for j in range(integer):
#         print("*",end="")
#     print()
    
i = 0
while i < integer:
    for j in range(integer):
        print("*",end="")  
    print() 
    i += 1
