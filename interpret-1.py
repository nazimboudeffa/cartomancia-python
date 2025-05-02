import random

# Dictionnaire des significations simples pour chaque carte
card_meanings = {
    # Cœurs (H - Hearts) : domaine affectif, famille, amour
    ('7', 'H'): "Petit bonheur affectif",
    ('8', 'H'): "Pensées amoureuses",
    ('9', 'H'): "Bonheur tranquille",
    ('T', 'H'): "Joie inattendue",
    ('J', 'H'): "Message sentimental",
    ('Q', 'H'): "Femme sincère et aimante",
    ('K', 'H'): "Homme protecteur et bienveillant",
    ('A', 'H'): "Amour sincère et durable",

    # Carreaux (D - Diamonds) : domaine matériel, argent, communication
    ('7', 'D'): "Gain inattendu",
    ('8', 'D'): "Invitation ou lettre",
    ('9', 'D'): "Affaires prospères",
    ('T', 'D'): "Déplacement favorable",
    ('J', 'D'): "Nouvelle professionnelle",
    ('Q', 'D'): "Femme d’affaires ou intéressée",
    ('K', 'D'): "Homme influent, financier",
    ('A', 'D'): "Réussite financière ou professionnelle",

    # Trèfles (C - Clubs) : chance, travail, réussite
    ('7', 'C'): "Petit gain ou aide",
    ('8', 'C'): "Nouvelles liées au travail",
    ('9', 'C'): "Succès dans un projet",
    ('T', 'C'): "Chance ou opportunité",
    ('J', 'C'): "Bonne surprise",
    ('Q', 'C'): "Femme active et travailleuse",
    ('K', 'C'): "Homme ambitieux et chanceux",
    ('A', 'C'): "Réussite générale, chance",

    # Piques (S - Spades) : domaine des épreuves, décisions, spiritualité
    ('7', 'S'): "Retard ou obstacle mineur",
    ('8', 'S'): "Préoccupation ou inquiétude",
    ('9', 'S'): "Déception ou tristesse",
    ('T', 'S'): "Changement inévitable",
    ('J', 'S'): "Message conflictuel",
    ('Q', 'S'): "Femme froide ou distante",
    ('K', 'S'): "Homme autoritaire ou difficile",
    ('A', 'S'): "Décision importante, parfois rupture",
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

def interpret_cards(cards, tirage_type="PPF"):
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
    # Partie principale
    deck = create_deck()
    shuffle_times = int(input("Combien de fois voulez-vous mélanger le deck ? "))
    deck = shuffle_deck_times(deck, shuffle_times)

    print("\nChoisissez un type de tirage :")
    print("1 - Passé / Présent / Futur")
    print("2 - Situation / Obstacle / Conseil")
    choice = input("Votre choix (1 ou 2) : ")

    tirage_type = "PPF" if choice == "1" else "SOC"
    drawn = draw_cards(deck, 3)
    interpret_cards(drawn, tirage_type)

if __name__ == '__main__':
    main()