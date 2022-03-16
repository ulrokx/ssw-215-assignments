def remove_even_inds(toRemove: str) -> str:
    res=[]
    for i, v in enumerate(toRemove):
        if i % 2 == 1:
            res.append(v)
    res="".join(res)
    print(res)
    return res
remove_even_inds("Individual software engineering")
