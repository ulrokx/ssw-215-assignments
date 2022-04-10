# Richard Kirk SSW-215
# I pledge my honor that I have abided by the Stevens Honor System
# Resources:
#   https://docs.python.org/3/library/typing.html

from typing import Dict, List, Tuple
fruits: str
try:
    raw = open("fruits.txt", "rt")
    fruits = raw.read()
    raw.close()
    fruits = fruits[1:-1]  # Get rid of beginning and ending quotation marks
except IOError:
    fruits = "Mango banana apple pear Banana grapes strawberry Apple pear mango banana Kiwi apple mango strawberry"


def char_index(string: str) -> List[int]:
    """Returns the index values of each occurance of the character 'r'"""
    res = []
    for i, v in enumerate(string):
        if v == 'r':
            res.append(i)
    print(
        f"This  index  values  of  each  occurrences  of character ‘r’ in the string are {res}")
    return res


def count_vc(string: str) -> Tuple[int, int]:
    """Returns the tuple with the number of vowels and consonants in the given string"""
    vowels = consonants = 0
    for v in string:
        if v in "aeiou":
            vowels += 1
        else:
            consonants += 1
    print(
        f"There are {vowels} vowels and {consonants} consonants in your string.")
    return (vowels, consonants)

def count_vowels(string: str) -> Dict[str, int]:
    """Returns a dictionary with the counts of each vowel in the given string"""
    hm = {}
    for v in string:
        if v in "aeiou":
            hm[v] = hm[v] + 1 if v in hm else 1
    print(f"Vowel counts: {', '.join(f'{k.upper()} - {hm[k]}' for k in hm)}")
    return hm


def alternate_case(string: str) -> str:
    """Returns the given string with character cases inverted"""
    res = "".join(c.lower() if c.isupper() else c.upper() for c in string)
    print(res)
    return res


char_index(fruits)
count_vc(fruits)
count_vowels(fruits)
alternate_case(fruits)
