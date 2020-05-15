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
    
class Deck:
    #store 52 objects in a card list
    #that can be shuffled
    #instatiate all 52 card objects and add them to our list
    #build card objects inside our Deck
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = "" #starting with empty string
        for card in self.deck:
            deck_comp += '\n' + str(card) # add each Card object's print
        return deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
