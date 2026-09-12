Класс может наследовать (`extend`) только один суперкласс, но очень часто одно и то же поведение нужно классам, которые больше ничем не связаны. **Миксин** — это многоразовый фрагмент поведения, который может подхватить любое число классов.

Миксин объявляется ключевым словом **`mixin`**, а класс подхватывает его ключевым словом **`with`**:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` не объявляет ни одного собственного члена, но у каждого `Fish` есть `swim`, потому что члены миксина становятся членами класса. Миксин может использовать сколько угодно классов, связаны они или нет.

---

Тело миксина выглядит как тело класса: методы, геттеры и поля записываются точно так же. Разница — в том, что можно делать с самим объявлением.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

Имя миксина — это ещё и **тип**, поэтому `Server() is Timestamped` равно `true`, а переменную можно объявить как `Timestamped t = Server();`. Теперь два никак не связанных класса используют одну реализацию, не наследуясь при этом друг от друга.

---

Миксин не ограничен методами: он может объявлять и **поля**, причём каждый объект каждого класса, использующего миксин, получает собственную копию этих полей.

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

Именно это делает миксин большим, чем интерфейс: он приносит и данные, и код, который с ними работает.

---

Объявление `mixin` — **не** класс. Оно существует только для того, чтобы подмешиваться в другие классы, поэтому у него нет собственного конструктора, и его нельзя ни инстанцировать, ни унаследовать:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

Имя при этом по-прежнему работает как тип, поэтому `Team() is Scored` и `Scored s = Team();` вполне допустимы. У миксина нет конструктора, поэтому non-nullable поле должно инициализироваться в месте объявления (или быть помечено `late`), как `int score = 0;` выше.

---

Миксин может объявить член **без тела**. Такой член абстрактен: миксин его использует, а класс, подхватывающий миксин, обязан его предоставить.

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

Миксин приносит поведение, класс приносит данные. Поля в классе, например `final String name;`, достаточно, чтобы удовлетворить абстрактный геттер с тем же именем.

---

Если собрать всё вместе, программа, использующая миксин, состоит из трёх частей: объявления `mixin`, одного или нескольких классов, подхватывающих его через `with`, и кода, вызывающего общий член.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Объявления верхнего уровня в Dart можно писать в любом порядке, но читать файл сверху вниз проще, когда миксин идёт перед классами, которые его используют.

---

Класс может использовать **несколько миксинов сразу**, перечисленных после `with` и разделённых запятыми. Dart применяет их **слева направо**, накладывая каждый поверх предыдущего, поэтому когда два миксина объявляют один и тот же член, побеждает **последний** в списке:

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

Такое наложение называется **линеаризацией**: `with A, B` строит цепочку `Object` → `A` → `B` → сам класс.

---

Поскольку побеждает последний миксин, порядок списка `with` — часть смысла класса, а не деталь стиля. Изменив порядок, ты меняешь то, какая реализация в итоге окажется у объекта:

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

Члены, которые объявляет только один миксин, никогда не конкурируют: они доступны при любом порядке. Читай `with X, Y` как «начни с `X`, затем позволь `Y` переопределить его».

---

Миксины и `extends` работают вместе. Класс может иметь суперкласс **и** список миксинов, причём миксины всегда применяются **поверх** суперкласса:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

Цепочка здесь: `Object` → `Document` → `Timestamped` → `Report`. Поиск члена начинается с конца цепочки, поэтому `Report().header()` сначала находит версию из `Timestamped`. Объявлять один и тот же член и в суперклассе, и в миксине совершенно допустимо: именно так миксин заменяет или оборачивает унаследованное поведение.

---

Тело класса стоит в самом конце цепочки, поэтому член, объявленный в классе, **переопределяет** одноимённый член из любого его миксина. Внутри переопределения **`super`** достаёт версию, предоставленную миксином:

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

Сам миксин при этом не тронут: `Guest` по-прежнему получает оригинальный `greet`. Именно `super.greet()` позволяет `Host` строить на общем поведении, а не копировать его.

---

Некоторое поведение имеет смысл только поверх определённого класса, и для своей работы оно требует члены этого класса. Условие **`on`** объявляет это требование:

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

`on Animal` делает две вещи: позволяет миксину использовать члены `Animal`, например `name` выше, и ограничивает, кто может использовать миксин. `class Rock with Noisy {}` — ошибка времени компиляции, потому что `Rock` не является `Animal`.

---

Миксин с условием `on` читает члены своего суперкласса как свои собственные — именно поэтому это удачное место для поведения, украшающего существующий тип:

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

`Square` переопределяет `kind`, и `show` автоматически подхватывает переопределение: миксин всегда вызывает член на реальном объекте.

---

Когда у миксина есть условие `on`, он может **переопределять** член этого типа и вызывать **`super`**, чтобы добраться до версии, расположенной ниже него в цепочке:

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

`super.log` — это не собственный `log` миксина, а тот, что находится ниже, поэтому бесконечной рекурсии не возникает. Сложи несколько таких миксинов через `with A, B`, и каждый обернёт предыдущий: вызов сначала входит в **последний** миксин и спускается вниз до суперкласса.

---

Объявление `mixin` нельзя инстанцировать или унаследовать, а обычный `class` нельзя использовать после `with`. Когда нужно одно объявление, которое работает **в обоих** ролях, пиши **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

`mixin class` платит за эту гибкость двумя ограничениями: он должен наследовать `Object`, поэтому не может иметь собственного условия `extends`, и не должен объявлять конструктор, потому что миксин никогда не запускает конструкторы.

---

Миксины, наследование и интерфейсы решают три разные задачи:

- **`extends`** даёт классу один суперкласс — для отношения «является разновидностью». Слот только один, поэтому его стоит отдать самому сильному отношению.
- **`with`** добавляет поведение, которое нужно многим не связанным между собой классам. Ограничений нет, а реализация используется совместно, а не копируется.
- **`implements`** обещает набор членов, но не приносит **никакой** реализации: каждый класс должен написать тело сам.

Верный признак того, что тебе нужен миксин, — метод, который иначе пришлось бы копировать в классы без естественного общего родителя, как `Duck`, `Plane` и `Kite`, которым всем нужен один и тот же `fly`.

---

Сложенные миксины — это способ объединить маленькие независимые правила в одном классе. Каждый миксин переопределяет один и тот же член, выполняет свою часть работы и вызывает `super`, чтобы передать работу дальше. Поскольку вызов сначала входит в **последний** миксин, порядок списка `with` решает, какое правило сработает раньше какого:

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

`class A extends Account with Doubled {}` удваивает каждый вклад. Добавь второй миксин после `Doubled`, и он получит вклад первым, прежде чем его увидит `Doubled`.
