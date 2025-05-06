import random

def create_deck_32():
    # Les couleurs des cartes
    suits = ['H', 'D', 'C', 'S']
    # Les valeurs des cartes (32 cartes : 7 à As)
    values = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    # Création du deck
    deck = [(value, suit) for suit in suits for value in values]
    
    return deck

def create_deck_52():
    # Les couleurs des cartes
    suits = ['H', 'D', 'C', 'S']
    # Les valeurs des cartes (32 cartes : 7 à As)
    values = ['2', '3', '4', '5,' ,'6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    # Création du deck
    deck = [(value, suit) for suit in suits for value in values]
    
    return deck

def shuffle_deck(deck):
    # Mélange le deck
    random.shuffle(deck)
    return deck

def shuffle_deck_times(deck, times=1):
    # Mélange le deck un certain nombre de fois
    for _ in range(times):
        random.shuffle(deck)
    return deck

def draw_cards(deck, number=3):
    return [deck.pop() for _ in range(number)]