#List Comprehensions 
result=[]
x = int(input("First line: ...  "))
y = int(input("Second line: ...  "))
z = int(input("Third line: ...  "))
n = int(input("N line: ...  "))
for i in range(0, x+1):
    for t in range(0, y+1):
        for l in range(0, z+1):
            if i+t+l == n:
                continue
            else:
                result.append([i, t, l])
print(result)
result2 =[ (a, b, c) for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c!=n]
print(result2)
#List Comprehensions
result=[]