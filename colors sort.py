input=[["R",1],["R",5],["B",4],["G",6],["B",6],["R",9],
       ["R",6],["R",12],["B",14],["G",16],["B",7],["R",11]]
print("Given input")
print(input)

for i in input:
    input.sort()

second=input
sec=[]
thi=[]
for i in second:
    if "R"  in i[0]:
        sec.append(i)

for j in second:
    if "R" not in j[0]:
        thi.append(j)

for i in thi:
    sec.append(i)
print("\nSorted colours output")
print(sec)



