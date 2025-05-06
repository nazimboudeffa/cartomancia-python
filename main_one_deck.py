from cards_32 import card_meanings_32, card_polarity_32
from cards_52 import card_meanings_52, card_polarity_52
from utils import create_deck_32, create_deck_52, shuffle_deck_times, draw_cards

def interpret_drawn_cards(cards, card_meanings):
    print("\nVoici les cartes tirées et leurs significations :\n")
    for value, suit in cards:
        signification = card_meanings.get((value, suit), "Signification inconnue")
        print(f"{value}{suit} : {signification}")

def interpret_cards(cards, card_meanings, tirage_type="PPF"):
    if tirage_type == "PPF":
        positions = ["Passé", "Présent", "Futur"]
    elif tirage_type == "SOC":
        positions = ["Situation", "Obstacle", "Conseil"]
    else:
        positions = [f"Carte {i+1}" for i in range(len(cards))]

    print("\nRésultat du tirage :\n")
    for pos, (value, suit) in zip(positions, cards):
        signification = card_meanings.get((value, suit), "Signification inconnue")
        print(f"{pos} ({value}{suit}) : {signification}")

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

    nb_cards = int(input("Combien de cartes voulez-vous tirer ? (ex : 1, 3 ou 5) "))
    drawn = draw_cards(deck, nb_cards)
    interpret_drawn_cards(drawn, card_meanings)

    print("\nChoisissez un type de tirage :")
    print("1 - Passé / Présent / Futur")
    print("2 - Situation / Obstacle / Conseil")
    choice = input("Votre choix (1 ou 2) : ")

    tirage_type = "PPF" if choice == "1" else "SOC"
    drawn = draw_cards(deck, 3)
    interpret_cards(drawn, card_meanings, tirage_type)

    # Tirage d'une carte pour le Oui/Non
    draw_yes_no(deck, card_meanings, card_polarity)

if __name__ == '__main__':
    main()