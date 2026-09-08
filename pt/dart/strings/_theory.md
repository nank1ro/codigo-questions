Uma **String** é um pedaço de texto: uma sequência de caracteres entre aspas. Em Dart você pode usar aspas simples `'...'` ou aspas duplas `"..."`, elas funcionam exatamente da mesma forma:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Escolher um tipo de aspas permite usar o outro tipo dentro do texto sem precisar de escape:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

Se você precisar da mesma aspa dentro do texto, escape-a com uma barra invertida: `'It\'s sunny'`.

---

Duas strings podem ser unidas em uma nova com o operador `+`, chamado **concatenação**:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart também une dois **literais** de string escritos um ao lado do outro, sem nenhum operador. Isso é útil para dividir um texto longo em várias linhas:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Apenas strings podem ser concatenadas com `+`: `'Age: ' + 30` é um erro de compilação, porque `30` é um `int`.

---

Em vez de concatenar, você pode inserir valores diretamente em uma string com **interpolação**. Escreva `$name` para inserir o valor de uma variável, e `${expression}` para inserir o resultado de qualquer expressão:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

A interpolação funciona com qualquer tipo: números, booleanos e listas são convertidos em texto automaticamente, então `'Age: $age'` é válido mesmo `age` sendo um `int`.

---

Toda string sabe quantos caracteres possui através de sua propriedade `.length`. Espaços e pontuação também contam como caracteres:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

Você pode ler um único caractere com colchetes e seu **índice**, começando em `0`. O resultado é uma `String` de um único caractere:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Ler um índice fora da string (como `word[5]`) gera um erro.

---

Strings em Dart são **imutáveis**: uma vez criada, uma string nunca muda. Métodos como `.toUpperCase()` e `.toLowerCase()` não modificam a string original, eles **retornam uma nova**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

Se você quiser que a variável passe a conter o novo valor, reatribua o resultado a ela: `word = word.toUpperCase();`.

---

Textos digitados por um usuário costumam ter espaços extras ao redor. O método `.trim()` retorna uma cópia da string sem espaços em branco no início e no fim (espaços, tabulações e quebras de linha). `.trimLeft()` e `.trimRight()` removem apenas de um dos lados:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

O método `.substring(start, end)` retorna a parte de uma string do índice `start` até, **sem incluir**, o índice `end`. Se você omitir `end`, ele pega tudo até o final da string:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Vários métodos permitem buscar dentro de uma string:

- `.contains(other)` retorna `true` se `other` aparece em qualquer lugar da string
- `.startsWith(other)` e `.endsWith(other)` verificam o início e o fim
- `.indexOf(other)` retorna o índice da primeira ocorrência, ou `-1` se não for encontrada

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

Todos eles diferenciam maiúsculas de minúsculas: `'Dart'.contains('dart')` é `false`.

---

O método `.replaceAll(from, to)` retorna uma nova string em que **toda** ocorrência de `from` é substituída por `to`. `.replaceFirst(from, to)` substitui apenas a primeira:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

O método `.split(separator)` corta uma string em uma `List<String>` a cada ocorrência do separador. O oposto é `.join(separator)`, um método de listas que cola os elementos em uma única string:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Chamar `.split('')` com um separador vazio retorna uma lista com cada caractere individual.
