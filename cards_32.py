# Dictionnaire des significations simples pour chaque carte
card_meanings_32 = {
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

card_polarity_32 = {
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