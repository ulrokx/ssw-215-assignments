def div7not5():
    res = []
    for i in range(2002, 3200, 7):
        if i % 5 != 0:
            res.append(i)
    return res
print(div7not5())