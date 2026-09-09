Un **commento** è una nota scritta all'interno del codice sorgente per le persone che lo leggono. Il compilatore ignora completamente i commenti, quindi non modificano mai ciò che il programma fa.

Il commento più semplice è il **commento su una riga**: inizia con `//` e continua fino alla fine della riga.
```swift
// Greets the user
print("Hello")
```
Usa i commenti per spiegare a cosa serve un pezzo di codice, o perché è stato scritto in quel modo.

---

Un commento non ha bisogno di una riga tutta per sé: può seguire il codice sulla stessa riga. Questo è un **commento in coda**, ed è il posto ideale per una breve nota su quella specifica istruzione:
```swift
let retries = 3 // give up after three attempts
```
Tutto ciò che va da `//` alla fine della riga viene ignorato, mentre il codice che lo precede viene eseguito come al solito.

---

Poiché il compilatore rimuove completamente i commenti, aggiungere o eliminare un commento non cambia mai ciò che un programma fa. Viene eseguito solo il codice che **non** è commentato.

Questo rende `//` un modo rapido per disattivare una riga di codice senza eliminarla. Questa operazione si chiama **commentare il codice**:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
La seconda riga ora è un commento, quindi `total` resta `10`. Rimuovendo il `//` la riga torna in vita.

Commentare il codice è comodo mentre sperimenti, ma ricorda di fare pulizia: un codice che resta commentato a lungo non fa che confondere chi lo leggerà dopo.

---

Quando un commento ha bisogno di più di una riga, Swift offre il **commento multi-riga** (chiamato anche commento a blocco): inizia con `/*` e termina con `*/`, e tutto ciò che sta nel mezzo viene ignorato, compresi gli a-capo.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
Un commento a blocco può anche essere breve e stare su una riga sola: `/* like this */`.

---

A differenza di `//`, che si ferma alla fine della riga, un commento `/*` si ferma solo al `*/`. Se dimentichi di chiuderlo, il compilatore tratta tutto il codice seguente come parte del commento e segnala un errore:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
Sia `//` che `/* */` funzionano come commenti in coda, ma con `/*` assicurati sempre che ci sia il `*/`.

---

In molti linguaggi i commenti a blocco non possono contenere altri commenti a blocco, ma in Swift **possono essere annidati**: ogni `/*` deve avere il suo `*/`, e il commento finisce solo quando viene chiuso quello più esterno.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Qui `still a comment */` fa parte del commento esterno, quindi viene stampato solo `done`. È questo che ti permette di commentare un intero blocco di codice anche quando quel blocco contiene già un commento `/* */`.

---

Per commentare più righe in una volta sola, racchiudile in un unico commento a blocco invece di aggiungere `//` a ogni riga:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Grazie all'annidamento questo funziona anche quando una di quelle righe contiene già un commento `/* */`.

---

Un uso comune dei commenti a blocco è il **commento di intestazione**: un breve blocco messo subito sopra una funzione che dice cosa fa e cosa significano i suoi parametri.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Chi chiama `toSeconds` può ora leggere l'intestazione invece del corpo. Tieni l'intestazione vicino alla funzione, così vengono aggiornate insieme.

---

Swift ha un terzo tipo di commento, il **commento di documentazione**: un commento su una sola riga che inizia con `///` (tre barre) messo subito sopra una funzione, un tipo o una proprietà.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
Per il compilatore è solo un commento, ma strumenti come Xcode lo leggono e lo mostrano come testo di aiuto per `greet`. I commenti di documentazione supportano il **Markdown**, quindi puoi usare i backtick per il codice, `**grassetto**` ed elenchi.

---

La prima riga di un commento di documentazione è il **riassunto**: una frase breve che dice cosa fa la funzione. Scrivila alla terza persona, come se descrivessi la funzione: "Returns...", "Adds...", "Checks...".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
Il commento deve stare subito sopra la dichiarazione, senza righe vuote in mezzo, altrimenti Xcode non lo associa alla funzione.

---

I commenti di documentazione esistono anche in forma a blocco: `/**` lo apre e `*/` lo chiude, esattamente come un commento su più righe ma con un secondo asterisco all'inizio.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// testo` e `/** testo */` significano la stessa cosa per gli strumenti; `///` è la scelta più comune nel codice Swift, mentre `/** */` è comodo per descrizioni lunghe. Un normale commento `/* */` o `//` **non** è documentazione, nemmeno se messo sopra una funzione.

---

Dopo il riassunto, un commento di documentazione può descrivere i parametri e il valore restituito con speciali elementi di elenco Markdown che Xcode riconosce:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
L'ordine è sempre lo stesso: prima il riassunto, poi `- Parameter nome:` per ogni parametro, poi `- Returns:`.

---

Alcuni commenti seguono una convenzione che gli editor riconoscono. In Swift i **marcatori** più comuni sono:
- `// MARK: - Titolo` etichetta una sezione del file, così compare nel menu di navigazione di Xcode
- `// TODO: ...` segnala qualcosa che deve ancora essere scritto
- `// FIXME: ...` segnala codice che si sa essere sbagliato e che va corretto

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Per il compilatore sono commenti ordinari; Xcode li elenca, così il lavoro in sospeso è facile da trovare. Una volta finito il lavoro, cancella il marcatore: un `TODO` vecchio è fuorviante.

---

Un `TODO` di solito sta accanto a un segnaposto che tiene il codice compilabile finché non viene scritta l'implementazione vera. Quando completi il lavoro, sostituisci il segnaposto e togli il marcatore nella stessa modifica, così il commento non mente mai sullo stato del codice.

---

Un `FIXME` è diverso da un `TODO`: il codice esiste già, ma si sa che è sbagliato. Un buon `FIXME` dice qual è il bug e, quando possibile, dà un esempio che lo mostra, così la persona successiva può correggerlo in fretta. Come per il `TODO`, cancella il marcatore una volta corretto il bug, ma tieni il commento di documentazione, che è ancora vero.

---

Un buon commento spiega **perché** il codice fa qualcosa, non **cosa** fa. Il codice mostra già cosa succede; ripeterlo a parole aggiunge rumore e invecchia appena il codice cambia:
```swift
// set timeout to 30
let timeout = 30
```
Il motivo dietro il numero è ciò che chi legge non può indovinare:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
Se un commento si limita a ripetere la riga sotto di esso, cancellalo o sostituiscilo con il motivo.
