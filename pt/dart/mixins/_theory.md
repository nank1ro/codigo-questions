Uma classe só pode `extend` uma superclasse, mas muito frequentemente o mesmo comportamento é necessário em classes que não têm mais nada em comum. Um **mixin** é uma fatia reutilizável de comportamento que qualquer número de classes pode adotar.

Você declara um com a palavra-chave **`mixin`**, e uma classe o adota com a palavra-chave **`with`**:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` não declara nenhum membro próprio, ainda assim todo `Fish` tem `swim`, porque os membros do mixin se tornam membros da classe. Um mixin pode ser usado por quantas classes você quiser, relacionadas ou não.

---

O corpo de um mixin se parece com o corpo de uma classe: métodos, getters e campos, escritos exatamente da mesma forma. A diferença está no que você pode fazer com a própria declaração.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

O nome de um mixin também é um **tipo**, então `Server() is Timestamped` é `true` e uma variável pode ser declarada como `Timestamped t = Server();`. Duas classes sem relação agora compartilham uma mesma implementação sem que uma herde da outra.

---

Um mixin não se limita a métodos: ele também pode declarar **campos**, e todo objeto de toda classe que usa o mixin recebe sua própria cópia deles.

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

É isso que faz um mixin ser mais do que uma interface: ele traz tanto os dados quanto o código que trabalha sobre eles.

---

Uma declaração `mixin` **não** é uma classe. Ela existe apenas para ser misturada em outras classes, então não tem construtor próprio e não pode ser instanciada nem estendida:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

O nome ainda funciona como um tipo, então `Team() is Scored` e `Scored s = Team();` são ambos válidos. Um mixin não tem construtor, então um campo não anulável deve ser inicializado onde é declarado (ou marcado com `late`), como `int score = 0;` acima.

---

Um mixin pode declarar um membro **sem corpo**. Esse membro é abstrato: o mixin o utiliza, e a classe que adota o mixin precisa fornecê-lo.

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

O mixin traz o comportamento, a classe traz os dados. Um campo na classe, como `final String name;`, é suficiente para satisfazer um getter abstrato de mesmo nome.

---

Juntando as peças, um programa que usa um mixin tem três partes: a declaração `mixin`, uma ou mais classes que o adotam com `with`, e o código que chama o membro compartilhado.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Declarações de nível superior podem ser escritas em qualquer ordem em Dart, mas ler um arquivo de cima para baixo fica mais fácil quando o mixin vem antes das classes que o usam.

---

Uma classe pode usar **vários mixins ao mesmo tempo**, listados depois de `with` e separados por vírgulas. Dart os aplica **da esquerda para a direita**, empilhando cada um sobre o anterior, então quando dois mixins declaram o mesmo membro o **último** da lista vence:

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

Esse empilhamento é chamado de **linearização**: `with A, B` constrói a cadeia `Object` → `A` → `B` → a própria classe.

---

Como o último mixin vence, a ordem da lista `with` faz parte do significado da classe, e não é um detalhe de estilo. Reordená-la muda qual implementação o objeto acaba tendo:

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

Membros que apenas um mixin declara nunca estão em disputa: estão disponíveis independentemente da ordem. Leia `with X, Y` como "comece de `X`, depois deixe `Y` sobrescrevê-lo".

---

Mixins e `extends` trabalham juntos. Uma classe pode ter uma superclasse **e** uma lista de mixins, e os mixins são sempre aplicados **por cima da** superclasse:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

A cadeia aqui é `Object` → `Document` → `Timestamped` → `Report`. Um membro é procurado a partir do fim da cadeia, então `Report().header()` encontra primeiro a versão de `Timestamped`. Declarar o mesmo membro na superclasse e em um mixin é perfeitamente legal: é assim que um mixin substitui ou envolve o comportamento herdado.

---

O corpo da classe fica no fim da cadeia, então um membro declarado na classe **sobrescreve** o mesmo membro vindo de qualquer um dos seus mixins. Dentro da sobrescrita, **`super`** alcança a versão que o mixin forneceu:

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

O mixin em si não é alterado: `Guest` ainda recebe o `greet` original. `super.greet()` é o que permite a `Host` construir sobre o comportamento compartilhado em vez de copiá-lo.

---

Alguns comportamentos só fazem sentido por cima de uma classe específica e precisam dos membros dessa classe para fazer seu trabalho. A cláusula **`on`** declara o requisito:

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` faz duas coisas: permite que o mixin use os membros de `Animal`, como `name` acima, e restringe quem pode usar o mixin. `class Rock with Noisy {}` é um erro de compilação, porque `Rock` não é um `Animal`.

---

Um mixin com uma cláusula `on` lê os membros da sua superclasse como se fossem seus, e é isso que o torna um bom lugar para comportamento que decora um tipo existente:

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` sobrescreve `kind`, e `show` captura a sobrescrita automaticamente: o mixin sempre chama o membro no objeto real.

---

Quando um mixin tem uma cláusula `on`, ele pode **sobrescrever** um membro desse tipo e chamar **`super`** para alcançar a versão abaixo dele na cadeia:

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` não é o `log` do próprio mixin, é o que está abaixo dele, então não há recursão infinita. Empilhe vários mixins assim com `with A, B` e cada um envolve o anterior: a chamada entra primeiro no **último** mixin e desce até a superclasse.

---

Uma declaração `mixin` não pode ser instanciada nem estendida, e uma `class` comum não pode ser usada depois de `with`. Quando você precisa de uma declaração que funcione das **duas** formas, escreva **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

Uma `mixin class` paga por essa flexibilidade com duas restrições: ela deve estender `Object`, então não pode ter sua própria cláusula `extends`, e não deve declarar construtor, porque um mixin nunca executa um.

---

Mixins, herança e interfaces resolvem três problemas diferentes:

- **`extends`** dá a uma classe uma superclasse, para uma relação "é um tipo de". Há apenas uma vaga, então ela deve ir para a relação mais forte.
- **`with`** adiciona comportamento que muitas classes sem relação precisam. Não há limite, e a implementação é compartilhada, não copiada.
- **`implements`** promete um conjunto de membros mas não traz **nenhuma** implementação: toda classe tem que escrever o corpo dela mesma.

Um sinal claro de que você quer um mixin é um método que, de outra forma, você copiaria para classes que não têm pai comum natural, como `Duck`, `Plane` e `Kite` precisando todas do mesmo `fly`.

---

Mixins empilhados são a forma de combinar regras pequenas e independentes em uma única classe. Cada mixin sobrescreve o mesmo membro, faz a sua parte e chama `super` para passar o trabalho adiante. Como a chamada entra primeiro no **último** mixin, a ordem da lista `with` decide qual regra roda antes de qual:

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` dobra cada depósito. Adicione um segundo mixin depois de `Doubled` e ele recebe o depósito primeiro, antes de `Doubled` sequer o ver.
