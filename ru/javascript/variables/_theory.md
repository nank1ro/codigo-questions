Variables are containers for storing data values.
Every variable in JavaScript is an object.
To create a variable, we need to give it a **name** keeping in mind that it must not contain spaces.
A variable is created the moment you first assign a value to it.
In JavaScript you declare constants with the `let` or `const` keywords and variables with the `var` keyword.
The value of a constant can't be changed once it's set, whereas a variable can be set to a different value in the future.
An example of a variable creation named `x` is:
```javascript
var x = 1;
```
In this way we have assigned the value `1` to the variable named `x`.
If we print the variable `x` we get back the number `1`:
```javascript
console.log(x);
// prints 1
```

---

Variables are called in this way because the value they store can change.
We can update `x` by using `=` and giving it a new value.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

We can also give variables the values of other variables.
Here, we can give to the `y` variable the value of `x`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

When we update a variable, it forgets its previous value.
Here we can display the `x` variable twice and see how its value updates.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

In JavaScript string variables can be declared using both double quotes and single quotes:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

If we want a variable name with multiple words, we use **camelCase**.
It is the practice of writing phrases such that each word in the middle of the phrase begins with a capital letter
