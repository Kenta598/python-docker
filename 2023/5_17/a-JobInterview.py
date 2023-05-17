n = map(int,input())
s = input()

def is_ok():
    if (s.find('o') != -1) and (s.find('x') == -1):
        return True
    else:
        False

print('Yes' if is_ok() else 'No')