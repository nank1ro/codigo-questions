В Dart **список** — это упорядоченная коллекция элементов. Простейший способ создать список — использовать синтаксис литерала `[]`:

```dart
List<int> numbers = [1, 2, 3];
```

Можно также использовать вывод типа с помощью `var`:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

Аннотация типа `List<String>` сообщает Dart, что каждый элемент списка должен быть типа `String`.

---

Списки в Dart **индексируются с нуля**, то есть первый элемент находится по индексу `0`, второй — по индексу `1` и так далее.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

Доступ к элементу по индексу осуществляется с помощью синтаксиса `list[index]`.

---

Метод `.add()` добавляет один элемент в **конец** списка:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Обратите внимание, что `.add()` изменяет список **на месте** и возвращает `void`.

---

Свойство `.length` возвращает количество элементов в списке:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Пустой список имеет длину `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

Метод `.contains()` проверяет, содержит ли список заданное значение. Возвращает `true`, если значение найдено, и `false` в противном случае:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Это удобно для проверки наличия элемента без использования цикла.

---

Метод `.remove(value)` удаляет **первый** элемент, равный `value`, из списка. Он возвращает `true`, если элемент был удалён, или `false`, если значение не найдено.

```dart
var colors = ['red', 'green', 'blue'];
bool removed = colors.remove('green');
print(removed); // true
print(colors); // [red, blue]
```

---

Свойства `.first` и `.last` дают первый и последний элемент списка без использования индекса.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.first); // red
print(colors.last); // blue
```

Оба выбрасывают ошибку, если список пуст.

---

Свойство `.isEmpty` равно `true`, когда список не содержит элементов, а `.isNotEmpty` равно `true`, когда в нём есть хотя бы один элемент.

```dart
var colors = <String>[];
print(colors.isEmpty); // true
colors.add('red');
print(colors.isNotEmpty); // true
```

---

Метод `.indexOf(value)` возвращает индекс первого элемента, равного `value`. Если значения нет в списке, возвращается `-1`.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.indexOf('green')); // 1
print(colors.indexOf('pink')); // -1
```

---

Метод `.where()` оставляет только те элементы, для которых функция возвращает `true`. Он возвращает не новый список, а ленивый `Iterable`, поэтому вызовите `.toList()`, чтобы снова превратить результат в `List`.

```dart
var numbers = [1, 2, 3, 4];
List<int> big = numbers.where((n) => n > 2).toList();
print(big); // [3, 4]
```
