In Dart, una **lista** è una raccolta ordinata di elementi. Il modo più semplice per creare una lista è usare la sintassi letterale `[]`:

```dart
List<int> numbers = [1, 2, 3];
```

Puoi anche usare l'inferenza di tipo con `var`:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

L'annotazione di tipo `List<String>` indica a Dart che ogni elemento della lista deve essere un `String`.

---

Le liste in Dart sono **indicizzate a partire da zero**, il che significa che il primo elemento si trova all'indice `0`, il secondo all'indice `1`, e così via.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

L'accesso a un elemento tramite indice avviene con la sintassi `list[index]`.

---

Il metodo `.add()` aggiunge un singolo elemento alla **fine** di una lista:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Nota che `.add()` modifica la lista **in-place** e restituisce `void`.

---

La proprietà `.length` restituisce il numero di elementi in una lista:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Una lista vuota ha lunghezza `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

Il metodo `.contains()` verifica se una lista include un dato valore. Restituisce `true` se trovato, `false` altrimenti:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Questo è utile per verificare l'appartenenza senza necessità di un ciclo.
