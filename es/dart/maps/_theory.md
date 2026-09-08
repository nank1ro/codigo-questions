Un **mapa** es una colección de **pares clave-valor**: cada valor se almacena bajo una clave única, y usas la clave para volver a encontrar el valor. Un mapa se crea con la sintaxis literal `{}`, escribiendo cada par como `key: value`:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

La anotación de tipo `Map<String, int>` le indica a Dart que cada clave es un `String` y cada valor es un `int`. Al igual que con las listas, `var` infiere el tipo a partir del literal:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

Para leer un valor usas la clave entre corchetes, igual que un índice en una lista:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

Si la clave no está en el mapa, la búsqueda **no** lanza un error: devuelve `null`. Por esta razón, el tipo de `ages['Ann']` es `int?` (un `int` nullable), no `int`:

```dart
print(ages['Zed']); // null
```

---

Una asignación con `map[key] = value` **agrega** un nuevo par, cuando la clave todavía no está en el mapa, o **actualiza** el valor almacenado bajo una clave existente:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // agrega Bob
ages['Ann'] = 31; // actualiza Ann
print(ages); // {Ann: 31, Bob: 25}
```

Las claves nuevas se añaden después de las existentes, así que un mapa recuerda el orden de inserción.

---

El método `.remove(key)` elimina una clave y su valor del mapa. Devuelve el valor eliminado, o `null` si la clave no estaba:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

La propiedad `.length` devuelve el número de pares clave-valor:

```dart
print(ages.length); // 1
```

---

Para comprobar si un mapa tiene una clave dada, usa `.containsKey(key)`. Para comprobar si algún par almacena un valor dado, usa `.containsValue(value)`. Ambos devuelven un `bool`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Leer una clave que falta nunca lanza un error, así que siempre debes considerar que una búsqueda puede darte `null`. Un patrón seguro es proporcionar un valor por defecto con el operador `??`:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

La propiedad `.keys` da todas las claves de un mapa y `.values` da todos los valores, en orden de inserción. Son `Iterable`s perezosos, así que llama a `.toList()` cuando necesites una `List` real:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
