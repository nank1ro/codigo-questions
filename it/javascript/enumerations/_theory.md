Una **enumerazione** (o *enum*) è un tipo comune per un piccolo gruppo di valori fissi e correlati: i giorni della settimana, i semi di un mazzo di carte, i possibili stati di un ordine.
A differenza di molti linguaggi, JavaScript **non** ha una parola chiave `enum`. Il sostituto idiomatico è un semplice oggetto le cui proprietà sono i membri, passato a `Object.freeze()` in modo che nessuno possa modificarlo in seguito:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// stampa red
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
// stampa done
```
Una volta congelato, l'oggetto non può nemmeno ricevere nuove proprietà, e `Object.isFrozen(obj)` ti dice se un oggetto è stato congelato:
```javascript
console.log(Object.isFrozen(Status));
// stampa true
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
// stampa s
console.log(Size.MEDIUM);
// stampa undefined
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
// stampa true
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
// stampa [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// stampa [ 'red', 'blue' ]
```
Combinare `Object.values()` con il metodo dell'array `includes()` è il modo standard per verificare se un valore arbitrario, ad esempio uno letto da un input dell'utente, è un membro valido:
```javascript
console.log(Object.values(Color).includes("red"));
// stampa true
console.log(Object.values(Color).includes("pink"));
// stampa false
```

---

Le enumerazioni si abbinano naturalmente all'istruzione `switch`, che confronta un valore con un elenco di etichette `case` ed esegue il codice della prima corrispondente.
Ogni ramo termina con `return` o `break`, e il ramo opzionale `default` viene eseguito quando nulla corrisponde:
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// stampa go
```
Confronta sempre con i membri (`Light.RED`), mai con i valori grezzi (`"red"`): se il valore cambia in futuro, lo `switch` continua a funzionare.

---

Risalire da un valore al nome del suo membro si chiama **ricerca inversa**. Scorri i nomi con `Object.keys()` e scegli il primo il cui valore corrisponde, usando il metodo dell'array `find()`, che restituisce il primo elemento per cui il callback è `true` (o `undefined` se non ce n'è nessuno):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// stampa HIGH
```
`Priority[key]` legge il membro il cui nome è memorizzato nella variabile `key`, la stessa notazione con parentesi quadre che usi per qualsiasi oggetto.

---

I membri stringa hanno un punto debole: qualsiasi stringa con lo stesso testo viene accettata come membro.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// stampa true
```
Quando vuoi membri uguali **solo** a se stessi, usa un `Symbol`. `Symbol(description)` crea un valore completamente nuovo, diverso da ogni altro simbolo, anche uno creato con la stessa descrizione:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// stampa true
console.log(Suit.HEARTS === Symbol("hearts"));
// stampa false
console.log(typeof Suit.HEARTS);
// stampa symbol
```
Il testo che passi è solo un'etichetta per il debug; puoi rileggerlo con la proprietà `description` (`Suit.HEARTS.description` è `"hearts"`).

---

I valori di un'enumerazione vengono spesso usati come **chiavi** di un altro oggetto, ad esempio per mappare ogni membro a un'etichetta o a un prezzo. All'interno di un oggetto letterale, racchiudere una chiave tra parentesi quadre `[ ]` valuta l'espressione e usa il suo risultato come chiave (una **chiave calcolata**). Funziona sia con membri di tipo stringa che di tipo simbolo:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// stampa Completed
```
Senza le parentesi, `Status.DONE: "Completed"` sarebbe un errore di sintassi, e `"Status.DONE"` sarebbe una semplice chiave stringa.

---

Quando ogni membro ha bisogno di più dati o di propri metodi, una **classe** può svolgere il ruolo dell'enumerazione. Ogni membro è un'istanza della classe, memorizzata in una proprietà `static`, cioè una proprietà che appartiene alla classe stessa invece che a ciascuna istanza:
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// stampa Earth
```
Chiama `Object.freeze(Planet)` dopo la classe per impedire a chiunque di aggiungere o sostituire membri, e congela ogni istanza nel costruttore con `Object.freeze(this)` in modo che i membri stessi rimangano di sola lettura.
