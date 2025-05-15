import random

p1Score = 0
p2Score = 0
play = True
player_1_deals = False
player_1_off = True

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


def p2_choose_trump(option, open_choice):#open_choice is true if you can choose any suit, pick_up is true if p2 would have to pick up the card
    global trump
    p2suits = []
    for botsdsd in p2Hand:
        p2suits.append(botsdsd.suit)
    if p2suits.count(option.suit) >= 2:
        return True


def p2_discard():
    pass


def choose_trump(start):#start is true if P2 deals, returns true if player one is offense and false if player two is offense
    global trump, reset, p1Hand, p2Hand
    crd = deck.pop()
    print(crd)
    if start:
        if input("P1, do you want the trump card?(y/n)") == "y":
            p1Hand.pop(int(input("P1, what card do you want to clear?(Write the index of the card in your hand) ")))
            p1Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return True
        elif p2_choose_trump(crd, False):
            p1Hand.pop(int(input("P2 has taken offense. P1, what card do you want to clear?(Write the index of the card in your hand) ")))
            p1Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return False
        elif input("P1, do you want to choose trump suit?(y/n)") == "y":
            trump = card(input("What suit? "), 0)
            reset = False
            return True
        elif p2_choose_trump(crd, True):
            trump = card(input("What suit? "), 0)
            reset = False
            return False
        else:
            print("Replaying hand")
            return True
    else:
        if p2_choose_trump(crd, False):
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
        elif p2_choose_trump(crd, True):
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


def win(player1card, player2card, lead):#Lead is true when P1 leads, returns true if p1 wins
    ranks = ["9", "10", "Jack", "Queen", "King", "Ace"]
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
        elif ranks.index(player1card.rank) > ranks.index(player2card.rank):
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
        elif ranks.index(player2card.rank) > ranks.index(player1card.rank):
            return False
        else:
            return True


def score(p1_tricks, p2_tricks, p1_off):#adds score to correct players score(logic needed)
    global p1Score, p2Score
    pass


def choose_card(p1card, do_lead):#do_lead is true if p2 leads and therefore ignores the p1card input which should be null
    global p2Hand
    chosen_card = p2Hand.pop(0)#logic needed
    return chosen_card


# while True:
#     global deck
#     shuffle()
#     for x in deck:
#         print(x)
round=0
while play:
    global trump, reset, p1Hand, p2Hand
    round+=1
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
    print(f"Round {round}, current score: P1: {p1Score} - P2: {p2Score}, Player one to lead: {player_1_off}")
    player_1_tricks = 0
    player_2_tricks = 0
    player_1_lead = player_1_off
    while len(p1Hand) > 0:
        if player_1_lead:
            p1input = int(input("P1, what card do you want to play?(Write the index of the card in your hand) "))
            p1card = p1Hand[p1input]
            p2card = choose_card(p1card, False)
        else:
            p2card = choose_card(card, True)
            print(f"P2 plays the {p2card}")
            p1input = int(input("P1, what card do you want to play?(Write the index of the card in your hand) "))
            p1card = p1Hand[p1input]
            p1Suits = []
            for suity in p1Hand:
                p1Suits.append(suity.suit)
            while (p1card.suit != p2card.suit and p2card.suit in p1Suits) or (p2card.rank == "Jack" and p2card.suit != trump.suit and p2card.color == trump.color and p1card.suit == trump.suit):
                print("Not a valid play.")
                p1input = int(input("P1, what card do you want to play?(Write the index of the card in your hand) "))
                p1card = p1Hand[p1input]
        if win(p1Hand.pop(p1input), p2card, player_1_lead):
            player_1_tricks+=1
            player_1_lead = True
            print(f"P1 wins the trick, {p1card} vs {p2card}. Trump is {trump.suit}. The score is now P1: {p1Score} - P2: {p2Score}")
        else:
            player_2_tricks += 1
            player_1_lead = False
            print(f"P2 wins the trick, {p2card} vs {p1card}. Trump is {trump.suit}. The score is now P1: {p1Score} - P2: {p2Score}")
    if player_1_off:
        if player_2_tricks >=3:
            p2Score +=2
        elif player_1_tricks == 5:
            p1Score += 2
        else:
            p1Score += 1
    else:
        if player_1_tricks >=3:
            p1Score += 2
        elif player_2_tricks == 5:
            p2Score += 2
        else:
            p2Score += 1
    if p1Score >= 10:
        print(f"Player one wins. Final Score: {p1Score} - {p2Score}")
        play = False
    if p2Score >= 10:
        print(f"Player two wins. Final Score: {p2Score} - {p1Score}")
        play = False

