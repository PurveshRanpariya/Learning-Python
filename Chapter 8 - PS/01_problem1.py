def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = 1
b = 23
c = 3

print(greatest(a, b, c))


def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Eneter Temp in F :"))
c = f_to_c(f)
print(f"{round(c, 2)} degree c")


#Q6
def i_to_c(i):
    return i*2.54
i = int(input("Enter inches: "))
c = i_to_c(i)
print(f"{c} cm")
    


    