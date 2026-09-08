Un **Set** è una collezione di valori **unici**: lo stesso valore può comparire al massimo una volta. Come una mappa, un Set si crea con la sintassi letterale `{}`, ma contiene valori semplici invece di coppie `key: value`:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

L'annotazione di tipo `Set<int>` indica a Dart che ogni elemento è un `int`. Come per le liste e le mappe, `var` deduce il tipo dal letterale:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Un Set non memorizza mai lo stesso valore due volte. Se un letterale contiene duplicati, viene mantenuta solo la prima occorrenza e le altre vengono scartate a runtime senza alcun errore (l'analyzer ti avviserà di un letterale che ripete un valore):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

La proprietà `.length` restituisce quanti elementi **unici** contiene il Set:

```dart
print(letters.length); // 3
```

---

Il metodo `.add(value)` inserisce un singolo valore. Restituisce `true` se il valore è stato aggiunto e `false` se era già presente nel Set, nel qual caso non cambia nulla. Il metodo `.addAll(iterable)` inserisce ogni elemento di una lista o di un altro Set, saltando anch'esso quelli già presenti:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

Un letterale `{}` vuoto è una **mappa**, non un Set. Per creare un Set vuoto, assegnagli un tipo:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

Il metodo `.remove(value)` elimina un valore dal Set. Restituisce `true` se il valore era presente e `false` in caso contrario:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

Per eliminare tutti gli elementi in una volta, usa `.clear()`.

---

Per verificare se un valore è presente in un Set usa `.contains(value)`, che restituisce un `bool`. La proprietà `.isEmpty` è `true` quando il Set non ha elementi, e `.isNotEmpty` quando ne ha almeno uno:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Il Set predefinito in Dart ricorda l'**ordine di inserimento**: quando lo stampi o lo scorri, gli elementi vengono restituiti nell'ordine in cui sono stati aggiunti per la prima volta. Aggiungere un valore già presente non lo sposta:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Un Set è un `Iterable`, quindi puoi scorrere i suoi elementi direttamente con `for-in`, proprio come una lista. Non ci sono indici: gli elementi vengono visitati nell'ordine di inserimento:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
