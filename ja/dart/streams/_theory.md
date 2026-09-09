`Future` は後から届く**単一**の値を表します。**Stream** は時間とともに届く値の**並び**を表します。キー入力、ファイルの断片、サーバーからのメッセージなどです。それぞれの値は**イベント**と呼ばれ、最後のイベントのあとストリームは**完了**します。

ストリームを作る最も簡単な方法は `Stream.fromIterable` で、リストの各要素を順番に送り出します：

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

イベントを1つずつ消費するには、**`await for`** ループを使います。`await` と同じく、`async` が付いた関数の中でしか使えないので、`main` は `Future<void> main() async` になります。ループ本体はイベントごとに1回実行され、ストリームが完了するとループは終わります：

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

ここでは普通の `for` ループは使えません。`Stream` は `Iterable` ではなく、その値は一度にすべて手に入るわけではないからです。

---

`Stream.fromIterable` にはすべての値を前もって渡す必要があります。値を1つずつ**生成**するには、**非同期ジェネレーター**を書きます。本体が `async*` で印を付けられ、戻り値の型が `Stream<T>` の関数です。その中で `yield` がストリームに1つのイベントを送ります：

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

`countTo(3)` を呼んでも本体は実行されません。リスナーが値を求めるのに応じて遅延実行され、本体が終わるとストリームは完了します。

すべてのイベントを `List` に集めるには `toList()` を呼びます。これは `Future<List<T>>` を返すので、`await` で待ちます：

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

`await for` ループは出力するだけではありません。ループの前で宣言した変数を更新することもできます。ストリームを消費して結果を計算する関数は `async` で印を付ける必要があり、その結果の `Future` を返します：

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

この関数はストリームが完了して初めて `return` に到達するので、呼び出し側は future を待ったときに最終的な値を受け取ります：

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

どのストリームもいつかは終わります。`async*` ジェネレーターの場合、関数の本体が終わった時点でストリームは**完了**します。最後まで到達した場合でも、`return` に当たった場合でも同じです。完了したストリームに対する `await for` ループは抜け、`toList()` の future はすべて完了します。

ストリームはやり直したり値を繰り返したりしません。一度完了したら、完了したままです。

---

`await for` はストリームが完了するまで現在の関数を一時停止します。**待たずに**イベントへ反応したいときは、`listen` を呼んでコールバックを渡します。コールバックはイベントごとに1回呼ばれ、`listen` のあとのコードはすぐに実行されます。

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` は名前付きパラメーター `onDone` も受け取ります。これはストリームが終わったときに呼ばれる、引数のない関数です：

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

`async*` ジェネレーターは `yield*`（yield-star）で**別のストリームのすべてのイベント**を転送できます。各値を yield する `await for` ループを、1行で書いたようなものです：

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

内側のストリームが完了すると、外側のストリームは自分の `yield` を続けます。

---

`Iterable` と同じように、`Stream` にも既存のストリームから**新しいストリーム**を作るメソッドがあります：

- `map` は各イベントを変換します
- `where` は条件を満たすイベントだけを残します
- `take` は指定した数のイベントのあとで止まります

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

これらのメソッドは**遅延評価**です。誰かが結果のストリームを購読するまで何も実行されません。連結でき、元のストリームは決して変更されません。

---

`where`、`map`、`take` はそれぞれストリームを返すので、これらを連結し、最後に `toList()` を付けて結果をリストとして受け取れます。`Future` を返すのは最後の `toList()` だけなので、`await` が必要なのもそこだけです：

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

`toList()` のほかにも、ストリームにはすべてのイベントを**消費**して単一の `Future` を返すメソッドがあります：

- `first` と `last` は最初または最後のイベントで完了します
- `length` はイベントの個数で完了します
- `join(separator)` はすべてのイベントを1つの `String` に連結した結果で完了します
- `reduce(combine)` はイベントを2つずつまとめて1つの値にします

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` はそれまでの結果と次のイベントを `combine` に渡します。ストリームが空だと例外を投げるので、イベントが少なくとも1つあると保証されるときだけ使ってください。

---

`Stream` のメソッドは2つのグループに分かれます：

- `map`、`where`、`take`、`skip` のような**変換**メソッドは**新しい `Stream`** を返し、遅延評価です。新しいストリームが購読されるまでイベントは処理されません
- `toList`、`reduce`、`join`、`first`、`last`、`length` のような**消費**メソッドはストリームを購読し、最終結果を持つ **`Future`** を返します

したがって、チェーンは0個以上の変換呼び出しに、最大1個の消費呼び出しが続く形になります。

---

ジェネレーターは1つの関数の中でイベントを生み出します。イベントが**別の場所**（ボタン、ネットワークのコールバック、他のオブジェクト）から来る場合は、**`StreamController`** が必要です。これは `dart:async` ライブラリにあるので、ファイルの先頭に `import 'dart:async';` が必要です。

コントローラーはストリームを持ち、そこにイベントを送り込ませてくれます：

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` は1つのイベントを送ります
- `close()` はストリームを終わらせます。忘れるとリスナーは永遠に待ち続けます
- `stream` はリスナーが消費する `Stream` です

誰かが購読する前に追加されたイベントはバッファーに保持されるので、上のコードは安全です。あとから来たリスナーもちゃんと `4` と `2` を受け取ります。

---

`StreamController` は同じ場所で作られて消費されることがよくあります。`listen` で `controller.stream` を購読し、それから `add` でイベントを追加し、`close` でコントローラーを閉じます。`listen` は待たないので、イベントは現在のコードが終わったあとに配信されますが、必ず追加された順に届きます：

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

ここまで見てきたストリームは**シングルサブスクリプション**です。リスナーはちょうど1つしか許されません。`listen`、`await for`、あるいは消費メソッドを2度目に呼ぶと `StateError`（"Stream has already been listened to"）が投げられます。

1つのストリームを複数のリスナーで共有するには、`asBroadcastStream()` で**ブロードキャスト**ストリームに変換します：

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

ブロードキャストストリームはバッファーを持ちません。リスナーは購読した**あと**に送り出されたイベントしか受け取りません。例では両方のリスナーが最初の `await` より前に購読しているので、どちらもすべてのイベントを受け取ります。

---

コントローラーは名前付きコンストラクター `StreamController<T>.broadcast()` で直接ブロードキャストストリームを作れます。その `stream` はいくつでもリスナーを受け入れ、各イベントは購読した順に全員へ配信されます：

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

どのブロードキャストストリームとも同じく、バッファーは持ちません。リスナーが購読する前に追加されたイベントは、そのリスナーにとっては失われます。

---

ストリームは値だけでなく**エラー**も運べます。`async*` ジェネレーターの中では `throw` がエラーイベントを送ってストリームを終わらせます。`StreamController` は `addError` でエラーを送れます。

消費する側では、`await for` ループがループのある場所でエラーを再スローするので、ループを普通の `try`/`catch` で囲んで処理します：

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

`listen` の場合は、代わりに `onError` コールバックを渡します：`stream.listen(print, onError: (e) => print('caught: $e'));`
