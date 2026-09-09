**高階関数**とは、別の関数を引数として受け取るか、関数を返すか、その両方を行う関数のことです。あなたはすでに`map`、`filter`、`reduce`、`sorted(by:)`を見たことがあります。これらはクロージャを受け取り、コレクションの要素に適用します。Swiftには他にも多くの高階関数があり、それらを知っていれば長いループを読みやすい1行に置き換えられます。
`compactMap`は`map`と同じように動作しますが、クロージャがオプショナルを返し、`nil`の結果は捨てられます:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")`は`nil`なので、その要素は消え、結果は`[Int?]`ではなく`[Int]`になります。

---

`flatMap`は、**配列**を返すクロージャのためのものです。配列の配列を作る代わりに、返されたすべての配列を1つの平坦な結果に結合します:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
クロージャは、内側の配列を平坦化する前に変換することもできます。例えば、`teams.flatMap { $0.reversed() }`は`["Bob", "Ann", "Cid"]`になります。

---

3つの`map`系関数は、クロージャが何を返すかだけが異なります:
- `map`: 任意の値、要素ごとに1つの結果
- `compactMap`: オプショナル、`nil`の結果は捨てられる
- `flatMap`: 配列、すべての結果が1つの配列に結合される

`flatMap`に渡すクロージャは、内側の配列に対して自分自身で`map`を呼び出すことができ、ある変換を別の変換の中にネストできます:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce`はすべてのステップで新しい累積値を作りますが、結果が配列や辞書の場合には無駄が生じます。`reduce(into:)`はクロージャに累積値を`inout`引数として渡すので、`return`なしでその場で変更できます:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()`は空の辞書を作り、`result[word, default: 0]`は現在のカウント、またはキーが存在しないときは`0`を読み取ります。

---

高階関数の中には、コレクションを変換する代わりにコレクションについての質問に答えるものがあります。これらはすべて`Bool`を返すクロージャを受け取ります:
- `first(where:)`: クロージャを満たす最初の要素を返し、なければ`nil`を返す
- `contains(where:)`: 少なくとも1つの要素がクロージャを満たせば`true`を返す
- `allSatisfy`: すべての要素がクロージャを満たせば`true`を返す

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
`filter`と違い、`first(where:)`は最初の一致で停止し、新しい配列を作りません。

---

`contains(where:)`と`allSatisfy`は、フラグ変数を持つループというよくあるパターンを置き換えます。どちらも答えが分かった時点で停止します。`contains(where:)`は最初の一致で、`allSatisfy`は最初に失敗する要素で停止します。
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }`は`contains(where:)`のトレーリングクロージャの形であり、特定の値を探す`contains(_:)`と混同しないでください。

---

高階関数は、自分で作った構造体の配列を含む任意の配列に対して動作します。`filter`の後に`map`を連結するのが、いくつかの要素を選び、それぞれから値を取り出すいつもの方法です:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
逆の順序、つまり`map`の後に`filter`で行うと、チェックで使う前に`pages`プロパティが失われてしまいます。

---

クロージャが1つのプロパティを読むだけなら、代わりに**キーパス**を渡せます。`\.name`は「要素の`name`プロパティ」を意味し、`map(\.name)`は`map { $0.name }`と同じです。
プロパティによるソートでは、いつもの2引数のクロージャを使い、両方の要素のそのプロパティを比較します:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

**複数の基準**でソートするには、最初のプロパティを比較し、最初の値が等しい場合にだけ2番目のプロパティにフォールバックします:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
ここでは人々が年齢順に並び、同じ年齢の人々は名前順に並びます。クロージャは、最初の要素が2番目の要素より前に来るべき場合にだけ`true`を返さなければならないので、等しい場合は次の比較に委ねられます。

---

`enumerated()`は配列を`(offset, element)`のペアのシーケンスに変換するので、クロージャは各要素の値と一緒にその位置を使うことができます:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
各ペアはタプルなので、クロージャでそれを分割代入することもできます。`.map { (i, step) in "\(i + 1). \(step)" }`のようになります。

---

`zip`は2つのシーケンスの要素を位置ごとにペアにし、タプルのシーケンスを作ります。短い方のシーケンスの終わりで停止します:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
クロージャの中では、`$0`が最初のシーケンスの要素、`$1`が2番目のシーケンスの要素です。`zip`はメソッドではなくフリー関数です。つまり、`a.zip(b)`ではなく`zip(a, b)`と書きます。

---

`forEach`は`for-in`ループの高階関数版です。要素ごとに順番にクロージャを1回呼び出します。違いはループを抜ける方法にあります。`for-in`では`break`や`continue`が使えますが、`forEach`のクロージャの中では`break`と`continue`は使えず、`return`はクロージャの**現在の呼び出し**だけを終了させ、その後は通常どおり次の要素が処理されます:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
すべての要素に対する短い副作用には`forEach`を、早く停止する必要があるときには`for-in`を使いましょう。

---

`Dictionary(grouping:by:)`はコレクションを配列の辞書に分割します。クロージャが各要素の**キー**を計算し、同じキーを持つすべての要素が同じ配列に入ります:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues`はキーを保ったまま辞書のすべての値を変換するので、グループ化の次のステップとして自然な選択です:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)`は、クロージャが`true`を返す**限り**先頭から要素を取り込み、たとえ後の要素がまた条件を満たすとしても、最初に失敗する要素で停止します。`drop(while:)`はその補完です。同じ先頭の連続部分をスキップし、残りをすべて返します:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
どちらも`ArraySlice`を返します。これは元の配列に対するビューで、配列のように表示され、`Array(...)`で配列に変換できます。

---

自分自身の高階関数を書くこともできます。クロージャを受け取り、それをもとに**新しいクロージャを返す**関数はよくあるパターンです。返されたクロージャは元のクロージャをキャプチャするので、引数は`@escaping`でなければなりません。
例えば、`negate`は述語をその反対に変え、`filter`に渡せるようにします:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
`filter(negate(isEven))`は、トレーリングクロージャ構文を使わずに、クロージャを普通の引数として渡していることに注意してください。

---

配列に対する`map`と`filter`は**正格**です。それぞれが配列全体を処理して新しい配列を作ってから、次のステップが実行されます。大きなコレクションや最初の結果だけが必要な場合には、無駄な作業になります。
`lazy`プロパティは、要素が実際に要求されたときにだけ処理が実行されるビューを返します。1つの要素がチェーン全体を通して一度に処理されます:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
ここでは`1, 2, ..., 8`だけが2乗されます。`first(where:)`は条件を満たす要素が見つかるまで要素を要求し、そこでチェーンは停止します。`lazy`がなければ、`map`はまず1000個すべての数値を2乗してしまいます。
