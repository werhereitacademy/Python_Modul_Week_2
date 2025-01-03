'''
#Hackerrank Solution 1
print( [ [i, j, k] for i in list(range(0, x+1)) for j in list(range(0, y+1)) for k in list(range(0, z+1)) if i + j + k != n] )

#Hackerrank Solution 2

 n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(hash(t))
'''

