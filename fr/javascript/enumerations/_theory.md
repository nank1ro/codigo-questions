Une **énumération** (ou *enum*) est un type commun pour un petit groupe de valeurs fixes et liées : les jours de la semaine, les couleurs d'un jeu de cartes, les états possibles d'une commande.
Contrairement à de nombreux langages, JavaScript **n'a pas** de mot-clé `enum`. Le remplacement idiomatique est un simple objet dont les propriétés sont les membres, passé à `Object.freeze()` pour que personne ne puisse le modifier ensuite :
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// affiche red
```
Par convention, l'objet est déclaré avec `const`, son nom commence par une majuscule et les noms des membres sont écrits en `UPPER_CASE`, exactement comme les autres constantes.

---

La valeur stockée dans chaque membre dépend de vous. Les **chaînes de caractères** sont le choix le plus courant car elles sont lisibles lorsqu'elles sont affichées, journalisées ou enregistrées dans un fichier :
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// affiche done
```
Une fois gelé, l'objet ne peut plus non plus recevoir de nouvelles propriétés, et `Object.isFrozen(obj)` vous indique si un objet a été gelé :
```javascript
console.log(Object.isFrozen(Status));
// affiche true
```

---

Pourquoi geler l'objet ? Un objet gelé rejette tout changement : assigner une valeur à un membre existant, en ajouter un nouveau ou en supprimer un n'a aucun effet.
La façon dont le rejet se manifeste dépend du mode dans lequel votre code s'exécute :
- en **mode permissif** (*sloppy mode*, le mode par défaut pour les scripts simples), l'assignation est **ignorée silencieusement**
- en **mode strict** (fichiers commençant par `"use strict"`, modules ES et corps de classe), une `TypeError` est **levée**

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// affiche s
console.log(Size.MEDIUM);
// affiche undefined
```
Dans les deux cas, l'énumération conserve les valeurs que vous avez définies, ce qui est exactement ce que l'on attend d'un ensemble de constantes.

---

Les membres peuvent aussi contenir des **nombres**. Les valeurs numériques sont pratiques quand les membres ont un ordre naturel, car vous pouvez les comparer avec les opérateurs habituels :
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// affiche true
```
Le compromis est la lisibilité : afficher `Priority.HIGH` montre `3`, ce qui vous en dit beaucoup moins que la chaîne `"high"`.

---

Comme une énumération est simplement un objet, les outils habituels des objets vous permettent de l'inspecter :
- `Object.keys(Enum)` renvoie un tableau avec les **noms** des membres
- `Object.values(Enum)` renvoie un tableau avec les **valeurs** des membres
- `Object.entries(Enum)` renvoie un tableau de paires `[name, value]`

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// affiche [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// affiche [ 'red', 'blue' ]
```
Combiner `Object.values()` avec la méthode de tableau `includes()` est le moyen standard de vérifier si une valeur arbitraire, par exemple une valeur lue depuis une saisie utilisateur, est un membre valide :
```javascript
console.log(Object.values(Color).includes("red"));
// affiche true
console.log(Object.values(Color).includes("pink"));
// affiche false
```

---

Les énumérations se marient naturellement avec l'instruction `switch`, qui compare une valeur à une liste d'étiquettes `case` et exécute le code de la première correspondance.
Chaque branche se termine par `return` ou `break`, et la branche facultative `default` s'exécute quand rien ne correspond :
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// affiche go
```
Comparez toujours avec les membres (`Light.RED`), jamais avec les valeurs brutes (`"red"`) : si la valeur change un jour, le `switch` continue de fonctionner.

---

Retrouver le nom d'un membre à partir de sa valeur s'appelle une **recherche inverse**. Parcourez les noms avec `Object.keys()` et choisissez le premier dont la valeur correspond, en utilisant la méthode de tableau `find()`, qui renvoie le premier élément pour lequel le callback vaut `true` (ou `undefined` s'il n'y en a aucun) :
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// affiche HIGH
```
`Priority[key]` lit le membre dont le nom est stocké dans la variable `key`, la même notation par crochets que vous utilisez pour n'importe quel objet.

---

Les membres de type chaîne ont une faiblesse : toute chaîne ayant le même texte est acceptée comme membre.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// affiche true
```
Quand vous voulez des membres égaux **uniquement** à eux-mêmes, utilisez un `Symbol`. `Symbol(description)` crée une toute nouvelle valeur, différente de tout autre symbole, même un symbole créé avec la même description :
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// affiche true
console.log(Suit.HEARTS === Symbol("hearts"));
// affiche false
console.log(typeof Suit.HEARTS);
// affiche symbol
```
Le texte que vous passez n'est qu'une étiquette de débogage ; vous pouvez le relire avec la propriété `description` (`Suit.HEARTS.description` vaut `"hearts"`).

---

Les valeurs d'énumération sont souvent utilisées comme **clés** d'un autre objet, par exemple pour associer chaque membre à un libellé ou un prix. Dans un objet littéral, entourer une clé de crochets `[ ]` évalue l'expression et utilise son résultat comme clé (une **clé calculée**). Cela fonctionne aussi bien avec des membres de type chaîne que de type symbole :
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// affiche Completed
```
Sans les crochets, `Status.DONE: "Completed"` serait une erreur de syntaxe, et `"Status.DONE"` serait une simple clé de type chaîne.

---

Quand chaque membre a besoin de plusieurs données ou de ses propres méthodes, une **classe** peut jouer le rôle de l'énumération. Chaque membre est une instance de la classe, stockée dans une propriété `static`, c'est-à-dire une propriété qui appartient à la classe elle-même plutôt qu'à chaque instance :
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// affiche Earth
```
Appelez `Object.freeze(Planet)` après la classe pour empêcher quiconque d'ajouter ou de remplacer des membres, et gelez chaque instance dans le constructeur avec `Object.freeze(this)` pour que les membres eux-mêmes restent en lecture seule.
