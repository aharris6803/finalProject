import random

from sympy import false


class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if self.suit == "Diamonds" or self.suit == "Hearts":
            self.color = "Red"
        else:
            self.color = "Black"
    def __str__(self):
        return self.rank + " of " + self.suit

p1Score = 0
p2Score = 0
play = True
player_1_deals = False
player_1_off = True


def shuffle():
    global deck
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
    deck = []
    tempdeck = []
    for suit in suits:
        for rank in ranks:
            tempdeck.append(card(suit, rank))
    for x in range(1000):
        tempdeck.append(tempdeck.pop(random.randint(0, len(tempdeck)-1)))
    deck = tempdeck


def deal(start):#true if it's player 2 dealing, false if it's player one to deal
    global p1Hand, p2Hand
    p1Hand = []
    p2Hand = []
    if start:
        for x in range(3):
            p2Hand.append(deck.pop())
        for x in range(2):
            p1Hand.append(deck.pop())
        for x in range(2):
            p2Hand.append(deck.pop())
        for x in range(3):
            p1Hand.append(deck.pop())
    else:
        for x in range(3):
            p1Hand.append(deck.pop())
        for x in range(2):
            p2Hand.append(deck.pop())
        for x in range(2):
            p1Hand.append(deck.pop())
        for x in range(3):
            p2Hand.append(deck.pop())

def choose_trump(start):
    global trump, reset, p1Hand, p2Hand
    crd = deck.pop()
    print(crd)
    if start:
        if input("P1, do you want the trump card?(y/n)") == "y":
            p1Hand.pop(int(input("What card do you want to clear?(Write the index of the card in your hand) ")))
            p1Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return True
        elif input("P2, do you want the trump card?(y/n)") == "y":
            p1Hand.pop(int(input("P1, what card do you want to clear?(Write the index of the card in your hand) ")))
            p1Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return False
        elif input("P1, do you want to choose trump suit?(y/n)") == "y":
            trump = card(input("What suit? "), 0)
            reset = False
            return True
        elif input("P2, do you want to choose trump suit?(y/n)") == "y":
            trump = card(input("What suit? "), 0)
            reset = False
            return False
        else:
            print("Replaying hand")
            return True
    else:
        if input("P2, do you want the trump card?(y/n)") == "y":
            p2Hand.pop(int(input("What card do you want to clear?(Write the index of the card in your hand) ")))
            p2Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return False
        elif input("P1, do you want the trump card?(y/n)") == "y":
            p2Hand.pop(int(input("P1, what card do you want to clear?(Write the index of the card in your hand) ")))
            p2Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return True
        elif input("P2, do you want to choose trump suit?(y/n)") == "y":
            trump = card(input("What suit? "), 0)
            reset = False
            return False
        elif input("P1, do you want to choose trump suit?(y/n)") == "y":
            trump = card(input("What suit? "), 0)
            reset = False
            return True
        else:
            print("Replaying hand")
            return True

def win(player1card, player2card, lead):
    suits = ["9", "10", "Jack", "Queen", "King", "Ace"]
    if lead:
        if player1card.suit == trump.suit and player1card.rank == "Jack":
            return True
        elif player1card.rank == "Jack" and trump.color == player1card.color:
            if player2card.suit == trump.suit and player2card.rank == "Jack":
                return False
            else:
                return True
        elif player1card.suit != player2card.suit:
            if player2card.suit == trump.suit:
                return False
            else:
                return True
        elif suits.index(player1card.rank) > suits.index(player2card.rank):
            return True
        else:
            return False
    else:
        if player2card.suit == trump.suit and player2card.rank == "Jack":
            return False
        elif player2card.rank == "Jack" and trump.color == player2card.color:
            if player1card.suit == trump.suit and player1card.rank == "Jack":
                return True
            else:
                return False
        elif player2card.suit != player1card.suit:
            if player1card.suit == trump.suit:
                return True
            else:
                return False
        elif suits.index(player2card.rank) > suits.index(player1card.rank):
            return False
        else:
            return True



# while True:
#     global deck
#     shuffle()
#     for x in deck:
#         print(x)
while play:
    global trump, reset, p1Hand, p2Hand
    reset = True
    if p1Score>=10:
        play=False
        print(f"P1 wins. Final score: {p1Score}-{p2Score}")
        continue
    if p2Score>=10:
        play=False
        print(f"P2 wins. Final score: {p2Score}-{p1Score}")
        continue
    shuffle()
    deal(player_1_deals)
    print("Player 1 hand")
    print("{")
    for x in p1Hand:
        print(x)
    print("}")
    while reset:
        player_1_off = choose_trump(True)
    reset = False
    print("Player 1 hand ")
    print("{")
    for x in p1Hand:
        print(x)
    print("}")