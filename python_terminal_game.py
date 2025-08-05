#This is a sipme text based game where a user tries to guess what a item is based on its description. 
# The user has 3 attempts to guess the item correctly. If they guess correctly, they move on to the next item. After 10 correct guesses, the game ends.


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
        Item("Elephant", "A large animal with a trunk and tusks.")
    ]

    for item in items:
        print(f"\nDescription: {item.description}")
        while player.attempts > 0:
            guess = input(f"{player.name}, what do you think this item is? (Attempts left: {player.attempts}) ")
            if player.guess(item.name, guess):
                print(f"Correct! The item is a {item.name}.")
                print(f"Your score: {player.score}")
                break
            else:
                print("Incorrect guess. Try again.")
                print(f"Your score: {player.score}")
        if player.attempts == 0:
            print(f"Sorry, you've run out of attempts. The item was a {item.name}.")
            break
        if player.score >= 10:
            print(f"Congratulations {player.name}! You've scored {player.score} points and completed the game!")
            break

main()