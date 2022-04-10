import re
def alice_prog(filename, *, cutoff = 1):
    with open(filename, "r") as file:
        text = file.read() # open file and read it
    words = text.split() # split text into words
    # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    nonwords = re.compile('[\W_]+') # regex to remove non-alphanumeric characters
    words = [nonwords.sub('', word).lower() for word in words] # remove non-alphanumeric characters and lowercase
    wordsOver5  = {}  # create empty dictionary
    for word in words:
        if len(word) > 5:# add word to dictionary if it is over 5 characters long
            wordsOver5[word] = wordsOver5.get(word, 0) + 1
    wordsOver5 = sorted(wordsOver5.items(), key=lambda x: x[1], reverse=True) # sort dictionary by value (frequency) and reverse it (highest frequency first)
    for word, count in wordsOver5:
        if count >= cutoff:
            print(word, ": ", count, sep="", end="\n") # print word and frequency
    return wordsOver5
alice_prog("alice.txt", cutoff=5)
