from copy import deepcopy
from multiprocessing.sharedctypes import Value
from random import randint
# https://docs.python.org/3/library/random.html


def test_random(iterations):
    freq = {v: 0 for v in range(1, 13)}
    for _ in range(iterations):
        freq[randint(1, 12)] += 1

    print("\n".join([f"{k}: {v}" for k, v in freq.items()]))
    print(f"Standard deviation: {std_dev(freq.values())}")


# https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step
def std_dev(data):
    mean = sum(data) / len(data)
    return (sum([(x - mean) ** 2 for x in data]) / len(data)) ** 0.5

class Character:
    def __init__(self, name, starting_items={}):
        self.name = name
        self.inventory = starting_items

    def increment_item(self, item_name, amount=1): # add amount to item
        if item_name in self.inventory:
            self.inventory[item_name] += amount
        else:
            raise ValueError("Item is not in inventory!")
        return self

    def decrement_item(self, item_name, amount=1): # remove amount from item
        if item_name not in self.inventory:
            raise ValueError("Item is not in inventory!")
        elif item_name in self.inventory and self.inventory[item_name] >= amount:
            self.inventory[item_name] -= amount
        else:
            raise ValueError("Not enough items left to decrement!")
        return self

    def add_item(self, item_name, amount=1): # add item to inventory
        if item_name in self.inventory:
            raise ValueError("Item already in inventory!")
        self.inventory[item_name] = amount
        return self

    def remove_item(self, item_name): # remove item from inventory
        if item_name not in self.inventory:
            raise ValueError("Item not in inventory!")
        del self.inventory[item_name]
        return self

    def __str__(self) -> str: # return string representation of inventory
        return f'{self.name}: {", ".join([f"{k}: {v}" for k, v in self.inventory.items()])}'


class Game:
    def __init__(self, characters=[]): # initialize game with list of characters or empty
        self.characters = characters

    def add_character(self, name, starting_items={}): # add character to game
        for c in self.characters:
            if c.name == name:
                raise ValueError("Character with that name already exists!")
        self.characters.append(Character(name, starting_items))

    def remove_character(self, name): # remove character from game
        for c in self.characters:
            if c.name == name:
                self.characters.remove(c)
                return
        raise ValueError("Character with that name does not exist!")

    def get_by_name(self, name): # return character with given name
        for c in self.characters: 
            if c.name == name:
                return c
    # https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

    def duplicate_character(self, from_name, to_name): # duplicate character with given name
        for c in self.characters:
            if c.name == from_name:
                self.characters.append(Character(to_name, deepcopy(c.inventory)))
                return
        raise ValueError("No character exists with that name in this game!")

    def print_total_counts_of_items(self): # print total counts of items in inventory
        counts = {}
        for c in self.characters:
            for i, ic in c.inventory.items():
                counts[i] = counts.get(i, 0) + ic
        print(f"Total Counts: {', '.join([f'{k}: {v}' for k, v in counts.items()])}")

    def print_all_characters(self): # print all characters in game
        for c in self.characters:
            print(c)

if __name__ == "__main__":
    game = Game()
    game.add_character("Gandolf")
    game.add_character("Frodo", {"food": 0, "kiwi": 5,
                      "wand of confusion": 7, "green potion": 8})
    game.add_character(
        "Sauron", {"bat wing": 5, "evil spell": 10, "fire wand": 5})
    game.get_by_name("Gandolf").add_item("food", 5).add_item("grapefruit", 10).add_item(
        "green potion", 7).add_item("red potion", 8).add_item("spell of enchantment", 10)
    # i think this design is good as it allows chaining methods to be called in one line
    game.duplicate_character("Frodo", "Bilbo")
    game.print_all_characters()
    game.print_total_counts_of_items()

    test_random(10000)