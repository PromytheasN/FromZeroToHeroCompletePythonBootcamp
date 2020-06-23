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
        self.cards = [] #starting with a nempty list.
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

"""
This notes are for better understanding of how to call methods within classes.     
we can test/call it using this ways.
Print(Deck()), if we do Print(Deck) we will get the position where Deck is stored, by adding () we 
call the self of the Deck. The reason we can print the class Deck is because of we used the magic method __str__,
otherwise the only way to call/print it is by creating an object as bellow using the blue print of the Class Deck
So we could create object: first_deck = Deck(), first_deck.__str__() or because we used __str__ print(first_deck())
again () is the self, without it we will get the position of the fist_deck in the memory of the system. 
"""
