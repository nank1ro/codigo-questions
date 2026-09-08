Parfois, vous n'avez besoin d'une toute petite fonction qu'une seule fois, par exemple pour doubler un nombre.
Écrire un bloc `def` complet pour cela paraît lourd.
Python propose une forme plus courte : l'expression **lambda**, une fonction _anonyme_ écrite sur une seule ligne :
```python
lambda x: x * 2
```
La syntaxe est `lambda paramètres: expression`.
Une lambda n'a pas de nom, mais vous pouvez la stocker dans une variable et l'appeler comme n'importe quelle autre fonction :
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Remarquez que le corps de la lambda n'a pas de mot-clé `return`.
Le corps est une **expression unique**, et sa valeur est retournée automatiquement :
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

Une lambda peut prendre **plus d'un paramètre**.
Séparez-les par des virgules, exactement comme dans une fonction `def` :
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Parce que le corps doit être une expression unique, une lambda **ne peut pas contenir d'instructions**.
Ni `return`, ni blocs `if`, ni boucles, ni affectations :
```python
# SyntaxError
increment = lambda x: return x + 1
```
Si vous avez besoin de l'un de ces éléments, écrivez plutôt une fonction `def` normale.

---

Les paramètres d'une lambda acceptent aussi des **valeurs par défaut** :
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

Vous n'êtes même pas obligé de stocker une lambda : vous pouvez **l'appeler immédiatement**.
Entourez la lambda de parenthèses, puis ajoutez les arguments :
```python
print((lambda x: x + 1)(4))  # 5
```

---

Les lambdas brillent vraiment en tant qu'**arguments d'autres fonctions**.
`sorted()` accepte un paramètre `key` : une fonction appelée sur chaque élément, et son résultat décide de l'ordre.
Une lambda est parfaitement adaptée :
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

La lambda `key` peut choisir n'importe quelle partie d'un élément.
Pour une liste de listes, `lambda p: p[1]` trie selon le deuxième élément de chaque liste interne.

---

`map()` applique une fonction à **chaque élément** d'une liste.
Elle retourne un _objet map_ spécial, il faut donc l'entourer de `list()` pour voir les valeurs :
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` ne conserve que les éléments pour lesquels la fonction retourne `True` :
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Afficher directement un objet `map` ne montre pas ses valeurs : on obtient quelque chose comme `<map object at 0x7f2b1c>`.
Seul `list()` (ou une boucle) le transforme en les valeurs attendues.

---

Les lambdas ne se limitent pas aux fonctions intégrées : **vos propres fonctions** peuvent prendre une fonction en paramètre et l'appeler.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` et `min()` acceptent aussi une fonction `key`, tout comme `sorted()` :
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**Quand devriez-vous préférer `def` ?**
Une lambda est idéale pour une fonction courte et jetable passée en argument.
Si la logique a besoin d'un nom, de plusieurs lignes, d'une docstring, ou est réutilisée à de nombreux endroits, une fonction `def` est plus claire.
Une dernière astuce : `sorted()` accepte aussi `reverse=True` pour obtenir d'abord les plus grandes valeurs :
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
