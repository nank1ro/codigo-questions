Swift e' un linguaggio di programmazione orientato agli oggetti, il che significa che manipola i costrutti di programmazione chiamati oggetti.
Si può pensare ad un oggetto come ad una singola struttura di dati che contiene sia dati che funzioni; le funzioni di un oggetto sono chiamate i suoi metodi.
Per esempio, quando richiami:
```swift
nomeDizionario.removeValue(forKey: "nomeChiave")
```
Swift controlla se `nomeDizionario` ha un metodo chiamato `removeValue()` (che tutti i dizionari hanno) ed esegue quel metodo se lo trova.

---

Le _strutture_ e le _classi_ sono costrutti generici e flessibili che diventano i mattoni del codice del vostro programma.
Una _classe/struttura_ di base è composta solo dalla parola chiave `class` o `struct` e dal suo nome, per esempio:
```swift
class NomeClasse {
	// definizione classe
}
struct NomeClasse {
	// definizione struttura
```

---

Inseriamo qualcosa all'interno della nostra classe `Animale`

---

La definizione di una classe non crea un oggetto.
Per farlo, dobbiamo creare un'__istanza__ di una classe

---

Quando una classe ha le proprie funzioni, queste si chiamano __metodi__.

---

Le strutture e le classi di Swift hanno molte cose in comune. Entrambe possono:
- Definire le proprietà per memorizzare i valori
- Definire i metodi per fornire funzionalità
- Definire i subscript per fornire l'accesso ai loro valori utilizzando la sintassi dei subscript
- Definire gli inizializzatori per impostare il loro stato iniziale
- Essere esteso per espandere le loro funzionalità al di là di un'implementazione predefinita
- Conformarsi ai protocolli per fornire funzionalità standard di un certo tipo

Ma le classi hanno capacità aggiuntive che le strutture non hanno:
- L'ereditarietà permette ad una classe di ereditare le caratteristiche di un'altra
- Il Type casting consente di controllare e interpretare il tipo di istanza di classe durante il runtime
- I deinizializzatori consentono ad un'istanza di una classe di liberare le risorse che ha assegnato
- Il conteggio dei riferimenti permette più di un riferimento ad un'istanza di classe

---

È possibile accedere alle proprietà di un'istanza utilizzando la _sintassi punto_.
Nella sintassi punto, si scrive il nome della proprietà immediatamente dopo il nome dell'istanza, separato da un punto `.`, senza spazi:
```swift
istanza.proprieta
```
Utilizzando la stessa sintassi possiamo anche aggiornare il valore di una proprietà

---

Un vantaggio delle strutture è che hanno un inizializzatore generato automaticamente, che si può usare per inizializzare le proprietà dei membri di nuove istanze di strutture.
I valori iniziali delle proprietà della nuova istanza possono essere passati all'inizializzatore per nome
