s = list(input())

def count():
    count = 0
    for i in s:
        if i == "1":
            count += 1
    return count

print(count())