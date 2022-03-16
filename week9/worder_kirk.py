def word_order(string):
    words = list(set(string.split(", ")))
    words.sort()
    print(", ".join(words))
word_order("apple, mango, carrot, apple, orange, mango, berry")
