import random

p1Score = 0
p2Score = 0
play = True
player_2_deals = True
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
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "King", "Queen", "Jack", "10", "9"]
    deck = []
    tempdeck = []
    for suit in suits:
        for rank in ranks:
            tempdeck.append(card(suit, rank))
    for x in range(1000):
        tempdeck.append(tempdeck.pop(random.randint(0, len(tempdeck)-1)))
    deck = tempdeck


def deal(start):#True if it's player 2 dealing, false if it's player 1 to deal
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


def p2choosetrump(option, open_choice):#open_choice is true if you can choose any suit, pick_up is true if p2 would have to pick up the card
    global trump, p2suits
    p2suits = []
    for botsdsd in p2Hand:
        p2suits.append(botsdsd.suit)
    if not open_choice:
        if p2suits.count(option.suit) >= 2:
            return True
    else:
        if p2suits.count(mostcommon(p2suits)) > 2:
            return True
    return False


def p2sorthand():#should sort p2hand by how good the cards are
    global p2Hand
    p2Hand.sort(key=forsort)


def forsort(inputcard):
    overallrank = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    suits.remove(trump.suit)
    ranks = ["Ace", "King", "Queen", "Jack", "10", "9"]
    overallrank.append(card(trump.suit, "Jack"))
    if trump.suit == "Diamonds":
        overallrank.append(card("Hearts", "Jack"))
    elif trump.suit == "Hearts":
        overallrank.append(card("Diamonds", "Jack"))
    elif trump.suit == "Clubs":
        overallrank.append(card("Spades", "Jack"))
    elif trump.suit == "Spades":
        overallrank.append(card("Clubs", "Jack"))
    for rank in ranks:
        if not rank == "Jack":
            overallrank.append(card(trump.suit, rank))
    for suit in suits:
        for rank in ranks:
            if not (rank == overallrank[1].rank and suit == overallrank[1].suit):
                overallrank.append(card(suit, rank))
    x = 0
    for goodcard in overallrank:
        if goodcard.__str__() == inputcard.__str__():
            return x
        x+=1


def mostcommon(lst):
    return max(set(lst), key=lst.count)


def choosetrump(start):#start is true if P2 deals, returns true if player one is offense and false if player two is offense
    global trump, reset, p1Hand, p2Hand
    crd = deck.pop()
    print(f"The possible trump is the {crd}")
    if start:
        if input("Do you want the trump card?(y/n)") == "y":
            p1Hand.pop(int(input("What card do you want to discard?(Write the index of the card in your hand) ")))
            p1Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return True
        elif p2choosetrump(crd, False):
            trump = card(crd.suit, 0)
            p2sorthand()
            p2Hand.pop(4)
            p1Hand.append(crd)
            reset = False
            return False
        elif input("Do you want to choose trump suit?(y/n)") == "y":
            trump = card(input("What suit? "), 0)
            reset = False
            return True
        elif p2choosetrump(crd, True):
            trump = card(mostcommon(p2suits), 0)
            print(f"P2 chooses {trump.suit} as the suit")
            reset = False
            return False
        else:
            print("Replaying hand")
            return True
    else:
        if p2choosetrump(crd, False):
            p2Hand.pop(int(input("What card do you want to clear?(Write the index of the card in your hand) ")))
            p2Hand.append(crd)
            trump = card(crd.suit, 0)
            reset = False
            return False
        elif input("P2 has passed, do you want the trump card?(y/n)") == "y":
            trump = card(crd.suit, 0)
            p2sorthand()
            p2Hand.pop(4)
            p2Hand.append(crd)
            reset = False
            return True
        elif p2choosetrump(crd, True):
            trump = card(mostcommon(p2suits), 0)
            print(f"P2 has chosen {trump.suit}")
            reset = False
            return False
        elif input("Do you want to choose trump suit?(y/n)") == "y":
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


def choosecard(p1card, do_lead):#do_lead is true if p2 leads and therefore ignores the p1card input which should be null
    global p2Hand
    if not do_lead:
        if returnlegal(p1card) != []:
            legal = returnlegal(p1card)
            if not win(p1card, legal[0], True):
                return p2Hand.index(legal[0])
            else:
                return len(p2Hand)-1
        else:
            return len(p2Hand)-1
    else:
        return 0


def returnlegal(leadcard):
    legalhand = []
    for mamds in p2Hand:
        if mamds.suit == leadcard.suit:
            legalhand.append(mamds)
        if mamds.suit != trump.suit and mamds.color == trump.color and mamds.rank == "Jack":
            legalhand.append(mamds)
    return legalhand


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
    print(f"Round {round}, current score: P1: {p1Score} - P2: {p2Score}, Player one to lead: {player_1_off}")
    shuffle()
    deal(player_2_deals)
    print("Player 1 hand")
    print("{")
    for x in p1Hand:
        print(x)
    print("}")
    while reset:
        player_1_off = choosetrump(player_2_deals)
    reset = True
    p2sorthand()
    print("Player 1 hand ")
    print("{")
    for x in p1Hand:
        print(x)
    print("}")
    player_1_tricks = 0
    player_2_tricks = 0
    player_1_lead = player_1_off
    while len(p1Hand) > 0:
        if player_1_lead:
            p1input = int(input("What card do you want to play?(Write the index of the card in your hand) "))
            p1card = p1Hand[p1input]
            p2card = p2Hand[choosecard(p1card, False)]
            p2Hand.remove(p2card)
        else:
            p2card = p2Hand[choosecard(card, True)]
            p2Hand.remove(p2card)
            print(f"P2 plays the {p2card}")
            p1input = int(input("What card do you want to play?(Write the index of the card in your hand) "))
            p1card = p1Hand[p1input]
            p1Suits = []
            for suity in p1Hand:
                p1Suits.append(suity.suit)
            while (p1card.suit != p2card.suit and p2card.suit in p1Suits) or (p2card.rank == "Jack" and p2card.suit != trump.suit and p2card.color == trump.color and p1card.suit == trump.suit):
                print("Not a valid play.")
                p1input = int(input("What card do you want to play?(Write the index of the card in your hand) "))
                p1card = p1Hand[p1input]
        if win(p1Hand.pop(p1input), p2card, player_1_lead):
            player_1_tricks+=1
            player_1_lead = True
            print(f"P1 wins the trick, {p1card} vs {p2card}. Trump is {trump.suit}. The score is now P1: {player_1_tricks} - P2: {player_2_tricks}")
        else:
            player_2_tricks += 1
            player_1_lead = False
            print(f"P2 wins the trick, {p2card} vs {p1card}. Trump is {trump.suit}. The score is now P1: {player_1_tricks} - P2: {player_2_tricks}")
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
    if player_2_deals:
        player_2_deals = False
    else:
        player_2_deals = True
