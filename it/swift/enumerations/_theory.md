Una `enumerazione` definisce un tipo comune per un gruppo di valori correlati e consente di lavorare con questi valori in modo sicuro all'interno del proprio codice.
Dichiariamo le enumerazioni utilizzando la parola chiave `enum`:
```swift
enum Colori {
	case blu
	case rosso
	case verde
}
```
I valori definiti in un'enumerazione (come `blu`, `rosso` e `verde`) sono i suoi _casi_.
Utilizziamo la parola chiave `case` per introdurre nuovi casi di enumerazione

---

Più casi di enumerazione possono essere presenti in una singola riga, separati da virgole:
```swift
enum Colori {
	case blu, rosso, verde
}
```

---

Possiamo abbinare i singoli valori dell'enumerazione con una dichiarazione `switch`:
```swift
let colori = Colori.red
switch colori {
	case .blu:
		print("Blu")
	case .rosso:
		print("Rosso")
	case .verde:
		print("Verde")
}
// stampa "Rosso"
```
Tieni presente che se non vuoi fornire un `case` per ogni caso di enumerazione, puoi fornire un `default` case per coprire tutti i casi che non sono stati affrontati esplicitamente

---

Per alcune enumerazioni, e' utile avere una raccolta di tutti i casi di tale enumerazione.
Per abilitarlo bisogna aggiungere `: CaseIterable" dopo il nome dell'enumerazione.
Swift espone una raccolta di tutti i casi con la proprietà `allCases`:
```swift
enum Colori: CaseIterable {
	case blue, rosso, verde
}
for colore in Colori.allCases {
    print(colore)
}
// stampa blue, rosso, verde
```
