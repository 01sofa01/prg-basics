def f(uid):
    for name in range(len(uid)):
        if (uid.pop() in uid):
            return False
    return True

print(f(["jik","uiop","jik"]))