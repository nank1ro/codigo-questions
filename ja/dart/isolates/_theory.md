これまでに書いた Dart のコードは、すべて **isolate** の中で実行されてきました。isolate とは、自分専用のメモリとイベントループを持つスレッドのようなものです。プログラムは1つの isolate、すなわち *メイン* isolate で始まり、さらに追加で始められます。

isolate を特別なものにしているのは、何も**共有しない**という点です。2つの isolate が同じオブジェクトを見ることは決してないので、ロックもデータ競合も、途中まで更新された値もありません。isolate 同士は、メッセージの**コピー**を渡すことによってだけやり取りします。

2つ目の isolate を使ういちばん手軽な方法が **`Isolate.run`** です。関数を1つ受け取り、まったく新しい isolate の上で実行し、その結果を持った `Future` を返してくれます：

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` は `dart:isolate` ライブラリにあります。そのため、ファイルは `import 'dart:isolate';` で始まる必要があります。新しい isolate が計算している間も、メインの isolate は自由なままです。これが本当の**並列性**であり、処理は別のプロセッサコアの上で行われます。

---

`Isolate.run` に渡す関数は、周囲の変数を**キャプチャ**できます。それらの値は関数と一緒に新しい isolate へコピーされるので、計算は呼び出し元に依存できます：

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` は、関数が返すものの `Future` を返します。だから `triple` は単にそれを返せばよく、future をそのまま渡すだけなら `async` も `await` も必要ありません。

処理を別の isolate に移すポイントは、長い計算がメインの isolate を固めなくなることです。1秒間動き続けるループは、メインの isolate の上で動けばすべてをブロックします。`Isolate.run` の中にあれば別の場所で動き、メインの isolate は自分のイベントを処理し続けられます。

---

isolate の間でコピーされるのは**データ**だけです。**コード**はコピーされません。プログラムのすべての isolate は、そのプログラムのトップレベル関数とクラスをすでに見ることができるので、`Isolate.run` に渡された計算はそれらを自由に呼び出せます：

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

行き来するのは、入り口でキャプチャされた `text` と、出口で結果としてできた `int` で、どちらもコピーです。パターンはいつも同じです。重い関数はその場所に置いたままにし、その**呼び出し**を `Isolate.run` で包みます。

---

`await` と `Isolate.run` は2つの異なる問題を解決します。両者を区別しておく価値があります。

`await` は1つの isolate の上で**並行性**を与えます。ある関数がタイマーやサーバーを待っている間に、isolate は他の待機中のコードを実行します。同じ瞬間に何かが動くわけではなく、isolate が遊んでいる時間をなくすだけです。待つための正しい道具です。

`Isolate.run` は**並列性**を与えます。2つ目のプロセッサコアに2つ目の isolate があり、1つ目と同じ瞬間にそれぞれのコードを実行します。計算のための正しい道具です。

```dart
await Future.delayed(const Duration(seconds: 1)); // waiting: no core is busy
await Isolate.run(() => hugeCalculation());       // computing: another core is busy
```

遅い計算を `await` しても何の役にも立ちません。`await bigSum()` は `bigSum` を現在の isolate の上で実行し、最後の行までそれをブロックします。その処理をどこかへ追い出せるのは、2つ目の isolate だけです。

---

`Isolate.run` は結果が1つだけのときの近道です。動き続けて2回以上報告してくる isolate がほしいときは、**`Isolate.spawn`** で自分で起動し、答えを返す手段を与えます。

その手段が2つのポートです。**`ReceivePort`** はメールボックスです。自分の側で作り、届いたメッセージを読みます。その **`sendPort`** がメールボックスの住所であり、返事をするために他の isolate が必要なのはこれだけです。

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` は実行する関数と、それに渡す1つのメッセージ（ここでは `SendPort`）を受け取ります。向こう側では `send` が値をメールボックスに投げ入れ、`await receivePort.first` は最初のメッセージを待ってポートを閉じます。

---

`Isolate.spawn` に渡される関数は**エントリーポイント**と呼ばれます。ちょうど1つのパラメーター、すなわち `Isolate.spawn` が渡すメッセージを受け取るトップレベル（または静的）関数でなければなりません。

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

`ReceivePort` に届くメッセージの静的な型は `dynamic` です。どんな値でも送られていた可能性があるからです。他の isolate が何を送るか分かっているなら、キャストします：

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

起動された isolate は、いつも同じ4つのステップをたどります。メールボックスを開く、その住所と一緒にワーカーを起動する、答えを待つ、使う。

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

`Isolate.spawn` の前の `await` は、isolate が仕事を終えるのではなく、isolate が*始まる*のを待ちます。結果はあとでポートを通して届きます。

---

`Isolate.spawn` はエントリーポイントにちょうど**1つ**のメッセージを渡します。そしてワーカーは通常、答えを返すための `SendPort` と、処理するいくつかのデータの両方を必要とします。定番のテクニックは、すべてを1つの `List` にまとめ、向こう側で取り出すことです：

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

リストは入り口でコピーされるので、ワーカーは自分自身の値を読みます。`SendPort` はコピーされずに共有される数少ないものの1つです。作った isolate のメールボックスを指し続けるので、まさに返信先として使えます。

---

`first` は1つのメッセージを読んでメールボックスを閉じます。`ReceivePort` は **`Stream`** でもあるので、多くのメッセージを読むには `await for` でループします。

ループは自分では終わりません。ポートは、来るかもしれないし来ないかもしれないメッセージを待ち続けます。そこでワーカーは、合図として最後の値（よく `null`）を送り、リスナーは **`close()`** を呼んで応じます。これがストリームとループを終わらせます：

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

一連のメッセージをまとめて集めるには、1つの定石があります。ループの前に空のリスト、実際のメッセージごとに1回の `add`、ストリームを終わらせる合図で `close()`。ポートが閉じられれば `await for` は終了し、関数は値を返せます：

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

メッセージは送られた順序を保つので、作ったリストは他の isolate の仕事を一歩一歩映し出します。

---

開いた `ReceivePort` は未処理の仕事として数えられます。1つでも存在する限り、それを持つ isolate には生き続ける理由があり、イベントループはメッセージを待ち続けます。コマンドラインのプログラムでは、開いたポートを持つメインの isolate は単純に**決して終了せず**、手で止めなければなりません。

したがって、ポートを閉じることは最適化ではなく仕事の一部です：

- `await port.first` は1つのメッセージのあとでポートを自動的に閉じます
- `port.close()` はポートを明示的に閉じます。`await for` ループのあとで必要なのはこちらです

`Isolate.run` にはこうした後片付けが一切ありません。ポートを作り、閉じ、isolate を止めるところまで自動でやってくれます。結果が1つで足りるなら、いつでもこちらを選んでください。

---

isolate の中で投げられた例外は、別の isolate へ飛び越えることができません。両者は別々のスタックを持つからです。`Isolate.run` はその溝を埋めてくれます。エラーを捕まえ、向こうからこちらへコピーし、返される future をそのエラーで失敗させます。だからこちら側では、`await` の周りの `try`/`catch` で捕まえる、ふつうの非同期エラーとして扱えます：

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

`try` の中の `await` は、他の future とまったく同じように重要です。これがないと、future は `try` ブロックを未完成のまま出て行き、`catch` は決して実行されません。

`Isolate.spawn` にはこうした橋はありません。捕まえられなかったエラーは起動された isolate を黙って殺し、親は決して届かないメッセージを待ち続けます。これも、まず `Isolate.run` を選ぶもう1つの理由です。

---

`Isolate.run` から返ってくるエラーは、向こう側で投げられたものの**コピー**です。だからいつものチェックがそのまま働きます。`catch (e)` がオブジェクトを渡し、`e is FormatException` がどんな種類の失敗だったかを教えてくれます。

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

頼れないのは、自分の isolate の中を指すスタックトレースです。エラーは移動しましたが、スタックは移動しません。

---

まとめると、`Isolate.run` を使ったプログラムはふつうの逐次コードのように読めます。呼び出しの前の行はメインの isolate で実行され、計算は別の場所で実行され、`await` の後の行は結果を手にしてメインの isolate に戻って実行されます。

```dart
import 'dart:isolate';

int double(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => double(4));
  print(result);
}
// start
// 8
```

---

isolate はメモリを共有しないので、すべてのメッセージは渡るときに**コピー**されます。数値、ブール値、文字列、`null`、リスト、マップ、そしてたいていのプレーンなオブジェクトは旅ができます。開いたソケットのように、まったくコピーできないものもいくつかあり、それを送ろうとすると `ArgumentError` が投げられます。

その帰結が、isolate を安全にするルールです。送ったあと、両側は**2つの独立したオブジェクト**を持ちます。ある isolate が自分のコピーに何をしようと、相手には見えません。

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // the copy grows
print(numbers);                           // [1, 2, 3]
```

`SendPort` はこのルールを証明する例外です。コピーではなく共有されます。それはまさに、元のメールボックスを指し続けられるようにするためです。

---

それぞれの `Isolate.run` は自分専用の isolate を起動します。だから複数あれば、マシンが持つコアの数だけ、本当に同じ瞬間に実行されます。パターンは future ですでに知っているものです。まずすべての計算を始め、それから `Future.wait` で全部を待ちます。`Future.wait` は結果を入力の順序のまま保ちます。

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

isolate の起動は無料ではありません。メモリと数ミリ秒のコストがかかります。1つの長い計算を少数の isolate に分割するのは見合いますが、些細な足し算一千個を千個の isolate に送るのは見合いません。
