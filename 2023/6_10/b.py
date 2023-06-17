p, q = input().split()

def replace(str):
    if str == 'A':
        return 0
    elif str == 'B':
        return 1
    elif str == 'C':
        return 2
    elif str == 'D':
        return 3
    elif str == 'E':
        return 4
    elif str == 'F':
        return 5
    else:
        return 6
    
dis = [3,1,4,1,5,9,0]
if replace(p) > replace(q):
    ind_start = replace(q)
    ind_finish = replace(p)
else:
    ind_start = replace(p)
    ind_finish = replace(q)
result = 0

for i in range(ind_start,ind_finish,1):
    result += dis[i]

print(result)