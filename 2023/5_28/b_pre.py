a, b = map(int, input().split())

def check():
    if (a*b)%2 == 0:
        return True
    else:
        return False

print("Even" if check() else "Odd") 