import random

# Génère un nombre aléatoire entre 1 et 6 pour simuler un lancer de dé
random_integer = random.randint(1, 6)
print(f"Résultat du dé: {random_integer}")

# Sélectionne aléatoirement un fruit dans une liste
fruits = ["pomme", "orange", "cerise", "poire"]  # Déclaration de la liste des fruits
selected_fruit = random.choice(fruits)  # Choix aléatoire d'un fruit dans la liste
print(f"Fruit choisi: {selected_fruit}")  # Affichage du fruit sélectionné