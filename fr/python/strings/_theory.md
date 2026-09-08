Une **chaîne de caractères** (string) est un morceau de texte : une séquence de caractères entourée de guillemets.
Python accepte à la fois les guillemets simples `'...'` et doubles `"..."`, qui fonctionnent exactement de la même façon :
```python
name = 'Ada'
language = "Python"
```
Le choix compte lorsque le texte lui-même contient un guillemet.
Une apostrophe à l'intérieur de guillemets simples terminerait la chaîne trop tôt, alors entourez ce texte de guillemets doubles à la place :
```python
print("It's sunny")  # It's sunny
```

---

La fonction intégrée `len()` renvoie la **longueur** d'une chaîne, c'est-à-dire le nombre de caractères qu'elle contient.
Les espaces et la ponctuation comptent aussi comme des caractères :
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Chaque caractère d'une chaîne a une position appelée **index**.
Les index commencent à `0`, pas à `1` : le premier caractère est à l'index `0`, le deuxième à l'index `1`, et ainsi de suite.
Écrivez l'index entre crochets après la chaîne pour lire un seul caractère :
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Demander un index qui n'existe pas, comme `word[6]`, déclenche une `IndexError`.

---

Les index peuvent aussi être **négatifs** : ils comptent depuis la fin de la chaîne.
`-1` est le dernier caractère, `-2` celui d'avant, et ainsi de suite :
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
C'est pratique car vous n'avez pas besoin de connaître la longueur de la chaîne pour atteindre sa fin.

---

Une **slice** (tranche) extrait une partie d'une chaîne.
Écrivez `[start:end]` entre crochets : le caractère à `start` est inclus, celui à `end` est **exclu** :
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
Vous pouvez omettre `start` pour découper depuis le début, ou `end` pour découper jusqu'à la fin :
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Le découpage ne déclenche jamais d'erreur : un `end` supérieur à la longueur s'arrête simplement au dernier caractère.

---

Vous savez déjà que `+` assemble deux chaînes (**concaténation**).
L'opérateur `*` **répète** une chaîne un certain nombre de fois :
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
La répétition est un moyen rapide de dessiner des séparateurs et des motifs simples.

---

L'opérateur `in` vérifie si une chaîne en **contient** une autre.
Il renvoie `True` ou `False`, donc il s'intègre naturellement dans un `if` :
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` effectue la vérification inverse.

---

Les chaînes disposent de nombreuses **méthodes** intégrées : des fonctions appelées avec un point après la chaîne.
`upper()` renvoie le texte en majuscules, `lower()` en minuscules :
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Remarquez que les méthodes **renvoient une nouvelle chaîne** : la `word` d'origine n'est pas modifiée.
`lower()` est souvent utilisé pour comparer des textes sans tenir compte de la casse : `"Yes".lower() == "yes"`.

---

Les chaînes sont **immuables** : une fois créées, leurs caractères ne peuvent pas être modifiés.
Assigner à un index déclenche une `TypeError` :
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
Pour "changer" une chaîne, vous en construisez une nouvelle, par exemple avec des slices et de la concaténation, et vous la stockez dans la variable :
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

Le texte saisi par les utilisateurs a souvent des espaces superflus autour.
La méthode `strip()` renvoie une copie de la chaîne **sans espaces au début ni à la fin** (espaces, tabulations et retours à la ligne) :
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Les espaces au milieu du texte sont conservés.
`lstrip()` supprime uniquement le côté gauche et `rstrip()` uniquement le côté droit.

---

`split()` découpe une chaîne en une **liste** de morceaux.
Sans argument, elle découpe sur les espaces ; avec un argument, elle découpe sur ce séparateur :
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` fait l'inverse : elle assemble les éléments d'une liste en une seule chaîne.
Elle s'appelle sur le **séparateur**, et la liste est l'argument :
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` renvoie une copie de la chaîne dans laquelle **chaque** occurrence de `old` est remplacée par `new` :
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Comme les chaînes sont immuables, pensez à stocker le résultat si vous voulez le conserver.

---

`find(sub)` renvoie l'**index** de la première occurrence de `sub`, ou `-1` si elle n'est pas trouvée :
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` renvoie **combien de fois** `sub` apparaît :
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` et `endswith(suffix)` renvoient `True` ou `False` selon la façon dont la chaîne commence ou se termine :
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
C'est la façon habituelle de vérifier des extensions de fichiers, des protocoles ou des préfixes.

---

Certains caractères ne peuvent pas être tapés directement dans une chaîne.
Une **séquence d'échappement** est un antislash `\` suivi d'une lettre ou d'un symbole qui représente un caractère spécial :

- `\n` un retour à la ligne
- `\t` une tabulation
- `\"` un guillemet double dans une chaîne entre guillemets doubles
- `\'` un guillemet simple dans une chaîne entre guillemets simples
- `\\` un antislash littéral

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
affiche :
```
Line 1
Line 2
She said "hi"
```
Chaque séquence d'échappement compte comme **un seul** caractère, même si vous en tapez deux.

---

Une chaîne qui s'étend sur **plusieurs lignes** peut être écrite avec des **triples guillemets** `"""..."""` (ou `'''...'''`).
Chaque retour à la ligne à l'intérieur des guillemets fait partie de la chaîne, donc vous n'avez pas besoin de `\n` :
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
affiche :
```
Roses are red,
Violets are blue
```
Les chaînes avec triples guillemets peuvent aussi contenir librement des guillemets simples et doubles.

---

Comme chaque méthode de chaîne renvoie une nouvelle chaîne, vous pouvez **enchaîner** les méthodes les unes après les autres.
Chaque appel travaille sur le résultat du précédent :
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
Une slice accepte aussi une troisième valeur, le **pas** (step).
Le pas `-1` parcourt la chaîne à l'envers, l'astuce classique pour l'inverser :
```python
print("abc"[::-1])  # cba
```

---

Un **slug** est une version d'un titre adaptée aux URL : en minuscules, sans espaces autour, et avec les mots séparés par des tirets, comme `hello-world`.
En construire un n'est qu'un enchaînement des méthodes que vous avez apprises : `strip()`, `lower()` et `replace()`.
