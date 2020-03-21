#setup our objects
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

################Classes################

#setup single card class
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#setup deck class
class Deck():
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f"The deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


#setup class for dsealer and players hands
class Hand():
    def __init__(self):
        self.cards = [] 
        self.value = 0   
        self.aces = 0   
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


#setup players bank
class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet



################Functions################

#ask player for a bet function
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How much do you want to bet? "))
        except:
            print("Please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Bet exceeds bank of {chips.total} chips")
            else: 
                break

#player hit function
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        next_move = input("\nWould you like to hit or stand? ")
        
        if next_move[0].lower() == 'h':
            hit(deck,hand)
        elif next_move[0].lower() == 's':
            print("Player stands.")
            playing = False
        else:
            print("Please enter hit or stand.")
        break

#dealer hit function
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


#functions to show the cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print("   <card hidden>")
    print('  ',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n   ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n   ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n   ')
    print("Player's Hand =",player.value)


#end gamne scenarios
def player_busts(player,dealer,chips):
    print("\nPlayer busts :(")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer wins :(")
    chips.lose_bet()
    
def push(player,dealer):
    print("\nIt's a tie!")

#initial deal
def deal_cards(player,dealer,deck):
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    player.add_card(deck.deal())



##################gameplay####################

while True:
    # Print an opening statement
    print("Welcome to Blackjack")
    
    # Create & shuffle the deck
    new_deck = Deck()
    new_deck.shuffle()
    
    #set up player and dealer
    dealer_hand = Hand()
    player_hand = Hand()
    
    #add 2 cards to player and dealer
    deal_cards(player_hand, dealer_hand, new_deck)
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    print("\nIt's the Dealers turn.")
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(new_deck, dealer_hand)
            
        # Show all cards
        show_all(player_hand, dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value == player_hand.value:
            push(player_hand, dealer_hand)
    
    # Inform Player of their chips total 
    print(f"\nYour new chip balance is: {player_chips.total}")
    
    # Ask to play again
    new_game = input("\nPlay again? y or n: ")
    
    if new_game == 'y':
        playing = True
    else:
        print("Thank you for playing")
        break