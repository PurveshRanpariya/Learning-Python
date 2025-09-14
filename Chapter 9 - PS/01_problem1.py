f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content") 

f.close()

# with statement

with open("poem.txt") as f:
    c = f.read()
    if("twinkle" in c):
        print("The word twinkle is present in the content")
    else: 
        print("The word twinkle is not present in the content")   

