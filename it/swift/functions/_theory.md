Avrai potuto considerare la situazione in cui vorresti riutilizzare un pezzo di codice, cambiando solo alcuni valori.
Invece di riscrivere l'intero codice, e' molto piu' pulito definire una funzione, che può poi essere utilizzata ripetutamente.
In Swift usiamo la parola chiave `func` seguita dal nome della funzione:
```swift
func saluta() {
    print("Ciao!")
}
saluta() // stampa "Ciao!"
```

---

Le parentesi nella definizione di __funzione__ non devono essere vuote se vogliamo specificare i parametri

---

A volte vogliamo che una funzione __restituisca__ un valore.
Bene, possiamo usare la parola chiave `return`

---

Le funzioni possono avere parametri di ingresso multipli, che vengono scritti tra le parentesi della funzione, separati dalle virgole.
```swift
func saluta(name: String, nuovoUtente: Bool) -> String {
  var saluto: String = "Ciao \(name)!"
  if (nuovoUtente) {
    saluto += " Benvenuto a bordo :)"
  }
  return saluto
}
// stampa "Ciao Smith! Benvenuto a bordo :)"
print(saluta(name: "Smith", nuovoUtente: true))
```

---

È possibile utilizzare una tupla come `return` di una funzione, in modo da restituire più valori assieme.

---

Se non si vuole utilizzare una label per indicare un parametro, possiamo scrivere un trattino basso `_` prima del parametro.

---

È possibile definire un valore di _default_ per qualsiasi parametro di una funzione assegnando un valore al parametro dopo il suo tipo.
Se viene definito un valore di default, si può omettere quel parametro quando si chiama la funzione
```swift
func unaFunzione(parametroSenzaDefault: Int, parametroConDefault: Int = 12) {
    // esegui qui il codice della funzione
}
```

---

Un _parametro variadico_ accetta zero o più valori di un tipo specifico.
Per aggiungere un parametro variadico usiamo `...` dopo il nome del tipo di parametro.
I valori passati ad un parametro variadico sono resi disponibili all'interno del corpo della funzione come array del tipo appropriato.
Per esempio, un parametro variadico con il nome `numeri` e un tipo `Double...` viene reso disponibile all'interno del corpo della funzione come un array costante chiamato `numeri` di tipo `[Double]`

---

Nelle funzioni possiamo aggiungere un _commento opzionale_ che spieghi il funzionamento di una funzione:
```swift
/// Stampa 'Hello World' nella console.
func helloWorld() {
    print("Hello, World!")
}
```
Possiamo usare `///` per commentare una singola linea, mentre `/** */` per un commento multi-linea
