import random

#Creating global variables for suites, ranks and values
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10,
          "Queen":10, "King":10, "Ace":11}

#playing loop
playing = True

#Card Class
class Card:
  
  def __init__(self, suit, rank):
    """
    We define atributes of the Card object, suites and ranks.
    """
    
    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    """
    Function that prints the information of the object (rank & value).
    """
    return f"{self.rank} of {self.suit}"   

#we can test it like this.
#no1 = Card("Hearts","Two")
#print(no1) or no1.__str__()
    
class Deck:
    """
    store 52 objects in a card list
    that can be shuffled
    instatiate all 52 card objects and add them to our list
    build card objects inside our Deck
    """
    
    def __init__(self):
        self.deck = []
        for suit in suits:  # start with an empty list
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # build Card objects and add them to the list
                
    def __str__(self):
        deck_comp = "" #starting with empty string
        for card in self.deck:
            deck_comp += '\n' + str(card) # add each Card object's print
        return deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop() #Taking a card out of the deck list.
        return single_card

class Hand:
    """
    We create a class for the Hand that the player holds.
    """
    def __init__(self):
        self.cards = [] #starting with an empty list.
        self.value = 0 #Starting with zero Value
        self.aces = 0 #Keeping track of aces
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace": #We count the aces we hold
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces: #Making sure that if we have Aces we can use value 1 instead of 10 if valuie is over 21 in total
            self.value -= 10
            self.aces -= 1
          
          
class Chips:
    
    """
    Cheaps class for keeping record of the total chips of the player, winnings and losses from each bet
    and the total amount betting each time.
    """
    
    def __init__(self):
        
        #We can also do self.total = total and define the total like this __init__(self, total = 200)
        self.total = 200 #This is the default value and can could be set by users input as well.
        
        
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
          
    """
    Function that requires user to input the amount of chips he wishes to bet, and checks if input is integar.
    """
    
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except ValueError:
            print("Sorry, invalid input, bet must be a physichal number!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your best can't exceed your total chips:". chips.total)
                
            else:
                break
                
def take_hit(deck,hand):
    
    """
    function that takes hits from player until they bust
    """
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    
    """
    Function that asks the player to hit or stand
    """
    
    global playing # to control playing variable
    
    while True:
        choice = input("Would you like to Hit or Stand? Enter 'H' or 'S'")
        
        if choice[0].lower() =="h":
            take_hit(deck,hand) #tappes into hit() function
            
        elif choice[0].lower() == 's':
            print("Player stands. Dealer is playing now.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

def display_some_cards(player,dealer):
    print("\nDealer's Hand: <card hidden> ", dealer.cards[1], "\nPlayer's Hand:", *player.cards, sep = "\n ")
    
def show_all_cards(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =",player.value)
          
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

    
#Now we will combine everything so we can have a functional game.


while True:
    #Printing an opening statment
    print("Welcome to Promytheous' BlackJack! Get as close to 21 as you can without getting busted\
you shall be rewarded from the Gods, with gifts beyond your imagination! \n\
I shall share my light of FIRE to assist you. Dealer hits until she reaches 17. Aces will count\
 as 1 or 11. Let the game begin!")
    
    #Creating and shuffling the deck, dealing two cards to each player.
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #Setting players cheaps
    player_chips = Chips() #default = 200
    
    #Ask player for their bet
    take_bet(player_chips)
    
    #Show cards while keeping one of the dealer's cards hidden
    display_some_cards(player_hand, dealer_hand)
    
    while playing: #recall this variable from our hit_or_stand function
        
        #Ask player to hit or stand
        hit_or_stand(deck,player_hand)
        
        #Show cards (keeping dealers 1 card hidden)
        display_some_cards(player_hand,dealer_hand)
    
        #If player's hand exceeds 21, run player_busts() and break out loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
            
    #If player hasn't busted, play dealer's hand until dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            take_hit(deck,dealer_hand)
            
        #Show all cards
        show_all_cards(player_hand, dealer_hand)
        
        #Run different winning scenario
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value > player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            
        else:
            push(player_hand, dealer_hand)
    
    #Inform Player of their chips total
    print("\nPlayer's winnings stand at",player_chips.total)
    
    #Ask to play again
    new_game = input("Would you like to play another hand? Enter 'Y' or 'N'")
    
    if new_game[0].lower()=="y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
        
