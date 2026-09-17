An **enumeration** (or *enum*) is a common type for a small group of related, fixed values: the days of the week, the suits of a deck, the possible states of an order.
Unlike many languages, JavaScript has **no** `enum` keyword. The idiomatic replacement is a plain object whose properties are the members, passed to `Object.freeze()` so that nobody can change it later:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
```
By convention the object is declared with `const`, its name starts with a capital letter and the member names are written in `UPPER_CASE`, exactly like other constants.

---

The value stored in each member is up to you. **Strings** are the most common choice because they are readable when printed, logged or saved to a file:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// prints done
```
Once frozen, the object cannot receive new properties either, and `Object.isFrozen(obj)` tells you whether an object has been frozen:
```javascript
console.log(Object.isFrozen(Status));
// prints true
```

---

Why freeze the object at all? A frozen object rejects every change: assigning to an existing member, adding a new one or deleting one has no effect.
How the rejection shows up depends on the mode your code runs in:
- in **sloppy mode** (the default for plain scripts) the assignment is **silently ignored**
- in **strict mode** (files starting with `"use strict"`, ES modules and class bodies) it **throws** a `TypeError`

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// prints s
console.log(Size.MEDIUM);
// prints undefined
```
Either way the enumeration keeps the values you defined, which is exactly what you want from a set of constants.

---

Members can also hold **numbers**. Numeric values are handy when the members have a natural order, because you can compare them with the usual operators:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// prints true
```
The trade-off is readability: printing `Priority.HIGH` shows `3`, which tells you much less than the string `"high"` would.

---

Because an enumeration is just an object, the usual object helpers let you inspect it:
- `Object.keys(Enum)` returns an array with the member **names**
- `Object.values(Enum)` returns an array with the member **values**
- `Object.entries(Enum)` returns an array of `[name, value]` pairs

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
Combining `Object.values()` with the array method `includes()` is the standard way to check whether an arbitrary value, for example one read from user input, is a valid member:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```

---

Enumerations pair naturally with the `switch` statement, which compares one value against a list of `case` labels and runs the code of the first matching one.
Each branch ends with `return` or `break`, and the optional `default` branch runs when nothing matches:
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
// prints go
```
Always compare against the members (`Light.RED`), never against the raw values (`"red"`): if the value ever changes, the `switch` keeps working.

---

Going from a value back to its member name is called a **reverse lookup**. Loop over the names with `Object.keys()` and pick the first one whose value matches, using the array method `find()`, which returns the first element for which the callback is `true` (or `undefined` if there is none):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// prints HIGH
```
`Priority[key]` reads the member whose name is stored in the variable `key`, the same bracket notation you use for any object.

---

String members have one weakness: any string with the same text is accepted as a member.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// prints true
```
When you want members that are equal **only** to themselves, use a `Symbol`. `Symbol(description)` creates a brand-new value that is different from every other symbol, even one created with the same description:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// prints true
console.log(Suit.HEARTS === Symbol("hearts"));
// prints false
console.log(typeof Suit.HEARTS);
// prints symbol
```
The text you pass is only a label for debugging; you can read it back with the `description` property (`Suit.HEARTS.description` is `"hearts"`).

---

Enumeration values are often used as **keys** of another object, for example to map every member to a label or a price. Inside an object literal, wrapping a key in square brackets `[ ]` evaluates the expression and uses its result as the key (a **computed key**). This works both with string and with symbol members:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// prints Completed
```
Without the brackets, `Status.DONE: "Completed"` would be a syntax error, and `"Status.DONE"` would be a plain string key.

---

When each member needs several pieces of data or its own methods, a **class** can play the role of the enumeration. Every member is an instance of the class, stored in a `static` property, that is a property that belongs to the class itself instead of to each instance:
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
// prints Earth
```
Call `Object.freeze(Planet)` after the class to stop anyone from adding or replacing members, and freeze each instance in the constructor with `Object.freeze(this)` so that the members themselves stay read-only.
