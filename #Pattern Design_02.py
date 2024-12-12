#Pattern Design_01
x = str("*")
i = 0
y = int(input("How many times do u need to repeat this command?"))
n = (y - 1)
s = (" ")


while i < y:
    print((n * s) + x)
    x = x + "**"
    i = i + 1
    n = n - 1


