JavaScript e' un linguaggio di programmazione orientato agli oggetti, il che significa che manipola i costrutti di programmazione chiamati oggetti.
Si può pensare ad un oggetto come ad una singola struttura di dati che contiene sia dati che funzioni; le funzioni di un oggetto sono chiamate i suoi metodi.
Per esempio, quando richiami:
```javascript
nomeDizionario.push("valore");
```
JavaScript controlla se `nomeDizionario` ha un metodo chiamato `push()` (che tutti gli array hanno) ed esegue quel metodo se lo trova.

---

Le _classi_ sono costrutti generici e flessibili che diventano i mattoni del codice del vostro programma.
Una _classe_ di base è composta solo dalla parola chiave `class` e dal suo nome, per esempio:
```javascript
class NomeClasse {
	// definizione classe
}
```

---

Inseriamo qualcosa all'interno della nostra classe `Animale`.
Per aggiungere alcuni _attributi_ dobbiamo usare il `construttore` di default

---

La definizione di una classe non crea un oggetto.
Per farlo, dobbiamo creare un'__istanza__ di una classe
Su JavaScript per creare una nuova istanza di una classe, dobbiamo sempre usare le parola chiave `new` prima del nome della classe.
Se vuoi assegnare un valore di default agli attributi, fallo nella lista di nomi di parametri che assegni al costruttore

---

Quando una classe ha le proprie funzioni, queste si chiamano __metodi__.

---

JavaScript ci permette di creare una classe che eredita da un'altra classe, utilizzando la parola chiave `extends`

---

È possibile accedere alle proprietà di un'istanza utilizzando la _sintassi punto_.
Nella sintassi punto, si scrive il nome della proprietà immediatamente dopo il nome dell'istanza, separato da un punto `.`, senza spazi:
```javascript
istanza.proprieta
```
Utilizzando la stessa sintassi possiamo anche aggiornare il valore di una proprietà
