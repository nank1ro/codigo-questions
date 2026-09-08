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
