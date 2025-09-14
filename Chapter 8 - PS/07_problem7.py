# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l
    

# l = ["Harry" , "an" , "purvesh"]
# print(rem(l, "an"))



# def rem(l, word):
#     n = [] 
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l = ["Harry", "Rohan", "Shubham", "an"]

# print(rem(l, "an"))


def mulTable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
        
mulTable(5)        
    
    