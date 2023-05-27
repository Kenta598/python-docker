N = int(input())
S = list(input())
T = list(input())

def similar(N,S,T):
    for i in range(N):
        if (S[i] == '0' and T[i] == 'o') or (S[i] == 'o' and T[i] == '0'):
            continue
        elif (S[i] == 'l' and T[i] == '1') or (S[i] == '1' and T[i] == 'l'):
            continue
        elif S[i] == T[i]:
            continue
        else:
            return False
    return True

print('Yes' if similar(N,S,T) else 'No')