class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n # Adding two objects

n = Number(1) # Creating object of Number class
m = Number(2) # Creating object of Number class


print(n + m)

