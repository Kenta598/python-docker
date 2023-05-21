A,B = map(int,input().split())

def kill(A,B):
    count = (A + B - 1)//B #切り上げ
    return count

print(kill(A,B))