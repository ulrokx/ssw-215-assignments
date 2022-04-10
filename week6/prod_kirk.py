def prod_len_name(fname: str, lname: str) -> int:
    res = len(fname) * len(lname)
    print(f"The product of the value of the lengths of my firstname and lastname is {res}.")
    return res
prod_len_name("Richard", "Kirk")