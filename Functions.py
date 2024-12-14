v1 = int(input("Name first value"))
v2 = int(input("Name the second value"))
v3 = int(input("Name the thrid value"))
v4 = int(input("Name the forth value"))
v5 = int(input("Name the fifth value"))

list1 = [v1, v2, v3, v4, v5]

def add_func(v1, v2, v3, v4, v5):
    return int(v1 + v2 + v3 + v4 + v5)

def avg_func(v1, v2, v3, v4, v5):
  z = (v1 + v2 + v3 + v4 + v5) / 5
  return z 

def max_func(v1, v2, v3, v4, v5):
   return max(v1, v2, v3, v4, v5)

def min_func(v1, v2, v3, v4, v5):
   return min(v1, v2, v3, v4, v5)


list1.sort()


print(f"Your values were{v1} and {v2}")
print(f"Added : {add_func(v1, v2, v3, v4, v5)}")
print(f"Average : {avg_func(v1, v2, v3, v4, v5)}")
print(f"Maximum value : {max_func(v1,v2, v3, v4, v5)}")
print(f"Minmium Value : {min_func(v1, v2, v3, v4, v5)}")
print(list1)
 