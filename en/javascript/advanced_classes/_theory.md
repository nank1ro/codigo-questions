You already know that `extends` makes one class a child of another. What that keyword really gives you is **inheritance**: the child gets every property and method of the parent for free, and can add its own on top.

The piece that makes inheritance useful is **`super`**. Inside a child constructor, `super(...)` calls the parent constructor, so the parent can set up the part of the object it owns:
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
Here `super(name)` hands `name` to `Animal`, which stores it, and `Dog` only has to worry about `breed`.

---

A child class does not have to redefine anything the parent already provides. Methods are inherited too, so an instance of the child can call them as if they were its own:
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
When a child declares its own constructor, calling `super(...)` in it is **mandatory**: without it the object is never initialised and JavaScript throws a `ReferenceError`. A child with no constructor at all is fine, because JavaScript writes one that forwards every argument to the parent.

---

The rule about `super()` is stricter than "call it somewhere". In a child constructor the word `this` does not exist until `super()` has run, because it is the parent constructor that creates the object. Touching `this` before that line throws:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
So `super(...)` should be the **first statement** of any child constructor that uses `this`.

---

When a child defines a method that the parent already has, the child version wins. This is called **overriding**:
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
Overriding does not delete the parent version, it only hides it. Inside the child method, `super.methodName(...)` still reaches it, which lets you extend the parent behaviour instead of replacing it:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
Note the difference: `super(...)` calls the parent **constructor**, `super.name(...)` calls a parent **method**.

---

Until now every property was created inside the constructor. A **class field** lets you declare it directly in the class body, with an optional starting value:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
Fields are assigned to each new instance before the constructor body runs, so the constructor can already rely on them. A field without a value is still declared, it just starts as `undefined`:
```javascript
class Task {
    done = false;
    title;
}
```
Note the syntax: no `let`, no `const`, no `this` in the declaration, and the line ends with a semicolon.

---

Order matters when classes inherit from each other. A `class` declaration is **not** hoisted the way a `function` is: the name only exists from the line where the class is written onwards. So a child class has to appear *after* the parent it extends, otherwise the `extends` clause fails with a `ReferenceError`.

---

Some behaviour belongs to the class itself rather than to any single instance. A conversion between two units, for example, does not need an object to work on. Marking a method **`static`** puts it on the class:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
A static method is called on the class name, never on an instance: `new MathUtils().double(4)` throws a `TypeError`, because instances do not receive static members. Inside a static method `this` refers to the class, so one static can call another with `this.otherStatic(...)`.

---

`static` works on fields too. A **static property** is stored once on the class, not once per instance, which makes it the natural place for a shared counter or a constant:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
Because there is only one copy, every instance that updates it updates the same value. Inside a constructor you reach it through the class name, `Circle.PI`, and not through `this`: `this.PI` would look for a property on the instance, find nothing, and give you `undefined`.

---

A very common use of a static method is a **factory**: a method that builds an instance from some other shape of data and returns it. It keeps `new` in one place and gives the construction a name that says what it does:
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
A factory can be called before any instance exists, which a normal method could not.

---

A **getter** is a method that is read like a property. Write `get` in front of it and drop the parentheses at the call site:
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
`r.area` runs the method and gives back its result, so it is a number. Adding parentheses would then try to call that number, which fails.

The mirror image is a **setter**, declared with `set`, which runs when the property is assigned. It takes exactly one parameter:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

The real value of a setter is that it can refuse. Between the assignment and the stored value you get a chance to check, clamp or reject what arrives:
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
A getter and a setter with the same name form one property, so they cannot also be a normal field: the stored value lives under a different name, by convention the same name with a leading underscore.

---

The leading underscore of `_temperature` is only a convention: nothing stops the outside world from writing `v._level = 999` and walking straight past your setter. A **private field** is enforced by the language. Its name starts with `#`, it must be declared in the class body, and it can only be read or written from inside that class:
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
Two details are easy to trip over. The `#` is part of the name, so you always write `this.#code`, never `this.code`. And a private field does not show up in `Object.keys` or in `console.log` of the instance.

---

Methods can be private too. Prefix the name with `#` and the method disappears from the public surface of the class, while still being callable from any other method with `this.#name(...)`:
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
This is how you keep helper steps out of the API: the caller sees `print`, not the formatting detail behind it. Private fields and private methods together give a class a clear inside and outside.

---

Printing an object usually gives something unhelpful. Whenever JavaScript needs a string and gets an object instead, it calls the object's **`toString`** method, and the default one returns `[object Object]`. Defining your own replaces that:
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
The same method is used by string concatenation and by `String(value)`. If you also want a sensible **number**, define `[Symbol.toPrimitive](hint)`, which receives `"string"`, `"number"` or `"default"` and decides what to return; when it exists it wins over `toString`.

---

The **`instanceof`** operator asks whether an object was built from a class, or from any class that inherits from it:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript has no `abstract` keyword, but the same idea is written by hand: a base class defines the shape and every method that a child *must* provide simply throws:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
A child that forgets to override `area` fails loudly the first time it is used, instead of silently returning `undefined`.

---

`for...of` and the spread operator `...` do not work on any object: they work on **iterables**, objects that provide a method stored under the special key `Symbol.iterator`. Give your class that method and it joins the club:
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
The `*` in front of the name makes it a **generator**: a function that hands values out one at a time with `yield` and pauses between them. That is the shortest way to satisfy the iteration protocol, and it works for values that are computed rather than stored.
