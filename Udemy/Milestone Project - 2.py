'''
Milestone Project 2 - Blackjack Game

In this milestone project you will be creating a Complete BlackJack Card Game
in Python.

Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:

    You must use OOP and classes in some portion of your game. You can not
    just use functions in your game. Use classes to help you define the Deck
    and the Player's hand. There are many right ways to do this, so explore
    it well!

Feel free to expand this game. Try including multiple players. Try adding in
Double-Down and card splits! Remember to you are free to use any resources
you want and as always:

HAVE FUN!
'''

import random
import os
import sys

suits = {'0': 'Heart', '1': 'Spades', '2': 'Diamond',
         '3': 'Club', '11': 'Jack', '12': 'Queen', '13': 'King'}


class Deck():

    def __init__(self):
        # generate the cards, using *range.  * operator needs to be used.
        # assume 1st level list are suits = 'Hearts', 'Diamonds', 'Spades', 'Clubs'
        # self.deck = [[*range(1, 14)], [*range(1, 14)],[*range(1, 14)], [*range(1, 14)]]

        # generate a sequenced deck via double iteration list comprehension then shuffle it.
        # this generates a shuffled string list of cards in SuitNumber format.
        self.deck = [(str(suit) + str(num))
                     for suit in range(4) for num in range(1, 14)]
        random.shuffle(self.deck)

    def __str__(self):
        # typecast list into string for printing.
        return(str(self.deck))


class BlackjackPlayer():
    # Class type for player.

    def __init__(self, name='', cards=[], bet=0, balance=0):
        self.name = name
        self.balance = balance
        # This [] needs to be explicitly set to avoid class data sharing.
        self.cards = []
        self.bet = 0
        self.score = 0
        self.total = 0
        self.total2 = 0
        self.ace = False

    def putbet(self):
        while True:
            try:
                self.bet = int(input("Please enter your bet: "))
                if player.bet > player.balance:
                    print('Insufficient balance to place this bet.')
                    raise Exception()
            except:
                print("Please enter a valid amount.")
                continue
            else:
                break

    def getcard(self):
        self.deal = cards.deck.pop(0)
        self.suit = suits[self.deal[0]]

        # check if card is King, Queen or Jack, set score to 10.
        if int(self.deal[1:]) > 10:
            self.score = 10
        else:
            self.score = int(self.deal[1:])

        self.total += self.score
        if self.score == 1:
            self.ace = True
            self.total2 = self.total + 10
            self.cards.append(f'Ace {self.suit}')
        else:
            self.total2 += self.total
            self.cards.append(f'{self.deal[1:]} {self.suit}')
        return

    def __str__(self):
        # format balance with comma notation.
        return(f'Player "{self.name}" has ${self.balance:,} balance to play.')
        pass


def display_board(playername='Player', status=False):
    os.system('cls')
    print("Welcome to Black Jack!\n")
    if status:
        print(
            f'Dealer\'s Cards: [{dealer.cards[0]}, HIDDEN], Score = {dealer.total}')
    else:
        print(f'Dealer\'s Cards: {dealer.cards}')
    print(f'{playername}\'s Cards: {player.cards} Score = {player.total}')
    print(f'{playername} Balance= ${player.balance:,} Bet= ${player.bet:,}\n')


def yesno(message):
    while True:
        answer = input(message)
        if answer.upper() == 'Y':
            return True
        if answer.upper() == 'N':
            return False
        else:
            continue


def iswinner(hitdeal=False):
    # check if the initial deal already has a winner.

    if player.total > 21:
        player.balance -= player.bet
        print('\nBUSTed, Dealer win!')
        return True

    if player.total == 21 or player.total2 == 21:
        if hitdeal:
            player.balance += player.bet
            print(f'{player.name} won!')
        else:
            player.balance += player.bet * 1.5
            print(f'BLACK JACK! {player.name} won!')
        return True

    # after asking for a hit, check if someone won.
    if hitdeal:
        if dealer.total > 21:
            player.balance += player.bet
            print(f'{player.name} won!')

        # if there is an ACE, check score assuming ace = 11
        elif player.total2 < 21 and player.total2 > dealer.total and player.ace:
            player.balance += player.bet
            print(f'{player.name} won!')

        elif player.total > dealer.total:
            player.balance += player.bet
            print(f"{player.name} won!")

        elif player.total == dealer.total:
            print(f"PUSH (DRAW)")

        else:
            player.balance -= player.bet
            print("Dealer won!")
        return True

    return False


def initialdeal():
    # Deal two cards to the player(s).
    player.getcard()
    player.getcard()

    # Dealer's card total should be greater than 16.
    while dealer.total < 17:
        dealer.getcard()


def retry():
    retry = yesno("Do you want to play again? (Y/N)?")
    if retry:
        player.__init__(name=player.name, balance=player.balance)
        dealer.__init__()
        cards.__init__()
    else:
        sys.exit()


# initialize variables
cards = Deck()
player = BlackjackPlayer()
dealer = BlackjackPlayer(name='Dealer')

while True:
    display_board()

    # initialize player details.
    try:
        if not player.name:
            player.name = input("To start game, please enter Player name: ")
        if not player.balance:
            player.balance = int(input("Please enter your balance: "))
        player.putbet()
    except:
        print("Please enter a valid amount.\n")
        # press any key to continue
        os.system("pause")
        continue

    initialdeal()
    if iswinner():
        retry()
        continue

    while True:
        display_board(player.name, True)

        # Ask player if he wants a HIT or STAY.
        hit = yesno("Do you want another card? (Y / N)")
        if hit:
            player.getcard()
            continue
        else:
            if iswinner(True):
                retry()
                break


print("Thank you for playing BLACK JACK!  Bye!")
