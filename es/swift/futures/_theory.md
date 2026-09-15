Hay trabajo que no termina de inmediato: descargar un archivo, leer de una base de datos, esperar un temporizador. Si un programa simplemente se detuviera y esperara, no podría pasar nada más mientras tanto. Swift resuelve esto con **funciones asíncronas**.

Una función marcada como **`async`** puede pausarse a mitad de camino y reanudarse más tarde. La palabra clave va después de la lista de parámetros, antes de la flecha:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
Llamarla también es distinto: debes escribir **`await`** delante de la llamada. `await` marca el punto exacto donde el programa puede pausarse, y te da el valor directamente cuando la función termina:
```swift
let n = await fetchNumber()
print(n)
// imprime 42
```
En un script de Swift el nivel superior ya admite `await`, así que puedes llamar a funciones asíncronas directamente, sin ninguna configuración extra. Olvidar `async` o `await` es un error de compilación, no un error silencioso.

---

Una función asíncrona sigue siendo una función ordinaria: puede recibir parámetros y devolver un valor de cualquier tipo. Solo cambian dos cosas, la palabra clave `async` en la firma y el `await` en cada llamada:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// imprime 10.0
```
El valor devuelto es un `Double` normal, no un envoltorio: cuando `await` ha terminado, trabajas con él exactamente como siempre.

---

Las funciones asíncronas suelen construirse unas sobre otras. Dentro de una función `async` puedes hacer `await` sobre cualquier otra función `async`, y el resultado se usa como cualquier valor normal:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// imprime 15
```
`await` solo está permitido dentro de un contexto asíncrono: una función `async`, o el nivel superior de un script. Una función normal, que no sea `async`, no puede hacer `await` de nada.

---

El trabajo que ocurre a lo largo del tiempo a menudo falla: un servidor está caído, falta un archivo, la entrada es incorrecta. Esa función se marca como **`async throws`**, y se llama con **`try await`**:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
Para manejar el error envuelves la llamada en un bloque `do` y la capturas:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// imprime could not load
```
El orden de las palabras clave es fijo: `try` va primero, luego `await`.

---

Cuando no te importa *por qué* falló la llamada, `try?` es más corto que un bloque `do`. Convierte una llamada que lanza errores en un **opcional**: el valor si hay éxito, `nil` si falla. Combinado con `await` se escribe `try? await`:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Como el resultado es opcional, encaja directamente en un `if let`:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Usa `try? await` para un respaldo rápido, y `do` / `catch` cuando el error en sí importa.

---

Varias llamadas con `await` escritas una tras otra se ejecutan **secuencialmente**: la segunda llamada ni siquiera empieza hasta que la primera ha terminado. El código se lee de arriba abajo, exactamente como el código ordinario:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
Esto es lo que quieres cuando la segunda llamada necesita el resultado de la primera. Cuando las llamadas son independientes, esperar una antes de empezar la otra es tiempo perdido, y los siguientes ejercicios muestran cómo evitarlo.

---

Para ejecutar dos llamadas independientes al mismo tiempo, decláralas con **`async let`**. El trabajo empieza de inmediato, y el programa sigue adelante sin esperar:
```swift
async let left = step("A")
async let right = step("B")
```
El valor aún no está, así que no puedes usar la variable directamente: debes hacer `await` en el punto donde por fin la necesites. Un solo `await` delante de la expresión cubre cada `async let` que haya dentro:
```swift
let both = await left + right
```
Si cada llamada tarda un segundo, la versión secuencial necesita dos segundos mientras que la versión con `async let` necesita alrededor de uno, porque las dos llamadas se solapan.

---

Cuando necesitas los resultados por separado, reúne varias variables `async let` en una tupla y haz `await` de la tupla entera de una vez:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
Ambas llamadas ya estaban en marcha; el único `await` espera a que termine la más lenta de las dos. Recuerda que `async let` solo inicia el trabajo: un `async let` que nunca esperas se cancela y se espera implícitamente cuando el ámbito termina.

---

`async let` está atado al ámbito donde se escribe. Para iniciar trabajo concurrente y conservar un manejador de él, usa una **`Task`**. El cierre pasado a `Task { }` se ejecuta por su cuenta, y la tarea puede almacenarse, pasarse o devolverse:
```swift
let job = Task {
    return await double(21)
}
```
El resultado se lee más tarde con **`.value`**, al que se espera con `await`:
```swift
print(await job.value)
// imprime 42
```
El tipo del manejador dice qué produce y qué puede lanzar: `Task<Int, Never>` es una tarea que devuelve un `Int` y nunca lanza errores. A diferencia de `async let`, una `Task` puede crearse desde código ordinario, que no sea asíncrono.

---

`Task.sleep` pausa la tarea actual durante un tiempo sin bloquear nada más. Puede interrumpirse, así que es una llamada asíncrona que lanza errores y necesita `try await`. La duración se indica con ayudantes como `.seconds`, `.milliseconds` o `.nanoseconds`:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
Es la forma estándar de simular trabajo lento en un ejemplo, en lugar de una llamada de red real. Ten en cuenta que no congela el programa: mientras una tarea duerme, las demás siguen ejecutándose.

---

Ahora la diferencia entre secuencial y concurrente se puede medir. Supón que `work` duerme un segundo antes de devolver:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Esperar las llamadas una por una tarda unos **dos** segundos, porque el segundo sueño solo empieza cuando el primero ha terminado:
```swift
let a = await work(1)
let b = await work(2)
```
Iniciarlas con `async let` tarda alrededor de **un** segundo, porque ambos sueños se solapan:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Escribir `await work(1) + await work(2)` en una sola línea no cambia nada: las dos llamadas se evalúan igualmente una tras otra. La concurrencia viene de `async let` o de las tareas, nunca de cómo se formatea la línea.

---

`async let` funciona cuando sabes cuántas llamadas hay mientras escribes el código. Para una lista cuyo tamaño solo se conoce en tiempo de ejecución, usa un **grupo de tareas**.

`withTaskGroup(of:)` abre un grupo, `addTask` inicia una tarea hija por elemento, y el grupo se lee después con `for await`, que entrega los resultados a medida que terminan:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` declara lo que devuelve cada tarea hija. Toda la llamada a `withTaskGroup` es una expresión, así que necesita un único `await` delante, y no devuelve hasta que cada tarea hija ha terminado.

---

Un grupo de tareas te entrega los resultados en **orden de finalización**, no en el orden en que se añadieron las tareas. La tarea hija más rápida llega primero, así que recoger los valores en un array da un orden impredecible.

Cuando el orden importa hay dos soluciones. Si los valores simplemente se pueden reordenar, ordénalos al final:
```swift
return values.sorted()
```
Si cada resultado pertenece a una posición, haz que cada tarea devuelva un par `(index, value)` y escríbelo en un array preparado:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
Una suma, un máximo o un recuento no necesita ninguna de las dos soluciones, porque el orden de los valores no cambia la respuesta.
