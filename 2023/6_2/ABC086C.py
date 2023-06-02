N = int(input())
Travel = [list(map(int,input().split())) for _ in range(N)]

t = 0
x = 0
y = 0
flag = True

def between(x,y,x_pre,y_pre):
    return abs(x - x_pre) + abs(y-y_pre)

for i in Travel:
    t_step = i[0] - t
    t_need = between(i[1],i[2],x,y)
    if (t_need - t_step <= 0) and ((t_need - t_step)%2 == 0):
        t = i[0]
        x = i[1]
        y = i[2]
        continue
    else:
        flag = False
        break

print("Yes" if flag else "No")