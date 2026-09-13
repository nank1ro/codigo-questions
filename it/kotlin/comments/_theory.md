Un **commento** è una nota scritta dentro il codice sorgente per le persone che lo leggono. Il compilatore ignora completamente i commenti, quindi non cambiano mai ciò che il programma fa.

Il commento più semplice è il **commento su una riga**: inizia con `//` e continua fino alla fine della riga.
```kotlin
// Greets the user
println("Hello")
```
Usa i commenti per spiegare a cosa serve un pezzo di codice, o perché è stato scritto in quel modo.

---

Un commento non ha bisogno di una riga tutta per sé: può seguire il codice sulla stessa riga. Questo è un **commento a fine riga**, ed è un buon posto per una breve nota su quella specifica istruzione:
```kotlin
val retries = 3 // give up after three attempts
```
Tutto ciò che va da `//` alla fine della riga viene ignorato, mentre il codice che lo precede viene eseguito come di consueto.

---

Poiché il compilatore rimuove completamente i commenti, aggiungere o eliminare un commento non cambia mai ciò che fa un programma. Viene eseguito solo il codice che **non** è commentato.

Questo rende `//` un modo rapido per disattivare una riga di codice senza eliminarla. Questo si chiama **commentare**:
```kotlin
var total = 10
// total = total + 5
println(total) // prints 10
```
La seconda riga ora è un commento, quindi `total` rimane `10`. Togliendo il `//` la riga torna in vita.

Commentare è comodo mentre fai esperimenti, ma ricorda di fare pulizia: un codice che resta commentato a lungo non fa che confondere chi lo leggerà dopo.

---

Quando un commento ha bisogno di più di una riga, Kotlin offre il **commento su più righe** (chiamato anche commento a blocco): inizia con `/*` e termina con `*/`, e tutto ciò che sta in mezzo viene ignorato, compresi gli a capo.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
Un commento a blocco può anche essere breve e stare su una sola riga: `/* like this */`.

---

A differenza di `//`, che si ferma alla fine della riga, un commento `/*` si ferma solo al `*/`. Se dimentichi di chiuderlo, il compilatore tratta tutto il codice successivo come parte del commento e segnala un errore:
```kotlin
val width = 10 /* in centimetres
println(width) // still inside the comment: error, the comment is never closed
```
Sia `//` che `/* */` funzionano come commenti a fine riga, ma con `/*` assicurati sempre che il `*/` sia presente.

---

In Java un commento a blocco non può contenere un altro commento a blocco, ma in Kotlin **possono essere annidati**: ogni `/*` deve essere abbinato al suo `*/`, e il commento termina solo quando quello più esterno viene chiuso.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Qui `still a comment */` fa parte del commento esterno, quindi viene stampato solo `done`. È proprio questo che ti permette di commentare un intero blocco di codice anche quando quel blocco contiene già un commento `/* */`.

---

Per commentare più righe contemporaneamente, avvolgile in un unico commento a blocco invece di aggiungere `//` a ogni riga:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // prints 100
```
Grazie all'annidamento, questo funziona anche quando una di quelle righe contiene già un commento `/* */`.

---

Un uso comune dei commenti a blocco è il **commento di intestazione**: un breve blocco posto direttamente sopra una funzione che dice cosa fa e cosa significano i suoi parametri.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Chi chiama `toSeconds` può così leggere l'intestazione invece del corpo. Tieni l'intestazione accanto alla funzione, in modo che vengano aggiornati insieme.

---

Kotlin ha un terzo tipo di commento, il **commento di documentazione**, scritto in un formato chiamato **KDoc**: inizia con `/**` (una barra e due asterischi) e termina con `*/`, e viene posto direttamente sopra una funzione, una classe o una proprietà.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
Per il compilatore è solo un commento, ma strumenti come IntelliJ IDEA lo leggono e lo mostrano come testo di aiuto per `greet`. Il `*` all'inizio delle righe interne è solo una convenzione che mantiene il blocco allineato. Dentro KDoc puoi usare Markdown, e le parentesi quadre come `[name]` diventano link a quel parametro.

---

La prima riga di un commento di documentazione è il **sommario**: una breve frase che dice cosa fa la funzione. Scrivila in terza persona, come se descrivessi la funzione: "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
Il commento deve trovarsi subito sopra la dichiarazione, senza altre istruzioni in mezzo, altrimenti gli strumenti non lo collegano alla funzione.

---

Dopo il sommario, un commento di documentazione può descrivere i parametri e il valore restituito con i **tag KDoc**, che iniziano sempre con `@`:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` è seguito dal nome del parametro e poi dalla sua descrizione; c'è un `@param` per ogni parametro. `@return` descrive il valore che la funzione restituisce. L'ordine è sempre lo stesso: prima il sommario, poi i tag `@param`, infine `@return`.

---

Una funzione con più di un parametro ha un tag `@param` per ognuno di essi, scritti nello stesso ordine dei parametri:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
Un tag è comunque solo un commento: se rinomini un parametro e dimentichi il tag, nulla si rompe, ma la documentazione inizia a mentire. Aggiorna il KDoc insieme alla firma.

---

Il compilatore cerca i commenti solo nel codice, mai dentro una **stringa letterale**. Tra le doppie virgolette, `//` e `/* */` sono caratteri ordinari:
```kotlin
println("50 // 2") // prints 50 // 2
```
Il primo `//` fa parte del testo, il secondo inizia un vero commento. Questo sorprende soprattutto con gli indirizzi web, che contengono `//` subito dopo il protocollo.

---

Alcuni commenti seguono una convenzione che gli editor capiscono. I **marker** più comuni sono:
- `// TODO: ...` segnala qualcosa che deve ancora essere scritto
- `// FIXME: ...` segnala codice notoriamente sbagliato e che deve essere corretto

```kotlin
val limit = 10
// TODO: read the limit from the settings
```
Per il compilatore sono commenti ordinari; IntelliJ IDEA li raccoglie in una finestra dedicata, così il lavoro in sospeso è facile da trovare. Un `TODO` di solito sta accanto a un segnaposto che mantiene il codice compilabile finché non viene scritta l'implementazione vera e propria. Quando completi il lavoro, sostituisci il segnaposto e rimuovi il marker nella stessa modifica, così il commento non mente mai sullo stato del codice.

---

Un `FIXME` è diverso da un `TODO`: il codice esiste già, ma si sa che è sbagliato. Un buon `FIXME` dice qual è il bug e, quando possibile, dà un esempio che lo mostra, così chi verrà dopo può correggerlo rapidamente. Come per il `TODO`, elimina il marker una volta corretto il bug, ma conserva il commento di documentazione, che resta valido.

---

Un buon commento spiega **perché** il codice fa qualcosa, non **cosa** fa. Il codice mostra già cosa succede; ripeterlo a parole aggiunge solo rumore e diventa obsoleto appena il codice cambia:
```kotlin
// set timeout to 30
val timeout = 30
```
Il motivo che sta dietro al numero è ciò che un lettore non può indovinare:
```kotlin
// the server drops idle connections after 35 seconds, so stop earlier
val timeout = 30
```
Se un commento si limita a ripetere la riga sotto di sé, eliminalo o sostituiscilo con il motivo. I commenti migliori sono quelli che dicono qualcosa che il codice non può dire.
