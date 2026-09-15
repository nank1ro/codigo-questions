Certains travaux ne se terminent pas immédiatement : télécharger un fichier, lire dans une base de données, attendre un minuteur. Si un programme se contentait de s'arrêter et d'attendre, rien d'autre ne pourrait se passer entre-temps. Swift résout ce problème avec des **fonctions asynchrones**.

Une fonction marquée **`async`** a le droit de se mettre en pause en cours de route et de reprendre plus tard. Le mot-clé se place après la liste des paramètres, avant la flèche :
```swift
func fetchNumber() async -> Int {
    return 42
}
```
L'appel est différent lui aussi : tu dois écrire **`await`** devant l'appel. `await` marque le point exact où le programme peut se mettre en pause, et te donne la valeur telle quelle une fois la fonction terminée :
```swift
let n = await fetchNumber()
print(n)
// affiche 42
```
Dans un script Swift, le niveau supérieur prend déjà en charge `await`, tu peux donc appeler des fonctions asynchrones directement, sans aucune configuration supplémentaire. Oublier `async` ou `await` est une erreur de compilation, pas un bug silencieux.

---

Une fonction asynchrone reste une fonction ordinaire : elle peut prendre des paramètres et renvoyer une valeur de n'importe quel type. Seules deux choses changent, le mot-clé `async` dans la signature et le `await` à chaque site d'appel :
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// affiche 10.0
```
La valeur renvoyée est un `Double` normal, pas un emballage : une fois que `await` a terminé, tu travailles avec exactement comme d'habitude.

---

Les fonctions asynchrones sont généralement construites les unes sur les autres. Dans une fonction `async`, tu peux faire un `await` sur n'importe quelle autre fonction `async`, et le résultat s'utilise comme n'importe quelle valeur normale :
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// affiche 15
```
`await` n'est autorisé que dans un contexte asynchrone : une fonction `async`, ou le niveau supérieur d'un script. Une fonction ordinaire, non `async`, ne peut pas faire de `await`.

---

Le travail qui s'étire dans le temps échoue souvent : un serveur est en panne, un fichier est manquant, l'entrée est incorrecte. Une telle fonction est marquée **`async throws`**, et on l'appelle avec **`try await`** :
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
Pour gérer l'erreur, tu places l'appel dans un bloc `do` et tu l'interceptes :
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// affiche could not load
```
L'ordre des mots-clés est fixe : `try` vient en premier, puis `await`.

---

Quand tu te fiches de savoir *pourquoi* l'appel a échoué, `try?` est plus court qu'un bloc `do`. Il transforme un appel qui peut lever une erreur en **optionnel** : la valeur en cas de succès, `nil` en cas d'échec. Combiné avec `await`, il s'écrit `try? await` :
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Comme le résultat est optionnel, il s'intègre directement dans un `if let` :
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Utilise `try? await` pour une solution de repli rapide, et `do` / `catch` quand l'erreur elle-même compte.

---

Plusieurs appels avec `await` écrits l'un après l'autre s'exécutent **séquentiellement** : le deuxième appel ne démarre même pas tant que le premier n'est pas revenu. Le code se lit de haut en bas, exactement comme du code ordinaire :
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
C'est ce que tu veux quand le deuxième appel a besoin du résultat du premier. Quand les appels sont indépendants, attendre l'un avant de démarrer l'autre fait perdre du temps, et les prochains exercices montrent comment l'éviter.

---

Pour exécuter deux appels indépendants en même temps, déclare-les avec **`async let`**. Le travail démarre immédiatement, et le programme continue sans attendre :
```swift
async let left = step("A")
async let right = step("B")
```
La valeur n'est pas encore là, tu ne peux donc pas utiliser la liaison directement : tu dois faire un `await` au moment où tu en as enfin besoin. Un seul `await` devant l'expression couvre tous les `async let` qu'elle contient :
```swift
let both = await left + right
```
Si chaque appel prend une seconde, la version séquentielle a besoin de deux secondes tandis que la version `async let` n'en a besoin qu'environ d'une, car les deux appels se chevauchent.

---

Quand tu as besoin des résultats séparément, rassemble plusieurs liaisons `async let` dans un tuple et attends le tuple entier d'un coup :
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
Les deux appels tournaient déjà ; le seul `await` attend que le plus lent des deux soit terminé. Retiens que `async let` ne fait que démarrer le travail : un `async let` que tu n'attends jamais est annulé et implicitement attendu quand la portée se termine.

---

`async let` est lié à la portée où il est écrit. Pour démarrer un travail simultané et garder une référence dessus, utilise une **`Task`**. La fermeture passée à `Task { }` s'exécute de son côté, et la tâche peut être stockée, transmise ou renvoyée :
```swift
let job = Task {
    return await double(21)
}
```
Le résultat se lit plus tard avec **`.value`**, qui est attendu :
```swift
print(await job.value)
// affiche 42
```
Le type de la référence dit ce qu'elle produit et ce qu'elle peut lever : `Task<Int, Never>` est une tâche qui renvoie un `Int` et ne lève jamais d'erreur. Contrairement à `async let`, une `Task` peut être créée depuis du code ordinaire, non asynchrone.

---

`Task.sleep` met en pause la tâche courante pendant un moment sans bloquer quoi que ce soit d'autre. Elle peut être interrompue, c'est donc un appel asynchrone qui peut lever une erreur et il nécessite `try await`. La durée est donnée avec des helpers comme `.seconds`, `.milliseconds` ou `.nanoseconds` :
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
C'est la manière standard de simuler un travail lent dans un exemple, au lieu d'un vrai appel réseau. Note qu'il ne fige pas le programme : pendant qu'une tâche dort, les autres continuent de s'exécuter.

---

Maintenant, la différence entre séquentiel et simultané est mesurable. Supposons que `work` dort une seconde avant de renvoyer :
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Attendre les appels un par un prend environ **deux** secondes, car la deuxième pause ne démarre que lorsque la première est finie :
```swift
let a = await work(1)
let b = await work(2)
```
Les démarrer avec `async let` prend environ **une** seconde, car les deux pauses se chevauchent :
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Écrire `await work(1) + await work(2)` sur une seule ligne ne change rien : les deux appels sont toujours évalués l'un après l'autre. La simultanéité vient de `async let` ou des tâches, jamais de la façon dont la ligne est formatée.

---

`async let` fonctionne quand tu sais combien d'appels il y a au moment où tu écris le code. Pour une liste dont la taille n'est connue qu'à l'exécution, utilise un **groupe de tâches**.

`withTaskGroup(of:)` ouvre un groupe, `addTask` démarre une tâche enfant par élément, et le groupe est ensuite lu avec `for await`, qui délivre les résultats au fur et à mesure qu'ils se terminent :
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` déclare ce que renvoie chaque tâche enfant. Tout l'appel `withTaskGroup` est une seule expression, il a donc besoin d'un unique `await` devant lui, et il ne renvoie rien tant que chaque tâche enfant n'est pas terminée.

---

Un groupe de tâches te remet les résultats dans **l'ordre d'achèvement**, pas dans l'ordre où les tâches ont été ajoutées. La tâche enfant la plus rapide arrive en premier, donc rassembler les valeurs dans un tableau donne un ordre imprévisible.

Quand l'ordre compte, il y a deux solutions. Si les valeurs peuvent simplement être réordonnées, trie-les à la fin :
```swift
return values.sorted()
```
Si chaque résultat appartient à une position, fais renvoyer à chaque tâche une paire `(index, value)` et écris-la dans un tableau préparé :
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
Une somme, un maximum ou un comptage n'a besoin d'aucune de ces solutions, car l'ordre des valeurs ne change pas la réponse.
