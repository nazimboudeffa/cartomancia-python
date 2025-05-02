import random

# Dictionnaire des significations simples pour chaque carte
card_meanings = {
    ('A', 'H'): "Amour sincère",
    ('K', 'H'): "Protection d’un homme",
    ('Q', 'H'): "Femme bienveillante",
    ('J', 'H'): "Nouvelles liées à l’amour",
    ('T', 'H'): "Joie inattendue",
    ('9', 'H'): "Bonheur simple",
    ('8', 'H'): "Pensées d’amour",
    ('7', 'H'): "Petit plaisir affectif",
    # Tu feras de même pour D, C, S…
}

def create_deck():
    # Les couleurs des cartes
    suits = ['H', 'D', 'C', 'S']
    # Les valeurs des cartes (32 cartes : 7 à As)
    values = ['7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
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

def interpret_cards(cards):
    print("\nVoici les cartes tirées et leurs significations :\n")
    for value, suit in cards:
        signification = card_meanings.get((value, suit), "Signification inconnue")
        print(f"{value}{suit} : {signification}")

def main():
    # Exemple d'utilisation
    deck = create_deck()

    # Demander combien de fois mélanger
    shuffle_times = int(input("Combien de fois voulez-vous mélanger le deck (vous pouvez utiliser un dé de 6) ? "))
    deck = shuffle_deck_times(deck, shuffle_times)

    nb_cards = int(input("Combien de cartes voulez-vous tirer ? (ex : 1, 3 ou 13) "))
    drawn = draw_cards(deck, nb_cards)
    interpret_cards(drawn)

if __name__ == '__main__':
    main()