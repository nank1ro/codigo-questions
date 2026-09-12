Une **expression régulière** (ou **regex**) est un petit motif qui décrit une forme de texte : « quatre chiffres », « un mot suivi de `@` », « tout ce qui se trouve entre guillemets ». En Kotlin un motif est un objet `Regex`, construit de deux façons équivalentes :
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
La plupart des caractères d'un motif représentent eux-mêmes, mais quelques-uns sont des **raccourcis** :
- `\d` est n'importe quel chiffre, écrit `"\\d"` dans une chaîne Kotlin car `\` doit être échappé
- `[a-z]` est n'importe quelle lettre minuscule, et `[abc]` est `a`, `b` ou `c`
- `+` après un élément signifie « au moins une fois », donc `\d+` est une suite de chiffres

La question la plus simple que vous puissiez poser est `matches`, qui vaut `true` uniquement quand le motif décrit la chaîne **entière** :
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, la lettre n'est pas un chiffre
```

---

`matches` est souvent trop strict : en général vous voulez seulement savoir si le motif apparaît **quelque part** dans le texte. C'est le rôle de `containsMatchIn` :
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, la chaîne entière n'est pas des chiffres
println(digits.containsMatchIn("order 42"))  // true, « 42 » s'y trouve
```
À côté de `\d` il y a deux autres raccourcis que vous utiliserez sans cesse : `\w` est un caractère de mot (lettre, chiffre ou `_`) et `\s` est un caractère d'espacement. Chacun peut être répété avec un **quantificateur** :
- `+` un ou plusieurs
- `*` zéro ou plusieurs
- `?` zéro ou un
- `{3}` exactement trois, `{2,4}` de deux à quatre

Doubler chaque barre oblique inverse devient vite bruyant, donc les motifs sont généralement écrits comme des **chaînes brutes** avec triple guillemet, où `\` n'est qu'un caractère :
```kotlin
val digits = Regex("""\d+""") // identique à Regex("\\d+")
```

---

`containsMatchIn` dit seulement *si* le motif s'y trouve. `find` dit aussi **quoi** et **où** : il renvoie la première correspondance sous forme de `MatchResult`, ou `null` quand il n'y a rien à trouver.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` est le texte correspondant et `range` les indices qu'il couvre dans la chaîne d'origine. Comme le résultat est nullable vous y accédez avec l'appel sûr `?.`, qui donne `null` au lieu de planter quand aucune correspondance n'a été trouvée :
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Les parenthèses dans un motif créent un **groupe de capture** : une portion de la correspondance que vous voulez relire séparément. `MatchResult.groupValues` les contient, avec l'indice `0` pour la correspondance entière et `1`, `2`, ... pour les groupes, de gauche à droite :
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
Quand il n'y a aucune correspondance, `find` renvoie `null` et il n'y a rien à lire, donc une fonction qui extrait un groupe décide généralement quoi retourner dans ce cas :
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Compter les parenthèses pour découvrir que l'hôte est le groupe `2` devient fragile dès que le motif grandit. Un groupe peut recevoir un **nom** avec `(?<name>...)` et être lu depuis `groups` par ce nom :
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` renvoie le groupe sous forme de `MatchGroup?`, donc vous demandez quand même son `.value`. Un groupe nommé est aussi numéroté comme d'habitude, donc `groupValues[1]` continue de fonctionner à côté.

---

`find` s'arrête à la première correspondance. `findAll` renvoie **toutes** les correspondances, sous forme de `Sequence<MatchResult>` : une chaîne paresseuse que vous pouvez traiter comme une liste avec `map`, `filter`, `count` et `toList`.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
Quand rien ne correspond, `findAll` renvoie une séquence vide au lieu de `null`, donc il n'y a pas d'appel sûr à écrire. Afficher la séquence elle-même n'est pas utile, elle montre l'objet, pas les correspondances : transformez-la d'abord en liste.

---

`replace` réécrit le texte : il renvoie une **nouvelle** chaîne où chaque correspondance est remplacée par la substitution, en laissant l'original intact.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
Dans la chaîne de remplacement, `$1`, `$2`, ... représentent les groupes capturés de cette correspondance, donc vous pouvez réordonner ou réutiliser les morceaux trouvés :
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` est la correspondance entière. Si vous avez besoin d'un `$` littéral dans le remplacement, échappez-le avec `\$`.
`replace` réécrit **toutes** les correspondances, donc quand seule une chaîne complète doit être réécrite, ancrez le motif avec les **ancres** `^` (début du texte) et `$` (fin du texte) :
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, rien n'est remplacé
```

---

Une chaîne de remplacement ne peut que réarranger les morceaux qu'on lui donne. Quand le nouveau texte doit être **calculé**, passez plutôt une lambda à `replace` : elle reçoit le `MatchResult` et renvoie la chaîne qui prend sa place.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Dans la lambda vous avez le `MatchResult` complet, donc `m.value`, `m.range` et `m.groupValues` sont tous disponibles. Notez que `$1` n'a aucun sens ici : c'est un caractère ordinaire dans la chaîne que vous renvoyez.

---

`split` coupe une chaîne partout où le motif correspond et renvoie les morceaux sous forme de `List<String>`. Contrairement à une séparation sur une chaîne délimiteur fixe, un séparateur regex peut décrire toute une famille de séparateurs :
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
Les séparateurs trouvés ne font pas partie du résultat. Si le texte commence ou se termine par un séparateur, le morceau voisin est vide :
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` accepte un `limit` en second argument pour s'arrêter après un nombre donné de morceaux, en laissant le reste intact dans le dernier.

---

Les motifs sont sensibles à la casse : `Regex("kotlin")` ne correspond pas à `"Kotlin"`. Au lieu d'écrire `[kK][oO]...`, passez une option en second argument :
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
L'option appartient au `Regex`, donc chaque méthode de cet objet la respecte : `matches`, `find`, `findAll`, `replace` et `split` aussi. Les autres options utiles sont `RegexOption.MULTILINE`, qui fait correspondre `^` et `$` à chaque ligne, et `RegexOption.DOT_MATCHES_ALL`. Pour les combiner, passez un ensemble : `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` correspond aussi au `cat` à l'intérieur de `catalog`. Pour exiger un mot entier, utilisez la **limite de mot** `\b` : elle correspond à la position vide entre un caractère de mot et tout le reste, y compris le début et la fin du texte.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
Un motif est une chaîne ordinaire, donc il peut être construit à partir de morceaux à l'exécution :
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

Les caractères `. * + ? ( ) [ ] { } | ^ $ \` ont un sens spécial à l'intérieur d'un motif. Le plus piégeux est `.`, qui correspond à **n'importe quel** caractère, pas à un point. Pour désigner le caractère lui-même, échappez-le avec une barre oblique inverse :
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, le point correspond au x
println(Regex("""3\.14""").matches("3x14")) // false
```
Quand le texte à chercher provient d'une variable et doit être pris littéralement, laissez la bibliothèque faire l'échappement avec `Regex.escape` :
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` et les groupes transforment ensemble une ligne de texte en données structurées. Chaque `MatchResult` de la séquence porte ses propres `groupValues`, donc une seule chaîne peut construire une liste, une map ou un total :
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` construit une map à partir des paires `key to value` renvoyées par la lambda. Quand un motif a un nombre fixe de groupes, `destructured` vous permet de les déballer dans des variables nommées au lieu de les lire par indice :
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Les crochets définissent une **classe de caractères** : un seul caractère parmi l'ensemble listé. À l'intérieur vous pouvez utiliser des plages, et un `^` en tête nie toute la classe :
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, aucun chiffre autorisé
```
Une classe ne choisit qu'entre des caractères uniques. Pour choisir entre des alternatives entières, utilisez `|`, généralement enveloppé dans un groupe pour qu'il n'avale pas le reste du motif :
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Comme `findAll` donne une séquence, les méthodes d'agrégation que vous connaissez déjà fonctionnent aussi sur les correspondances : `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Extraire des nombres d'un texte libre est un travail en deux étapes : les trouver, puis convertir le texte en nombre.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

Un motif réaliste mélange généralement tout à la fois : des groupes pour garder les parties dont vous avez besoin, un `\.` échappé pour les points littéraux, et un remplacement par lambda pour reconstruire le texte autour d'eux.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Gardez les motifs aussi simples que le travail le permet : un motif qui essaie de décrire toutes les adresses e-mail légales est illisible, tandis que `\w+@\w+\.\w+` suffit pour trouver les adresses dans une phrase.
