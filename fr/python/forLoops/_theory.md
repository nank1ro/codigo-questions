Nous savons comment répéter du code en utilisant une boucle `while`.
Comme ce programme qui répète les instructions pour afficher `hello`
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
Mais nous pouvons faire la même chose avec des boucles `for` :
```python
for i in range(5):
    print("hello")
```

---

Dans une boucle `for`, nous pouvons spécifier le nombre de fois que nous voulons que notre boucle s'exécute avec la fonction `range()`

---

Ajouter un nombre comme `5` à l'intérieur de la fonction `range()` signifie qu'il va boucler sur le bloc de code 5 fois, de `0` jusqu'à `4`

---

La variable appelée `i` est la variable compteur.
Nous pouvons lui donner le nom que nous voulons.
Elle compte à quelle itération de la boucle nous sommes actuellement

---

La fonction `range()` retourne une séquence de nombres, en commençant par 0 par défaut, et augmente par 1 (par défaut), et s'arrête avant un nombre spécifié.
Ceci est la syntaxe de la fonction :
```python
range(start, stop, step)
```
`start` et `step` sont optionnels, tandis que `stop` est requis
