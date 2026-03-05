Vous avez peut-être envisagé la situation où vous aimeriez réutiliser un morceau de code, juste avec quelques valeurs différentes.
Au lieu de réécrire tout le code, il est beaucoup plus propre de définir une fonction, qui peut ensuite être utilisée à plusieurs reprises.
En JavaScript, nous utilisons le mot-clé `function` suivi du nom de la fonction :
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

Les parenthèses dans la __définition de fonction__ ne doivent pas être vides si nous voulons spécifier des paramètres

---

Parfois, nous voulons qu'une fonction __retourne__ une valeur.
Eh bien, il y a le mot-clé `return`.

---

Les fonctions peuvent avoir plusieurs paramètres d'entrée, qui sont écrits entre les parenthèses de la fonction, séparés par des virgules.
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

Vous pouvez définir une valeur _par défaut_ pour n'importe quel paramètre dans une fonction en attribuant une valeur au paramètre après le type de ce paramètre.
Si une valeur par défaut est définie, vous pouvez omettre ce paramètre lors de l'appel de la fonction
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

La syntaxe du __paramètre rest__ nous permet de représenter un nombre indéfini d'arguments comme un tableau.
Écrivez les paramètres rest en insérant trois caractères de point `...` avant le nom du paramètre.
Les valeurs transmises à un paramètre rest sont mises à disposition dans le corps de la fonction sous forme de tableau.
Par exemple, un paramètre rest avec un nom de `numbers` est mis à disposition dans le corps de la fonction en tant que tableau constant appelé numbers

---

Dans les fonctions, nous pouvons ajouter un _commentaire optionnel_ qui explique ce que fait la fonction :
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
Nous pouvons utiliser `//` pour un commentaire d'une seule ligne et `/** */` pour un commentaire multilignes
