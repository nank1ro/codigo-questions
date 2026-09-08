JavaScript ha due modi diversi per dire "qui non c'è alcun valore".
`undefined` significa che un valore **non è mai stato fornito**. Una variabile dichiarata senza valore contiene `undefined`, e lo stesso vale per una proprietà che non esiste in un oggetto:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` è un valore che **tu** assegni di proposito per dire "vuoto, e lo so":
```javascript
let owner = null;
console.log(owner);
// prints null
```
Quindi `undefined` è di solito il linguaggio che ti dice che manca qualcosa, mentre `null` è il programmatore che dichiara che qualcosa è volutamente vuoto.

---

Le funzioni producono `undefined` in altre due situazioni.
Quando chiami una funzione con **meno argomenti** di quanti ne dichiara, i parametri mancanti contengono `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Quando una funzione termina **senza un `return`** (o con un semplice `return;`), chiamarla restituisce `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Nota che passare `null` esplicitamente non è la stessa cosa che omettere l'argomento: `greet(null)` stampa `null`, perché `null` è un valore reale che è stato passato alla funzione.

---

L'operatore `typeof` restituisce il tipo di un valore come stringa. Per `undefined` risponde `"undefined"`, come ti aspetteresti:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Per `null`, invece, risponde `"object"`. Questo è un bug della primissima versione di JavaScript che non è mai stato corretto, perché troppo codice dipende da esso:
```javascript
console.log(typeof null);
// prints object
```
Quindi `typeof` è un modo affidabile per rilevare `undefined`, ma non `null`. Per controllare `null`, confronta direttamente con esso: `value === null`.

---

Come si confrontano tra loro `null` e `undefined`? Dipende dall'operatore.
L'uguaglianza **lasca** `==` li tratta come la stessa cosa, e li considera diversi da qualsiasi altro valore, incluso `0`, `""` e `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
L'uguaglianza **stretta** `===` confronta anche il tipo, e `null` e `undefined` hanno tipi diversi:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

Nella maggior parte dei casi non ti interessa *quale* dei due marcatori di "assenza di valore" hai ricevuto: vuoi solo sapere se c'è un valore.
Poiché `null == undefined` è `true` e nessun altro valore è lascamente uguale a `null`, il confronto `value == null` è l'idioma standard per intercettare **entrambi** in una volta:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
Questo è l'unico caso in cui `==` è preferito a `===`: scrivere `value === null || value === undefined` fa esattamente lo stesso lavoro, solo più lungo.
Valori come `0`, `""` e `false` *non* sono `null`: sono valori reali che per caso sono falsy.

---

Leggere una proprietà di `null` o `undefined` è un errore che ferma il programma:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` è `undefined`, e `undefined` non ha proprietà. L'operatore di **optional chaining** `?.` risolve questo problema: se il valore alla sua sinistra è `null` o `undefined`, l'intera espressione si ferma e vale `undefined` invece di lanciare un errore:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Quando il lato sinistro ha un valore, `?.` si comporta esattamente come un normale `.`. Puoi concatenarne diversi: `user.address?.street?.name` restituisce `undefined` non appena manca un qualsiasi anello.

---

L'optional chaining non è limitato alle proprietà con il punto. Esistono altre due forme.
`?.[]` legge un elemento o una chiave calcolata solo quando il lato sinistro ha un valore:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` chiama una funzione solo quando esiste, il che è utile per i callback opzionali:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
In ogni forma, il controllo si applica al valore **immediatamente prima** del `?.`: `post?.tags?.[0]` è sicuro anche quando `post` stesso è `null` o `undefined`.

---

Una volta che sai che un valore può mancare, di solito vuoi un **predefinito** al suo posto. Due operatori lo fanno, e differiscono in ciò che considerano "mancante".
`a || b` restituisce `b` ogni volta che `a` è **falsy**: non solo `null` e `undefined`, ma anche `0`, `""`, `false` e `NaN`.
L'operatore di **nullish coalescing** `a ?? b` restituisce `b` solo quando `a` è `null` o `undefined`, e conserva ogni altro valore:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Usa `??` quando `0`, `""` o `false` sono valori legittimi che devono essere conservati, e `||` quando vuoi davvero sostituire ogni valore falsy.

---

Uno schema molto comune è "compila questa proprietà solo se non è ancora impostata". Scritto con `??` ripete il nome:
```javascript
options.timeout = options.timeout ?? 1000;
```
L'operatore di **nullish assignment** `??=` fa la stessa cosa in un solo passo: assegna il lato destro solo quando il lato sinistro è attualmente `null` o `undefined`, e lascia intatto qualsiasi altro valore:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` resta `0` perché `0` non è nullish; `timeout` non esisteva, quindi riceve `1000`. La stessa idea esiste per `||` come `||=`, che sovrascrive ogni valore falsy.

---

Un **parametro predefinito** assegna a un parametro un valore quando chi chiama non ne fornisce uno. La regola è precisa: il valore predefinito è usato solo quando l'argomento è `undefined`, il che include il caso in cui viene omesso. Passare `null` **non** attiva il valore predefinito, perché `null` è un valore:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
I parametri predefiniti seguono la regola dell'`undefined`, mentre `??` copre sia `null` che `undefined`: scegli quello che corrisponde a come la tua funzione verrà chiamata.

---

L'optional chaining e il controllo `== null` lavorano bene insieme: la catena legge il valore annidato senza lanciare errori, e il controllo decide cosa fare quando il risultato manca:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Dentro l'ultimo `return` un normale `.` è sicuro, perché il controllo ha già provato che ogni anello esiste.

---

Molti metodi integrati segnalano "niente trovato" restituendo `undefined`. Il metodo degli array `find(callback)` è l'esempio tipico: restituisce il primo elemento per cui il callback è `true`, oppure `undefined` quando nessun elemento corrisponde:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Leggere `found.price` qui lancerebbe un errore, quindi `?.` e `??` sono i compagni naturali di `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` e `undefined` si comportano diversamente quando un oggetto viene convertito in JSON con `JSON.stringify()`.
Il JSON ha un valore `null` ma niente `undefined`, quindi una proprietà il cui valore è `undefined` viene semplicemente **omessa**, mentre una proprietà `null` viene conservata:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Dentro gli array le posizioni non possono sparire, quindi lì `undefined` diventa `null`:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Controllare `obj.key === undefined` non può distinguere due situazioni: la proprietà non esiste, oppure esiste e contiene il valore `undefined`.
`Object.hasOwn(obj, key)` risponde solo alla prima domanda: restituisce `true` quando l'oggetto ha una proprietà **propria** chiamata `key`, qualunque sia il suo valore:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"Propria" significa dichiarata sull'oggetto stesso: i membri ereditati come `toString` sono disponibili su ogni oggetto ma `Object.hasOwn(config, "toString")` è `false`.
