I **dizionari** (Object) sono simili agli array, ma si accede ai valori cercando una *chiave* invece di un indice.
Una chiave può essere qualsiasi stringa o numero.
I dizionari sono racchiusi in parentesi graffe, così:
```javascript
var nomeDizionario = {"chiave1": 1, "chiave2": 2, "chiave3": 3};
```
Questo e' un dizionario chiamato `nomeDizionario` con tre *coppie di chiavi-valore*.
La `chiave1` indica il valore `1`, `chiave2` il `2`, e così via.

---

Accedere ai valori del dizionario con la chiave e' come accedere ai valori dell'array con l'indice:
```javascript
// ottieni il valore dell'età dal dizionario utente
utente['eta'];
```

---

Come gli array, i dizionari sono _mutabili_.
Ciò significa che possono essere modificati dopo essere stati creati (se non vengono dichiarati costanti).
Un vantaggio e' che possiamo aggiungere nuove coppie di _chiave/valore_ al dizionario dopo che e' stato creato, ad esempio:
```javascript
nomeDizionario[nuovoNomeChiave] = nuovoValore;
```

---

Poiche' i dizionari (dichiarati come variabili) sono mutabili, possono essere cambiati in molti modi.
I valori possono essere rimossi da un dizionario con il metodo `removeValue(forKey:)`:
```javascript
delete nomeDizionario[nomeChiave];
```
rimuoverà la chiave `nomeChiave` e il suo valore associato dal dizionario

---

E se volessimo elencare tutte le chiavi del dizionario?
Beh, possiamo usare il metodo `Object.keys()`.

---

E se volessimo elencare tutti i valori del dizionario?
Bene, possiamo usare il metodo `Object.values()`.

---

Esattamente come per gli array, possiamo fare un ciclo per gli elementi del dizionario usando il metodo `Object.entries()`.
```javascript
var utente = {"nome": "John", "cognome": "Hood", "eta": 30};
for (const [chiave, valore] of Object.entries(utente)) {
    console.log(`${chiave}: ${valore}`);
}
```
