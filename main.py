import random

# Générer un numéro entre 1 & 6 comme un dé

random_integer = random.randint(1, 6)
print(f"Résultat du dé: {random_integer}")

# Choisir un fruit à partir d'un tableau

# Créer un tableau
fruit = ["pomme", "orange", "cerise", "poire"]
# Créer une variable fruit sélectionné = choix aleatoire du tableau fruit
selected_fruit = random.choice(fruit)
# Afficher le texte + le résultat du fruit aléatoire
print(f"Fruit choisi: {selected_fruit}")