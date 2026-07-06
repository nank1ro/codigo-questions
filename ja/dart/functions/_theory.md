**関数**とは、特定のタスクを実行する再利用可能なコードブロックです。Dartでは、戻り値の型、名前、`()` のペアで関数を定義します。

関数が値を返さない場合、戻り値の型は `void` になります：

```dart
void sayHello() {
  print("Hello!");
}
```

関数を呼び出すには、名前の後に `()` を記述します：

```dart
sayHello(); // prints Hello!
```

---

関数は呼び出し元に**値を返す**ことができます。関数名の前に戻り値の型を宣言し、`return` キーワードを使って値を返します：

```dart
int getAge() {
  return 25;
}
```

関数名の前の型（`int`）は、関数が返す値の種類をDartに伝えます。`String`、`int`、`double`、`bool` などを使用できます。

---

関数は**パラメータ**を受け取ることができます — 関数を呼び出すときに渡される値です。パラメータは型と名前を伴って括弧の中に宣言されます：

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

各パラメータには型（`int`）と名前（`n`）があります。複数のパラメータはカンマで区切られます。

---

Dartは `=>` 構文を使った**アロー関数**をサポートしています。関数本体が単一の式の場合、`{ return ...; }` の代わりに `=>` で短縮できます：

```dart
// 通常の関数
int double(int n) {
  return n * 2;
}

// アロー関数 — 同じ結果
int double(int n) => n * 2;
```

アロー関数はコードをより簡潔にします。`=>` は波括弧と `return` キーワードの両方を置き換えます。

---

Dartは**名前付きパラメータ**をサポートしています — 波括弧 `{}` で囲まれたパラメータです。名前付きパラメータは名前で呼び出す必要があり、デフォルト値を持つか `required` としてマークできます：

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

名前付きパラメータは可読性を向上させます。特に関数に多くのパラメータがある場合に有効です。
