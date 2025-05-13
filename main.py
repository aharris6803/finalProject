import random

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(suit, rank)


p1Hand = []
p2Hand = []
trump = ""

p1Score = 0
p2Score = 0
play = True

def shuffle():
    for x in range(1000):
        deck.append(deck.pop(random.randint(0, len(deck)-1)))
    return deck


def deal(start):#true if it's player 2 dealing, false if it's player one to deal
    if start:
        for x in range(3):
            p1Hand.append(deck.pop())
        for x in range(2):
            p2Hand.append(deck.pop())
        for x in range(2):
            p1Hand.append(deck.pop())
        for x in range(3):
            p2Hand.append(deck.pop())
    else:
        for x in range(3):
            p2Hand.append(deck.pop())
        for x in range(2):
            p1Hand.append(deck.pop())
        for x in range(2):
            p2Hand.append(deck.pop())
        for x in range(3):
            p1Hand.append(deck.pop())

def trump(start):
    card = deck.pop()
    print(card)
    if input("P1, do you want the trump card?(Y/N)") == "Y":
        p1Hand.remove(input("What card do you want to clear?"))
        p1Hand.append(card)
        trump = card.
        return True
    elif input("P2, do you want the trump card?(Y/N)") == "Y":
        p2Hand.remove(input("What card do you want to clear?"))
        p2Hand.append(card)
        return False
    elif input("P1, do you want to choose trump suit?(Y/N)") == "Y":




while play:
    if p1Score>=10:
        play=False
        print(f"P1 wins. Final score: {p1Score}-{p2Score}")
        continue
    if p2Score>=10:
        play=False
        print(f"P2 wins. Final score: {p2Score}-{p1Score}")
        continue
    deck = shuffle()
    trump(True)