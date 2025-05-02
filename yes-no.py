import random

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

card_polarity = {
    # Cœurs
    'H': {'7': 'positive', '8': 'positive', '9': 'positive', 'T': 'positive',
          'J': 'positive', 'Q': 'positive', 'K': 'positive', 'A': 'positive'},
    # Carreaux
    'D': {'7': 'positive', '8': 'positive', '9': 'positive', 'T': 'positive',
          'J': 'positive', 'Q': 'positive', 'K': 'positive', 'A': 'positive'},
    # Trèfles
    'C': {'7': 'positive', '8': 'positive', '9': 'positive', 'T': 'positive',
          'J': 'positive', 'Q': 'positive', 'K': 'positive', 'A': 'positive'},
    # Piques
    'S': {'7': 'negative', '8': 'neutral', '9': 'negative', 'T': 'neutral',
          'J': 'negative', 'Q': 'negative', 'K': 'negative', 'A': 'negative'},
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

def draw_yes_no(deck):
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
    import random

    # Création et mélange du deck
    # Partie principale
    deck = create_deck()
    shuffle_times = int(input("Combien de fois voulez-vous mélanger le deck ? "))
    deck = shuffle_deck_times(deck, shuffle_times)

    # Tirage d'une carte pour le Oui/Non
    draw_yes_no(deck)


if __name__ == '__main__':
    main()