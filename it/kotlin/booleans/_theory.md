Kotlin ha un tipo Booleano basico, chiamato `Boolean`.
I valori booleani sono indicati come logici, perché possono essere solo veri o falsi.
È possibile valutare qualsiasi espressione in Kotlin, e ottenere una delle due risposte, `true` o `false`.

---

Possiamo memorizzare il valore booleano `true` in una variabile proprio come un numero o una stringa.

---

Il valore opposto di `true` e' `false`

---

I valori booleani possono anche essere negati usando il simbolo `!` prima del valore booleano, ad esempio:
```kotlin
println(!true) // stampa false
println(!false) // stampa true
```

---

Possiamo anche creare espressioni booleane usando gli operatori `&&` (_e_) e `||` (_o_):

- `&&` (_e_): produce `true` (vero) solo se l'espressione booleana a sinistra dell'operatore e quella alla destra sono entrambe vere.
- `||` (_o_): produce `true` (vero) se almeno una delle espressioni alla sinitra e alla destra dell'operatore è vera, o se entrambe sono vere.

```kotlin
println(true && true) // stampa true
println(true && false) // stampa false
println(false && false) // stampa false
println(true || true) // stampa true
println(true || false) // stampa true
println(false || false) // stampa false
```
