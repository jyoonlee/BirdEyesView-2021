def sync(b):
    global a
    if a == b:
        print("{} {}".format(a, b))
        return None
    dif = abs(a - b)
    i = max(a, b) // dif

    if a>b:
     b = max(a, b) - i
    sync(a, b)


a, b = map(int, input().split())

if a == b:
    print("Videos have same FPS")
elif max(a, b) % abs(a - b) == 0:
    a = min(a, b)
    b = max(a, b) - abs(a - b)
    print("{} {}".format(a, b))
else:
    sync(b)
