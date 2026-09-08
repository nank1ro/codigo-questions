Una **mappa** è una collezione di **coppie chiave-valore**: ogni valore è memorizzato sotto una chiave univoca, e usi la chiave per ritrovare il valore. Una mappa si crea con la sintassi letterale `{}`, scrivendo ogni coppia come `key: value`:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

L'annotazione di tipo `Map<String, int>` indica a Dart che ogni chiave è una `String` e ogni valore è un `int`. Come per le liste, `var` deduce il tipo dal letterale:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

Per leggere un valore usi la chiave tra parentesi quadre, proprio come un indice in una lista:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

Se la chiave non è nella mappa, la ricerca **non** genera un errore: restituisce `null`. Per questo motivo il tipo di `ages['Ann']` è `int?` (un `int` nullable), non `int`:

```dart
print(ages['Zed']); // null
```

---

Un'assegnazione con `map[key] = value` **aggiunge** una nuova coppia, quando la chiave non è ancora nella mappa, oppure **aggiorna** il valore memorizzato sotto una chiave esistente:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // aggiunge Bob
ages['Ann'] = 31; // aggiorna Ann
print(ages); // {Ann: 31, Bob: 25}
```

Le nuove chiavi vengono aggiunte dopo quelle esistenti, quindi una mappa ricorda l'ordine di inserimento.

---

Il metodo `.remove(key)` elimina una chiave e il suo valore dalla mappa. Restituisce il valore rimosso, oppure `null` se la chiave non era presente:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

La proprietà `.length` restituisce il numero di coppie chiave-valore:

```dart
print(ages.length); // 1
```

---

Per verificare se una mappa ha una determinata chiave, usa `.containsKey(key)`. Per verificare se una qualsiasi coppia memorizza un determinato valore, usa `.containsValue(value)`. Entrambi restituiscono un `bool`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Leggere una chiave mancante non genera mai un errore, quindi considera sempre che una ricerca può restituirti `null`. Uno schema sicuro è fornire un valore di riserva con l'operatore `??`:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

La proprietà `.keys` restituisce tutte le chiavi di una mappa e `.values` restituisce tutti i valori, nell'ordine di inserimento. Sono `Iterable` pigri, quindi chiama `.toList()` quando hai bisogno di una vera `List`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
