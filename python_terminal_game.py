#This is a sipme text based game where a user tries to guess what a item is based on its description. 
# The user has 3 attempts to guess the item correctly. If they guess correctly, they move on to the next item. After 10 correct guesses, the game ends.
import random

# A player class to manage player attributes and actions
class Player:
    def __init__(self, name):
        self.name = name
        self.attempts = 3
        self.score = 0

    def guess(self, item, guess):
        if guess.lower() == item.lower():
            self.score += 1
            return True
        else:
            self.attempts -= 1
            self.score -= 1 if self.score > 0 else 0
            return False


# An item class to represent items with a name and description
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    items = [
    Item("Apple", "A round fruit that is red or green."),
    Item("Banana", "A long yellow fruit that monkeys love."),
    Item("Carrot", "An orange vegetable that bunnies eat."),
    Item("Dog", "A loyal pet that barks."),
    Item("Elephant", "A large animal with a trunk and tusks."),
    Item("Flashlight", "A handheld device that helps you see in the dark."),
    Item("Sword", "A sharp blade used by warriors."),
    Item("Book", "A collection of pages filled with knowledge or stories."),
    Item("Map", "A piece of paper that shows the layout of the land."),
    Item("Potion", "A magical liquid that restores health or grants powers."),
    Item("Key", "A small metal object used to unlock doors."),
    Item("Backpack", "A container you wear on your back to carry items."),
    Item("Rock", "A small, heavy object that could be thrown."),
    Item("Lantern", "A light source powered by oil or magic."),
    Item("Coin", "A shiny piece of currency made of metal."),
    Item("Helmet", "A protective head covering, useful in battle."),
    Item("Scroll", "An old piece of parchment with mysterious writing."),
    Item("Rope", "A sturdy length of fiber, useful for climbing or tying."),
    Item("Gem", "A rare and shiny stone that sparkles in the light."),
    Item("Boots", "Worn on your feet for protection and style."),
    Item("Shield", "A defensive tool used to block attacks."),
    Item("Tent", "Shelter for resting while adventuring outdoors."),
    Item("Water Bottle", "A container filled with fresh drinking water."),
    Item("Matches", "Small sticks used to start a fire."),
    Item("Camera", "A device used to capture memories or spy on enemies."),
    Item("Magic Ring", "A mysterious ring rumored to hold ancient power."),
    Item("Compass", "A device that helps you find your way by pointing north."),
    Item("Gloves", "Hand coverings that provide warmth and grip."),
    Item("Binoculars", "A tool that helps you see distant objects clearly."),
    Item("Fishing Rod", "A long stick with a line used to catch fish.")
    ]

    random.shuffle(items)  # Shuffle items to randomize the order

    for item in items:
        print(f"\nDescription: {item.description}")
        while player.attempts > 0:
            guess = input(f"{player.name}, what do you think this item is? (Attempts left: {player.attempts}) ")
            if player.guess(item.name, guess): # Check if the guess is correct
                print(f"Correct! The item is a {item.name}.")
                print(f"Your score: {player.score}")
                break
            else: # If the guess is incorrect, reduce attempts and score
                print("Incorrect guess. Try again.")
                print(f"Your score: {player.score}")
        if player.attempts == 0: # If the player runs out of attempts, the game ends
            print(f"Sorry, you've run out of attempts. The item was a {item.name}.")
            break
        if player.score >= 10: #If the player reaches a score of 10, they win the game
            print(f"Congratulations {player.name}! You've scored {player.score} points and completed the game!")
            break

main()