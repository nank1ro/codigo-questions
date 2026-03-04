En Swift podemos usar el signo `+` para mostrar dos o más cadenas juntas, como:
```swift
print("Hello " + "Swift!") // imprime "Hello Swift!"
```

---

Pero usar el signo `+` para agregar un número como '10' a una cadena como ` "amigos"` produce un error ya que son un tipo diferente de valores

---

La interpolación de cadenas nos permite mostrar expresiones como agregar una cadena a un número, sin ningún error.

---

Cada declaración de interpolación de cadena consta de dos partes, el `\()` donde insertamos el número o variable, y la cadena normal

---

A continuación, agregamos el tipo diferente de valor entre llaves para que se muestre como una declaración de impresión. Como aquí, con `\(5)`

---

Insertar variables como `amigos` entre los paréntesis también muestra su valor

---

Podemos usar paréntesis para insertar valores tantas veces como queramos dentro de la interpolación de cadenas

---

Las interpolaciones de cadenas se utilizan mejor en declaraciones de impresión, pero también podemos almacenarlas en variables como cadenas normales.
