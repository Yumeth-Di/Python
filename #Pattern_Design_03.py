#Pattern_Design_03
x = ("*")
y = int(input("How much stars do u need in a row?"))
z = y
n = int(0)
i  = 0


while n < y:
    x = x + "*"
    n = n + 1

while i < z :
    print(x)
    i = i + 1