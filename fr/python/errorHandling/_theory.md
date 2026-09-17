Une **exception** est la façon dont Python indique qu'une instruction ne peut pas être exécutée. Diviser par zéro, convertir `"abc"` en entier ou lire une clé de dictionnaire absente lèvent tous une exception. Quand rien ne la gère, le programme s'arrête immédiatement et affiche une **traceback** :
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
La traceback liste les lignes qui étaient en cours d'exécution, et la dernière ligne indique le **type d'exception** (`ZeroDivisionError`) et son message (`division by zero`). C'est cette dernière ligne qu'il faut lire en premier.

Pour garder le programme en vie, placez l'instruction risquée dans un bloc `try` et décrivez la récupération dans un bloc `except` :
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python exécute le bloc `try` ; si l'exception nommée est levée, il saute directement au bloc `except` correspondant et poursuit avec le reste du programme.

---

Le bloc `try` s'arrête à la **première** instruction qui lève une exception ; les lignes qui suivent sont ignorées et le contrôle passe au bloc `except`. Rien dans le bloc `try` n'est annulé, gardez-le donc aussi court que possible :
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
Un `return` à l'intérieur d'un `except` fonctionne comme n'importe quel autre `return`, ce qui fait de `try`/`except` un moyen naturel de renvoyer une valeur de secours au lieu de planter.

---

Une exception qu'aucun bloc `except` ne gère continue de se propager : hors de la ligne, hors de la fonction qui l'a exécutée, hors de son appelant, et ainsi de suite. Si rien ne l'intercepte avant le sommet du programme, Python affiche la traceback et le processus se termine avec un code de sortie non nul. Les lignes qui suivent l'instruction défaillante ne s'exécutent jamais.

---

Une clause `except` n'intercepte que le type qu'elle nomme, et ses sous-classes. C'est tout l'intérêt : tout le reste continue de se propager, de sorte qu'un bug auquel vous ne vous attendiez pas apparaît toujours sous forme de traceback au lieu d'être avalé.

`int(text)` lève une **`ValueError`** quand le texte ne décrit pas un nombre entier, c'est donc le type à nommer lors de la lecture d'une saisie utilisateur :
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
Nommer `ValueError` ici est une décision, pas une formalité : `int(None)` lève une `TypeError`, que cette fonction ne capture délibérément **pas**, parce que passer `None` est une erreur de programmation qui doit être vue.

---

Choisir le type le plus étroit qui couvre la défaillance attendue est ce qui rend la gestion des erreurs digne de confiance. Une fonction qui lit du texte doit se remettre d'un texte invalide (`ValueError`) mais ne doit pas masquer le fait d'être appelée avec le mauvais type d'argument (`TypeError`) — cette erreur appartient à l'appelant, laissez-la passer.

---

Un bloc `try` peut être suivi de **plusieurs** clauses `except`, chacune gérant une défaillance différente avec une récupération différente. Python compare l'exception levée à ces clauses de haut en bas et exécute la **première** qui correspond ; les autres sont ignorées :
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Comme la première correspondance gagne, l'ordre compte quand les types sont liés : une clause pour un type général placée au-dessus d'une clause pour un type plus spécifique gagnerait toujours, rendant la clause spécifique inaccessible.

---

Quand plusieurs défaillances méritent la **même** récupération, les lister sous forme de tuple dans une seule clause est plus court que de répéter le bloc :
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
Les parenthèses sont obligatoires : `except ValueError, ZeroDivisionError:` est une erreur de syntaxe en Python 3. Un tuple reste une liste explicite de types.

---

Un `except:` sans type après lui est un **bare except** (« except nu »). Il correspond à tout, y compris aux exceptions qui n'ont rien à voir avec l'opération que vous protégiez, donc la règle est simple : nommez toujours les types dont vous pouvez réellement vous remettre.

---

Une exception est un objet, et `as` la lie à un nom pour que le gestionnaire puisse l'examiner :
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — ce qu'utilisent `print(e)` et un emplacement de f-string — donne le message avec lequel l'exception a été construite, et `type(e).__name__` donne le nom de la classe sous forme de texte. Le nom lié par `as` n'existe qu'à l'intérieur du bloc `except` ; Python le supprime quand le bloc se termine.

---

Un bloc `try` peut être suivi d'un bloc `else`, qui s'exécute **uniquement quand le bloc `try` s'est terminé sans lever d'exception** :
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
Placer `print(number * 2)` dans le bloc `try` fonctionnerait aussi, mais alors une `ValueError` levée par l'affichage lui-même serait confondue avec un échec de conversion. `else` limite le bloc `try` à la seule instruction protégée, et regroupe tout ce qui doit se passer en cas de succès.

---

Un bloc `finally` s'exécute **quoi qu'il arrive** : après un bloc `try` sans incident, après un bloc `except`, même pendant qu'une exception que personne n'a interceptée se propage, et même quand le bloc `try` ou `except` exécute un `return` :
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Les deux chemins affichent `done` avant que la valeur ne quitte la fonction. Cette garantie est la raison d'être de `finally` : fermer un fichier, libérer un verrou, restaurer un paramètre. La forme complète est `try` / `except` / `else` / `finally` ; un `try` a besoin d'au moins un `except` ou d'un `finally`, et `else` ne fonctionne qu'accompagné d'un `except`.

---

Votre propre code peut aussi lever des exceptions, avec l'instruction `raise` suivie d'un objet exception :
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` arrête la fonction immédiatement, exactement comme le ferait une défaillance intégrée. Renvoyer une valeur d'erreur à la place — `-1`, `None`, `False` — est facile à oublier pour un appelant ; une exception ne peut pas être ignorée par accident.

Choisissez le type qui décrit le problème : `ValueError` quand l'argument a le bon type mais une valeur impossible, `TypeError` quand il a carrément le mauvais type. Le texte passé à l'exception est son message.

---

Une poignée d'exceptions intégrées couvre la plupart des défaillances du quotidien :

| Exception | Levée quand | Exemple |
|---|---|---|
| `ValueError` | le type est bon mais la valeur est impossible | `int("abc")` |
| `TypeError` | le type lui-même est erroné | `"x" + 1` |
| `ZeroDivisionError` | une division ou un modulo a un diviseur nul | `1 / 0` |
| `KeyError` | un dictionnaire n'a pas une telle clé | `{"a": 1}["b"]` |
| `IndexError` | un index de séquence est hors de portée | `[1, 2][5]` |

Utiliser l'une d'elles au lieu d'inventer un nouveau type garde vos erreurs lisibles pour quiconque connaît Python.

---

Parfois, un gestionnaire doit réagir à une défaillance sans en prendre la responsabilité : l'enregistrer, la compter, fermer quelque chose — puis laisser l'appelant s'en occuper. Un `raise` seul à l'intérieur d'un bloc `except` **relance** l'exception en cours de traitement, avec son type, son message et sa traceback d'origine intacts :
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
Écrire `raise ValueError(...)` à la place créerait une nouvelle exception avec sa propre traceback — ce ne serait plus la même défaillance que celle que vous avez interceptée, ce qui est exactement ce qu'un `raise` seul préserve.

---

Quand aucun type intégré ne convient, définissez le vôtre en le faisant hériter de `Exception`. Un corps vide suffit généralement — le nom est le message pour le lecteur :
```python
class ConfigError(Exception):
    pass
```
Elle se comporte comme n'importe quelle autre exception : `raise ConfigError("bad port")`, et `except ConfigError:` l'intercepte.

Traduire une défaillance de bas niveau dans votre propre type est courant, et l'erreur d'origine ne doit pas se perdre dans le processus. `raise NewError(...) from original` les **chaîne** : il stocke `original` dans l'attribut `__cause__` de la nouvelle exception, et la traceback affiche les deux sous *The above exception was the direct cause of the following exception* :
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
Sans `from e`, les deux restent liés implicitement, mais `from` dit explicitement que la première erreur a causé la seconde.
