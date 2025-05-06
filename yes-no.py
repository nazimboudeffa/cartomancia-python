from cards_32 import card_meanings_32, card_polarity_32
from cards_52 import card_meanings_52, card_polarity_52
from utils import create_deck_32, create_deck_52, shuffle_deck_times, draw_cards

def draw_yes_no(deck, card_meanings, card_polarity):
    card = deck.pop()
    value, suit = card
    signification = card_meanings.get(card, "Signification inconnue")
    polarity = card_polarity.get(suit, {}).get(value, 'neutre')

    verdict = {
        'positive': "OUI",
        'neutral': "PEUT-ÊTRE",
        'negative': "NON"
    }.get(polarity, "INCONNU")

    print("\nTirage Oui / Non :\n")
    print(f"Carte tirée : {value}{suit}")
    print(f"Signification : {signification}")
    print(f"Interprétation : {verdict}")

def main():
    # Choisir le type de jeu de cartes
    print("Choisissez le type de jeu de cartes :")
    print("1. 32 cartes")
    print("2. 52 cartes")
    choice = input("Entrez votre choix (1 ou 2) : ")

    if choice == '1':
        card_meanings = card_meanings_32
        card_polarity = card_polarity_32
        deck = create_deck_32()
    elif choice == '2':
        card_meanings = card_meanings_52
        card_polarity = card_polarity_52
        deck = create_deck_52()
    else:
        print("Choix invalide. Utilisation du jeu de 32 cartes par défaut.")
        card_meanings = card_meanings_32
        card_polarity = card_polarity_32
        deck = create_deck_32()

    # Demander combien de fois mélanger
    shuffle_times = int(input("Combien de fois voulez-vous mélanger le deck (vous pouvez utiliser un dé de 6) ? "))
    deck = shuffle_deck_times(deck, shuffle_times)

    # Tirage d'une carte pour le Oui/Non
    draw_yes_no(deck, card_meanings, card_polarity)


if __name__ == '__main__':
    main()