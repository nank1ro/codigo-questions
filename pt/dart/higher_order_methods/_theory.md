Um **método de ordem superior** é um método que recebe uma função como argumento. As coleções do Dart oferecem muitos deles, e a função que você passa geralmente é uma função anônima escrita com a sintaxe de seta `(x) => ...`.

`map` é o mais comum: ele chama a função em cada elemento e produz os resultados, um para cada elemento, deixando a coleção original intocada:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Observe os **parênteses** na saída. `map` não retorna uma `List`: ele retorna um `Iterable`, uma sequência que você pode percorrer. Para obter uma lista de verdade de volta, chame **`toList()`** nela:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Colchetes na saída são o sinal de que você está vendo uma `List`, parênteses de que está vendo um `Iterable` simples.

---

`where` recebe uma função que retorna um `bool`, chamada de **predicado**, e mantém apenas os elementos para os quais ela responde `true`. A ordem dos elementos que sobrevivem nunca muda:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Como `map`, `where` retorna um `Iterable` e nunca modifica a coleção original, então `toList()` é novamente o que transforma o resultado em uma `List`.

Em outras linguagens esse método se chama `filter`; em Dart ele é `where`.

---

A função dada a `map` não precisa retornar o mesmo tipo dos elementos que recebe. Mapear uma lista de strings para seus comprimentos transforma uma `List<String>` em um `Iterable<int>`, que `toList()` então torna uma `List<int>`:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

O resultado sempre tem **exatamente tantos elementos quanto o original**, na mesma ordem: `map` transforma elementos, ele nunca adiciona ou remove nenhum.

---

Alguns métodos de ordem superior respondem a uma pergunta sobre a coleção em vez de construir uma nova. Eles recebem um predicado e retornam um `bool`:

- `any` é `true` quando **pelo menos um** elemento satisfaz o predicado
- `every` é `true` quando **todos** os elementos o satisfazem

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Ambos param assim que a resposta é certa: `any` no primeiro elemento que corresponde, `every` no primeiro que não corresponde.

Em uma coleção vazia `any` é `false` e `every` é `true`: não há elemento para provar o primeiro, e nenhum para quebrar o segundo.

---

`map` e `where` são **preguiçosos**: chamá-los não executa nada. Eles retornam um `Iterable` que lembra a fonte e a função, e a função só é chamada enquanto algo percorre o resultado, um elemento por vez.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // nothing computed yet
print(doubled.first);                      // computes only 2
```

`toList()` é o que **materializa** a sequência: ele a percorre do começo ao fim e armazena cada resultado em uma `List` de verdade.

A preguiça tem duas consequências que vale a pena lembrar. Um `Iterable` preguiçoso é recomputado toda vez que você o itera, então materializar uma vez com `toList()` é mais barato quando você precisa dos valores mais de uma vez. E ele continua olhando para a coleção original, então mudar essa coleção muda o que o `Iterable` produz:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` combina uma coleção inteira em um **único valor**. Ele recebe dois argumentos: o valor inicial do **acumulador**, e uma função que recebe o acumulador até o momento e o próximo elemento, e retorna o novo acumulador:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Aqui `acc` começa em `0`, depois se torna `1`, `3`, `6` e finalmente `10`.

O acumulador não precisa ser um número, nem do mesmo tipo dos elementos: começar de `''` e adicionar texto constrói uma `String` a partir de uma lista de qualquer coisa.

Um detalhe para ter em mente: o Dart deduz o tipo do acumulador a partir do valor inicial **e** de onde o resultado é usado. Dentro de `print(...)` o tipo esperado é desconhecido, então armazene o resultado em uma variável primeiro (ou escreva `fold<int>(...)`), caso contrário o compilador reclama que não pode usar `+` no acumulador.

---

`reduce` é o parente mais curto de `fold`. Ele não recebe valor inicial: o **primeiro elemento** é o acumulador inicial, e a função roda para cada elemento restante:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Como não há valor inicial, o resultado sempre tem o **mesmo tipo dos elementos**, e chamar `reduce` em uma coleção vazia lança um `StateError`: não há primeiro elemento de onde começar. `fold` não tem esse problema, e é por isso que é a escolha mais segura por padrão.

`reduce` está em seu melhor quando você procura um elemento entre muitos, como o maior:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` retorna o **primeiro** elemento que corresponde a um predicado, em vez de todos eles:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

Quando nada corresponde, não há elemento para retornar, então `firstWhere` lança um `StateError`. Para dar uma resposta em vez de um erro, passe o argumento nomeado **`orElse`**: uma função sem parâmetros que produz o valor alternativo.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` é uma função, não um valor simples, então ela só é chamada quando a busca falha. Escrever `orElse: 'none'` não compila.

---

Quando a função que você passa para `map` retorna uma coleção para cada elemento, você acaba com uma sequência de coleções. **`expand`** faz o mesmo trabalho, mas depois junta todas elas em uma única sequência plana:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

A ordem é preservada: tudo o que o primeiro elemento produz vem primeiro, depois tudo o que o segundo produz, e assim por diante.

Como a coleção retornada pode ter qualquer tamanho, `expand` também é a maneira de produzir **mais ou menos** elementos do que você tinha no começo: retornar uma lista vazia para um elemento simplesmente o descarta.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` mantém os **primeiros** `n` elementos e `skip(n)` os descarta. Nenhum dos dois recebe uma função, mas ambos retornam um `Iterable` preguiçoso, então eles se encaixam naturalmente entre os outros métodos de ordem superior:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Pedir mais elementos do que existem não é um erro: você simplesmente recebe o que existe, ou um resultado vazio.

`takeWhile` e `skipWhile` são as versões com um predicado. Eles pegam ou descartam elementos a partir do começo **enquanto** o predicado for verdadeiro, e param no primeiro elemento que não o satisfaz, mesmo que os seguintes voltem a satisfazê-lo:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart não tem um método `sorted`. `sort` pertence a `List`, reordena a lista **no lugar** e não retorna nada:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Como ele retorna `void`, você não pode usar o resultado de jeito nenhum: `final sorted = numbers.sort();` dá um valor que o compilador não deixa você ler. O idioma para uma **cópia** ordenada é `toList()` seguido da cascata `..sort()`: `toList()` faz a cópia, e `..` executa `sort` nela mas continua devolvendo a própria cópia.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], untouched
```

`sort` também aceita um **comparador**: uma função de dois elementos que retorna um número negativo quando o primeiro vem antes do segundo, `0` quando eles são iguais, e um número positivo caso contrário. `compareTo` produz exatamente isso, então ordenar por qualquer critério cabe em uma linha:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` e `reduce` se parecem, e escolher entre os dois se resume a duas perguntas: a coleção pode estar vazia, e o resultado tem o mesmo tipo dos elementos?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String from Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int from Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` só consegue devolver o tipo dos elementos, porque começa a partir de um elemento. `fold` começa a partir de um valor que você escolhe, então o acumulador pode ser um `int` contando, uma `String` crescendo, ou até uma `List` sendo construída. E como esse valor inicial já existe, para uma coleção vazia ele é simplesmente a resposta que `fold` devolve sem mudanças, enquanto `reduce` não tem nada para retornar e lança um erro.

---

Cada um desses métodos retorna um `Iterable`, e todo `Iterable` tem os mesmos métodos de novo. É isso que permite **encadeá-los**: um cálculo inteiro se lê como um pipeline da esquerda para a direita, cada etapa trabalhando sobre o que a anterior produziu.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Só a última etapa precisa de `toList()`: chamá-lo no meio construiria uma lista que ninguém guarda.

O tipo muda ao longo da cadeia, e muda também o que a próxima função recebe: depois de `where` em uma `List<String>` você ainda tem strings, mas depois de `map((w) => w.length)` a etapa seguinte vê números.

Como cada etapa é preguiçosa, a ordem importa para o trabalho feito, não só para o resultado: filtrar primeiro com `where` significa que `map` é chamado em menos elementos.

---

Não há nada de especial nesses métodos: eles simplesmente têm uma **função como parâmetro**, e suas próprias funções podem fazer o mesmo. O tipo de um parâmetro de função é escrito como o tipo de retorno, depois `Function`, depois os tipos dos parâmetros entre parênteses:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

Quem chama decide **o que** acontece, a função decide **sobre o quê**. Repare como `operation` é passado direto para `map`: um valor de função pode ser repassado como qualquer outro valor.

O argumento pode ser uma função anônima, ou o **nome** de uma função existente, escrito sem parênteses. Colocar os parênteses a chamaria em vez de passá-la:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

Uma função também pode **retornar** uma função. O tipo de retorno é escrito exatamente como um tipo de parâmetro de função, e o valor retornado costuma ser uma função anônima:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` não multiplica nada: ele constrói e devolve uma nova função que multiplica por `3`. Essa função é então armazenada, chamada, ou passada para `map` como qualquer outra:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

A função retornada continua lembrando de `factor` depois que `multiplier` terminou. Uma função que guarda as variáveis do escopo onde foi criada se chama **closure**, e é isso que torna possíveis fábricas de funções como esta.

---

Juntos, esses métodos substituem a maior parte dos laços escritos à mão. Um pipeline costuma se ler em três etapas: **selecionar** os elementos com `where`, **transformá-los** com `map`, e depois **combiná-los** com `fold`:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Como `fold` escolhe seu próprio valor inicial, ele também pode encerrar uma cadeia com um tipo que não tem nada a ver com os elementos, como uma `String` crescendo um pedaço de cada vez:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Cada etapa continua curta e diz o que faz, que é a verdadeira razão para preferi-las a um laço que faz as três coisas ao mesmo tempo.
