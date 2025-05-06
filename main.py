from cards_32 import card_meanings_32
from cards_52 import card_meanings_52
from utils import create_deck_32, create_deck_52, shuffle_deck_times, draw_cards

def interpret_cards(cards, card_meanings):
    print("\nVoici les cartes tirées et leurs significations :\n")
    for value, suit in cards:
        signification = card_meanings.get((value, suit), "Signification inconnue")
        print(f"{value}{suit} : {signification}")

def main():
    # Exemple d'utilisation

    # Choisir le type de jeu de cartes
    print("Choisissez le type de jeu de cartes :")
    print("1. 32 cartes")
    print("2. 52 cartes")
    choice = input("Entrez votre choix (1 ou 2) : ")

    if choice == '1':
        card_meanings = card_meanings_32
        deck = create_deck_32()
    elif choice == '2':
        card_meanings = card_meanings_52
        
    else:
        print("Choix invalide. Utilisation du jeu de 32 cartes par défaut.")
        card_meanings = card_meanings_32
        deck = create_deck_32()

    # Demander combien de fois mélanger
    shuffle_times = int(input("Combien de fois voulez-vous mélanger le deck (vous pouvez utiliser un dé de 6) ? "))
    deck = shuffle_deck_times(deck, shuffle_times)

    nb_cards = int(input("Combien de cartes voulez-vous tirer ? (ex : 1, 3 ou 5) "))
    drawn = draw_cards(deck, nb_cards)
    interpret_cards(drawn, card_meanings)

if __name__ == '__main__':
    main()