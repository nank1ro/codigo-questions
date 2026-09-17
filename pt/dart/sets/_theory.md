Um **conjunto** (`Set`) é uma coleção de valores **únicos**: o mesmo valor pode aparecer no máximo uma vez. Assim como um map, um conjunto é criado com a sintaxe literal `{}`, mas ele contém valores simples em vez de pares `chave: valor`:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

A anotação de tipo `Set<int>` informa ao Dart que cada elemento é um `int`. Assim como nas listas e nos maps, `var` infere o tipo a partir do literal:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Um conjunto nunca armazena o mesmo valor duas vezes. Se um literal contiver duplicatas, apenas a primeira ocorrência é mantida e as demais são descartadas em tempo de execução sem nenhum erro (o analisador avisará sobre um literal que repete um valor):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

A propriedade `.length` retorna quantos elementos **únicos** o conjunto contém:

```dart
print(letters.length); // 3
```

---

O método `.add(value)` insere um único valor. Ele retorna `true` se o valor foi adicionado e `false` se ele já estava no conjunto, caso em que nada muda. O método `.addAll(iterable)` insere todos os elementos de uma lista ou de outro conjunto, novamente ignorando os que já estão presentes:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, já está lá
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

Um literal `{}` vazio é um **map**, não um conjunto. Para criar um conjunto vazio, dê a ele um tipo:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

O método `.remove(value)` exclui um valor do conjunto. Ele retorna `true` se o valor estava lá e `false` caso contrário:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

Para excluir todos os elementos de uma vez, use `.clear()`.

---

Para verificar se um valor está em um conjunto, use `.contains(value)`, que retorna um `bool`. A propriedade `.isEmpty` é `true` quando o conjunto não tem elementos, e `.isNotEmpty` quando ele tem pelo menos um:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

O conjunto padrão em Dart lembra a **ordem de inserção**: quando você o imprime ou percorre, os elementos saem na ordem em que foram adicionados pela primeira vez. Adicionar um valor que já está presente não o move:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Um conjunto é um `Iterable`, então você pode percorrer seus elementos diretamente com `for-in`, assim como uma lista. Não há índices: os elementos são visitados na ordem de inserção:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```

---

Conjuntos suportam as operações clássicas de conjuntos. Cada uma retorna um **novo** conjunto e deixa os originais intactos:

- `a.union(b)` contém os elementos que estão em `a` **ou** em `b`
- `a.intersection(b)` contém os elementos que estão em **ambos** `a` e `b`
- `a.difference(b)` contém os elementos de `a` que **não** estão em `b`

```dart
var a = {1, 2, 3};
var b = {2, 3, 4};
print(a.union(b));        // {1, 2, 3, 4}
print(a.intersection(b)); // {2, 3}
print(a.difference(b));   // {1}
```

---

Converter uma lista em um conjunto é a maneira mais fácil de **remover duplicatas**: toda lista tem um método `.toSet()` que retorna um conjunto com seus elementos únicos, na ordem da primeira aparição. Um conjunto tem um método `.toList()` que faz o caminho inverso, então encadear os dois lhe dá uma lista sem duplicatas:

```dart
var votes = ['a', 'b', 'a', 'c', 'b'];
Set<String> unique = votes.toSet();
print(unique); // {a, b, c}
List<String> cleaned = votes.toSet().toList();
print(cleaned); // [a, b, c]
```

---

Tanto listas quanto conjuntos têm um método `.contains()`, mas eles funcionam de maneiras muito diferentes. Uma lista verifica seus elementos um por um desde o início, então uma busca em uma lista longa fica mais lenta conforme a lista cresce. Um conjunto armazena seus elementos pelo seu hash, então `.contains()` encontra um valor em tempo praticamente constante, não importa quantos elementos existam.

Se você precisa verificar a presença de um valor muitas vezes e a ordem ou as duplicatas não importam, um conjunto é a ferramenta certa:

```dart
var banned = {'spam', 'scam'};
print(banned.contains('spam')); // rápido, mesmo com milhões de elementos
```
