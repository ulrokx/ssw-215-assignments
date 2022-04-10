def max_name_len(fname: str, lname: str) -> int:
    res = max(len(fname), len(lname))
    print(f"The largest value of the length of my firstname and lastname is {res}.")
    return res
max_name_len("Richard", "Kirk")