st = "Hey Harry you are amazing \n"
st2 = "Hey Purvesh ypu are hendsom" 

f = open("myfile.txt", "w")

f.write(st)
f.write(st2)

f.close()

a = open("myfile.txt")
print(a.read())
a.close()