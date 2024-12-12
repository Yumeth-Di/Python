#Pattern Design
x = ("*")
i = 0
y = int(input("How many times do u need to repeat this command?"))

while i < y:
    print(x)
    x = x + "*"
    i = i + 1
