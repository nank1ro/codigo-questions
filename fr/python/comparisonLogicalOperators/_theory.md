Les opérateurs de comparaison comparent deux valeurs et renvoient un **booléen**, `True` ou `False` : `==` égal, `!=` différent, `<` inférieur à, `>` supérieur à, `<=` inférieur ou égal, `>=` supérieur ou égal :
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
Le résultat peut être stocké dans une variable ou affiché directement. Un simple `=` est une affectation, pas une comparaison.

---

Les opérateurs de comparaison ne se limitent pas aux nombres. Les chaînes sont comparées caractère par caractère à l'aide de leurs points de code, donc `"apple" < "banana"` vaut `True` et, comme toute majuscule vient avant les minuscules, `"Zoo" < "apple"` vaut aussi `True`. Les listes et les tuples sont comparés élément par élément de la même façon :
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
Une comparaison est une expression, donc une fonction peut faire `return a < b` directement au lieu de l'envelopper dans un `if`.

---

Les comparaisons peuvent être **chaînées** : `1 < x < 10` vérifie que `x` est supérieur à `1` **et** inférieur à `10`, exactement comme `1 < x and x < 10`, mais `x` n'est évalué qu'une seule fois :
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
N'importe quels opérateurs de comparaison peuvent être chaînés et chacun s'applique à ses deux voisins : `a < b == c` signifie `a < b and b == c`. Lire une chaîne comme un intervalle, `low < x < high`, en est l'usage le plus courant.

---

Les opérateurs logiques combinent des booléens. `and` vaut `True` seulement quand les deux côtés valent `True`, `or` quand au moins un côté l'est, et `not` inverse une seule valeur :
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
Les comparaisons sont prioritaires sur les opérateurs logiques, donc `age >= 18 and member` n'a pas besoin de parenthèses. Les parenthèses sont nécessaires pour regrouper un `or` à l'intérieur d'un `and` : `a and (b or c)`.

---

Lorsque `not`, `and` et `or` apparaissent dans une même expression, Python applique d'abord `not`, puis `and`, puis `or`. Ainsi `a or b and c` signifie `a or (b and c)`, et `not a == b` signifie `not (a == b)` :
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
Lorsqu'un autre regroupement est voulu, ajoutez des parenthèses ; elles rendent aussi l'expression plus lisible.

---

Chaque valeur a une **valeur de vérité**. `bool(value)` renvoie `False` pour `0`, `0.0`, `None`, la chaîne vide `""` et les conteneurs vides comme `[]`, `{}` et `set()` ; toute autre valeur est vraie, y compris `"0"` et `[0]` :
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` et `not` utilisent cette règle, donc `if items:` vérifie que la liste n'est pas vide et `not name` vérifie que la chaîne est vide ; il est inutile d'écrire `len(items) > 0` ou `name == ""`.

---

Comme `if value:` applique déjà la valeur de vérité, comparer avec `== True` ou `== False` est inutile et peut même être faux : `2 == True` vaut `False`, et pourtant `2` est vrai. Testez la valeur elle-même :
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` et `or` ne renvoient pas toujours `True` ou `False` : ils renvoient l'un de leurs **opérandes**. `a and b` renvoie `a` s'il est faux, sinon `b` ; `a or b` renvoie `a` s'il est vrai, sinon `b` :
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
Le résultat est vrai ou faux exactement quand l'expression entière l'est, c'est pourquoi `if a and b:` fonctionne malgré tout. Un usage courant est la valeur par défaut : `name = user_input or "guest"`.

---

Les opérateurs logiques sont à **court-circuit** : `and` s'arrête dès qu'un opérande est faux et `or` dès qu'un opérande est vrai, car le résultat est déjà connu. Les opérandes restants ne sont jamais évalués, donc s'il s'agit d'appels de fonction ils ne s'exécutent pas :
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` compare les **valeurs** ; `is` compare l'**identité**, c'est-à-dire si les deux noms désignent exactement le même objet. Deux listes égales construites séparément sont `==` mais pas `is` :
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` est destiné aux singletons comme `None`, `True` et `False` : écrivez `value is None` ou `value is not None`, jamais `value == None`, car une classe peut définir `==` pour renvoyer n'importe quoi. Utiliser `is` avec des nombres ou des chaînes n'est pas fiable et Python vous en avertit.

---

L'évaluation en court-circuit est une manière sûre de **protéger** une opération qui échouerait sur certaines valeurs. Dans `word is not None and len(word) < 4`, `len(word)` ne s'exécute que lorsque `word` n'est pas `None`, donc l'appel ne lève jamais d'erreur. La protection doit venir en premier :
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Gardez à l'esprit que `and` renvoie un opérande : `word and len(word) < 4` donne `None` pour `None` et `""` pour la chaîne vide, pas `False`. Protégez avec une vraie comparaison lorsqu'un booléen est requis.

---

L'opérateur `in` vérifie l'**appartenance** : si un élément est dans une liste, un tuple ou un ensemble, si une sous-chaîne est dans une chaîne, ou si une clé est dans un dictionnaire. `not in` en est la négation :
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Les deux renvoient un booléen et se lisent comme de l'anglais, ce qui en fait la façon privilégiée de tester l'appartenance au lieu d'écrire une boucle.
