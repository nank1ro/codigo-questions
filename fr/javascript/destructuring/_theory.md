Lire les valeurs d'un tableau un index à la fois est fastidieux :
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
La **déstructuration** fait le même travail en une ligne. À gauche du `=`, vous écrivez un motif qui ressemble au tableau lui-même, et chaque nom à l'intérieur reçoit l'élément à la même position :
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
Le motif n'a pas besoin de couvrir tout le tableau : les éléments en trop sont simplement ignorés, et un nom sans élément correspondant devient `undefined`.

---

La déstructuration est la plus utile au moment même où un tableau arrive : un argument de fonction, ou le résultat d'un appel. Au lieu de garder le tableau sous la main et de l'indexer partout, vous le déballez une seule fois et donnez de vrais noms à ses parties :
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
Rien n'est copié ni modifié dans le tableau d'origine, le motif ne fait qu'y lire.

---

Parfois, un seul élément au plus profond du tableau compte. Vous pouvez laisser une position vide dans le motif, en gardant la virgule qui la sépare : une telle position vide s'appelle un **trou**, et il saute l'élément sans le nommer :
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
Comptez les virgules, pas les noms : chaque virgule fait avancer le motif d'une position, qu'un nom se trouve ou non devant elle.

---

Un tableau n'est pas toujours aussi long que le motif ne l'attend. Écrire `= value` après un nom lui donne une valeur **par défaut**, utilisée chaque fois que le tableau n'a rien à cette position :
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
La valeur par défaut n'est évaluée que lorsqu'elle est nécessaire, elle peut donc même être un appel de fonction, et une valeur par défaut peut être donnée à n'importe quelle position, pas seulement à la dernière.

---

Un motif peut aussi se trouver à gauche d'une affectation simple, sans `const` ni `let` devant, et il écrit alors dans des variables qui existent déjà. Cela transforme l'échange de deux valeurs en une seule ligne, sans variable temporaire :
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
Le côté droit est construit en premier, donc les deux anciennes valeurs sont déjà en sécurité dans le tableau temporaire quand l'affectation a lieu. Attention au point-virgule de la ligne précédente : une ligne qui commence par `[` serait sinon lue comme un index de ce qui précède.

---

Les objets peuvent aussi être déstructurés, avec des accolades au lieu de crochets. Ici la position ne signifie rien : chaque nom est confronté à la **clé** qui s'écrit de la même façon :
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
Permuter `age` et `name` dans le motif ne change rien, et les clés que le motif ne mentionne pas sont simplement laissées de côté. Un nom sans clé correspondante devient `undefined`.

---

Les motifs d'objets et les valeurs par défaut se combinent exactement comme ceux des tableaux, ce qui en fait une façon élégante de lire un objet de configuration dont les clés sont présentes ou non :
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
Puisque le motif entier ne fait qu'une instruction, une fonction peut déballer tout ce dont elle a besoin depuis son argument dès sa toute première ligne.

---

Un motif d'objet nomme ses variables d'après les clés, ce qui est gênant quand les clés sont obscures ou déjà prises. Écrire `key: newName` **renomme** la variable :
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
Lisez-le comme « prends `n`, appelle-le `name` ». Les deux-points ne déclarent pas un type, et `n` lui-même n'est jamais créé comme variable, seul `name` l'est. Un nom renommé peut toujours recevoir une valeur par défaut, écrite après lui : `{ n: name = "unknown" }`.

---

Les valeurs par défaut ont une règle qui surprend tout le monde : elles ne s'appliquent **qu'à** `undefined`. Une clé qui existe et contient `null`, `0`, `""` ou `false` est une vraie valeur, donc le motif la prend et la valeur par défaut n'est jamais utilisée :
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null` se comporte ici de la même façon que `0`, même s'il signifie souvent « aucune valeur » dans une réponse d'API. Quand `null` doit aussi être remplacé, déstructurez d'abord et retombez ensuite sur une valeur avec `??`.

---

Là où une clé contient un autre objet ou un tableau, le motif peut simplement continuer et décrire cette forme aussi :
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
Attention à ce que cette ligne crée : `address: { city }` signifie « va dans `address` », pas « donne-moi `address` », donc seul `city` devient une variable. Pour obtenir les deux, mentionnez la clé deux fois : `const { address, address: { city } } = user;`. Les motifs de tableaux et d'objets s'imbriquent librement l'un dans l'autre, comme dans `{ tags: [first] }`.

---

Prendre la tête d'un tableau et garder la queue est un besoin si courant que les motifs ont leur propre syntaxe pour cela. Trois points devant le dernier nom en font un **élément rest** (rest), et il rassemble tous les éléments restants dans un tout nouveau tableau :
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
Un élément rest doit venir en dernier dans le motif et ne peut pas avoir de valeur par défaut : quand il ne reste rien, c'est simplement un tableau vide.

---

Les motifs d'objets ont aussi un rest, et là il rassemble toutes les clés que le motif n'a pas mentionnées dans un nouvel objet :
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
C'est la façon la plus courte de construire une copie d'un objet sans une de ses clés : l'original n'est jamais touché, et l'objet rest est neuf et contient les valeurs restantes.

---

Un motif peut remplacer un nom de paramètre dans une déclaration de fonction, si bien que le déballage a lieu au moment de l'appel :
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
Dans le corps, il n'y a pas du tout de variable objet, seulement `width` et `height`. L'appelant passe un seul objet, mais la signature documente exactement quelles clés la fonction lit, et les clés peuvent arriver dans n'importe quel ordre.

---

Un paramètre déstructuré avec des valeurs par défaut fait un bel objet d'options, mais il casse toujours quand l'appelant ne passe rien : lire une clé sur `undefined` lève une `TypeError`. Donner au motif entier une valeur par défaut de `{}` corrige le problème :
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
Lisez la ligne de l'extérieur vers l'intérieur : `= {}` fournit un objet vide quand l'argument est absent, et chaque valeur par défaut interne remplit ensuite sa propre clé.

---

`Object.entries(obj)` transforme un objet en un tableau de paires `[key, value]`. Placez un motif de tableau dans la tête d'une boucle `for...of` et chaque paire est déballée pendant que la boucle tourne :
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
C'est la façon lisible de parcourir un objet : pas d'index, pas de recherche, juste les deux noms qui vous importent. `Object.keys` et `Object.values` ne donnent chacun qu'un seul côté, `Object.entries` donne les deux.

---

Tout ce qui a été vu jusqu'ici appartient à une seule syntaxe, donc les pièces se combinent librement : un motif d'objet peut imbriquer un autre motif d'objet, qui peut contenir une clé renommée avec une valeur par défaut, à côté d'un motif de tableau se terminant par un élément rest. Une ligne décrit alors toute la forme qu'une fonction attend :
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
Gardez-le lisible : un motif qui ne tient plus sur quelques lignes est généralement le signe que la fonction en demande trop.
