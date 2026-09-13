Vous savez déjà que `extends` fait d'une classe l'enfant d'une autre. Ce que ce mot-clé vous donne vraiment, c'est l'**héritage** : l'enfant reçoit gratuitement chaque propriété et chaque méthode du parent, et peut ajouter les siennes par-dessus.
Ce qui rend l'héritage utile, c'est **`super`**. Dans un constructeur enfant, `super(...)` appelle le constructeur parent, afin que le parent puisse mettre en place la partie de l'objet qu'il possède :
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
Ici, `super(name)` transmet `name` à `Animal`, qui le stocke, et `Dog` n'a plus qu'à se soucier de `breed`.

---

Une classe enfant n'a pas besoin de redéfinir ce que le parent fournit déjà. Les méthodes sont héritées elles aussi, si bien qu'une instance de l'enfant peut les appeler comme si elles étaient les siennes :
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// prints Max makes a sound
```
Quand un enfant déclare son propre constructeur, y appeler `super(...)` est **obligatoire** : sans cela, l'objet n'est jamais initialisé et JavaScript lève une `ReferenceError`. Un enfant sans constructeur du tout, en revanche, ne pose aucun problème, car JavaScript en écrit un qui transmet chaque argument au parent.

---

La règle sur `super()` est plus stricte que « appelez-le quelque part ». Dans un constructeur enfant, le mot `this` n'existe pas tant que `super()` n'a pas été exécuté, car c'est le constructeur parent qui crée l'objet. Toucher `this` avant cette ligne lève une erreur :
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
`super(...)` devrait donc être la **première instruction** de tout constructeur enfant qui utilise `this`.

---

Quand un enfant définit une méthode que le parent possède déjà, c'est la version de l'enfant qui l'emporte. C'est ce qu'on appelle la **redéfinition** :
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// prints Woof
```
La redéfinition ne supprime pas la version du parent, elle se contente de la masquer. À l'intérieur de la méthode enfant, `super.methodName(...)` l'atteint toujours, ce qui permet d'étendre le comportement du parent au lieu de le remplacer :
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
Notez la différence : `super(...)` appelle le **constructeur** parent, `super.name(...)` appelle une **méthode** parente.

---

Jusqu'ici, chaque propriété était créée dans le constructeur. Un **champ de classe** permet de la déclarer directement dans le corps de la classe, avec une valeur de départ facultative :
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
Les champs sont assignés à chaque nouvelle instance avant que le corps du constructeur ne s'exécute, donc le constructeur peut déjà compter sur eux. Un champ sans valeur est tout de même déclaré, il commence simplement à `undefined` :
```javascript
class Task {
    done = false;
    title;
}
```
Notez la syntaxe : pas de `let`, pas de `const`, pas de `this` dans la déclaration, et la ligne se termine par un point-virgule.

---

L'ordre compte quand des classes héritent les unes des autres. Une déclaration `class` n'est **pas** hissée comme l'est une `function` : le nom n'existe qu'à partir de la ligne où la classe est écrite. Une classe enfant doit donc apparaître *après* le parent qu'elle étend, sinon la clause `extends` échoue avec une `ReferenceError`.

---

Certains comportements appartiennent à la classe elle-même plutôt qu'à une instance en particulier. Une conversion entre deux unités, par exemple, n'a pas besoin d'un objet sur lequel travailler. Marquer une méthode **`static`** la place sur la classe :
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
Une méthode statique s'appelle sur le nom de la classe, jamais sur une instance : `new MathUtils().double(4)` lève une `TypeError`, car les instances ne reçoivent pas les membres statiques. Dans une méthode statique, `this` désigne la classe, donc une méthode statique peut en appeler une autre avec `this.otherStatic(...)`.

---

`static` fonctionne aussi sur les champs. Une **propriété statique** est stockée une seule fois sur la classe, pas une fois par instance, ce qui en fait l'endroit tout indiqué pour un compteur partagé ou une constante :
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
Comme il n'existe qu'une seule copie, chaque instance qui la met à jour met à jour la même valeur. Dans un constructeur, vous y accédez par le nom de la classe, `Circle.PI`, et non par `this` : `this.PI` chercherait une propriété sur l'instance, ne trouverait rien et vous donnerait `undefined`.

---

Un usage très courant d'une méthode statique est la **factory** : une méthode qui construit une instance à partir d'une autre forme de données et la renvoie. Elle garde `new` à un seul endroit et donne à la construction un nom qui dit ce qu'elle fait :
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// prints 120
```
Une factory peut être appelée avant même qu'une instance existe, ce qu'une méthode normale ne peut pas faire.

---

Un **getter** est une méthode qui se lit comme une propriété. Écrivez `get` devant elle et laissez tomber les parenthèses au moment de l'appel :
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// prints 12
```
`r.area` exécute la méthode et renvoie son résultat, c'est donc un nombre. Ajouter des parenthèses reviendrait alors à appeler ce nombre, ce qui échoue.
L'image miroir est un **setter**, déclaré avec `set`, qui s'exécute quand la propriété est assignée. Il prend exactement un paramètre :
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

La vraie valeur d'un setter, c'est qu'il peut refuser. Entre l'assignation et la valeur stockée, vous avez une occasion de vérifier, de borner ou de rejeter ce qui arrive :
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// prints 3, the setter rejected 50
```
Un getter et un setter de même nom forment une seule propriété, ils ne peuvent donc pas être en même temps un champ normal : la valeur stockée vit sous un autre nom, par convention le même nom précédé d'un underscore.

---

Le underscore de tête de `_temperature` n'est qu'une convention : rien n'empêche le monde extérieur d'écrire `v._level = 999` et de passer directement outre votre setter. Un **champ privé** est imposé par le langage. Son nom commence par `#`, il doit être déclaré dans le corps de la classe, et il ne peut être lu ou écrit que depuis l'intérieur de cette classe :
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
Deux détails font facilement trébucher. Le `#` fait partie du nom, donc vous écrivez toujours `this.#code`, jamais `this.code`. Et un champ privé n'apparaît ni dans `Object.keys` ni dans le `console.log` de l'instance.

---

Les méthodes peuvent aussi être privées. Préfixez le nom avec `#` et la méthode disparaît de la surface publique de la classe, tout en restant appelable depuis n'importe quelle autre méthode avec `this.#name(...)` :
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// prints $7
```
C'est ainsi que vous gardez les étapes auxiliaires hors de l'API : l'appelant voit `print`, pas le détail de formatage derrière. Champs privés et méthodes privées donnent ensemble à une classe un intérieur et un extérieur clairs.

---

Afficher un objet donne généralement quelque chose d'inutile. Chaque fois que JavaScript a besoin d'une chaîne et reçoit un objet à la place, il appelle la méthode **`toString`** de l'objet, et celle par défaut renvoie `[object Object]`. Définir la vôtre remplace ce comportement :
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// prints $7
```
La même méthode est utilisée par la concaténation de chaînes et par `String(value)`. Si vous voulez aussi un **nombre** exploitable, définissez `[Symbol.toPrimitive](hint)`, qui reçoit `"string"`, `"number"` ou `"default"` et décide quoi renvoyer ; quand il existe, il l'emporte sur `toString`.

---

L'opérateur **`instanceof`** demande si un objet a été construit à partir d'une classe, ou de n'importe quelle classe qui en hérite :
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript n'a pas de mot-clé `abstract`, mais la même idée s'écrit à la main : une classe de base définit la forme et chaque méthode qu'un enfant *doit* fournir se contente de lever une erreur :
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
Un enfant qui oublie de redéfinir `area` échoue bruyamment à sa première utilisation, au lieu de renvoyer silencieusement `undefined`.

---

`for...of` et l'opérateur de spread `...` ne fonctionnent pas sur n'importe quel objet : ils fonctionnent sur les **itérables**, les objets qui fournissent une méthode stockée sous la clé spéciale `Symbol.iterator`. Donnez cette méthode à votre classe et elle rejoint le club :
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// prints [ 'a', 'b' ]
```
Le `*` devant le nom en fait un **générateur** : une fonction qui distribue les valeurs une à une avec `yield` et fait une pause entre elles. C'est la façon la plus courte de satisfaire le protocole d'itération, et cela fonctionne pour des valeurs calculées plutôt que stockées.
