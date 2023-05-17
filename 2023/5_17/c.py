n = map(int, input())
s = list(input())

dangolen = -1
buf = 0

for c in s:
    if c == "o":
        buf += 1
    elif (buf > 0) and (c == "-"):
        dangolen = max(dangolen, buf)
        buf = 0

s.reverse()
buf = 0

for c in s:
    if c == "o":
        buf += 1
    elif (buf > 0) and (c == "-"):
        dangolen = max(dangolen, buf)
        buf = 0

print(dangolen)