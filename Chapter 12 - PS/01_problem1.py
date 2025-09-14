
try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
    
    
    
try:
    f = open("4.txt" , "r")
    print(f.read())
except Exception as e:
    print(e)    
finally:
    print("No file name with 4.txt are their")        


print("Thank You!")


#Question 2
# my_list = [1, 2, 3, 4, 5, 7, 6, 90]
# for index, item in enumerate(my_list):
#    if(index == 2 or index == 4 or index == 6):          
#     print(item)  
    
