def squares(val, start = 0):
    if start*start > val:
        return []
    else:
        return [start*start, *squares(val, start + 1)]

print(squares(10000))