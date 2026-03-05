En Swift, nous pouvons utiliser le signe `+` pour afficher deux chaînes ou plus ensemble, comme :
```swift
print("Hello " + "Swift!") // prints "Hello Swift!"
```

---

Mais l'utilisation du signe `+` pour ajouter un nombre comme '10' à une chaîne comme `"friends"` produit une erreur car ce sont des types de valeurs différents

---

Interpolation de chaîne allow us to display expressions like adding a string to a number, without any error.

---

Chaque instruction d'interpolation de chaîne se compose de deux parties : le `\()` où nous insérons le nombre ou la variable, et la chaîne normale

---

Ensuite, nous ajoutons un type de valeur différent entre accolades pour qu'il s'affiche comme une seule instruction print. Comme ici, avec `\(5)`

---

Insérer des variables comme `friends` entre les parenthèses affiche aussi leur valeur

---

Nous pouvons utiliser les parenthèses pour insérer des valeurs autant de fois que nous le souhaitons dans l'interpolation de chaîne

---

Interpolation de chaînes are best used in print statements, but we can also store them in variables like normal strings.
