Variables son containers para almacenando datos valores.
Every variable en Swift es un object.
a Crea un variable, we necesita un dar lo un **nombre** manteniendo en mind ese lo debe no contain spaces.
A variable es creo el moment you primero assign un valor un it.
In Swift you declare constantes con el `permitir` palabra clave y variables con el `var` palabra clave.
el valor de un constante no puede ser cambio once it's set, whereas un variable puede ser establecer un a diferente valor en el future.
An ejemplo de un variable creation named `x` es:
```swift
var x = 1
```
In este way we tiene assigned el valor `1` un el variable named `x`.
si we Imprime el variable `x` we obtener back el numero `1`:
```swift
print(x) // prints 1
```

---

Variables son llamo en este way porque el valor ellos almacenar puede cambiar.
We puede Actualiza `x` por usando `=` y dando lo un nuevo valor.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

We puede tambien dar variables los valores de otro variables. Here, we puede dar un el `y` variable el valor de `x`
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

cuando we Actualiza un variable, lo forgets su previous valor. Here we puede display el `x` variable twice y ver como su valor updates.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

In Swift cadena variables puede ser declared solo por usando double quotes:
```swift
let x = "May"
```

---

si we querer un variable nombre con multiples words, we usar **camelCase**.
It es el practice de escribiendo phrases tal ese cada word en el middle de el phrase comienza con un capital letter
