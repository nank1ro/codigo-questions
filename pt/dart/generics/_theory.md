Uma `List` não armazena apenas valores, ela armazena valores **de um único tipo**. O tipo é escrito entre colchetes angulares logo depois do nome da coleção:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

`String` e `int` aqui são **argumentos de tipo**, e um tipo que recebe um é chamado de **genérico**. A classe de listas é escrita uma única vez, e `List<String>` e `List<int>` são dois tipos diferentes produzidos a partir dela.

A vantagem é que o compilador sabe o que há dentro:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // fine: first is a String
```

---

`List` não é a única coleção genérica. Um `Set` recebe um argumento de tipo, e um `Map` recebe **dois**: um para as chaves e um para os valores, nessa ordem.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

Um literal de coleção vazio não pode ser deduzido a partir do seu conteúdo, então você escreve os argumentos de tipo no próprio literal:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Uma vez que os tipos são conhecidos, tudo que você tira da coleção já tem o tipo certo: `ages['Ada']` é um `int?`, nunca um valor misterioso.

---

Dart também tem o tipo `dynamic`, que significa "tudo vale". Uma `List<dynamic>` aceita qualquer valor, então parece mais conveniente do que uma `List<String>`:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepted
print(things.first.toUpperCase()); // accepted
```

O problema é que nada é verificado enquanto você escreve o código. Toda chamada em um valor `dynamic` é resolvida enquanto o programa roda, então um erro de digitação como `things.first.toUpperCse()` compila sem reclamar e explode na frente do usuário.

Generics são a alternativa: um único código que funciona com **qualquer** tipo, enquanto cada uso dele ainda é verificado para **um** tipo. Esse é todo o objetivo deste tópico.

---

Você não está limitado às classes genéricas que o Dart traz: você pode declarar as suas. Um **parâmetro de tipo** vai entre colchetes angulares depois do nome da classe, e a partir daí é um tipo normal dentro do corpo:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` é apenas um marcador de posição. Ele é preenchido quando uma `Box` é criada, explicitamente ou por inferência:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, inferred from the argument
print(a.value + 1);      // 8, the compiler knows value is an int
```

A letra não importa: `T` é uma convenção para "tipo", nada mais.

---

Uma função pode ser genérica por si só, sem viver em uma classe genérica. O parâmetro de tipo vai entre o nome e a lista de parâmetros:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T is String here
print(firstOf([10, 20]));        // 10, T is int here
```

Um corpo de função, verificado uma vez, reutilizado para cada tipo. O argumento de tipo geralmente é inferido dos argumentos, mas pode ser escrito explicitamente quando a inferência não tem nada de que partir:

```dart
final empty = firstOf<String>(<String>[]); // throws, but the type is clear
```

Métodos dentro de uma classe seguem exatamente a mesma regra.

---

Dentro de uma classe genérica o parâmetro de tipo é visível em todos os lugares: em campos, em parâmetros de construtor, em assinaturas de métodos e em corpos de métodos. Ele é declarado uma vez, ao lado do nome da classe, e todo membro pode usá-lo.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

Criar o objeto é o que decide o tipo: `Holder<String>('fig')` torna `item` uma `String`, `Holder<int>(3)` o torna um `int`.

---

Uma classe pode declarar mais de um parâmetro de tipo, separados por vírgulas. `Map<K, V>` é o exemplo embutido: um tipo para as chaves, um para os valores.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

A **ordem** faz parte do tipo: `Entry<String, int>` e `Entry<int, String>` são tipos não relacionados, e um valor de um não pode ser atribuído ao outro. Parâmetros de tipo também podem ser reordenados em um tipo de retorno, que é como um método pode devolver uma versão invertida do objeto:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

Com sound null safety, o ponto de interrogação pode cair em dois lugares diferentes, e eles significam duas coisas diferentes:

```dart
Box<int?> a = Box(null); // a box that exists and holds a nullable int
Box<int>? b = null;      // no box at all, but if there is one it holds an int
```

Em `Box<int?>` o **argumento de tipo** é nullable, então `a.value` tem tipo `int?` e pode ser `null`, enquanto `a` em si sempre existe. Em `Box<int>?` a **variável** é nullable, então `b` pode ser `null` e você precisa de `b?.value` ou `b!.value` para alcançar o que há dentro dela.

Um `T` simples significa `T extends Object?`, então um argumento de tipo nullable como `Box<int?>` é perfeitamente legal.

---

A diferença importa assim que você usa o valor. Em uma `Box<int?>` você acessa o campo normalmente e depois lida com o `null` dentro dele, enquanto em uma `Box<int>?` você precisa primeiro passar pela caixa ausente:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, the box is there, its content is null

Box<int>? b = null;
print(b?.value ?? 0); // 0, the box itself is missing
```

Escrever `b.value` em uma `Box<int>?` não compila de forma alguma: o Dart se recusa a ler um campo de algo que pode não existir.

---

Um `T` sem bound pode ser qualquer coisa, então dentro do corpo você só pode usar o que todo objeto tem. Isto não compila:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

Um **bound** resolve isso. Escrever `T extends num` diz que "`T` só pode ser um número", e em troca o corpo pode usar tudo que um `num` oferece:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

O bound é verificado no ponto de chamada: `half(4)` e `half(2.5)` estão ok, `half('fig')` é um erro de compilação. Um bound é uma promessa nos dois sentidos, argumentos mais restritos por mais poder dentro.

---

A palavra-chave para um bound é sempre `extends`, mesmo quando o bound é uma interface em vez de uma superclasse. Não existe `implements` em uma lista de parâmetros de tipo.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Sem o bound, `a > b` não compilaria: o operador de comparação pertence a `num`, não a todo objeto.

---

Um bound pode mencionar o próprio parâmetro de tipo. `Comparable<T>` é a interface de tudo que sabe se comparar com seus semelhantes, por meio de `compareTo`:

```dart
print('fig'.compareTo('kiwi')); // negative: fig comes first
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

Então `T extends Comparable<T>` se lê como "qualquer tipo que pode ser comparado consigo mesmo", que é exatamente o que uma função de ordenação ou de máximo precisa:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` e `DateTime` a satisfazem diretamente. `int` e `double` implementam `Comparable<num>`, então uma lista de números simplesmente é comparada como `num`.

---

O mesmo bound funciona igualmente bem para o menor elemento: apenas o sinal da comparação muda. `compareTo` retorna um número negativo quando o receptor vem primeiro, então `item.compareTo(best) < 0` significa "este é o menor".

---

Uma classe genérica pode ter construtores nomeados e **factory** como qualquer outra classe, e o parâmetro de tipo está disponível dentro deles. Um construtor factory não cria o objeto em si: ele executa um corpo e retorna um, o que lhe permite escolher, reutilizar ou construir a instância da maneira que quiser.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

O argumento de tipo vai na classe, não no nome do construtor: `Box<int>.first(...)`. Dentro da factory, `<T>[]` é uma `List<T>` vazia de verdade, então uma factory é o lugar natural para construir um valor padrão para um tipo que você ainda não conhece.

---

Um parâmetro de tipo escrito sem um bound não é ilimitado de forma alguma: `class Box<T>` é uma abreviação de `class Box<T extends Object?>`. É por isso que `Box<int?>` é aceito, e por que dentro da classe você nunca pode assumir que `value` é não nulo.

Para proibir argumentos de tipo nullable, coloque o bound `Object` no parâmetro:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` é o tipo de tudo, exceto `null`, então `T extends Object` se lê como "qualquer coisa, desde que realmente esteja lá".

---

Um `typedef` dá um nome a um tipo, e pode receber parâmetros de tipo próprios. O motivo usual é nomear uma família de tipos de função uma única vez em vez de escrevê-la por extenso a cada uso:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` é apenas outra forma de escrever `int Function(String)`, então os dois são intercambiáveis. O ganho é legibilidade: um parâmetro declarado como `Transform<I, O> transform` diz para que a função serve, enquanto `O Function(I)` diz apenas como ela é.

Um typedef genérico e uma função genérica se combinam naturalmente, com os próprios parâmetros de tipo da função preenchendo os do typedef.
