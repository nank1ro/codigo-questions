---
language: kotlin
exerciseType: 1
difficulty: 1
title: ハミング距離
---

# --description--

DNAはヌクレオチドがつながったストランドとして書かれ、各ヌクレオチドは`A`、`C`、`G`、`T`のいずれか1文字で表されます。同じ長さの2本のストランドを横に並べると、同じヌクレオチドがくる位置もあれば、異なるヌクレオチドがくる位置もあります。

2本のストランドが異なる位置の数はハミング距離と呼ばれ、生物学者は2本のストランドがどれほど離れているかを測るためにこれを使います。`GAGCCTACTAACGGGAT`と`CATCGTAATGACGGCCT`を並べると7つの位置が異なるので、この2つのハミング距離は7です。

# --instructions--

同じ長さの2本のDNAストランドを受け取り、異なる位置の数を返す`hammingDistance`という関数を書いてください。

例:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 2本のストランドは常に同じ長さなので、異なる長さのストランドを扱う必要はありません。
- 2本の空のストランドはどこも異ならないため、その距離は0です。

# --seed--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

2本の空のストランドはどこも異なりません

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

同じ1文字のヌクレオチドからなる2本のストランドには違いがありません

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

異なる1文字のヌクレオチドからなる2本のストランドは1つの位置で異なります

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

すべての位置で異なる2本の短いストランド

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

最初の位置だけが異なる2本の短いストランド

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

ストランドの途中にある1つの異なるヌクレオチド

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

同じヌクレオチドでも位置が異なれば違いとして数えられます

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

4つの違いがある少し長いストランドのペア

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

ストランドを1つ位置ずらすと、ほぼすべての位置が異なります

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

説明にある2本のストランドの距離は7です

```kotlin
    tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    var distance = 0

    for (i in left.indices) {
        if (left[i] != right[i]) {
            distance++
        }
    }

    return distance
}
```
