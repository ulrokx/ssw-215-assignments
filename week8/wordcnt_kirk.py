def word_count(filename):
    with open(filename) as file:
        content = file.read()
    words = len(content.split())
    print(f"The file {filename} has about {words} words.")
    return words
print(word_count("alice.txt"))