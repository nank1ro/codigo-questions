時間のかかる処理があります。ファイルの読み込み、サーバーの呼び出し、タイマーの待機などです。Dart はそれらの実行中にプログラムをブロックしません。代わりに、そのような関数は **`Future<T>`** を返します。これは型 `T` の値が**あとで**利用できるようになるという約束です。

いちばん単純な future は、すでに値を持っているもので、`Future.value` で作ります：

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

future から値を取り出すには **`await`** します。`await` は future が完了するまで現在の関数を一時停止し、そのあとむき出しの値を返します。**`async`** が付いた関数の中でしか使えないので、`main` は `Future<void> main() async` になります：

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

`await` がないと `n` は `Future` そのものになり、`print(n)` は数値ではなく `Instance of 'Future<int>'` と表示します。

---

関数に `async` を付けると2つのことが起こります。本体の中で `await` が使えるようになり、関数が **`Future` を返す**ようになります。`return` した値がそのまま future の完了値になるので、本体がむき出しの `T` を返していても、宣言する戻り値の型は `Future<T>` です：

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

ここでは `Future.value` は不要です。`async` キーワードが返り値を包んでくれます。

---

`Future.value` はすぐに完了します。時間のかかる処理をまねるには **`Future.delayed`** を使います。これは `Duration` と関数を受け取り、その時間だけ待ってから、関数が返した値で完了します：

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` は `seconds`、`milliseconds`、`minutes` などの名前付きパラメータで作ります。`async` 関数の中では、値なしで遅延だけを await して、一時停止することもできます：

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

どちらのスタイルもよく使われます。2つめは普通の逐次コードのように読めます。

---

future の2つの側面をはっきり区別しておきましょう：

- `async` 関数は `Future<T>` を**宣言**し、むき出しの `T` を**返す**：包む処理は自動
- `Future<T>` を `await` する呼び出し側はむき出しの `T` を**受け取る**：取り出す処理は自動

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

`int count() async` と書くのはエラーです。`async` 関数は `Future`（または `void`）の戻り値の型を宣言しなければなりません。

---

future を使う方法は `await` だけではありません。**`then`** で**コールバック**を登録することもできます。渡した関数は、future が完了したときにその値とともに呼ばれます。`await` とは違って `then` は現在の関数を一時停止**しない**ので、そのあとのコードが先に実行されます：

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

`Future.value` で作った future でさえ、現在のコードが終わってからでないと値を届けません。だから `waiting` が先に出力されます。`then` は `async` かどうかにかかわらず、どんな関数の中でも使えます。

---

`async` 関数の中では、`await` のおかげで非同期の手順を普通の逐次コードのように書けます。それぞれの `await` は自分の future を待ち、次の行は値がそろってから初めて実行されます：

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` は式の中で直接使うこともできます。`return await width() * await height();` でも同じ結果になります。

---

関数が `await` にさしかかると、その行で**一時停止**し、プログラムの残りは進み続けます。`await` より後ろの行は、future が完了してから初めて実行されます。したがって `async` 関数を上から下へ読めば、その効果が起こる正確な順序がわかります：

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

future は**エラー**で完了することもあります。`async` 関数が例外を投げても、それはすぐには外に出ません。返された future のエラーになります。その future を `await` した側は `await` の位置で例外が投げられたように見えるので、普通の `try`/`catch` で処理できます：

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

`try` の中の `await` が肝心です。`return parseLater(s);` は future を**待たずに**呼び出し側へ渡してしまうので、エラーは `try` ブロックがすでに終わったあとに届き、`catch` は決して実行されません。

---

エラーはコールスタックではなく future とともに運ばれます。例外を投げる `async` 関数を呼んだだけでは、呼び出し側が落ちることはありません。エラーは返された future に保管され、その future が await される場所であとから現れます。したがって `try`/`catch` は future を作った呼び出しではなく、**`await`** を囲む必要があります。

失敗した future を誰も await も処理もしなければ、Dart は *unhandled exception* を報告し、コマンドラインプログラムではエラー終了します。

---

コールバックを使う場合、エラーは `then` の相方である **`catchError`** で処理します。どちらも新しい future を返すので、たいてい連鎖させます。future が成功すれば `then` が値を受け取り、失敗すれば `catchError` がエラーを受け取り、2つのうち片方のコールバックだけが実行されます：

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

`then` のあとに置いた `catchError` は、`then` のコールバックの中で投げられたエラーも捕まえます。`then` と同じく、連鎖のあとのコードが先に実行されます。コールバックは現在のコードが終わってから初めて呼ばれるからです。

---

複数の future が互いに依存していないときは、すべて **`Future.wait`** に渡します。これは `List<Future<T>>` を受け取り、それらを同時に走らせ、**すべて**が終わったときに完了する1つの `Future<List<T>>` を返します。結果は、どの future が先に終わったかに関係なく、入力リストの順序を保ちます：

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` は `25` ミリ秒かかります。`fast()` は `slow()` が完了してから初めて呼ばれるからです。`await Future.wait([slow(), fast()])` はいちばん長いものの時間、およそ `20` ミリ秒で済みます。

---

`Future.wait` は「いくつか読み込んでから続ける」ための道具です。典型的な形は、future のリストを作り、それに `await Future.wait` を適用し、得られたリストを使う、というものです：

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` のほうが先に完了しますが、リストはあくまで呼び出しの順序に従います。`stock()` が先、`orders()` が後です。

---

2つの future を同時に走らせるのに `Future.wait` は必須ではありません。`async` 関数は**呼ばれた**時点から最初の `await` まで走り始めます。受け取る future は、すでに進行中の処理です。つまりコツは、**先に呼んで、あとで await する**ことです：

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

`return await words() / await pages();` と比べてみましょう。こちらでは `pages()` が `words()` の完了後にしか呼ばれません。結果は同じで、時間は2倍です。2つめの呼び出しが1つめの結果を必要としないなら、常に並行する形を選びましょう。

---

エラーは、それを捕まえないすべての `await` を通って**伝播**します。`load()` が失敗すると、`loadTwice()` の中の `await load()` が例外を投げます。`loadTwice` には `try`/`catch` がないので、その future も同じエラーで失敗します。こうして、どこかの `await` が `try`/`catch` で囲まれるまで、連鎖をさかのぼっていきます：

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

これは同期呼び出しで例外が伝播するのと同じしくみです。どうすべきかを知っている階層で、一度だけ処理します。

---

`Future.wait` も同じ規則に従います。**どれか1つ**でも future が失敗すると、まとめられた future はそのエラーで完了し、`await Future.wait(...)` は例外を投げます。成功した値だけの部分的なリストが得られることはありません。ほかを残したいなら、`Future.wait` に渡す前に、個々の future の中でエラーを処理してください。たとえば `catchError` を使います。

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

`await` は future のエラーを普通の例外に変えるので、再試行のループも含め、いつもの `try`/`catch` のパターンがそのまま非同期コードにも当てはまります。`catch` ブロックの中で **`rethrow`** は同じエラーをもう一度投げます。最後の試行のあとであきらめるにはこうします：

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

`Future<String> Function() task` のような関数型のパラメータは、future ではなく**関数**そのものを受け取ります。`task()` を呼ぶたびに新しい試行が始まります。
