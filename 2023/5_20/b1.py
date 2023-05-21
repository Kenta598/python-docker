H, W = map(int,input().split())
S = [list(input()) for i in range(H)]
s_i = []
s_j = []
n_i = []
n_j = []
u_i = []
u_j = []
k_i = []
k_j = []
e_i = []
e_j = []

print(S[1][5])

def check(H, W, S):
    for i in range(H):
        for j in range(W):
            if S[i][j] == 's':
                print("a")
                s_i.append(i)
                s_j.append(j)
            if S[i][j] == 'n':
                n_i.append(i)
                n_j.append(j)
            if S[i][j] == 'u':
                u_i.append(i)
                u_j.append(j)
            if S[i][j] == 'k':
                k_i.append(i)
                k_j.append(j)
            if S[i][j] == 'e':
                e_i.append(i)
                e_j.append(j)

def snuke(snuke):
    s_len = len(s_i)
    n_len = len(n_i)
    u_len = len(u_i)
    k_len = len(k_i)
    e_len = len(e_i)
    for i in range(s_len):
        for j in range(n_len):
            if (i == j+1) or (i == j-1) or (i+1 = j) or (i-1 = j):
                for u in range(u_len):
                    if (u == )
