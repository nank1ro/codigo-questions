Un **Set** è una collezione di valori **unici**: ogni valore può comparire al massimo una volta, e non esiste un indice per accedere a un valore in base alla posizione.
I set sono perfetti quando ti interessa solo *quali* valori sono presenti, non quante volte o in quale ordine.
Crei un set vuoto con `new Set()`, aggiungi un valore con `add(value)` e controlli se un valore è presente con `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
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
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
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
// prints 3
```
L'operatore **spread** `...` funziona al contrario e trasforma un set di nuovo in un array:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` fa la stessa cosa.

---

Un set ricorda l'ordine in cui i valori sono stati aggiunti, e puoi scorrerlo con `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
I set hanno anche un metodo `forEach()` che chiama una funzione per ogni valore:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
