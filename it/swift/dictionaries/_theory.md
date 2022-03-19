I **dizionari** sono simili ad array e tuple, ma si accede ai valori cercando una *chiave* invece di un indice.
Una chiave può essere qualsiasi stringa o numero.
I dizionari sono racchiusi in parentesi quadre, così:
```swift
var nomeDizionario: [String: Int] = ["chiave1": 1, "chiave2": 2, "chiave3": 3]
```
Questo e' un dizionario chiamato `nomeDizionario` con tre *coppie di chiavi-valore*.
La `chiave1` indica il valore `1`, `chiave2` il `2`, e così via.

---

Accedere ai valori del dizionario con la chiave e' come accedere ai valori dell'array con l'indice:
```swift
// ottieni il valore dell'età dal dizionario utente
utente['eta']
```

---

Come gli array, i dizionari sono _mutabili_.
Ciò significa che possono essere modificati dopo essere stati creati (se non vengono dichiarati costanti).
Un vantaggio e' che possiamo aggiungere nuove coppie di _chiave/valore_ al dizionario dopo che e' stato creato, ad esempio:
```swift
nomeDizionario[nuovoNomeChiave] = nuovoValore
```

---

La lunghezza `count` di un dizionario e' il numero di coppie _chiave-valore_ che ha.
Ogni coppia conta una sola volta, anche se il valore e' un'array. (Esatto: si possono anche inserire liste all'interno dei dizionari!)

---

Poiche' i dizionari sono mutabili, possono essere cambiati in molti modi.
I valori possono essere rimossi da un dizionario con il metodo `removeValue(forKey:)`:
```swift
if let valoreRimosso = nomeDizionario.removeValue(forKey: "nomeChiave") {
    print("Il valore rimosso e' \(valoreRimosso).") // stampa il valore rimosso, se la chiave esiste
}
```
rimuoverà la chiave `nomeChiave` e il suo valore associato dal dizionario

---

E se volessimo elencare tutte le chiavi del dizionario?
Beh, possiamo usare la proprietà `keys`

---

E se volessimo elencare tutti i valori del dizionario?
Beh, possiamo usare la proprietà `values`

---

Esattamente come per gli array, possiamo fare un ciclo per gli elementi del dizionario usando le parole chiave `for..in`
Per ottenere sia la chiave che il valore nel ciclo non dobbiamo specificare alcuna proprietà:
```swift
for (chiave, valore) in nomeDizionario {
    print("\(chiave): \(valore)")
}
```

---

Possiamo anche usare la proprietà `isEmpty` che abbiamo gia' utilizzato con gli array per determinare se un dizionario e' vuoto

---

Per __aggiungere__ o __modificare__ i valori di un dizionario, possiamo anche usare il metodo `updateValue(_:forKey:)`

---

Precedentemente abbiamo visto come rimuovere una coppia di _chiave-valore_ dal dizionario con il metodo `removeValue()`
Possiamo anche rimuovere un elemento assegnando il valore `nil` alla chiave
```swift
nomeDizionario[keyName] = nil
// keyName e' stato rimosso dal dizionario nomeDizionario
```
