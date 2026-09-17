En Swift, une erreur est une **valeur**, pas un plantage. N'importe quel type peut jouer ce rôle en se conformant au protocole `Error`, et une énumération est le choix habituel parce que ses cas nomment exactement ce qui peut mal tourner :
```swift
enum LoginError: Error {
    case wrongPassword
}
```
Une fonction qui peut échouer est marquée `throws`, et elle signale l'échec avec `throw` :
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Appeler une telle fonction exige `try`, et l'appel doit se trouver dans un bloc `do` suivi d'un bloc `catch` qui indique quoi faire en cas d'échec :
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// affiche login failed
```
Quand `throw` s'exécute, le reste du bloc `do` est ignoré et `catch` prend le relais. Rien ne plante : le programme continue après le `catch`.

---

Une fonction qui peut lever une erreur peut quand même renvoyer une valeur. Le mot-clé `throws` se place entre la liste des paramètres et la flèche de retour :
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
En le lisant à voix haute : *square prend un `Int`, peut lever une erreur et renvoie un `Int`*.

Sur le site d'appel, la valeur n'existe que si rien n'a été levé, donc l'assignation se trouve dans le bloc `do` :
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
`try` n'est pas une décoration facultative : le compilateur refuse l'appel sans lui, donc un lecteur voit toujours quelles lignes peuvent échouer.

---

Un `catch` nu gère toutes les erreurs de la même manière. La plupart du temps, tu veux réagir à un échec en particulier, donc un `catch` peut porter un **motif** : le cas qu'il accepte de gérer.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift essaie les clauses `catch` de haut en bas et exécute la première dont le motif correspond.

Le dernier `catch` n'a pas de motif, et c'est exprès. Un `catch` avec motif ne couvre que le cas qu'il nomme, et Swift exige que chaque erreur soit gérée quelque part, donc un bloc `do` qui énumère des motifs a besoin d'un dernier `catch` sans motif pour ramasser le reste.

---

L'ordre compte. Swift compare la valeur levée à chaque motif `catch` dans l'ordre où ils sont écrits et s'arrête à la première correspondance, donc un `catch` sans motif placé en premier avalerait tout ce qui suit. Garde les cas spécifiques en haut et le fourre-tout en bas.

Une erreur qui ne correspond à aucun motif n'est pas ignorée : elle atterrit dans le dernier `catch` sans motif.

---

Un cas d'erreur peut transporter des données. Donne au cas des **valeurs associées** et le `throw` les remplit, pour que le gestionnaire apprenne non seulement *ce* qui a échoué mais aussi *de combien* :
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
Le `catch` correspondant lie ces valeurs avec `let` :
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
Le nom après `let` se choisit librement ; c'est une nouvelle constante disponible uniquement dans ce bloc `catch`. C'est ainsi qu'une erreur transporte un message utile sans que tu aies à coller des nombres dans des chaînes à l'endroit où l'échec se produit.

---

Une énumération contient généralement chaque manière dont une tâche unique peut échouer, un cas par raison :
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Écrire un `catch` par cas devient répétitif. Intercepte plutôt le type entier d'un coup et fais un `switch` sur la valeur :
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` signifie *intercepte tout ce qui est un `FormError`, et appelle-le `error`*. Dans le bloc, `error` a le type de l'énumération, donc le `switch` voit les cas et vérifie que tu les as tous couverts. Le dernier `catch` sans motif reste obligatoire, car un autre type d'erreur pourrait atteindre ce bloc `do`.

---

Un validateur se lit mieux quand les rejets viennent en premier et que le vrai travail reste sans indentation en bas. `guard` est fait pour cela : il énonce la condition qui doit être vraie, et son bloc `else` s'exécute quand elle ne l'est pas.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
Le bloc `else` d'un `guard` doit quitter la portée courante, et `throw` est l'une des façons de le faire, aux côtés de `return`, `break` et `continue`. Plusieurs `guard` empilés en haut d'une fonction se lisent comme la liste des règles que l'entrée doit satisfaire.

---

Parfois tu te fiches de savoir *pourquoi* quelque chose a échoué, seulement que ce soit le cas. `try?` transforme un appel qui peut lever une erreur en **optionnel** : la valeur quand il réussit, `nil` quand il lève une erreur.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
Pas de `do`, pas de `catch` : l'échec est replié dans l'optionnel que tu sais déjà déballer. Le prix à payer, c'est que la valeur de l'erreur est jetée, donc n'utilise `try?` que lorsqu'il n'y a vraiment rien à signaler.

---

Comme `try?` produit un optionnel, l'opérateur de coalescence `??` termine le travail en fournissant une valeur de repli :
```swift
let port = (try? readPort(text)) ?? 8080
```
Les parenthèses comptent. Sinon, `try?` tenterait de couvrir toute l'expression, `??` compris, et le compilateur te demande d'être explicite sur l'endroit où l'appel qui peut échouer se termine.

Lis la ligne comme une seule phrase : *utilise le port qu'on a réussi à lire, sinon 8080*. Deux lignes de `do`/`catch` se réduisent à une quand la récupération n'est vraiment qu'une valeur par défaut.

---

Il existe une troisième forme : `try!`. Il dit au compilateur *cet appel ne peut pas échouer*, donc pas de `do`, pas de `catch` et pas d'optionnel. S'il échoue quand même, le programme s'arrête immédiatement.
```swift
let pattern = try! Regex("[0-9]+")
```
C'est la forme où `try!` se justifie : l'argument est un littéral écrit par toi, dans ton propre code source, et s'il est faux, le programme est cassé et doit s'arrêter dès ta première exécution de test.

Tout ce qui arrive à l'exécution — une ligne saisie par un utilisateur, un fichier, une réponse réseau — peut être faux de façons que tu ne peux pas voir pendant que tu écris le code, et `try!` là-dessus transforme un échec récupérable en plantage devant l'utilisateur. Utilise `do`/`catch` ou `try?` dans ces cas.

---

Quand une fonction lève une erreur, tout ce qui suit le `throw` est ignoré — y compris la ligne qui devait fermer le fichier ou libérer le verrou. `defer` résout cela : il enregistre un bloc maintenant et l'exécute quand la portée courante se termine, quelle que soit la façon dont elle se termine.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
L'appel affiche `open`, puis `close`, et seulement ensuite l'erreur part vers l'appelant. Si la fonction était revenue normalement, `close` se serait quand même affiché — c'est tout l'intérêt. Place le nettoyage juste à côté de la mise en place et cesse de te demander quelle sortie le code emprunte.

---

Une portée peut enregistrer plusieurs `defer`. Ils s'exécutent dans l'ordre **inverse** : le dernier enregistré est le premier à s'exécuter.

Ce n'est pas une règle arbitraire. Les nettoyages défont généralement une mise en place qui s'est faite dans l'ordre — ouvrir le fichier, puis le verrouiller — et la défaire doit parcourir le chemin en sens inverse : déverrouiller, puis fermer. L'ordre inverse fait de chaque `defer` l'image miroir de la ligne au-dessus de lui.

---

Une fonction qui prend une fermeture a un problème : elle ne peut pas savoir si la fermeture qu'on lui remet va lever une erreur. Marquer la fonction `throws` obligerait chaque appelant à écrire `try`, même ceux qui passent une fermeture inoffensive. `rethrows` dit *je lève une erreur seulement si la fermeture que tu m'as donnée en lève une* :
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Dans le corps, tu écris quand même `try`, car l'appel peut vraiment échouer. Sur le site d'appel, le compilateur regarde la fermeture que tu as passée :
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // pas de try nécessaire
```
La bibliothèque standard utilise cela partout — `map`, `filter` et `sorted(by:)` sont tous `rethrows` — c'est pourquoi tu n'écris jamais `try` devant un `map` ordinaire.

---

Un bloc `do` n'est pas limité à un seul type d'erreur. Chaque étape peut échouer à sa manière, et chaque échec reçoit son propre `catch` :
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
Le premier `try` qui lève une erreur met fin au bloc, donc les étapes suivantes ne s'exécutent jamais — la valeur n'a tout simplement jamais existé. C'est ce qui rend cette forme lisible : le chemin heureux reste sur une seule ligne droite en haut, et chaque manière de mal tourner est listée en dessous.

---

L'endroit où se trouve le bloc `do` décide du coût d'un seul échec. Place-le **à l'intérieur** de la boucle et chaque élément obtient sa propre tentative, de sorte qu'une mauvaise valeur est ignorée et que le reste continue de s'exécuter :
```swift
for age in [4, -1, 7] {
    do {
        print(try label(age))
    } catch {
        print("skipped")
    }
}
```
Envelopper toute la boucle dans un seul `do` s'arrêterait à la première erreur et n'atteindrait jamais `7`. Aucune des deux n'est fausse — c'est la différence entre *un mauvais élément* et *abandonner*.

---

Tout dans ce chapitre répond à une seule question : qui s'occupe de l'échec ?

Une fonction qui lève une erreur refuse d'y répondre. Elle nomme ce qui a mal tourné — un cas d'une énumération `Error`, portant tout ce dont le gestionnaire aura besoin — et transmet la décision plus haut. L'appelant choisit alors un outil : `do`/`catch` pour réagir cas par cas, `try?` et `??` pour revenir à une valeur par défaut, `defer` pour nettoyer en sortant, quoi qu'il arrive.

Cette séparation est tout l'intérêt. La fonction qui détecte le problème sait rarement ce qui doit se passer ensuite, et le code qui le sait veut rarement répéter la vérification.
