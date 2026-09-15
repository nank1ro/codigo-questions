Una **espressione regolare** (o **regex**) è un piccolo pattern che descrive una forma di testo. La usi per rispondere a domande come "questa stringa contiene un numero?" o "dove compare la parola `cat`?".

In JavaScript il modo più breve per scriverla è un **letterale regex**: il pattern fra due barre.
```javascript
const pattern = /cat/;
```
I caratteri ordinari in un pattern coincidono con se stessi, quindi `/cat/` corrisponde alle tre lettere `c`, `a`, `t` in un qualsiasi punto di una stringa.

La cosa più semplice che puoi fare con un pattern è chiederti se compare in una stringa. Il metodo **`test`** prende il testo e restituisce `true` o `false`:
```javascript
console.log(/cat/.test("the cat sleeps"));
// stampa true
console.log(/cat/.test("the dog sleeps"));
// stampa false
```
Nota che `test` cerca il pattern *da qualche parte* nella stringa; non è necessario che tutta la stringa corrisponda.

---

I pattern diventano utili quando descrivono un *tipo* di carattere invece di un singolo carattere esatto. Poche **sequenze di escape** coprono la maggior parte delle esigenze:
- `\d` una cifra qualsiasi, da `0` a `9`
- `\w` un carattere di parola qualsiasi: una lettera, una cifra o `_`
- `\s` uno spazio bianco qualsiasi: uno spazio, una tabulazione, un ritorno a capo

```javascript
console.log(/\d/.test("room 12"));
// stampa true
console.log(/\d/.test("lobby"));
// stampa false
```
Un **quantificatore** dice quante volte può ripetersi il pezzo precedente. Il più comune è `+`, che significa "uno o più":
```javascript
console.log(/\d+/.test("42"));
// stampa true
```
Quindi `/\d/` corrisponde a una singola cifra e `/\d+/` corrisponde a una sequenza di cifre. Per un semplice `test` i due si comportano allo stesso modo, perché a entrambi basta che sia presente una cifra.

---

Un letterale come `/\d+/` è fisso una volta scritto. Quando il pattern deve essere **costruito a runtime**, usa il **costruttore `RegExp`**, che prende il pattern come stringa:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// stampa true
```
C'è una trappola. Dentro una stringa, una barra inversa inizia una sequenza di escape per la *stringa*, quindi scompare prima che la regex la veda. Per mettere una vera barra inversa nel pattern devi raddoppiarla:
```javascript
const digits = new RegExp("\\d+");
// lo stesso pattern di /\d+/
```
Scrivendo invece `new RegExp("\d+")` si ottiene il pattern `/d+/`, che corrisponde alla lettera `d`, non a una cifra.

Preferisci il letterale quando il pattern è noto mentre scrivi il codice; è più breve e non ha bisogno di barre inverse raddoppiate.

---

Altri due mattoni ti permettono di descrivere quasi ogni forma di testo.

Una **classe di caratteri** è un insieme di caratteri fra parentesi quadre; corrisponde esattamente a uno di essi. Un trattino scrive un intervallo, e una `^` all'inizio nega l'insieme:
```javascript
/[aeiou]/   // una vocale
/[a-z]/     // una lettera minuscola
/[A-Z0-9]/  // una lettera maiuscola o una cifra
/[^0-9]/    // un carattere che non è una cifra
```
I **quantificatori** dicono quante volte si ripete il pezzo precedente: `+` uno o più, `*` zero o più, `?` zero o uno, e `{n}` esattamente `n` volte.

Infine, le **ancore** legano il pattern alle estremità del testo: `^` significa "inizia qui" e `$` significa "finisce qui". Senza di esse un pattern può corrispondere in un punto qualsiasi della stringa, quindi `/\d{2}/.test("abc12def")` è `true`. Con entrambe le ancore deve corrispondere tutta la stringa:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// stampa false
console.log(/^\d{2}$/.test("12"));
// stampa true
```

---

`test` dice solo sì o no. Per ottenere il testo trovato, chiama **`match`** sulla stringa:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
Quando non trova nulla, `match` restituisce `null`. Quando trova qualcosa, restituisce un risultato simile a un array:
- `match[0]` è il testo che è stato trovato
- `match.index` è la posizione in cui inizia la corrispondenza
- `match.input` è la stringa intera che è stata cercata

```javascript
console.log(match[0]);
// stampa 42
console.log(match.index);
// stampa 6
```
Poiché il risultato può essere `null`, controllalo prima di leggere `match[0]`.

---

Poiché `match` restituisce `null` quando il pattern è assente, leggere `match[0]` direttamente lancia `TypeError: Cannot read properties of null`. Mettici una protezione:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
L'operatore di nullish coalescing scrive la stessa protezione su una riga, perché `match?.[0]` è `undefined` quando `match` è `null`:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Le parentesi tonde attorno a una parte di un pattern creano un **gruppo di acquisizione**: il testo trovato da quella parte viene messo da parte, così puoi rileggerlo.

I gruppi compaiono dopo `match[0]`, numerati da sinistra a destra in base alla loro parentesi di apertura:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// stampa 2026-09-12
console.log(match[1]);
// stampa 2026
console.log(match[3]);
// stampa 12
```
Quindi `match[0]` è sempre la corrispondenza intera, e `match[1]`, `match[2]`, ... sono i gruppi. Un gruppo che fa parte di un pattern che non corrisponde affatto fa sì che l'intero `match` restituisca `null`.

---

Acquisisci solo ciò che ti serve. Un gruppo non è solo un modo per rileggere un pezzo; dice anche a chi legge quale parte del pattern conta. In un pattern per l'ora in cui vuoi solo i minuti, raggruppa soltanto i minuti e lascia il resto senza gruppo:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// stampa 35
```
Il pattern intero deve comunque corrispondere, quindi le ore e i secondi restano comunque richiesti; semplicemente non vengono acquisiti. Meno gruppi significano meno numeri da tenere a mente quando leggi `match[1]`, `match[2]` e così via.

---

Contare le parentesi stanca, e aggiungere un gruppo nel mezzo di un pattern rinumera tutto ciò che viene dopo. Un **gruppo con nome** evita entrambi i problemi: scrivi `?<name>` subito dopo la parentesi di apertura e rileggi il pezzo da `match.groups`:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// stampa 2026
console.log(match.groups.month);
// stampa 09
```
I gruppi con nome restano comunque numerati, quindi `match[1]` continua a funzionare, ma `match.groups.year` dice che cosa significa il valore. Quando il pattern non ha alcun gruppo con nome, `match.groups` è `undefined`.

---

Tutto ciò che è stato visto finora si è fermato alla prima corrispondenza. I **flag**, scritti dopo la barra di chiusura di un letterale, cambiano questo e altri dettagli della ricerca:
- `g` global: trova ogni corrispondenza, non solo la prima
- `i` ignore case, quindi `/cat/i` corrisponde anche a `Cat` e `CAT`

Con il flag `g`, `match` si comporta diversamente: restituisce un semplice array delle **stringhe** trovate, senza `index` e senza gruppi, oppure `null` quando non ci sono corrispondenze:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// stampa [ '1', '22', '333' ]
console.log(numbers.length);
// stampa 3
```
I flag possono essere combinati in qualsiasi ordine, come in `/cat/gi`. Con il costruttore `RegExp` vanno nel secondo argomento: `new RegExp("\\d+", "g")`.

---

Il flag `g` ti dà ogni stringa trovata, ma butta via i gruppi. Quando ti servono i gruppi di *ogni* corrispondenza, usa **`matchAll`**. Restituisce un iteratore di oggetti corrispondenza completi, ognuno esattamente come il risultato di un normale `match`:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// stampa a -> 1
// stampa b -> 2
```
`matchAll` richiede il flag `g`; senza, lancia un `TypeError`. Poiché restituisce un iteratore, espandilo con `[...text.matchAll(pattern)]` quando vuoi un vero array, e nota che non produce proprio nulla quando il pattern non trova mai corrispondenze.

---

**`replace`** restituisce una nuova stringa con la corrispondenza sostituita con qualcos'altro. La stringa originale non viene mai modificata.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// stampa the dog sleeps
```
Dentro la stringa di sostituzione alcune sequenze hanno un significato speciale:
- `$1`, `$2`, ... il testo acquisito dal gruppo 1, dal gruppo 2, ...
- `$<name>` il testo acquisito da un gruppo con nome
- `$&` la corrispondenza intera

È ciò che rende `replace` uno strumento di riscrittura e non solo una sostituzione:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// stampa 12/09/2026
```
Senza il flag `g` viene sostituita solo la **prima** corrispondenza.

---

Per riscrivere **ogni** corrispondenza invece della prima hai due opzioni:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// stampa a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// stampa a# b#
```
**`replaceAll`** è il più chiaro dei due, e accetta anche una semplice stringa come pattern. Quando gli dai una regex, quella regex **deve** portare il flag `g`, altrimenti lancia un `TypeError`; è esattamente ciò che previene il bug silenzioso di usare `replace` e sistemare solo la prima corrispondenza.

---

La sostituzione non deve essere per forza una stringa. Quando passi una **funzione**, viene chiamata una volta per ogni corrispondenza e qualunque cosa restituisca viene inserita al posto di quella corrispondenza.

La funzione riceve prima la corrispondenza intera, poi ogni gruppo di acquisizione:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// stampa 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// stampa Ann Lee
```
È l'unico modo per calcolare la sostituzione a partire dal testo trovato, cosa che `$1` da solo non può fare.

---

**`split`** taglia una stringa in un array. Con una semplice stringa taglia su quel testo esatto, ma con una regex taglia a ogni corrispondenza del pattern, il che permette a una sola chiamata di gestire separatori che variano:
```javascript
console.log("a, b;c".split(", "));
// stampa [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// stampa [ 'a', 'b', 'c' ]
```
I separatori stessi non fanno parte del risultato. Fai attenzione a un separatore all'inizio o alla fine della stringa: produce una stringa vuota nell'array, perché su quel lato c'è un campo vuoto.

---

Un ultimo flag completa la serie. Per impostazione predefinita `^` e `$` indicano l'inizio e la fine della **stringa intera**, quindi un pattern ancorato con `^` può corrispondere solo all'inizio assoluto, anche quando il testo ha più righe.

Il flag **`m`** (multiline) cambia questo: `^` e `$` corrispondono allora anche subito dopo e subito prima di ogni ritorno a capo, così ogni riga è ancorata da sola:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// stampa [ 'note a' ]
console.log(text.match(/^note.*/gm));
// stampa [ 'note a', 'note c' ]
```
Due dettagli contano qui. Per impostazione predefinita il `.` non corrisponde a un ritorno a capo (solo il flag `s` cambia questo), quindi `.*` si ferma da solo alla fine della riga. E `match` con il flag `g` restituisce `null`, non un array vuoto, quando non trova nulla, quindi abbinalo a `?? []` quando prometti di restituire un array.
