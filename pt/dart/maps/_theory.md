Um **Map** é uma coleção de **pares chave-valor**: cada valor é armazenado sob uma chave única, e você usa a chave para encontrar o valor novamente. Um map é criado com a sintaxe literal `{}`, escrevendo cada par como `chave: valor`:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

A anotação de tipo `Map<String, int>` informa ao Dart que cada chave é uma `String` e cada valor é um `int`. Assim como nas listas, `var` infere o tipo a partir do literal:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

Para ler um valor você usa a chave entre colchetes, assim como um índice em uma lista:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

Se a chave não estiver no map, a busca **não** lança um erro: ela retorna `null`. Por isso o tipo de `ages['Ann']` é `int?` (um `int` anulável), e não `int`:

```dart
print(ages['Zed']); // null
```

---

Atribuir com `map[key] = value` **adiciona** um novo par, quando a chave ainda não está no map, ou **atualiza** o valor armazenado em uma chave existente:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // adiciona Bob
ages['Ann'] = 31; // atualiza Ann
print(ages); // {Ann: 31, Bob: 25}
```

Novas chaves são adicionadas depois das existentes, então um map lembra a ordem de inserção.

---

O método `.remove(key)` exclui uma chave e seu valor do map. Ele retorna o valor removido, ou `null` se a chave não existia:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

A propriedade `.length` retorna o número de pares chave-valor:

```dart
print(ages.length); // 1
```

---

Para verificar se um map contém uma determinada chave, use `.containsKey(key)`. Para verificar se algum par armazena um determinado valor, use `.containsValue(value)`. Ambos retornam um `bool`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Ler uma chave inexistente nunca lança um erro, então sempre considere que uma busca pode te dar `null`. Um padrão seguro é fornecer um valor alternativo com o operador `??`:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

A propriedade `.keys` retorna todas as chaves de um map e `.values` retorna todos os valores, na ordem de inserção. Ambas são `Iterable`s preguiçosas (lazy), então chame `.toList()` quando precisar de uma `List` de verdade:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```

---

Um map literal vazio `{}` não tem pares para inferir os tipos, então dê a ele tipos explícitos com `<K, V>{}` ou com uma anotação de tipo:

```dart
var cart = <String, int>{};
Map<String, int> other = {};
```

A propriedade `.isEmpty` é `true` quando um map não tem pares, e `.isNotEmpty` é `true` quando ele tem pelo menos um:

```dart
print(cart.isEmpty); // true
cart['pen'] = 2;
print(cart.isNotEmpty); // true
```

---

O método `.forEach()` executa uma função uma vez para cada par. A função recebe dois parâmetros: a chave e o valor:

```dart
var ages = {'Ann': 30, 'Bob': 25};
ages.forEach((name, age) {
  print('$name is $age');
});
// Ann is 30
// Bob is 25
```

---

Um map não é um `Iterable`, então você não pode percorrê-lo diretamente com `for-in`. Em vez disso, percorra `.entries`: cada elemento é um `MapEntry` com um `.key` e um `.value`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
for (var entry in ages.entries) {
  print('${entry.key}: ${entry.value}');
}
// Ann: 30
// Bob: 25
```

---

O método `.putIfAbsent(key, ifAbsent)` adiciona um par **somente se** a chave ainda não estiver no map. O segundo argumento é uma função que produz o valor. Se a chave já existir, o map permanece inalterado. Em ambos os casos, o valor agora armazenado sob a chave é retornado:

```dart
var ages = {'Ann': 30};
ages.putIfAbsent('Ann', () => 99); // Ann já está lá, nada muda
ages.putIfAbsent('Bob', () => 25); // Bob é adicionado
print(ages); // {Ann: 30, Bob: 25}
```

---

O método `.update(key, update)` substitui o valor de uma chave existente. O segundo argumento é uma função que recebe o valor atual e retorna o novo. Se a chave não existir, `.update()` lança um erro, a menos que você passe uma função `ifAbsent` que produza o valor inicial:

```dart
var stock = {'apple': 3};
stock.update('apple', (n) => n + 1); // apple se torna 4
stock.update('kiwi', (n) => n + 1, ifAbsent: () => 1); // kiwi é adicionado com 1
print(stock); // {apple: 4, kiwi: 1}
```
