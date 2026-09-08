Você já sabe como declarar uma função com um nome, como `void sayHello() { ... }`. O Dart também permite escrever uma função **sem nome**: uma **função anônima**. Ela tem as mesmas partes de uma função nomeada (parâmetros entre parênteses e um corpo entre chaves), mas sem tipo de retorno e sem nome:

```dart
(String name) {
  print('Hello, $name!');
}
```

Como ela não tem nome, a maneira usual de usá-la é armazená-la em uma variável e depois chamar a variável como uma função:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Observe o `;` após a chave de fechamento: a atribuição é uma instrução normal.

---

Uma função anônima pode receber parâmetros e `return` um valor, exatamente como uma função nomeada. O tipo de retorno não é escrito: o Dart o **infere** a partir das instruções `return` no corpo.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

Quando o corpo é uma única expressão, uma função anônima pode usar a **sintaxe de seta** `=>`, assim como uma função nomeada. A seta substitui as chaves e a palavra-chave `return`:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

Essa forma curta é de longe a maneira mais comum de escrever funções anônimas em Dart.

---

Funções são valores, então elas têm um tipo. O tipo de uma função é escrito como o **tipo de retorno**, depois a palavra-chave `Function`, e então os **tipos dos parâmetros** entre parênteses:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

Quando a variável é tipada dessa forma, os tipos dos parâmetros podem ser omitidos da função anônima, pois o Dart os infere do tipo declarado:

```dart
int Function(int, int) add = (a, b) => a + b;
```

O tipo puro `Function` aceita qualquer função, sejam quais forem seus parâmetros e tipo de retorno, mas não diz ao Dart nada sobre como chamá-la.

---

Como um tipo de função é um tipo normal, uma função pode receber **outra função como parâmetro**. Dentro do corpo, o parâmetro é chamado como qualquer função:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Aqui quem chama decide o que `apply` faz passando uma função anônima como segundo argumento.

---

Muitos métodos das coleções do Dart recebem uma função como argumento, e funções anônimas são a maneira natural de passar uma. O mais simples é o `forEach`, que chama a função dada uma vez para cada elemento de uma lista:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

O tipo do parâmetro é inferido da lista, então `fruit` é uma `String` sem precisar escrevê-lo.

---

Dois outros métodos muito comuns que recebem uma função anônima são `map` e `where`:

- `map` transforma cada elemento com a função e retorna os novos valores
- `where` mantém apenas os elementos para os quais a função retorna `true`

Ambos retornam um `Iterable` preguiçoso; chame `toList()` para transformar o resultado em uma `List`:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Como `map` e `where` retornam um `Iterable`, suas chamadas podem ser **encadeadas** uma após a outra. Cada etapa recebe o resultado da anterior, e `toList()` é chamado uma vez no final:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

O `sort` reordena uma lista no lugar. Por padrão ele usa a ordem natural dos elementos, mas você pode passar uma função anônima que **compara dois elementos** e retorna um número negativo, zero ou um número positivo. O `compareTo` fornece exatamente tal número, então é o bloco de construção usual:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

Trocar `a` e `b` na comparação inverte a ordem.

---

O `reduce` combina todos os elementos de uma lista em um único valor. Sua função anônima recebe dois parâmetros: o valor **acumulado até agora** e o **próximo elemento**, e retorna o novo valor acumulado. O primeiro elemento é usado como ponto de partida:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

O `reduce` lança um erro em uma lista vazia, pois não há um primeiro elemento para começar.

---

Uma função também pode **retornar uma função**. O tipo de retorno é então um tipo de função, e o corpo retorna uma função anônima:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Note que a função retornada ainda usa `amount`, um parâmetro de `makeAdder`, mesmo depois que `makeAdder` terminou. Uma função que lembra as variáveis ao seu redor como essa é chamada de **closure**.

---

Uma closure não apenas lê as variáveis que captura: ela também pode **modificá-las**, e as mudanças são mantidas entre as chamadas. Isso torna possível manter um estado privado sem uma classe:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Cada chamada a `makeTimer()` cria uma variável `seconds` completamente nova, então dois timers nunca compartilham sua contagem.
