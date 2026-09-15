Une **expression régulière** (ou **regex**) est un petit motif qui décrit une forme de texte. Tu l'utilises pour répondre à des questions comme « cette chaîne contient-elle un nombre ? » ou « où apparaît le mot `cat` ? ».

En JavaScript, la façon la plus courte d'en écrire une est un **littéral de regex** : le motif entre deux barres obliques.
```javascript
const pattern = /cat/;
```
Les caractères ordinaires d'un motif correspondent à eux-mêmes, donc `/cat/` correspond aux trois lettres `c`, `a`, `t` où qu'elles se trouvent dans une chaîne.

La chose la plus simple à faire avec un motif est de demander s'il apparaît dans une chaîne. La méthode **`test`** prend le texte et renvoie `true` ou `false` :
```javascript
console.log(/cat/.test("the cat sleeps"));
// affiche true
console.log(/cat/.test("the dog sleeps"));
// affiche false
```
Note que `test` cherche le motif *quelque part* dans la chaîne ; toute la chaîne n'a pas besoin de correspondre.

---

Les motifs deviennent utiles quand ils décrivent un *type* de caractère au lieu d'un caractère exact. Quelques **séquences d'échappement** couvrent la plupart des besoins :
- `\d` n'importe quel chiffre, de `0` à `9`
- `\w` n'importe quel caractère de mot : une lettre, un chiffre ou `_`
- `\s` n'importe quel espace : une espace, une tabulation, un retour à la ligne

```javascript
console.log(/\d/.test("room 12"));
// affiche true
console.log(/\d/.test("lobby"));
// affiche false
```
Un **quantificateur** indique combien de fois le morceau précédent peut se répéter. Le plus courant est `+`, qui signifie « un ou plus » :
```javascript
console.log(/\d+/.test("42"));
// affiche true
```
Ainsi `/\d/` correspond à un seul chiffre et `/\d+/` correspond à une suite de chiffres. Pour un simple `test` les deux se comportent pareil, car il suffit à chacun qu'un chiffre soit présent.

---

Un littéral comme `/\d+/` est figé dès que tu l'écris. Quand le motif doit être **construit à l'exécution**, utilise le **constructeur `RegExp`**, qui prend le motif sous forme de chaîne :
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// affiche true
```
Il y a un piège. Dans une chaîne, un antislash commence une séquence d'échappement pour la *chaîne*, donc il disparaît avant que la regex ne le voie jamais. Pour mettre un vrai antislash dans le motif, tu dois le doubler :
```javascript
const digits = new RegExp("\\d+");
// le même motif que /\d+/
```
Écrire `new RegExp("\d+")` à la place donne le motif `/d+/`, qui correspond à la lettre `d`, pas à un chiffre.

Préfère le littéral quand le motif est connu au moment où tu écris le code ; il est plus court et n'a pas besoin d'antislashs doublés.

---

Deux autres briques te permettent de décrire presque n'importe quelle forme de texte.

Une **classe de caractères** est un ensemble de caractères entre crochets ; elle correspond à exactement l'un d'entre eux. Un tiret écrit un intervalle, et un `^` au début nie l'ensemble :
```javascript
/[aeiou]/   // une voyelle
/[a-z]/     // une lettre minuscule
/[A-Z0-9]/  // une lettre majuscule ou un chiffre
/[^0-9]/    // un caractère qui n'est pas un chiffre
```
Les **quantificateurs** disent combien de fois le morceau précédent se répète : `+` un ou plus, `*` zéro ou plus, `?` zéro ou un, et `{n}` exactement `n` fois.

Enfin, les **ancres** attachent le motif aux extrémités du texte : `^` signifie « commence ici » et `$` signifie « finit ici ». Sans elles un motif peut correspondre n'importe où dans la chaîne, donc `/\d{2}/.test("abc12def")` vaut `true`. Avec les deux ancres toute la chaîne doit correspondre :
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// affiche false
console.log(/^\d{2}$/.test("12"));
// affiche true
```

---

`test` ne dit que oui ou non. Pour obtenir le texte correspondant lui-même, appelle **`match`** sur la chaîne :
```javascript
const match = "order 42 shipped".match(/\d+/);
```
Quand rien ne correspond, `match` renvoie `null`. Quand quelque chose correspond, il renvoie un résultat semblable à un tableau :
- `match[0]` est le texte qui a correspondu
- `match.index` est la position où la correspondance commence
- `match.input` est toute la chaîne qui a été parcourue

```javascript
console.log(match[0]);
// affiche 42
console.log(match.index);
// affiche 6
```
Comme le résultat peut être `null`, vérifie-le avant de lire `match[0]`.

---

Comme `match` renvoie `null` quand le motif est absent, lire `match[0]` directement lève `TypeError: Cannot read properties of null`. Protège-le :
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
L'opérateur de coalescence des nuls écrit la même protection sur une ligne, car `match?.[0]` vaut `undefined` quand `match` vaut `null` :
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Des parenthèses autour d'une partie d'un motif créent un **groupe de capture** : le texte que cette partie a correspondu est mis de côté pour que tu puisses le relire.

Les groupes apparaissent après `match[0]`, numérotés de gauche à droite par leur parenthèse ouvrante :
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// affiche 2026-09-12
console.log(match[1]);
// affiche 2026
console.log(match[3]);
// affiche 12
```
Ainsi `match[0]` est toujours toute la correspondance, et `match[1]`, `match[2]`, ... sont les groupes. Un groupe qui fait partie d'un motif qui ne correspond pas du tout fait renvoyer `null` à tout le `match`.

---

Ne capture que ce dont tu as besoin. Un groupe n'est pas seulement un moyen de relire un morceau ; il indique aussi au lecteur quelle partie du motif compte. Dans un motif d'heure où tu ne veux que les minutes, groupe les minutes seules et laisse le reste sans groupe :
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// affiche 35
```
Tout le motif doit quand même correspondre, donc les heures et les secondes restent obligatoires ; elles ne sont simplement pas capturées. Moins de groupes signifient moins de numéros à suivre quand tu lis `match[1]`, `match[2]` et ainsi de suite.

---

Compter les parenthèses devient fatigant, et ajouter un groupe au milieu d'un motif renumérote tout ce qui le suit. Un **groupe nommé** évite les deux problèmes : écris `?<nom>` juste après la parenthèse ouvrante et relis le morceau depuis `match.groups` :
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// affiche 2026
console.log(match.groups.month);
// affiche 09
```
Les groupes nommés restent numérotés, donc `match[1]` continue de fonctionner, mais `match.groups.year` dit ce que la valeur signifie. Quand le motif n'a aucun groupe nommé, `match.groups` vaut `undefined`.

---

Tout ce qui précède s'arrêtait à la première correspondance. Les **flags**, écrits après la barre oblique fermante d'un littéral, changent cela et d'autres détails de la recherche :
- `g` global : trouve chaque correspondance, pas seulement la première
- `i` ignore la casse, donc `/cat/i` correspond aussi à `Cat` et à `CAT`

Avec le flag `g`, `match` se comporte différemment : il renvoie un simple tableau des **chaînes** correspondantes, sans `index` et sans groupes, ou `null` quand il n'y a pas de correspondance :
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// affiche [ '1', '22', '333' ]
console.log(numbers.length);
// affiche 3
```
Les flags peuvent être combinés dans n'importe quel ordre, comme dans `/cat/gi`. Avec le constructeur `RegExp` ils vont dans le second argument : `new RegExp("\\d+", "g")`.

---

Le flag `g` te donne chaque chaîne correspondante, mais il jette les groupes. Quand tu as besoin des groupes de *chaque* correspondance, utilise **`matchAll`**. Il renvoie un itérateur d'objets de correspondance complets, chacun exactement comme le résultat d'un `match` simple :
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// affiche a -> 1
// affiche b -> 2
```
`matchAll` exige le flag `g` ; sans lui, il lève une `TypeError`. Comme il renvoie un itérateur, étale-le avec `[...text.matchAll(pattern)]` quand tu veux un vrai tableau, et note qu'il ne produit rien du tout quand le motif ne correspond jamais.

---

**`replace`** renvoie une nouvelle chaîne dans laquelle la correspondance est remplacée par autre chose. La chaîne d'origine n'est jamais modifiée.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// affiche the dog sleeps
```
Dans la chaîne de remplacement, quelques séquences ont un sens spécial :
- `$1`, `$2`, ... le texte capturé par le groupe 1, le groupe 2, ...
- `$<name>` le texte capturé par un groupe nommé
- `$&` toute la correspondance

C'est ce qui fait de `replace` un outil de réécriture et pas seulement un échange :
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// affiche 12/09/2026
```
Sans le flag `g` seule la **première** correspondance est remplacée.

---

Pour réécrire **chaque** correspondance au lieu de la première, tu as deux options :
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// affiche a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// affiche a# b#
```
**`replaceAll`** est le plus clair des deux, et il accepte aussi une simple chaîne comme motif. Quand tu lui donnes une regex, cette regex **doit** porter le flag `g`, sinon il lève une `TypeError` ; c'est exactement ce qui empêche le bug silencieux d'écrire `replace` et de ne corriger que la première correspondance.

---

Le remplacement ne doit pas forcément être une chaîne. Quand tu passes une **fonction**, elle est appelée une fois par correspondance et tout ce qu'elle renvoie est inséré à la place de cette correspondance.

La fonction reçoit d'abord toute la correspondance, puis chaque groupe de capture:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// affiche 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// affiche Ann Lee
```
C'est le seul moyen de calculer le remplacement à partir du texte correspondant, ce que `$1` seul ne peut pas faire.

---

**`split`** coupe une chaîne en un tableau. Avec une simple chaîne il coupe sur ce texte exact, mais avec une regex il coupe à chaque correspondance du motif, ce qui permet à un seul appel de gérer des séparateurs qui varient :
```javascript
console.log("a, b;c".split(", "));
// affiche [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// affiche [ 'a', 'b', 'c' ]
```
Les séparateurs eux-mêmes ne font pas partie du résultat. Méfie-toi d'un séparateur au début ou à la fin de la chaîne : il produit une chaîne vide dans le tableau, car il y a un champ vide de ce côté.

---

Un dernier flag complète la collection. Par défaut `^` et `$` signifient le début et la fin de **toute la chaîne**, donc un motif ancré avec `^` ne peut correspondre qu'au tout début, même quand le texte a plusieurs lignes.

Le flag **`m`** (multiline) change cela : `^` et `$` correspondent alors aussi juste après et juste avant chaque retour à la ligne, donc chaque ligne est ancrée à son compte :
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// affiche [ 'note a' ]
console.log(text.match(/^note.*/gm));
// affiche [ 'note a', 'note c' ]
```
Deux détails comptent ici. Par défaut le `.` ne correspond pas à un retour à la ligne (seul le flag `s` change cela), donc `.*` s'arrête à la fin de la ligne de lui-même. Et `match` avec le flag `g` renvoie `null`, pas un tableau vide, quand rien ne correspond, donc associe-le à `?? []` quand tu promets de renvoyer un tableau.
