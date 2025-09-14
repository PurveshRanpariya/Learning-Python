#Q1
# n = int(input("Enter Number: "))

# for i  in range(1, 11):
#     print(f"{n} * {i} = {n*i}")


#Q2
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

#3
# n = int(input("Enter Number : "))

# i = 1
# while(i<11):
#     print(f"{n} * {i} = {n*i}")
#     i = i+1
    
    
#4
# n = int(input("Enter Number: "))

# for i in range (2, n):
#     if(n % i) == 0:
#         print(" Not prime")
#         break
# else:
#     print(" prime")   

#Q5
# n = int(input("Enter Number: "))
# i = 1
# sum = 0

# while(i<n):
   
#     sum = sum + i
#     i = i + 1
# print(sum)    

#Q6

# n = int(input("Enter Number: "))

# product = 1

# for i in range(1, n+1):
#     product = product * i
    
#     print(product)
    
        
#Q7

# '''
#   *
#  ***
# *****  
# '''

# n = int(input("Enter Number : "))

# for i in range(1, n+1):
#     print(" "* (n-i),end="")
#     print("*"*(2*i-1), end="")
#     print("")

# #Q8

# '''
# *
# **
# ***
# '''
# n = int(input("Enter Number : "))

# for i in range(1, n+1):
#     print("*"*i, end="")
#     print("")
    
# #Q9

# '''
# ***
# * *
# ***
# '''    
# n = int(input("Enter Number : "))

# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")  
    
#Q10
        
n = int(input("Enter Number : "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
    