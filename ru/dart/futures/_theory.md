Некоторые операции занимают время: чтение файла, обращение к серверу, ожидание таймера. Dart не блокирует программу, пока они выполняются. Вместо этого такая функция возвращает **`Future<T>`**: обещание, что значение типа `T` станет доступно **позже**.

Самый простой future — тот, у которого значение уже есть, он строится через `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Чтобы достать значение из future, ты применяешь к нему **`await`**. `await` приостанавливает текущую функцию, пока future не завершится, а затем отдаёт тебе обычное значение. Он разрешён только внутри функции, помеченной **`async`**, поэтому `main` становится `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Без `await` `n` был бы самим объектом `Future`, и `print(n)` вывел бы `Instance of 'Future<int>'` вместо числа.

---

Пометка функции как `async` делает две вещи: разрешает `await` в теле и заставляет функцию **возвращать `Future`**. То, что ты возвращаешь через `return`, становится значением, которым завершается future, поэтому объявленный тип возврата — `Future<T>`, хотя тело возвращает обычное `T`:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

`Future.value` здесь не нужен: ключевое слово `async` само оборачивает возвращаемое значение.

---

`Future.value` завершается сразу. Чтобы сымитировать работу, занимающую время, используй **`Future.delayed`**: он принимает `Duration` и функцию, ждёт указанное время, а затем завершается тем, что вернула функция:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` строится с именованными параметрами, такими как `seconds`, `milliseconds` или `minutes`. Внутри `async`-функции можно также дождаться самой задержки, без значения, просто чтобы сделать паузу:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Оба стиля распространены; второй читается как обычный последовательный код.

---

Держи в голове две стороны future:

- `async`-функция **объявляет** `Future<T>` и **возвращает** обычное `T`: упаковка происходит автоматически
- тот, кто делает `await` над `Future<T>`, **получает** обычное `T`: распаковка происходит автоматически

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Написать `int count() async` — ошибка: `async`-функция обязана объявлять тип возврата `Future` (или `void`).

---

`await` — не единственный способ работать с future. Можно также зарегистрировать **колбэк** через **`then`**: функция, которую ты передаёшь, вызывается со значением, как только future завершится. В отличие от `await`, `then` **не** приостанавливает текущую функцию, поэтому код после него выполняется первым:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Даже future, построенный через `Future.value`, отдаёт своё значение только после того, как текущий код закончился, поэтому `waiting` печатается первым. `then` работает в любой функции, `async` она или нет.

---

Внутри `async`-функции `await` позволяет писать асинхронные шаги так, будто это обычный последовательный код. Каждый `await` ждёт свой future, и следующая строка выполняется только тогда, когда значение уже есть:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` можно использовать и прямо внутри выражения: `return await width() * await height();` даёт тот же результат.

---

Когда функция доходит до `await`, она **приостанавливается** на этой строке, а остальная часть программы продолжает работу. Строки после `await` выполнятся только тогда, когда future завершится. Поэтому чтение `async`-функции сверху вниз показывает точный порядок её эффектов:

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

Future может завершиться и **ошибкой**. Когда `async`-функция бросает исключение, оно не выходит наружу сразу: оно становится ошибкой возвращённого future. Тот, кто делает `await` над этим future, видит ошибку брошенной в точке `await`, поэтому её можно обработать обычным `try`/`catch`:

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

`await` внутри `try` принципиально важен: `return parseLater(s);` передал бы future вызывающему **без ожидания**, поэтому ошибка пришла бы, когда блок `try` уже закончился, и `catch` никогда бы не выполнился.

---

Ошибки путешествуют вместе с future, а не по стеку вызовов. Вызов `async`-функции, которая бросает исключение, сам по себе никогда не роняет вызывающего: ошибка сохраняется в возвращённом future и всплывает позже, в той точке, где future ожидают. Поэтому `try`/`catch` должен оборачивать **`await`**, а не вызов, который создал future.

Если неудавшийся future никто так и не дождётся и не обработает, Dart сообщает об *unhandled exception* и в консольной программе завершается с ошибкой.

---

При работе с колбэками ошибки обрабатывает **`catchError`**, парный к `then`. Оба возвращают новый future, поэтому их обычно объединяют в цепочку: `then` получает значение, если future завершился успешно, `catchError` получает ошибку, если он завершился неудачей, и выполняется только один из двух колбэков:

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

`catchError`, поставленный после `then`, ловит и ошибки, брошенные внутри колбэка `then`. Как и с `then`, код после цепочки выполняется первым, потому что колбэки вызываются только тогда, когда текущий код закончился.

---

Когда несколько future не зависят друг от друга, передай их все в **`Future.wait`**: он принимает `List<Future<T>>`, даёт им выполняться одновременно и возвращает один `Future<List<T>>`, который завершается, когда готовы **все**. Результаты сохраняют порядок входного списка, независимо от того, какой future закончил первым:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` занимает `25` миллисекунд, потому что `fast()` вызывается только после завершения `slow()`; `await Future.wait([slow(), fast()])` занимает около `20` — столько же, сколько самый долгий из них.

---

`Future.wait` — инструмент для сценария «загрузить несколько вещей, а потом продолжить». Типичная форма такова: собрать список future, применить к нему `await Future.wait`, а затем использовать получившийся список:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` завершается первой, но список всё равно следует порядку вызовов: сначала `stock()`, затем `orders()`.

---

Чтобы запустить два future одновременно, `Future.wait` не обязателен. `async`-функция начинает выполняться сразу, как только её **вызвали**, вплоть до первого `await`; future, который ты получаешь, — это уже идущая работа. Поэтому приём такой: **сначала вызвать, потом дождаться**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Сравни с `return await words() / await pages();`, где `pages()` вызывается только после завершения `words()`: результат тот же, времени вдвое больше. Предпочитай конкурентную форму всякий раз, когда второму вызову не нужен результат первого.

---

Ошибка **распространяется** через каждый `await`, который её не ловит. Если `load()` завершается неудачей, `await load()` внутри `loadTwice()` бросает исключение; поскольку у `loadTwice` нет `try`/`catch`, её собственный future завершается с той же ошибкой; и так далее вверх по цепочке, пока какой-нибудь `await` не окажется обёрнут в `try`/`catch`:

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

Это повторяет то, как исключения распространяются через синхронные вызовы: ты обрабатываешь их один раз, на том уровне, который знает, что делать.

---

`Future.wait` следует тому же правилу: если **любой** из future завершится неудачей, объединённый future завершится с этой ошибкой, и `await Future.wait(...)` бросит исключение. Ты никогда не получишь частичный список успешных значений. Чтобы сохранить остальные, обработай ошибку внутри каждого отдельного future, например через `catchError`, прежде чем передавать его в `Future.wait`.

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

Поскольку `await` превращает ошибки future в обычные исключения, к асинхронному коду применимы все привычные схемы `try`/`catch`, включая циклы с повторными попытками. Внутри блока `catch` **`rethrow`** бросает ту же ошибку снова — так ты сдаёшься после последней попытки:

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

Параметр функционального типа, такой как `Future<String> Function() task`, получает саму **функцию**, а не future: каждый вызов `task()` начинает новую попытку.
