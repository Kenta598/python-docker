H, W = map(int,input().split())
S = [list(input()) for i in range(H)]

print(H)
print(W)
print(S[0][1])

def check_s(H, W, S):
    for i in range(H):
        for j in range(W):
            if S[i][j] == 's':
                i_pre1, j_pre1 = check_next(S,i,j,'n')
                if (i_pre1 == 0 and j_pre1 == 0):
                    continue
                i_pre2, j_pre2 = check_next(S,i_pre1,j_pre1,'u')
                if (i_pre2 == 0 and j_pre2 == 0):
                    continue
                i_pre3, j_pre3 = check_next(S,i_pre2,j_pre2,'k')
                if (i_pre3 == 0 and j_pre3 == 0):
                    continue
                i_pre4, j_pre4 = check_next(S,i_pre3,j_pre3,'e')
                if (i_pre4 != 0) and (j_pre3 != 0):
                    return i_pre1, j_pre1, i_pre2, j_pre2, i_pre3, j_pre3, i_pre4, j_pre4
                else:
                    continue


def check_next(S,i,j,s):
    try:
        if S[i-1][j] == s:
            return i-1, j
        elif S[i-1][i-1] == s:
            return i-1, j+1
        elif S[i-1][i+1] == s:
            return i-1, i+1   
        elif S[i][j-1] == s:
            return i, j-1
        elif S[i][j+1] == s:
            return i, j+1
        elif S[i+1][i+1] == s:
            return i+1, i+1
        elif S[i+1][i-1] == s:
            return i+1, i-1
        elif S[i+1][j] == s:
            return i+1, j
        else:
            return 0, 0
    except:
        return 0, 0
    
print(check_s(H,W,S))