Un **Set** è una collezione di valori **unici**: ogni valore può comparire al massimo una volta, e non esiste un indice per accedere a un valore in base alla posizione.
I set sono perfetti quando ti interessa solo *quali* valori sono presenti, non quante volte o in quale ordine.
Crei un set vuoto con `new Set()`, aggiungi un valore con `add(value)` e controlli se un valore è presente con `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// stampa true
console.log(colors.has("green"));
// stampa false
```

---

Aggiungere un valore già presente nel set non fa **nulla**: i duplicati vengono semplicemente ignorati.
Altri due elementi essenziali:
- `delete(value)` rimuove il valore dal set
- `size` è il numero di valori memorizzati (una proprietà, quindi senza parentesi)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// stampa 2
tags.delete("css");
console.log(tags.size);
// stampa 1
```

---

`add()` restituisce il set stesso, quindi più chiamate possono essere concatenate:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Che tu concateni o no, un valore già presente non viene mai aggiunto una seconda volta, quindi `size` conta ogni valore distinto una sola volta.

---

Puoi costruire un set in un colpo solo passando un array a `new Set()`. I duplicati nell'array vengono eliminati, quindi questo è il modo più rapido per trovare i valori distinti di un array:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// stampa 3
```
L'operatore **spread** `...` funziona al contrario e trasforma un set di nuovo in un array:
```javascript
let unique = [...distinct];
console.log(unique);
// stampa [ 1, 2, 3 ]
```
`Array.from(distinct)` fa la stessa cosa.

---

Un set ricorda l'ordine in cui i valori sono stati aggiunti, e puoi scorrerlo con `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// stampa 3
// stampa 1
// stampa 2
```
I set hanno anche un metodo `forEach()` che chiama una funzione per ogni valore:
```javascript
nums.forEach((n) => console.log(n * 10));
// stampa 30
// stampa 10
// stampa 20
```

---

`delete(value)` restituisce `true` quando il valore è stato rimosso e `false` quando non era nel set.
Per rimuovere **tutti** i valori in una volta, chiama `clear()`:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// stampa true
console.log(cart.delete("pen"));
// stampa false
cart.clear();
console.log(cart.size);
// stampa 0
```

---

Un set decide se due valori sono "uguali" con quasi la stessa regola di `===` (tranne che `NaN` conta come uguale a se stesso). Per stringhe e numeri questo confronta il contenuto, ma **gli oggetti vengono confrontati per riferimento**: due oggetti letterali con campi identici sono due valori diversi.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// stampa 1
people.add({ name: "Alice" });
console.log(people.size);
// stampa 2
```
Solo aggiungere di nuovo esattamente lo stesso oggetto viene ignorato.

---

Combinare spread e `filter()` ti dà le operazioni classiche della teoria degli insiemi. Ognuna costruisce una **nuova** collezione e lascia invariati gli originali:
- **unione**, ogni valore presente in `a`, in `b` o in entrambi: `new Set([...a, ...b])`
- **intersezione**, solo i valori presenti in **entrambi**: `[...a].filter((x) => b.has(x))`
- **differenza**, i valori di `a` che **non** sono in `b`: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// stampa [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// stampa [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// stampa [ 1, 2 ]
```
I motori JavaScript più recenti offrono anche `a.union(b)`, `a.intersection(b)` e `a.difference(b)` direttamente sui set, ma le versioni con spread e filter funzionano ovunque.

---

Per mantenere la stessa interfaccia di `Map`, un set offre i metodi iteratori `values()`, `keys()` e `entries()`.
Poiché un set non ha chiavi, `keys()` è solo un altro nome per `values()`, e `entries()` restituisce ogni valore **due volte**, come coppia `[value, value]`:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// stampa [ 'a', 'b' ]
console.log([...letters.entries()]);
// stampa [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
In pratica ne hai raramente bisogno: `for...of` e spread scorrono già direttamente i valori.

---

`new Set()` accetta qualsiasi **iterabile**, non solo array. Una stringa è iterabile carattere per carattere, quindi ti dà i caratteri distinti di un testo:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// stampa [ 'h', 'e', 'l', 'o' ]
```
