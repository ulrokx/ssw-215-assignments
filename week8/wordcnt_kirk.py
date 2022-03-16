def word_count(filename):
    with open(filename) as file:
        content = file.read()
    return len(content.split())
print(word_count("alice.txt"))