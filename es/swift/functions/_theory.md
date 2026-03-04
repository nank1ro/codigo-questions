Podrías haber considerado la situación en la que te gustaría reutilizar un trozo de código, solo con unos pocos valores diferentes.
En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.
En Swift usamos la palabra clave `func` seguida del nombre de la función:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

Los paréntesis en la __definición de función__ no tienen que estar vacíos si queremos especificar parámetros

---

A veces queremos que una función __devuelva__ un valor.
Bueno, existe la palabra clave `return`.

---

Las funciones pueden tener múltiples parámetros de entrada, que se escriben dentro de los paréntesis de la función, separados por comas.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

Puedes usar un tipo de tupla como el tipo de retorno para que una función devuelva múltiples valores como parte de un valor de retorno compuesto.

---

Si no quieres una etiqueta de argumento para un parámetro, escribe un guion bajo `_` en lugar de una etiqueta de argumento explícita para ese parámetro

---

Puedes definir un valor _predeterminado_ para cualquier parámetro en una función asignando un valor al parámetro después del tipo de ese parámetro.
Si se define un valor predeterminado, puedes omitir ese parámetro al llamar a la función
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

Un _parámetro variádico_ acepta cero o más valores de un tipo especificado.
Usas un parámetro variádico para especificar que el parámetro puede recibir un número variable de valores de entrada cuando se llama a la función.
Escribe parámetros variádicos insertando tres caracteres de punto `...` después del nombre del tipo del parámetro.
Los valores pasados a un parámetro variádico se hacen disponibles dentro del cuerpo de la función como una matriz del tipo apropiado.
Por ejemplo, un parámetro variádico con un nombre de `numbers` y un tipo de `Double...` se hace disponible dentro del cuerpo de la función como una matriz constante llamada numbers de tipo `[Double]`

---

En las funciones podemos agregar un _comentario opcional_ que explique qué hace la función:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
Podemos usar `///` para un comentario de una sola línea y `/** */` para un comentario de múltiples líneas
