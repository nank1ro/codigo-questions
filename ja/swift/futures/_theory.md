すぐに終わらない処理があります。ファイルのダウンロード、データベースの読み込み、タイマーの待機などです。プログラムが単に停止して待ってしまったら、その間に他のことは何もできません。Swiftは**非同期関数**でこれを解決します。

**`async`**を付けた関数は、途中で一時停止し、後で再開することができます。このキーワードはパラメータリストの後、矢印の前に書きます:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
呼び出し方も異なります。呼び出しの前に**`await`**を書く必要があります。`await`はプログラムが一時停止する可能性のある正確な位置を示し、関数が完了するとプレーンな値を受け取れます:
```swift
let n = await fetchNumber()
print(n)
// 42 を出力
```
Swiftスクリプトではトップレベルがすでに`await`をサポートしているので、追加のセットアップなしで非同期関数を直接呼び出せます。`async`や`await`を忘れるのはコンパイルエラーであり、見つけにくいバグにはなりません。

---

非同期関数もやはり普通の関数です。パラメータを受け取り、任意の型の値を返せます。変わるのは2点だけ、シグネチャの`async`キーワードと、すべての呼び出し箇所の`await`です:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// 10.0 を出力
```
返される値はラッパーではなく普通の`Double`です。`await`が完了すれば、いつも通りに扱えます。

---

非同期関数は通常、互いの上に組み立てられます。`async`関数の中では他の`async`関数を`await`でき、その結果は普通の値と同じように使えます:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// 15 を出力
```
`await`は非同期コンテキストの中でのみ許可されます。つまり`async`関数の中か、スクリプトのトップレベルです。普通の非`async`関数は何も`await`できません。

---

時間をかけて行う処理はよく失敗します。サーバーがダウンしている、ファイルが見つからない、入力が間違っているなどです。そのような関数には**`async throws`**を付け、**`try await`**で呼び出します:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
エラーを処理するには、呼び出しを`do`ブロックで囲んでキャッチします:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// could not load を出力
```
キーワードの順序は決まっています。まず`try`、次に`await`です。

---

呼び出しが*なぜ*失敗したかを気にしないなら、`try?`は`do`ブロックより短くて済みます。スローする呼び出しを**オプショナル**に変えます。成功なら値、失敗なら`nil`です。`await`と組み合わせると`try? await`と書きます:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
結果はオプショナルなので、そのまま`if let`に入れます:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
手早いフォールバックには`try? await`を、エラーそのものが重要な場合には`do` / `catch`を使います。

---

続けて書かれた複数の`await`呼び出しは**順次**実行されます。1番目の呼び出しが返るまで、2番目の呼び出しは開始さえしません。コードは上から下へ、普通のコードとまったく同じように読めます:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
2番目の呼び出しが1番目の結果を必要とするなら、これが望ましい動作です。呼び出しが互いに独立している場合は、片方を開始する前にもう片方を待つのは時間の無駄です。次の演習ではその避け方を紹介します。

---

2つの独立した呼び出しを同時に実行するには、**`async let`**で宣言します。処理はすぐに開始され、プログラムは待たずに先へ進みます:
```swift
async let left = step("A")
async let right = step("B")
```
値はまだそこにないので、バインディングを直接使うことはできません。最終的に必要になる位置で`await`しなければなりません。式の前の1つの`await`で、その中のすべての`async let`をカバーします:
```swift
let both = await left + right
```
各呼び出しに1秒かかるなら、順次バージョンは2秒かかりますが、`async let`バージョンは2つの呼び出しが重なるため約1秒で済みます。

---

結果を別々に必要とするときは、複数の`async let`バインディングをタプルにまとめ、タプル全体を一度に`await`します:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
両方の呼び出しはすでに実行中です。1つの`await`は、2つのうち遅い方が終わるまで待ちます。`async let`は処理を開始するだけだという点に注意してください。一度もawaitしない`async let`はキャンセルされ、スコープが終わるときに暗黙的にawaitされます。

---

`async let`は書かれたスコープに結び付いています。並行処理を開始し、そのハンドルを保持するには**`Task`**を使います。`Task { }`に渡されたクロージャは独立して実行され、タスクは格納したり、渡したり、返したりできます:
```swift
let job = Task {
    return await double(21)
}
```
結果は後で**`.value`**で読み取ります。これはawaitされます:
```swift
print(await job.value)
// 42 を出力
```
ハンドルの型は、何を生成し何をスローしうるかを表します。`Task<Int, Never>`は`Int`を返し、決してスローしないタスクです。`async let`と異なり、`Task`は普通の非同期でないコードから作成できます。

---

`Task.sleep`は他の何もブロックせずに、現在のタスクをしばらく一時停止させます。中断される可能性があるため、スローする非同期呼び出しであり、`try await`が必要です。時間は`.seconds`、`.milliseconds`、`.nanoseconds`などのヘルパーで指定します:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
実際のネットワーク呼び出しの代わりに、例の中で遅い処理をシミュレートする標準的な方法です。プログラムが固まるわけではない点に注意してください。1つのタスクがスリープしている間も、他のタスクは実行を続けます。

---

これで順次と並行の違いが測定できるようになりました。`work`が返る前に1秒スリープするとします:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
呼び出しを1つずつawaitすると約**2**秒かかります。2番目のスリープは1番目が終わってから始まるためです:
```swift
let a = await work(1)
let b = await work(2)
```
`async let`で開始すると約**1**秒かかります。両方のスリープが重なるためです:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
`await work(1) + await work(2)`を1行に書いても何も変わりません。2つの呼び出しは依然として順番に評価されます。並行性は`async let`やタスクから生まれるものであり、行の書き方から生まれることはありません。

---

`async let`は、コードを書いているときに呼び出しがいくつあるか分かっている場合に使えます。実行時にしかサイズが分からないリストには、**タスクグループ**を使います。

`withTaskGroup(of:)`がグループを開き、`addTask`がアイテムごとに1つの子タスクを開始し、グループはその後`for await`で読み取ります。結果は完了した順に届きます:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self`は、すべての子タスクが何を返すかを宣言します。`withTaskGroup`呼び出し全体は1つの式なので、その前に1つの`await`が必要であり、すべての子タスクが完了するまで返りません。

---

タスクグループは、タスクが追加された順序ではなく**完了順**で結果を渡してきます。最も速い子タスクが最初に届くので、値を配列に集めると順序は予測できません。

順序が重要な場合、修正方法は2つあります。値を単純に並べ替えてよいなら、最後にソートします:
```swift
return values.sorted()
```
各結果が位置に対応するなら、すべてのタスクにペア`(index, value)`を返させ、用意した配列に書き込みます:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
合計、最大値、個数にはどちらの修正も不要です。値の順序が答えを変えないためです。
