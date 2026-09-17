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

---

Alguns caracteres não podem ser digitados diretamente dentro de aspas. **Sequências de escape** começam com uma barra invertida: `\n` é uma nova linha, `\t` é uma tabulação, `\\` é uma barra invertida e `\$` é um cifrão literal (caso contrário `$` inicia uma interpolação):

```dart
print('one\ntwo');   // imprime one e two em linhas separadas
print('Cost: \$5');  // Cost: $5
```

Uma **raw string** é prefixada com `r`: dentro dela, barras invertidas e `$` são caracteres comuns, nada é escapado ou interpolado:

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

Para textos que ocupam várias linhas, use uma **string multilinha** delimitada por aspas triplas `'''` ou `"""`: as quebras de linha dentro dela são mantidas.

```dart
var poem = '''
roses are red
violets are blue''';
```

---

Internamente, cada caractere de uma string é armazenado como um número, seu **code unit** (um código UTF-16). `.codeUnitAt(index)` fornece o código de um caractere e `.codeUnits` fornece a lista inteira. `String.fromCharCode(code)` faz o oposto, construindo uma string a partir de um código:

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

Letras consecutivas têm códigos consecutivos: `'A'` é 65, `'B'` é 66, e assim por diante.

---

Duas strings são iguais com `==` quando contêm exatamente os mesmos caracteres, na mesma ordem. A comparação é **sensível a maiúsculas/minúsculas** e conta cada espaço:

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

Para comparar ignorando maiúsculas/minúsculas, converta ambos os lados antes: `a.toLowerCase() == b.toLowerCase()`. Para ordenação, `.compareTo(other)` retorna um número negativo, `0` ou um número positivo dependendo se a string vem antes, é igual, ou vem depois da outra.

---

Como strings são imutáveis, construir um texto longo com `+=` em um loop cria uma nova string a cada passo. Um **StringBuffer** coleta pedaços de texto de forma eficiente e produz a string final apenas quando você pedir:

- `.write(value)` anexa um valor (qualquer tipo é convertido em texto)
- `.writeln(value)` anexa o valor seguido de uma quebra de linha
- `.toString()` retorna a string construída até o momento

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

Métodos de string retornam strings, então eles podem ser **encadeados** um após o outro. Combinado com `.split('')`, a propriedade de lista `.reversed` e `.join()`, isso permite inverter uma string em uma única expressão:

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

Um **palíndromo** é um texto que se lê da mesma forma de frente para trás e de trás para frente, como `level`.
