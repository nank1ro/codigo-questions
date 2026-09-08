Você já sabe declarar uma variável com um tipo, como `String name = 'Ada';`. Às vezes, porém, um valor simplesmente **falta**: um usuário sem apelido, uma busca que não encontra nada, um texto que não pode ser convertido em número. O Dart representa um valor ausente com `null`.

Desde o Dart 2.12 a linguagem tem **sound null safety**: um tipo normal como `String` **nunca** pode conter `null`. Tentar atribuí-lo é um erro de compilação, então o programa nem chega a rodar:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

Para permitir um valor ausente você adiciona um ponto de interrogação `?` depois do tipo. Um `String?` contém ou uma `String` ou `null`, e imprimir `null` mostra a palavra `null`:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

Tipos sem `?` são chamados **non-nullable**, tipos com `?` são **nullable**.

---

Uma variável nullable declarada **sem valor** começa como `null`, então `= null` pode ser omitido:

```dart
int? age;
print(age); // null
```

Uma variável non-nullable não tem esse padrão: o Dart se recusa a compilar qualquer código que a leia antes de um valor ter sido atribuído.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Chamar um método ou ler uma propriedade em `null` causaria uma falha, então o Dart não permite fazer isso em um valor nullable com o ponto normal:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

O operador de **acesso null-aware** `?.` resolve isso: se o valor for `null` a expressão inteira é `null` e nada mais é avaliado, caso contrário ele funciona como um `.` normal:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Como o resultado pode ser `null`, seu tipo é nullable: `text?.length` é um `int?`, não um `int`.

---

Muitas vezes um valor ausente deve ser substituído por um **padrão**. O operador **if-null** `??` retorna o operando da esquerda quando ele não é `null`, e o da direita caso contrário:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` reage apenas a `null`: uma string vazia `''` ou o número `0` são valores reais, então são mantidos.

`??` combina bem com `?.`, porque `?.` produz um resultado nullable:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

A grande vantagem do null safety é que a maioria dos erros com `null` é encontrada pelo **compilador**, e não pelos seus usuários. As regras até aqui:

- um tipo non-nullable (`String`, `int`, `List<int>`...) nunca pode ser `null`
- um tipo nullable (`String?`, `int?`, `List<int>?`...) pode, e começa como `null` quando declarado sem valor
- `.` em um valor nullable não compila: use `?.` ou forneça um padrão com `??`

---

O operador de **atribuição if-null** `??=` atribui um valor a uma variável **somente se** essa variável for atualmente `null`; caso contrário, ele a deixa intacta:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

Ele também funciona em entradas de map, que são nullable porque uma chave pode estar ausente:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

Às vezes **você** sabe que um valor nullable não é `null` em determinado ponto, mesmo que o compilador não consiga saber. O operador de **null assertion** `!` transforma um `String?` em uma `String` prometendo que o valor está presente:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Cuidado: `!` move a verificação do tempo de compilação para o tempo de execução. Se o valor **for** `null`, o programa lança um erro e para:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Use `!` com moderação, e apenas quando um `null` ali já seria um bug de qualquer forma.

---

Lembre-se da diferença entre os três operadores que você viu em um valor nullable:

- `?.` retorna `null` quando o valor é `null`, e nunca lança erro
- `??` substitui `null` por um padrão
- `!` assume que o valor está presente e **lança um erro em tempo de execução** quando não está

Nenhum deles é um erro de compilação: o compilador confia no seu `!`, e somente o programa em execução pode descobrir que a promessa foi quebrada.

---

Verificar um valor nullable com `if` é mais seguro do que `!`, e o Dart recompensa você por isso. Depois de uma verificação como `if (x != null)`, o compilador sabe que `x` não pode ser `null` dentro do bloco, então o trata como non-nullable ali. Isso se chama **promoção de tipo**:

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

A promoção também funciona depois de um retorno antecipado:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

A promoção se aplica a **variáveis locais e parâmetros**, cujo valor não pode mudar pelas suas costas entre a verificação e o uso.

---

A promoção de tipo **não** funciona em um **campo** de classe que pode ser alterado de fora, porque entre a verificação e o uso outro trecho de código (um getter sobrescrito em uma subclasse, outro método) poderia colocá-lo de volta como `null`:

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

A solução padrão é copiar o campo para uma **variável local**, que é promovida:

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

Um campo non-nullable normalmente precisa receber um valor no construtor. Quando o valor só é conhecido **mais tarde** (depois de ler um arquivo, abrir uma conexão...), você pode marcar o campo como `late`: o compilador aceita a ausência do inicializador e confia que você atribuirá o campo antes de lê-lo.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Ler um campo `late` que ainda não foi atribuído lança um `LateInitializationError` em tempo de execução. Assim como `!`, `late` troca uma garantia de compilação por uma verificação em tempo de execução, então é uma promessa que você deve cumprir.

`late` também pode ser combinado com um inicializador, que então roda de forma **preguiçosa**, na primeira vez que a variável é lida:

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

A nullability molda a forma como você declara **parâmetros nomeados**. Um parâmetro nomeado com um tipo nullable é opcional: quando quem chama o omite, ele é simplesmente `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

Um parâmetro nomeado com um tipo non-nullable e sem valor padrão ficaria sem valor quando omitido, então o Dart exige que você o marque como `required`; quem chama deve então sempre passá-lo:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

A nullability também se aplica aos **elementos** de uma coleção. Uma `List<int>` nunca contém `null`, enquanto uma `List<int?>` pode:

```dart
List<int?> scores = [7, null, 9];
```

Note a diferença com `List<int>?`, que é uma lista que pode estar ausente ela própria mas que, quando presente, contém apenas números reais.

Para se livrar dos elementos `null`, `nonNulls` retorna um `Iterable` apenas com os valores presentes, tipado sem `?`:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` faz o mesmo e também funciona quando a lista mistura vários tipos.

---

Muitas funções de bibliotecas usam `null` para informar que algo **não pôde ser feito**. Converter uma string em número é o exemplo clássico: `int.parse` lança uma `FormatException` quando o texto não é um número, enquanto `int.tryParse` retorna `null` e deixa você decidir o que fazer:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

O tipo de retorno de `int.tryParse` é `int?`, então tudo o que você aprendeu se aplica: `??` para um padrão, `?.` para encadear, e uma verificação com `if` para promover. `double.tryParse` funciona da mesma forma.

---

Mais dois operadores têm uma variante null-aware.

A **cascata null-aware** `?..` executa uma cadeia de operações em cascata apenas quando o objeto não é `null`, e pula todas elas caso contrário:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

O **spread null-aware** `...?` insere os elementos de uma coleção nullable em um literal, não adicionando nada quando a coleção é `null`:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Sem o `?`, `...extra` em uma `List<int>?` seria um erro de compilação.

---

Dados reais são cheios de lacunas: um campo de formulário deixado vazio, uma coluna ausente em um arquivo, uma string que não é bem um número. As ferramentas deste capítulo se combinam naturalmente para lidar com isso: `nonNulls` para descartar elementos ausentes, `int.tryParse` para converter com segurança, `??` ou uma verificação com `if` para tratar o que não pôde ser convertido.
