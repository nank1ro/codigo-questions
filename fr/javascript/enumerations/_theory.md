Une **énumération** (ou *enum*) est un type commun pour un petit groupe de valeurs fixes et liées : les jours de la semaine, les couleurs d'un jeu de cartes, les états possibles d'une commande.
Contrairement à de nombreux langages, JavaScript **n'a pas** de mot-clé `enum`. Le remplacement idiomatique est un simple objet dont les propriétés sont les membres, passé à `Object.freeze()` pour que personne ne puisse le modifier ensuite :
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
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
// prints done
```
Une fois gelé, l'objet ne peut plus non plus recevoir de nouvelles propriétés, et `Object.isFrozen(obj)` vous indique si un objet a été gelé :
```javascript
console.log(Object.isFrozen(Status));
// prints true
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
// prints s
console.log(Size.MEDIUM);
// prints undefined
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
// prints true
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
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
Combiner `Object.values()` avec la méthode de tableau `includes()` est le moyen standard de vérifier si une valeur arbitraire, par exemple une valeur lue depuis une saisie utilisateur, est un membre valide :
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
