n = int(input("Enter a number: "))


#List comprehension method
table = [n*i for i in range(1, 11)]
print(table)

#Normal method 
list = []
for i in range(1, 11):
   list.append(n*i)
print(list)


#for Question 5
f = open("tables.txt", "a")
f.write(f"Table of {n}: {str(table)} \n")
f.close()