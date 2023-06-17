H, W = map(int,input().split())
S = [list(input().split()) for _ in range(H)]

a = 501
b = -1
c = 501
d = -1

for i in range(H):
    j_sta = str(S[i]).find('#')
    j_fin = str(S[i]).rfind('#')
    if j_sta != -1:
        a = min(a,i)
        b = max(b,i)
        c = min(c,j_sta-2)
        d = max(d,j_fin-2)
    else:
        continue

for i in range(a,b+1,1):
    S_ls = list(str(S[i][0]))
    for j in range(c,d+1,1):
        if S_ls[j] != '#':
            print('{} {}'.format(i+1,j+1))
        else:
            continue