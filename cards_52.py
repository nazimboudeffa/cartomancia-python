card_meanings_52 = {
    # Cœurs (H - Hearts) : domaine affectif, famille, amour
    ('2', 'H'): "Naissance d’un sentiment",
    ('3', 'H'): "Rencontre ou début affectif",
    ('4', 'H'): "Stabilité émotionnelle",
    ('5', 'H'): "Soutien affectif",
    ('6', 'H'): "Évolution d'une relation",
    ('7', 'H'): "Petit bonheur affectif",
    ('8', 'H'): "Pensées amoureuses",
    ('9', 'H'): "Bonheur tranquille",
    ('T', 'H'): "Joie inattendue",
    ('J', 'H'): "Message sentimental",
    ('Q', 'H'): "Femme sincère et aimante",
    ('K', 'H'): "Homme protecteur et bienveillant",
    ('A', 'H'): "Amour sincère et durable",

    # Carreaux (D - Diamonds) : domaine matériel, argent, communication
    ('2', 'D'): "Petite somme ou cadeau",
    ('3', 'D'): "Appel ou nouvelle rapide",
    ('4', 'D'): "Économie ou prudence",
    ('5', 'D'): "Projet matériel ou achat",
    ('6', 'D'): "Échange utile ou fructueux",
    ('7', 'D'): "Gain inattendu",
    ('8', 'D'): "Invitation ou lettre",
    ('9', 'D'): "Affaires prospères",
    ('T', 'D'): "Déplacement favorable",
    ('J', 'D'): "Nouvelle professionnelle",
    ('Q', 'D'): "Femme d’affaires ou intéressée",
    ('K', 'D'): "Homme influent, financier",
    ('A', 'D'): "Réussite financière ou professionnelle",

    # Trèfles (C - Clubs) : chance, travail, réussite
    ('2', 'C'): "Coup de pouce ou opportunité",
    ('3', 'C'): "Collaboration ou aide au travail",
    ('4', 'C'): "Organisation bénéfique",
    ('5', 'C'): "Effort constant, récompensé",
    ('6', 'C'): "Progrès dans les affaires",
    ('7', 'C'): "Petit gain ou aide",
    ('8', 'C'): "Nouvelles liées au travail",
    ('9', 'C'): "Succès dans un projet",
    ('T', 'C'): "Chance ou opportunité",
    ('J', 'C'): "Bonne surprise",
    ('Q', 'C'): "Femme active et travailleuse",
    ('K', 'C'): "Homme ambitieux et chanceux",
    ('A', 'C'): "Réussite générale, chance",

    # Piques (S - Spades) : domaine des épreuves, décisions, spiritualité
    ('2', 'S'): "Petit contretemps",
    ('3', 'S'): "Discussion tendue",
    ('4', 'S'): "Blocage mental ou fatigue",
    ('5', 'S'): "Affrontement ou choix difficile",
    ('6', 'S'): "Situation délicate mais surmontable",
    ('7', 'S'): "Retard ou obstacle mineur",
    ('8', 'S'): "Préoccupation ou inquiétude",
    ('9', 'S'): "Déception ou tristesse",
    ('T', 'S'): "Changement inévitable",
    ('J', 'S'): "Message conflictuel",
    ('Q', 'S'): "Femme froide ou distante",
    ('K', 'S'): "Homme autoritaire ou difficile",
    ('A', 'S'): "Décision importante, parfois rupture",
}

card_polarity_52 = {
    # Cœurs (H) : globalement positifs, domaine affectif
    'H': {
        '2': 'positive', '3': 'positive', '4': 'positive',
        '5': 'positive', '6': 'positive', '7': 'positive',
        '8': 'positive', '9': 'positive', 'T': 'positive',
        'J': 'positive', 'Q': 'positive', 'K': 'positive',
        'A': 'positive',
    },

    # Carreaux (D) : matériel, plutôt positif
    'D': {
        '2': 'positive', '3': 'positive', '4': 'neutral',
        '5': 'positive', '6': 'positive', '7': 'positive',
        '8': 'positive', '9': 'positive', 'T': 'positive',
        'J': 'positive', 'Q': 'neutral', 'K': 'positive',
        'A': 'positive',
    },

    # Trèfles (C) : chance et travail, plutôt positif
    'C': {
        '2': 'positive', '3': 'positive', '4': 'neutral',
        '5': 'positive', '6': 'positive', '7': 'positive',
        '8': 'positive', '9': 'positive', 'T': 'positive',
        'J': 'positive', 'Q': 'positive', 'K': 'positive',
        'A': 'positive',
    },

    # Piques (S) : épreuves, plutôt négatif ou neutre
    'S': {
        '2': 'neutral', '3': 'negative', '4': 'negative',
        '5': 'negative', '6': 'neutral', '7': 'negative',
        '8': 'neutral', '9': 'negative', 'T': 'neutral',
        'J': 'negative', 'Q': 'negative', 'K': 'negative',
        'A': 'negative',
    },
}
