La prise de décision est nécessaire quand nous voulons exécuter du code seulement si une certaine condition est satisfaite.
Supposons que nous voulons jouer dehors seulement si le temps est beau.
En programmation, nous pouvons sauvegarder une variable booléenne `niceWeather` et effectuer l'action de jouer dehors `if` cette variable est `true`, comme :
```javascript
var niceWeather = true;
if (niceWeather) {
    // joue dehors
}
```

---

Continuons avec l'exemple précédent.
```javascript
var niceWeather = true;
if (niceWeather) {
    // joue dehors
}
```
Nous avons vu que l'instruction `if` exécute le bloc de code seulement si la condition est `true`.
Une autre chose importante à considérer est représentée par les **accolades** `{}` qui indiquent un bloc de code.

---

Nous venons de voir comment exécuter un bloc de code si une condition se produit, voyons maintenant comment exécuter un autre bloc de code si la première condition échoue.
Nous allons jouer dehors si le temps est beau ; sinon, nous restons à la maison.
En JavaScript nous pouvons utiliser l'instruction `else`, comme :
```javascript
var niceWeather = true;
if (niceWeather) {
    // joue dehors
} else {
    // reste à la maison
}
```

---

Supposons que nous avons une autre condition à vérifier, comme dans cet exemple :
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
et le résultat de ce code est `the number is 3`.
Tout d'abord, vérifions si le nombre est égal à 2, c'est faux.
Passons à la deuxième instruction et vérifions si `num` est égal à 3, étant vrai nous exécutons le bloc de code suivant en affichant `the number is 3`

---

Nous pouvons ajouter autant d'instructions `else if` que nous le souhaitons, il n'y a pas de limites
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
et le résultat de ce code est `the number is 4`.

---

Nous pouvons aussi imbriquer une instruction conditionnelle (`if`, `else if` ou `else`) dans une autre instruction conditionnelle, pour créer une structure plus complexe.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
et le résultat de ce code est `the number is 4`.

---

L'opérateur conditionnel ternaire est un opérateur spécial avec trois parties, qui prend la forme `question ? answer1 : answer2`.
C'est un raccourci pour évaluer l'une de deux expressions selon que `question` est true ou false.
Si `question` est true, il évalue `answer1` et retourne sa valeur ; sinon, il évalue `answer2` et retourne sa valeur.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// affiche 10
```
Le code abrégé pour le code ci-dessus est :
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// affiche 10
```
`c` est défini égal à `a`, parce que la condition `a < b` était true

---

L'opérateur _nil-coalescing_ `a ?? b` déplie un optionnel `a` s'il contient une valeur, ou retourne une valeur par défaut `b` si `a` est `nil`.
L'expression `a` est toujours d'un type optionnel.
L'expression `b` doit correspondre au type stocké dans a.
L'opérateur nil-coalescing est un raccourci pour le code ci-dessous :
```javascript
a != nil ? a! : b;
```

---

`if` est le mot-clé qui introduit une déclaration conditionnelle en JavaScript. Il n'y a pas de mot-clé `elif` ici — une deuxième condition s'introduit avec `else if`, écrit en deux mots séparés.

---

Les littéraux booléens de JavaScript sont en minuscules : `true` et `false`, pas `True`/`False`, et pas les chaînes `"true"`/`"false"`.

---

Pour empêcher un bloc de code de s'exécuter, la condition entre les parenthèses doit s'évaluer à `false`.

---

L'espace entre `if` et ses parenthèses est purement esthétique : `if(true)` et `if (true)` sont la même instruction pour JavaScript.

---

Ce sont les accolades qui regroupent plusieurs instructions en un seul bloc. Sans elles, un `if` ne contrôle que l'unique instruction qui le suit, donc `if (true) console.log("Hello!");` est du JavaScript valide.

---

La condition est évaluée une seule fois, avant que le bloc ne commence. JavaScript ne la revérifie pas pendant que les instructions entre les accolades s'exécutent.

---

Une condition `false` ignore entièrement le bloc, et le programme continue à la première instruction après l'accolade fermante.

---

Une condition n'a pas besoin d'être un booléen : JavaScript convertit tout ce qu'il trouve en un booléen, donc `if (1)` exécute son bloc et `if (0)` non. Un littéral `true` n'a besoin d'aucune conversion.

---

Un bloc de code ne se limite pas à une seule ligne — chaque instruction à l'intérieur des accolades s'exécute, dans l'ordre, quand la condition est `true`.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
et la sortie est `First line` suivi de `Second line`.

---

Les instructions à l'intérieur d'un bloc s'exécutent l'une après l'autre, de haut en bas, donc deux appels `console.log` dans le même bloc s'affichent sur deux lignes distinctes.

---

Indenter les instructions à l'intérieur d'un bloc n'est qu'une convention de lisibilité. JavaScript utilise les accolades, jamais l'indentation, pour décider de ce qui appartient au bloc.

---

Les instructions telles que `if`, `else if` et `else`, qui exécutent ou ignorent du code selon qu'une condition est `true` ou `false`, sont appelées des **déclarations conditionnelles**.

---

Une variable booléenne, même construite à partir d'une négation `!` comme `isAfternoon`, peut être utilisée directement comme condition d'un `if`, sans avoir besoin de comparaison.

---

La condition d'une déclaration `if` se place toujours entre parenthèses `()`, juste après le mot-clé `if` et avant l'accolade ouvrante.

---

Un bloc peut contenir n'importe quel nombre d'instructions, et il peut aussi n'en contenir aucune : `if (true) {}` est du JavaScript valide qui ne fait simplement rien.

---

Le bloc de code d'une déclaration `if` est l'ensemble des instructions à l'intérieur des accolades `{ }`, la partie qui s'exécute réellement quand la condition est `true`.
