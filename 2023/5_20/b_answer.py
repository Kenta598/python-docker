H,W = map(int,input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)
 
prefix = "snuke"
X = [-1,0,1]
Y = [-1,0,1]
detect = False
for j in range(H):
    for k in range(W):
        if S[j][k] != prefix[0]:
            continue
        for x in X:
            for y in Y:
                ans = "s"
                ind = [[j + 1, k + 1]]
                for p in range(1,5):
                    x_n, y_n = j + p*x, k + p*y
                    if W > y_n >= 0 and H > x_n >= 0 and S[x_n][y_n] == prefix[p]:
                        ind.append([x_n+1,y_n+1])
                        ans += S[x_n][y_n]
                    else:
                        break
                if ans == prefix:
                    detect = True
                    break
            if detect:
                break
        if detect:
            break
    if detect:
        break
                   
for e in ind:
    print(*e)