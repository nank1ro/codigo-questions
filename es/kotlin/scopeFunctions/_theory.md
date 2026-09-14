Las **funciones de ámbito** (*scope functions*) ejecutan un bloque de código *dentro del contexto de un objeto*. No añaden nuevas funciones al lenguaje: solo hacen que el código que trabaja sobre un objeto sea más corto y fácil de leer. Kotlin tiene cinco: `let`, `run`, `with`, `apply` y `also`.

Se diferencian en solo **dos** puntos: cómo se referencia el objeto dentro del bloque y qué devuelve la llamada. Empezamos con `let`: dentro de su bloque el objeto se llama `it`, y la llamada devuelve el **resultado de la última expresión** del bloque.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Sin `let` necesitarías una variable temporal; con él, el objeto está disponible bajo el nombre corto `it` mientras dure el bloque.

---

Como `let` devuelve el valor de su última expresión, es una forma práctica de **convertir un valor en otra cosa** sin nombrar una variable intermedia:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Dentro del bloque puedes usar `it` tantas veces como necesites:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` se vuelve realmente útil después de una llamada segura. `?.let { ... }` ejecuta el bloque **solo** cuando el valor no es `null`, y dentro del bloque `it` es un valor no nulo, así que no hace falta ninguna comprobación extra:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
Cuando el valor es `null` toda la expresión es `null` y el bloque nunca se ejecuta, por lo que el operador Elvis `?:` es el compañero natural para proporcionar un valor alternativo:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Dentro de un bloque `let` no estás obligado a llamar al objeto `it`: puedes darle un nombre al parámetro de la lambda, lo que mantiene el código legible cuando hay bloques anidados o cuando `it` no diría nada útil.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
Esta forma de nombrar funciona con todas las funciones de ámbito que usan `it`, es decir, con `let` y `also`.

---

`apply` avanza en ambos ejes a la vez: dentro de su bloque el objeto es el receptor `this` (así que sus miembros pueden usarse **sin ningún prefijo**) y la llamada devuelve **el propio objeto**, no el resultado del bloque.

Esa combinación hace de `apply` la herramienta para **configurar** un objeto justo donde lo creas:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
`host` y `port` dentro del bloque son `this.host` y `this.port`; como `apply` devuelve el `Server` configurado, puede asignarse directamente.

---

`apply` no se limita a los objetos que acabas de crear: funciona con cualquier objeto y, como devuelve el objeto, puedes usar la expresión completa donde sea que se espere ese objeto.
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
El bloque es un bloque de código normal, así que puede contener tantas sentencias como necesites.

---

`also` es la imagen especular de `apply`: el objeto se referencia como `it` y la llamada devuelve **el propio objeto**. Como el resultado del bloque se descarta, `also` está pensado para **efectos secundarios** como registrar o comprobar, y puede colocarse en medio de una cadena sin cambiar lo que la cadena produce:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Léelo como *"y también haz esto con ello"*: el valor sigue fluyendo intacto hacia el siguiente paso.

---

Cuando el bloque necesita el objeto como **argumento** de otra cosa, `also` se lee mejor que `apply`: `it` puede pasarse directamente, mientras que `this` tendría que escribirse explícitamente.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
El valor de la expresión sigue siendo `"ada"`: `also` solo lo observa pasar.

---

`run` es `let` con la otra forma de nombrar al objeto: dentro del bloque el objeto es `this`, así que sus miembros no necesitan prefijo, y la llamada devuelve el **resultado de la última expresión**.

Encaja cuando lees varios miembros del mismo objeto para calcular un valor:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Compáralo con `apply`, que usa `this` exactamente de la misma manera pero devuelve el objeto en lugar del resultado del bloque.

---

`with` hace el mismo trabajo que `run`, pero **no** es una extensión: el objeto se pasa como primer argumento en lugar de ser el receptor de una llamada con punto.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Dentro del bloque el objeto es `this` y la llamada devuelve la última expresión, exactamente como `run`. Prefiere `with` cuando ya tienes un objeto no nulo y quieres agrupar varias llamadas sobre él; prefiere `run` cuando el objeto sale de una cadena o puede necesitar una llamada segura (`obj?.run { ... }`).

---

Ya tienes sobre la mesa las cinco funciones de ámbito, y cada una es solo un punto en los dos ejes:
- `let` - el objeto es `it`, devuelve el resultado del bloque
- `run` - el objeto es `this`, devuelve el resultado del bloque
- `with` - el objeto es `this` (pasado como argumento), devuelve el resultado del bloque
- `apply` - el objeto es `this`, devuelve el objeto
- `also` - el objeto es `it`, devuelve el objeto

Elige la fila que necesites: `it` se lee mejor cuando pasas el objeto a otra cosa, `this` se lee mejor cuando tocas muchos de sus miembros; devuelve el resultado del bloque cuando quieres un valor nuevo, devuelve el objeto cuando quieres seguir trabajando con él.
