Leggere i valori di un array un indice alla volta è rumoroso:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
Il **destructuring** fa lo stesso lavoro in una riga. A sinistra di `=` scrivi un pattern che assomiglia all'array stesso, e ogni nome al suo interno riceve l'elemento nella stessa posizione:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
Il pattern non deve coprire tutto l'array: gli elementi in più vengono semplicemente ignorati, e un nome senza un elemento corrispondente diventa `undefined`.

---

Il destructuring è più utile proprio dove arriva un array: un argomento di una funzione, o il risultato di una chiamata. Invece di tenersi l'array e indicizzarlo dappertutto, lo scomponi una volta sola e dai alle parti dei nomi veri:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
Nell'array originale non viene copiato né modificato nulla, il pattern si limita a leggerlo.

---

A volte conta solo un elemento nascosto nell'array. Puoi lasciare una posizione vuota nel pattern, mantenendo la virgola che la separa: una posizione vuota del genere si chiama **buco**, e salta l'elemento senza dargli un nome:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
Conta le virgole, non i nomi: ogni virgola sposta il pattern in avanti di una posizione, che ci sia un nome prima o no.

---

Un array non è sempre lungo quanto il pattern si aspetta. Scrivere `= value` dopo un nome gli dà un **valore predefinito**, usato ogni volta che l'array non ha nulla in quella posizione:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
Il valore predefinito viene valutato solo quando serve, quindi può essere persino una chiamata di funzione, e si può dare un valore predefinito a qualsiasi posizione, non solo all'ultima.

---

Un pattern può anche stare alla sinistra di un assegnamento normale, senza `const` o `let` davanti, e allora scrive in variabili che esistono già. Questo trasforma lo scambio di due valori in una riga sola, senza variabile temporanea:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
Il lato destro viene costruito prima, quindi entrambi i vecchi valori sono già al sicuro nell'array temporaneo quando avviene l'assegnamento. Attento al punto e virgola nella riga precedente: altrimenti una riga che inizia con `[` verrebbe letta come un indice di ciò che la precede.

---

Anche gli oggetti possono essere destrutturati, con le graffe al posto delle quadre. Qui la posizione non conta nulla: ogni nome viene confrontato con la **chiave** che porta lo stesso nome:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
Scambiare `age` e `name` nel pattern non cambia nulla, e le chiavi che il pattern non menziona vengono semplicemente lasciate dov'è. Un nome senza una chiave corrispondente diventa `undefined`.

---

I pattern degli oggetti si combinano con i valori predefiniti esattamente come quelli degli array, il che li rende un modo ordinato per leggere un oggetto di configurazione le cui chiavi possono esserci o meno:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
Siccome l'intero pattern è una sola istruzione, una funzione può estrarre tutto ciò che le serve dal suo argomento nella primissima riga.

---

Un pattern di oggetto nomia le sue variabili come le chiavi, il che è scomodo quando le chiavi sono criptiche o già occupate. Scrivere `key: newName` **rinomina** la variabile:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
Leggilo come "prendi `n`, chiamalo `name`". I due punti non dichiarano un tipo, e `n` in sé non viene mai creata come variabile: l'unica variabile creata è `name`. Un nome rinominato può comunque ricevere un valore predefinito, scritto dopo: `{ n: name = "unknown" }`.

---

I valori predefiniti hanno una regola che sorprende tutti: valgono **solo** per `undefined`. Una chiave che esiste e contiene `null`, `0`, `""` o `false` è un valore vero, quindi il pattern la prende e il valore predefinito non viene mai usato:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null` si comporta qui come `0`, anche se spesso significa "nessun valore" in una risposta di un'API. Quando anche `null` deve essere sostituito, destruttura prima e ripiega dopo con `??`.

---

Quando una chiave contiene un altro oggetto o un array, il pattern può semplicemente proseguire e descrivere anche quella forma:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
Attenzione a ciò che quella riga crea: `address: { city }` significa "entra in `address`", non "dammi `address`", quindi solo `city` diventa una variabile. Per ottenere entrambi, cita la chiave due volte: `const { address, address: { city } } = user;`. I pattern di array e di oggetto si annidano liberamente uno dentro l'altro, come in `{ tags: [first] }`.

---

Prendere la testa di un array e conservarne la coda è un'esigenza così comune che i pattern hanno una sintassi apposita. Tre punti davanti all'ultimo nome lo rendono un **elemento rest**, che raccoglie tutti gli elementi rimanenti in un array nuovo di zecca:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
Un elemento rest deve stare per ultimo nel pattern e non può avere un valore predefinito: quando non resta nulla, è semplicemente un array vuoto.

---

Anche i pattern di oggetto hanno un rest, e lì raccoglie in un nuovo oggetto tutte le chiavi che il pattern non ha citato:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
È il modo più breve per costruire una copia di un oggetto senza una delle sue chiavi: l'originale non viene mai toccato e l'oggetto rest è nuovo e contiene i valori rimanenti.

---

Un pattern può sostituire il nome di un parametro nella dichiarazione di una funzione, così l'estrazione avviene nel momento della chiamata:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
Dentro il corpo non esiste alcuna variabile oggetto, solo `width` e `height`. Chi chiama passa un unico oggetto, ma la firma documenta esattamente quali chiavi la funzione legge, e le chiavi possono arrivare in qualsiasi ordine.

---

Un parametro destrutturato con valori predefiniti crea un comodo oggetto di opzioni, ma si rompe ancora quando chi chiama non passa nulla: leggere una chiave da `undefined` solleva un `TypeError`. Dare all'intero pattern un valore predefinito `{}` risolve il problema:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
Leggi la riga dall'esterno verso l'interno: `= {}` fornisce un oggetto vuoto quando l'argomento manca, e poi ogni valore predefinito interno riempie la propria chiave.

---

`Object.entries(obj)` trasforma un oggetto in un array di coppie `[chiave, valore]`. Metti un pattern di array nella testa di un ciclo `for...of` e ogni coppia viene estratta mentre il ciclo procede:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
È il modo leggibile per percorrere un oggetto: niente indici, niente accessi, solo i due nomi che ti interessano. `Object.keys` e `Object.values` danno un solo lato ciascuno, `Object.entries` li dà entrambi.

---

Tutto quello visto finora appartiene a un'unica sintassi, quindi i pezzi si combinano liberamente: un pattern di oggetto può annidare un altro pattern di oggetto, che può contenere una chiave rinominata con un valore predefinito, accanto a un pattern di array che termina con un elemento rest. Una sola riga descrive allora l'intera forma che una funzione si aspetta:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
Mantieni la leggibilità: un pattern che non sta più in un paio di righe di solito è il segno che la funzione sta chiedendo troppo.
