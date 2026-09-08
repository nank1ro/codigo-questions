Un **commento** è testo all'interno del tuo codice sorgente destinato alle persone, non al compilatore. Il compilatore scarta i commenti prima di costruire il programma, quindi puoi usarli per spiegare a cosa serve il codice, lasciare promemoria o annotare una decisione.

Il tipo più comune è il **commento su singola riga**: tutto quello che va da `//` alla fine della riga viene ignorato.
```c
// Greet the user
printf("Hello\n");
```
La prima riga non fa nulla quando il programma viene eseguito; solo il `printf` produce output.

---

Siccome il compilatore rimuove completamente i commenti, aggiungere o eliminare un commento non cambia mai ciò che fa un programma. Viene eseguito solo il codice che **non** è commentato.

Questo rende `//` un modo rapido per disattivare una riga di codice senza eliminarla. Questa operazione si chiama **commentare**:
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
La seconda riga ora è un commento, quindi `total` rimane `10`. Rimuovendo il `//` la riga torna attiva.

Commentare è utile mentre fai esperimenti, ma ricorda di ripulire: il codice che resta commentato a lungo non fa che confondere chi lo leggerà dopo.

---

Quando un commento deve occupare più di una riga, il C offre il **commento multi-riga** (detto anche commento a blocco): inizia con `/*` e termina con `*/`, e tutto ciò che sta in mezzo viene ignorato, compresi gli a capo.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
Un commento a blocco può anche essere breve e stare su una sola riga: `/* like this */`.

A differenza di `//`, che si ferma alla fine della riga, un commento `/*` si ferma solo al `*/`. Se dimentichi di chiuderlo, il compilatore tratterà tutto il codice seguente come parte del commento.

---

I commenti a blocco **non si annidano**. Il compilatore termina un commento `/*` al primo `*/` che trova, non importa quanti `/*` vengano prima:
```c
/* outer /* inner */ still code */
```
Qui il commento termina subito dopo `inner`, quindi `still code */` viene compilato come codice e produce un errore.

Questo è importante quando vuoi commentare un blocco che contiene già un commento `/* */`: il `*/` interno chiuderebbe il tuo commento esterno troppo presto. In tal caso, metti invece `//` davanti a ogni riga.

---

Un commento non ha bisogno di una riga tutta per sé: può seguire il codice sulla stessa riga. Questo è un **commento a fine riga**, ed è un buon posto per una breve nota su quella specifica istruzione:
```c
int retries = 3; // give up after three attempts
```
Sia `//` che `/* */` funzionano come commenti a fine riga, ma fai attenzione con `/*`: siccome si ferma solo al `*/`, un `/*` non chiuso alla fine di una riga ingoia le righe che seguono, e il programma non compila più.

---

Un uso comune dei commenti a blocco è il **commento di intestazione**: un breve blocco posto direttamente sopra una funzione che dice cosa fa, cosa significano i suoi parametri e cosa restituisce.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
Chi chiama `to_seconds` può ora leggere l'intestazione invece del corpo. Mantieni l'intestazione accanto alla funzione, così vengono aggiornate insieme.

---

Il compilatore sostituisce ogni commento con un singolo spazio. Questo significa che un commento `/* */` può apparire ovunque possa apparire uno spazio, anche in mezzo a un'istruzione o a un'espressione:
```c
int area = width /* cm */ * height /* cm */;
```
Questo è occasionalmente utile per etichettare gli operandi o gli argomenti di una chiamata. Un commento `//` non può farlo, perché commenterebbe il resto della riga, incluso il codice che segue.

---

I programmatori usano alcune parole chiave convenzionali all'inizio di un commento per segnalare lavoro non ancora finito:

- `TODO` contrassegna qualcosa che deve ancora essere scritto
- `FIXME` contrassegna del codice che si sa essere sbagliato e che deve essere corretto

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Editor e strumenti possono elencare questi contrassegni, così il lavoro in sospeso è facile da trovare. Una volta completato il lavoro, elimina il contrassegno: un `TODO` obsoleto è fuorviante.

---

Un buon commento spiega **perché** il codice fa qualcosa, non **cosa** fa. Il codice mostra già cosa succede; ripeterlo a parole aggiunge rumore e diventa obsoleto appena il codice cambia:
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
Il motivo dietro quei numeri è ciò che chi legge non può indovinare:
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
Se un commento si limita a ripetere la riga sottostante, eliminalo o sostituiscilo con il motivo.

---

Riassumendo: usa `//` per brevi note e commenti a fine riga, `/* */` per blocchi più lunghi e commenti di intestazione, contrassegna il lavoro non finito con `TODO` o `FIXME`, ed elimina il codice commentato e i contrassegni obsoleti quando non servono più.
