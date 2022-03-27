Python e' un linguaggio di programmazione orientato agli oggetti, il che significa che manipola i costrutti di programmazione chiamati oggetti.
Si può pensare ad un oggetto come ad una singola struttura di dati che contiene sia dati che funzioni; le funzioni di un oggetto sono chiamate i suoi metodi.
Per esempio, quando richiami:
```python
nome_dizionario.items()
```
Python controlla se `mio_dizionario` ha un metodo `items()` (che tutti i dizionari hanno) ed esegue quel metodo se lo trova.

---

Una classe di base e' composta solo dalla parola chiave `class` e dal nome della classe, per esempio:
```python
class NomeClasse:
	pass
```

---

Sostituiamo `pass` con qualcos'altro.
Il metodo `__init__()` e' richiesto per le classi, ed e' usato per __inizializzare__ gli oggetti che crea.
`__init__()` prende sempre almeno un argomento, `self`, che si riferisce all'oggetto che viene creato.
Si può pensare a `__init__()` come al metodo che avvia ogni oggetto creato dalla classe.

---

Ovviamente, il metodo `__init__()` può usare piu' parametri oltre `self`

---

Il primo argomento di `__init__()` e' usato per riferirsi all'oggetto istanza, e per convenzione, quell'argomento viene chiamato `self`.
Se si aggiungono altri argomenti (per esempio, `genere` e `zampe`), impostando ognuno di questi uguale a `self.genere` e `self.zampe` nel corpo di `__init__()` si farà in modo che quando si crea un oggetto istanza della propria classe `Animale`, sia necessario dare ad ogni istanza un genere ed il numero di zampe, e questi verranno associati all'istanza che si crea

---

La definizione di una classe non crea un oggetto.
Per farlo, dobbiamo creare un'__istanza__ di una classe

---

Quando una classe ha le proprie funzioni, queste si chiamano __metodi__.
Abbiamo già visto uno di questi metodi: `__init__()`.
Ma possiamo anche definire i nostri metodi!
