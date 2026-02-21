Podrías haber considerado la situación en la que te gustaría reutilizar un fragmento de código, solo con algunos valores diferentes.
En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.
En JavaScript usamos la palabra clave `function` seguida del nombre de la función:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

The parentheses in the __function definition__ don't have to be empty if we want to specify parameters

---

Sometimes we want a function to __return__ a value.
Well, there's the `return` keyword.

---

Functions can have multiple input parameters, which are written within the function's parentheses, separated by commas.
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

You can define a _default_ value for any parameter in a function by assigning a value to the parameter after that parameter's type.
If a default value is defined, you can omit that parameter when calling the function
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

The __rest parameter__ syntax allows us to represent an indefinite number of arguments as an array.
Write rest parameters by inserting three period characters `...` before the parameter's name.
The values passed to a rest parameter are made available within the function's body as an array.
For example, a rest parameter with a name of `numbers` is made available within the function's body as a constant array called numbers

---

In functions we can add an _optional comment_ that explains what the function does:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("¡Hola, mundo!");
}
```
We can use `//` for a single line comment and `/** */` for a multi line comment
