Una **stringa formattata** è un testo in cui alcune parti vengono riempite con valori a runtime: un prezzo, un nome, un punteggio. Swift ti offre due strumenti per farlo.

Il primo è l'**interpolazione di stringa**, che conosci già: qualsiasi cosa scritta dentro `\( )` viene valutata e inserita nel testo. Non deve essere una variabile, può essere qualsiasi espressione:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
L'interpolazione è il modo più rapido per costruire una stringa, ma stampa i numeri esattamente come Swift li memorizza: `3.5` resta `3.5`, mai `3.50`. Per il pieno controllo su cifre, larghezza e riempimento useremo `String(format:)`, introdotto nel prossimo esercizio.

---

Il secondo strumento è `String(format:)`, che proviene dal framework **Foundation**, quindi il file deve iniziare con `import Foundation`.

Prende una **format string** seguita dai valori da inserire. Dentro la format string, uno **specificatore** che inizia con `%` indica dove va ogni valore e come viene scritto. Lo specificatore per un intero è `%d`:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` restituisce una normale `String`, quindi puoi stamparla, memorizzarla o restituirla da una funzione.

---

Per i numeri decimali (`Double`) lo specificatore è `%f`. Da solo stampa sempre sei cifre dopo il punto:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
Per scegliere quanti decimali vuoi, scrivi un punto e un numero tra `%` e `f`. Questa è la **precisione**, e il valore viene arrotondato per adattarsi:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` è la scelta abituale per i prezzi, perché mostra sempre esattamente due decimali.

---

Un numero tra `%` e la lettera imposta la **larghezza minima** del campo. Se il valore è più corto, vengono aggiunti spazi a sinistra così che risulti **allineato a destra**; se è più lungo, non viene tagliato nulla:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
Larghezza e precisione si combinano: `%8.2f` significa "largo almeno 8 caratteri, con 2 decimali":
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
Le larghezze fisse sono ciò che allinea le colonne di una tabella.

---

Per impostazione predefinita il riempimento va a sinistra. Un segno meno subito dopo `%` mette invece il riempimento a destra, così il valore risulta **allineato a sinistra**:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
Il segno meno è un **flag**: cambia come viene riempito il campo senza cambiarne la larghezza.

---

Un altro flag è `0`: invece che con spazi, il campo viene riempito con zeri a sinistra. È così che ottieni numeri come `007` o `00042`:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
Come con gli spazi, un valore più lungo della larghezza non viene mai tagliato.

---

Una format string può contenere quanti specificatori vuoi. I valori seguono nello stesso ordine, separati da virgole, e ognuno deve corrispondere al tipo del suo specificatore: `%d` per un `Int`, `%f` per un `Double`:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Passare un `Double` a `%d` (o un `Int` a `%f`) compila, ma stampa un numero senza senso, quindi controlla sempre che specificatori e valori corrispondano.

---

Gli interi possono essere scritti anche in altre basi. `%x` stampa il valore in **esadecimale** con lettere minuscole, `%X` con lettere maiuscole, e `%o` in ottale:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
Anche qui funzionano la larghezza e il flag `0`: `%02x` è il modo classico per scrivere un byte di un colore, come in `#ff8000`.

---

Per inserire una `String` in una format string, usa lo specificatore `%@`:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` accetta direttamente una `String` di Swift. Non usare `%s` con una stringa Swift: quello specificatore si aspetta una stringa C e stampa spazzatura o va in crash.
