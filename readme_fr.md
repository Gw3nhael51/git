# 🎲 Générateur de lancer de dé en Python

Ce mini-script simule un lancer de dé classique (1 à 6) et sélectionne aléatoirement un fruit dans une liste grâce au module `random` de Python.

---

## 🔍 Exemple de code

```python
import random

# Générer un numéro entre 1 et 6 comme un dé
random_integer = random.randint(1, 6)
print(f"Résultat du dé: {random_integer}")

# Choisir un fruit à partir d'une liste
fruit = ["pomme", "orange", "cerise", "poire"]
selected_fruit = random.choice(fruit)
print(f"Fruit choisi: {selected_fruit}")
```

---

## 🐍 Activer votre environnement python

ouvrir le terminal en étant dans le chemin du projet: `*/nom_du_projet/git/` <br>
taper la commande: `./py_env_3.11/Scripts/activate` ce qui va alors activer l'environnement py
verifier la version de python: `python --version` ce qui va alors afficher la version || 3.11.8

---

## ▶️ Exécuter le script Python

Une fois l'environnement activé, vous pouvez lancer le script. Placez-vous dans le dossier où se trouve votre fichier (par exemple `main.py`) puis tapez la commande suivante dans le terminal :

```bash
python main.py
```

Vous devriez voir s'afficher un résultat aléatoire entre 1 et 6, ainsi qu'un fruit choisi au hasard, par exemple :

```
Résultat du dé: 4
Fruit choisi: orange
```

---

## 📝 Explication du code

- `import random` : importe le module Python permettant de générer des nombres aléatoires et de faire des sélections aléatoires.
- `random.randint(1, 6)` : génère un nombre entier aléatoire compris entre 1 et 6 inclus, simulant ainsi le lancer d'un dé classique.
- `print(f"Résultat du dé: {random_integer}")` : affiche le résultat du lancer dans le terminal.
- `fruit = ["pomme", "orange", "cerise", "poire"]` : crée une liste de fruits.
- `random.choice(fruit)` : sélectionne aléatoirement un fruit dans la liste.
- `print(f"Fruit choisi: {selected_fruit}")` : affiche le fruit choisi aléatoirement dans le terminal.

---

## 🛠️ Conseils de dépannage

- Si la commande `python` ne fonctionne pas, essayez `python3`.
- Vérifiez que l'environnement virtuel est bien activé (le prompt du terminal doit changer).
- Si vous obtenez une erreur concernant le module `random`, assurez-vous d'utiliser une version standard de Python (le module est inclus par défaut).

---

## 📚 Pour aller plus loin

- Essayez de modifier le script pour lancer plusieurs dés à la fois.
- Ajoutez une boucle pour relancer le dé ou choisir un fruit autant de fois que vous le souhaitez.
- Explorez d'autres modules de la bibliothèque standard Python pour enrichir votre script.
