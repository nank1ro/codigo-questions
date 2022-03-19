I **dizionari** sono simili a liste e tuple, ma si accede ai valori cercando una *chiave* invece di un indice.
Una chiave può essere qualsiasi stringa o numero.
I dizionari sono racchiusi in parentesi graffe, così:
```python
d = {"chiave1": 1, "chiave2": 2, "chiave3": 3}
```
Questo e' un dizionario chiamato `d` con tre *coppie di chiavi-valore*.
`chiave1` indica il valore `1`, `chiave2` il `2`, e così via.

---

Accedere ai valori del dizionario con la chiave e' come accedere ai valori della lista con l'indice:
```python
utente['eta']
# ottieni il valore dell'età dal dizionario utente
```

---

Come le liste, i dizionari sono _mutabili_.
Ciò significa che possono essere modificati dopo essere stati creati.
Un vantaggio e' che possiamo aggiungere nuove coppie di _chiave/valore_ al dizionario dopo che e' stato creato, ad esempio:
```python
nome_dizionario[nuovo_nome_chiave] = nuovo_valore
```

---

La lunghezza `len()` di un dizionario e' il numero di coppie _chiave-valore_ che ha.
Ogni coppia conta una sola volta, anche se il valore e' una lista. (Esatto: si possono anche inserire liste all'interno dei dizionari!)

---

Poiche' i dizionari sono mutabili, possono essere cambiati in molti modi.
I valori possono essere rimossi da un dizionario con la parola chiave `del`:
```python
del nome_dizionario[nome_chiave]
```
rimuoverà la chiave `nome_chiave` e il suo valore associato

---

E se volessimo elencare tutte le chiavi del dizionario?
Beh, possiamo usare il metodo `keys()`.

---

E se volessimo elencare tutti i valori del dizionario?
Beh, possiamo usare il metodo `values()`.

---

Esattamente come per le liste, possiamo fare un ciclo per gli elementi del dizionario usando le parole chiave `for..in`
Per ottenere sia la chiave che il valore nel ciclo possiamo usare il metodo `items()`:
```python
for chiave, valore in nome_dizionario:
	print(chiave, valore)
```

---

Possiamo anche usare la parola chiave `in` che abbiamo usato con i cicli per determinare se un dizionario contiene una certa __chiave__

---

Per __aggiungere__ o __modificare__ i valori in un dizionario, possiamo anche usare il metodo `update()` con le coppie di _chiave-valore_ che vogliamo aggiungere tra le parentesi

---

E se volessimo __rimuovere__ un valore da un dizionario?
Possiamo usare il metodo `pop()`:
```python
nome_dizionario.pop("nome_chiave")
```
