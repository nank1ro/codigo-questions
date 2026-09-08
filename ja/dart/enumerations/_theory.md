**列挙型**（*enum*）は、関連する値のグループに共通の型を定義し、それらの値を型安全な方法で扱えるようにします。Dartでは`enum`キーワードを使って宣言し、その**値**をカンマで区切って列挙します:

```dart
enum Direction { north, south, east, west }
```

慣例として、値の名前は変数と同様に`lowerCamelCase`で書きます。各値はenum名を通してアクセスされ、出力するとenum名と値の両方が表示されます:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

enumはファイルの**トップレベル**で宣言する必要があり、`main`のような関数の内部では宣言できません。

---

すべてのenumの値には2つの組み込みプロパティがあります:

- `name`はその値の名前を`String`として表したもの
- `index`は宣言内でのその位置で、`0`から始まります

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

すべてのenumには、宣言順にすべての値を保持する`values`という定数のリストもあります。通常のリストと同様にインデックスでアクセスしたり、`length`を読み取ったり、`for-in`でループしたりできます:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

`values`はリストなので、すでに知っているリストのメソッドと組み合わせて使えます。例えば`.map()`と`.name`を使うと、値を文字列のリストに変換できます:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

`values`をループするのは、enumのすべての値を処理する一般的な方法です。ループの中では現在の値は他のオブジェクトと同じように扱えるので、その`index`と`name`を読み取り、そのまま文字列補間で使えます:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

各enumの値はちょうど1つだけ存在するため、同じ値への2つの参照は常に等しくなります。`==`と`!=`で比較してください:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

`switch`文は、enumで分岐するための自然な方法で、値ごとに1つの`case`を持ちます:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) {
  switch (direction) {
    case Direction.north:
      return '^';
    case Direction.south:
      return 'v';
    case Direction.east:
      return '>';
    case Direction.west:
      return '<';
  }
}
```

すべての値を**網羅**するケースがあれば、そのswitchは*網羅的*とみなされ、`default`は不要です。値を1つでも書き忘れると、バグが実行時まで残る代わりにコンパイラがエラーを報告します。

---

Dart 3以降、`switch`は値を生成する**式**としても使えます。各ケースは`pattern => value`の形で書き、`case`キーワードや`break`を使わずにカンマで区切ります:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

文形式と同様に、enumに対するswitch式も網羅的でなければなりません。
