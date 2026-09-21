---
language: dart
exerciseType: 1
difficulty: 3
title: Сбалансированные скобки
---

# --description--

Текст, в котором есть код, математика или разметка, полон скобок, и каждой открывающей скобке нужна закрывающая того же вида. Строка сбалансирована, когда её скобки образуют пары и вкладываются друг в друга, как слои луковицы: `{[()]}` сбалансирована, а `{[(])}` — нет, ведь круглая пара закрывается раньше квадратной пары, внутри которой она находится.

Здесь учитываются три пары: круглые `()`, квадратные `[]` и фигурные `{}`. Все остальные символы строки игнорируются. Закрывающая скобка должна закрывать последнюю из ещё открытых скобок, а к концу строки не должно остаться ни одной незакрытой скобки.

# --instructions--

Напишите функцию `isBalanced`, которая принимает строку и возвращает `true`, если все скобки в ней образуют пары и правильно вложены, и `false` в противном случае.

Примеры:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Пустая строка сбалансирована.
- Символы, не являющиеся скобками, игнорируются.
- Закрывающая скобка должна соответствовать последней из ещё открытых скобок.
- К концу строки не должно оставаться ни одной открытой скобки.

# --seed--

```dart
bool isBalanced(String text) {
  
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

Пустая строка сбалансирована

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Одна пара круглых скобок сбалансирована

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

Три вида пар, вложенные друг в друга, сбалансированы

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Скобки вперемешку с другим текстом остаются сбалансированными

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Пары, стоящие друг за другом, сбалансированы

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Строка вовсе без скобок сбалансирована

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Перекрёстная пара не сбалансирована

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Открывающая скобка, которая никогда не закрывается, не сбалансирована

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Закрывающая скобка раньше любой открывающей не сбалансирована

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Перекрёстные пары в глубине строки не сбалансированы

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Лишняя закрывающая скобка в конце строки не сбалансирована

```dart
  test('test11', () {
    expect(isBalanced('())'), false, reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isBalanced(String text) {
  const pairs = {')': '(', ']': '[', '}': '{'};
  final stack = <String>[];

  for (final char in text.split('')) {
    if (char == '(' || char == '[' || char == '{') {
      stack.add(char);
    } else if (pairs.containsKey(char)) {
      if (stack.isEmpty || stack.removeLast() != pairs[char]) {
        return false;
      }
    }
  }

  return stack.isEmpty;
}
```
