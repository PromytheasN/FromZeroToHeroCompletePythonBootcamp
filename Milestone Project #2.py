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
    
    print(f"{rank} of {value}")
    
   
    
