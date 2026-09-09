Você sabe adicionar métodos a uma classe que você mesmo escreveu. Mas e `String`, `int` ou `List`, cujo código vive no SDK do Dart? Você não pode editá-los, mas muitas vezes gostaria que eles tivessem mais um método.

Uma **extension** resolve isso: ela adiciona novos membros a um tipo **existente**, sem tocar no código-fonte dele e sem criar uma subclasse. A sintaxe é:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

Dentro da extension, `this` se refere ao valor sobre o qual o membro é chamado. Uma vez declarada a extension, seus membros são chamados exatamente como os membros do próprio tipo:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Extensions são declaradas no **nível superior** de um arquivo, ao lado de classes e funções, nunca dentro de `main`.

---

Extensions funcionam com qualquer tipo, incluindo números. Esta extension dá a cada `int` um método que o dobra:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Como a extension se aplica ao **tipo**, você pode chamar o método em uma variável ou diretamente em um **literal**. Literais negativos precisam de parênteses, caso contrário o ponto é lido antes do sinal de menos:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

Uma extension também pode declarar **getters**, que são lidos como propriedades, sem parênteses. Dentro de uma extension você pode chamar os membros do próprio tipo diretamente: `this.` é opcional, exatamente como dentro de uma classe.

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

Escolha um getter quando o membro apenas **lê** um valor e não recebe parâmetros; escolha um método quando ele faz um trabalho ou precisa de argumentos.

---

O tipo depois de `on` pode ser um tipo **parametrizado** como `List<int>`. A extension então se aplica apenas a listas desse tipo de elemento: `[1, 2].total()` funciona, `['a', 'b'].total()` não compila.

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

Dentro da extension, `this` é a lista, então você pode percorrê-la, indexá-la ou chamar `length` como de costume.

---

Uma extension em `List<int>` não pode ser usada em uma `List<String>`. Para escrever uma extension que funciona com **qualquer** tipo de elemento, dê à extension um **parâmetro de tipo**, escrito entre colchetes angulares depois do nome dela, e use-o no tipo do `on`:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` é um espaço reservado para "qualquer que seja o tipo do elemento": em uma `List<int>` ele se torna `int`, em uma `List<String>` ele se torna `String`, então o getter acima retorna um `int` ou uma `String` de acordo. O compilador preenche o `T` para você em cada chamada.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

Uma extension em `String` não pode ser chamada em uma `String?`: o valor pode ser `null`, e o compilador recusa a chamada. Se você declarar a extension no tipo **nullable** em vez disso, o método pode ser chamado diretamente em uma `String?`, e dentro dela `this` tem tipo `String?`, então você mesmo deve tratar o caso `null`, por exemplo com `??`:

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

Um `int` non-nullable pode ser passado onde um `int?` é esperado, então a extension funciona em ambos.

---

Uma extension pode adicionar métodos, getters, setters e operadores, mas ela **não pode adicionar campos de instância**. Um valor `int` tem um layout fixo na memória, e uma extension é apenas um conjunto de funções que o compilador deixa você chamar com a sintaxe de ponto: não há lugar para armazenar dados extras por valor.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Getters e setters em uma extension só podem calcular valores a partir de `this` ou encaminhar para membros existentes: eles não conseguem lembrar nada entre chamadas.

---

Uma extension pode declarar membros **static**. Como em uma classe, eles pertencem à própria extension, não a nenhum valor, e são acessados através do **nome da extension**, não através do tipo que ela estende:

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

Membros static são um lugar prático para constantes e funções auxiliares relacionadas ao tipo estendido.

---

Extensions não são apenas para tipos do SDK: você também pode estender **suas próprias classes**. Isso é útil quando a classe vem de um pacote que você não controla, ou quando você quer manter a classe pequena e adicionar auxiliares opcionais ao lado do código que precisa deles.

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

A extension enxerga os campos e métodos públicos da classe, exatamente como código escrito fora da classe.

---

O Dart permite que um tipo defina o que operadores como `+`, `*` ou `==` significam para seus valores, usando um método cujo nome é a palavra-chave `operator` seguida do símbolo. O lado direito do operador é o parâmetro do método:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Como extensions podem declarar operadores, você pode dar a um tipo existente um novo operador que ele ainda não tem. `String` tem `+` e `*`, mas não `-`, então uma extension pode definir o que `'hello world' - 'o'` significa.

---

E se uma extension declara um membro que o tipo **já tem**? O membro do próprio tipo sempre vence: membros de extension só são considerados quando o próprio tipo não tem nenhum membro com esse nome. O membro da extension é silenciosamente ignorado, não há erro e não há sobrescrita.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

Então uma extension pode adicionar membros e preencher lacunas, mas nunca pode **mudar** o comportamento dos membros existentes.

---

O nome de uma extension é opcional. Uma extension **sem nome** funciona da mesma maneira, mas só é visível no arquivo que a declara:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

Um **nome** importa assim que duas extensions oferecem o mesmo membro no mesmo tipo: a chamada se torna **ambígua** e não compila. O nome permite resolver o conflito de duas maneiras. Quando as extensions vêm de arquivos diferentes, você pode usar `show` ou `hide` em uma delas no import:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

Ou, em qualquer lugar, você pode aplicar a extension **explicitamente**, envolvendo o valor no nome da extension como se fosse um construtor:

```dart
print(Loud('hi').describe());
```

Extensions sem nome não podem ser ocultadas nem aplicadas explicitamente, então prefira extensions com nome em código que outros vão importar.

---

Uma extension genérica pode receber **funções** como parâmetros, exatamente como `where` e `map` fazem. O tipo da função é escrito com o tipo de elemento `T`, então o callback recebe elementos do tipo correto:

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
