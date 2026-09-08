Una **enumerazione** (o *enum*) è un tipo comune per un piccolo gruppo di valori fissi e correlati: i giorni della settimana, i semi di un mazzo di carte, i possibili stati di un ordine.
A differenza di molti linguaggi, JavaScript **non** ha una parola chiave `enum`. Il sostituto idiomatico è un semplice oggetto le cui proprietà sono i membri, passato a `Object.freeze()` in modo che nessuno possa modificarlo in seguito:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
```
Per convenzione l'oggetto viene dichiarato con `const`, il suo nome inizia con una lettera maiuscola e i nomi dei membri sono scritti in `UPPER_CASE`, esattamente come le altre costanti.

---

Il valore memorizzato in ciascun membro dipende da te. Le **stringhe** sono la scelta più comune perché sono leggibili quando vengono stampate, registrate o salvate in un file:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// prints done
```
Una volta congelato, l'oggetto non può nemmeno ricevere nuove proprietà, e `Object.isFrozen(obj)` ti dice se un oggetto è stato congelato:
```javascript
console.log(Object.isFrozen(Status));
// prints true
```

---

Perché congelare l'oggetto? Un oggetto congelato rifiuta ogni modifica: assegnare un valore a un membro esistente, aggiungerne uno nuovo o eliminarne uno non ha alcun effetto.
Come si manifesta il rifiuto dipende dalla modalità in cui viene eseguito il tuo codice:
- in **modalità non strict** (*sloppy mode*, la modalità predefinita per gli script semplici) l'assegnazione viene **ignorata silenziosamente**
- in **modalità strict** (file che iniziano con `"use strict"`, moduli ES e corpi di classe) viene **lanciato** un `TypeError`

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// prints s
console.log(Size.MEDIUM);
// prints undefined
```
In entrambi i casi l'enumerazione mantiene i valori che hai definito, che è esattamente ciò che vuoi da un insieme di costanti.

---

I membri possono anche contenere **numeri**. I valori numerici sono utili quando i membri hanno un ordine naturale, perché puoi confrontarli con gli operatori consueti:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// prints true
```
Il compromesso è la leggibilità: stampare `Priority.HIGH` mostra `3`, che ti dice molto meno di quanto farebbe la stringa `"high"`.

---

Poiché un'enumerazione è solo un oggetto, i soliti strumenti per gli oggetti ti permettono di ispezionarla:
- `Object.keys(Enum)` restituisce un array con i **nomi** dei membri
- `Object.values(Enum)` restituisce un array con i **valori** dei membri
- `Object.entries(Enum)` restituisce un array di coppie `[name, value]`

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
Combinare `Object.values()` con il metodo dell'array `includes()` è il modo standard per verificare se un valore arbitrario, ad esempio uno letto da un input dell'utente, è un membro valido:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
