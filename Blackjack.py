"""
This is a code-along tutorial and is not my own work. 
All credit goes to freeCodeCamp.org. 

"""

import random

class Card:
  """
  Represents a single card in a deck, with a suit and a rank.
  """

  def __init__(self, suit, rank):
    """
    suit (str): The suit of the card.
    rank (dict): A dictionary that contains the ranks of each card and their value.
    """

    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"

class Deck:
  """
  Represents a deck of 52 playing cards.
  """

  def __init__(self):
    
    self.cards =[]
    suits = ["spades", "hearts", "clubs", "diamonds"]
    ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}, 
    ]

    # Create the full deck by combining suits and ranks
    for i in range(len(suits)):
      for j in range(len(ranks)):
        self.cards.append(Card(suits[i], ranks[j]))

  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)

  def deal(self, number):
    """
    number (int): The number of cards to deal.

    return:
      A list of cards dealt from the deck.
    """

    cards_dealt = []
    for i in range(number):
      if len(self.cards) > 0:
        card = self.cards.pop()
        cards_dealt.append(card)
    return cards_dealt

class Hand:
  """
  Represents a player's hand in the game, holding multiple cards.
  """

  def __init__(self, dealer = False):
    """
    dealer (bool): Default is false, and is true if the hand is the dealer's hand.
    """

    self.cards = []
    self.value = 0
    self.dealer = dealer

  def add_card(self, card_list):
    """
    Add a list of cards to the hand.
    """

    self.cards.extend(card_list)
  
  def calculate_value(self):
    """
    Calculate the total value of the hand, accounting for aces.
    """

    self.value = 0
    has_ace = False

    for card in self.cards:
      card_value = int(card.rank["value"])
      self.value += card_value
      if card.rank["rank"] == "A":
        has_ace = True
    
      # Adjust for ace value if hand value exceeds 21
      if has_ace and self.value > 21:
        self.value -= 10

  def get_value(self):
    """
    Calculate and return the current value of the hand.
    """

    self.calculate_value()
    return self.value
  
  def is_blackjack(self):
    return self.get_value() == 21
  
  def display(self, dealer_cards = False):
    """
    dealer_cards (bool): Default is false, and is true to show all dealer's cards.
    """
    print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
    for index, card in enumerate(self.cards):
      if index == 0 and self.dealer \
        and not dealer_cards and not self.is_blackjack():
        print("Hidden")
      else:
        print(card)
        
    if not self.dealer:
      print("Value", self.get_value())
    print()

class Game:
  """
  The main blackjack game logic
  """

  def play(self):
    """
    Handles user inputs
    """

    game_number = 0
    games_to_play = 0

    # Prompt the user to input the number of games to play
    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games do you want to play? "))
      except:
        print("You must enter a number.")
        games_to_play = 0
    
    # Main game loop
    while game_number < games_to_play:
      game_number += 1

      deck = Deck()
      deck.shuffle()

      player_hand = Hand()
      dealer_hand = Hand(dealer=True)
      for i in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print()
      print("*" * 30)
      print(f"Game {game_number} of {games_to_play}")
      print("*" * 30)
      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue
      
      # Player's turn: hit or stand
      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("Please choose 'Hit' or 'Stand': ").lower().strip()
        print()
        while choice not in ["h", "s", "hit", "stand"]:
          choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower().strip()
          print()
        if choice in ["hit", "h"]:
          player_hand.add_card(deck.deal(1))
          player_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      # Dealer's turn: hits until value is at least 17
      while dealer_hand_value < 17:
        dealer_hand.add_card(deck.deal(1))
        dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(dealer_cards=True)

      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final Results")
      print("Your hand:", player_hand_value)
      print("Dealer's hand:", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)
  
    print("\nThanks for playing!")

  def check_winner(self, player_hand, dealer_hand, game_over=False):
    """
    player_hand (Hand): The player's hand.
    dealer_hand (Hand): The dealer's hand.
    game_over (bool): True if the game has ended, False if still in progress.

    return:
      bool: Default is false, and is true if the game has ended
    """

    if not game_over:
      if player_hand.get_value() > 21:
        print("You busted. Dealer wins!")
        return True
      elif dealer_hand.get_value() > 21:
        print("Dealer busted. You win!")
        return True
      elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
        print("Both players have blackjack! Tie!")
        return True
      elif player_hand.is_blackjack():
        print("You have blackjack. You win!")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer has blackjack. You lose!")
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print("You win!")
      elif player_hand.get_value() == dealer_hand.get_value():
        print("Tie!")
      else:
        print("Dealer wins.")
      return True
    return False
  

g = Game()
g.play()
