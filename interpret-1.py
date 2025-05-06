from cards_32 import card_meanings_32
from cards_52 import card_meanings_52
from utils import create_deck_32, create_deck_52, shuffle_deck_times, draw_cards

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

def main():
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
        deck = create_deck_52()
    else:
        print("Choix invalide. Utilisation du jeu de 32 cartes par défaut.")
        card_meanings = card_meanings_32
        deck = create_deck_32()

    # Demander combien de fois mélanger
    shuffle_times = int(input("Combien de fois voulez-vous mélanger le deck (vous pouvez utiliser un dé de 6) ? "))
    deck = shuffle_deck_times(deck, shuffle_times)

    print("\nChoisissez un type de tirage :")
    print("1 - Passé / Présent / Futur")
    print("2 - Situation / Obstacle / Conseil")
    choice = input("Votre choix (1 ou 2) : ")

    tirage_type = "PPF" if choice == "1" else "SOC"
    drawn = draw_cards(deck, 3)
    interpret_cards(drawn, card_meanings, tirage_type)

if __name__ == '__main__':
    main()