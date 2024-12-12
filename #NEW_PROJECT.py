#NEW_PROJECT

print('''
            a1 ,a2 ,a3       x1, x2, x3 
            b1, b2, b3       y1, y2, y3
            c1, c2, c3       z1, z2, z3    
''')

a1 = int(input("Enter Value a1 : "))
a2 = int(input("Enter Value a2 : "))
a3 = int(input("Enter Value a3 : "))
b1 = int(input("Enter Value b1 : "))
b2 = int(input("Enter Value b2 : "))
b3 = int(input("Enter Value b3 : "))
c1 = int(input("Enter Value c1 : "))
c2 = int(input("Enter Value c2 : "))
c3 = int(input("Enter Value c3 : "))

x1 = int(input("Enter Value x1 : ")) 
x2 = int(input("Enter Value x2 : ")) 
x3 = int(input("Enter Value x3 : "))
y1 = int(input("Enter Value y1 : "))
y2 = int(input("Enter Value y2 : "))
y3 = int(input("Enter Value y3 : "))
z1 = int(input("Enter Value z1 : "))
z2 = int(input("Enter Value z2 : "))
z3 = int(input("Enter Value z3 : "))

print(f"""
{a1} / {a2} / {a3}     {x1} / {x2} / {x3}
{b1} / {b2} / {b3}     {y1} / {y2} / {y3}
{c1} / {c2} / {c3}     {z1} / {z2} / {z3}
""")

lista = (a1,a2,a3)
listb = (b1,b2,b3)
listc = (c1,c2,c3)

listd = (x1,y1,z1)
liste = (x2,y2,z2)
listf = (x3,y3,z3)

resultp1 = []
resultp2 = []
resultp3 = []
resultr1 = []
resultr2 = []
resultr3 = []
resultq1 = []
resultq2 = []
resultq3 = []

for i in range(len(lista)):
   resultp1.append(lista[i] * listd[i])

for i in range(len(lista)):
   resultp2.append(lista[i] * liste[i])

for i in range(len(lista)):
   resultp3.append(lista[i] * listf[i])

for i in range(len(listb)):
   resultr1.append(listb[i] * listd[i])

for i in range(len(listb)):
   resultr2.append(listb[i] * liste[i])

for i in range(len(listb)):
   resultr3.append(listb[1] * listf[i])

for i in range(len(listc)):
   resultq1.append(listc[i] * listd[i])

for i in range(len(listc)):
   resultq2.append(listc[i] * liste[i])

for i in range(len(listc)):
   resultq3.append(listc[1] * listf[i])

print (f"""{(sum(resultp1))} / {(sum(resultp2))}  / {(sum(resultp3))}
{(sum(resultr1))} / {(sum(resultr2))}  / {(sum(resultr3))}
{(sum(resultq1))} / {(sum(resultq2))}  / {(sum(resultq3))}""")
