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

---

Dart 2.17以降、enumはクラスと同じように**フィールド**と**コンストラクタ**を宣言できます。これは*拡張enum*と呼ばれます。各値はコンストラクタに独自の引数を渡します:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);
}

print(Planet.mars.moons); // 2
```

3つのルールに注目してください: 値のリストは**セミコロン**`;`で終わること、フィールドは`final`でなければならないこと、コンストラクタは`const`でなければならないことです。

---

拡張enumは**メソッド**や**ゲッター**も宣言できます。それらの中では`this`は現在の値を指すため、その`name`、`index`、フィールドを直接使うことができます:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);

  bool get hasMoons => moons > 0;

  String describe() => '$name has $moons moon(s)';
}

print(Planet.earth.hasMoons);   // true
print(Planet.mars.describe()); // mars has 2 moon(s)
```

フィールドを持たないenumでも、メソッドを宣言できます。その場合、値のリストは`;`で終わり、その後にメンバーが続きます。

---

`String`からenumの値に戻すには、`values`リストに対して`byName`を呼び出します。これは`name`が完全に一致する値を返します:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

その名前を持つ値がない場合、`byName`は`ArgumentError`をスローします。文字列がユーザー入力から来る場合は、`asNameMap()`の方が安全な選択です。これは名前から値への`Map<String, Direction>`を返すため、未知の名前を検索するとエラーではなく`null`が得られます:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

enumの値は**マップのキー**として非常に優れています。一意であり、比較が容易で、コンパイラが実在する値しか使われないことを保証してくれます。enumをキーの型としてマップを宣言し、`[]`で値を検索します:

```dart
enum Direction { north, south, east, west }

Map<Direction, String> arrows = {
  Direction.north: '^',
  Direction.south: 'v',
  Direction.east: '>',
  Direction.west: '<',
};

print(arrows[Direction.east]); // >
```

通常のマップと同様に、キーが存在しない場合の検索結果は`null`になるため、`??`でフォールバックを用意してください。

---

enumは`implements`キーワードを使って**インターフェースを実装**できます。enumはインターフェースが宣言するすべてのメンバーを提供することを約束し、その値はそのインターフェース型が期待される場所ならどこでも使用できます:

```dart
abstract class Describable {
  String describe();
}

enum Animal implements Describable {
  dog,
  cat;

  @override
  String describe() => 'I am a $name';
}

Describable pet = Animal.cat;
print(pet.describe()); // I am a cat
```

インターフェースで宣言されたゲッターは、ゲッターまたは同名の`final`フィールドのどちらでも実装できます。
