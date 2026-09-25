---
language: kotlin
exerciseType: 1
difficulty: 2
title: ランレングス符号化
---

# --description--

ランレングス符号化は、圧縮のテクニックの中でも最も古いものの1つです。同じ文字を何度も書き連ねる代わりに、その文字が何回繰り返されるかを書き、その後に文字そのものを書きます。

ほとんどが空白のページをスキャンするファックスは、同じピクセルが長く続く部分に出会います。そのため、`W` が12個並んだ1行は、はるかに短い `12W` となって回線を流れていきます。文字が1度しか現れない場合は、数えても得るものがないため、その文字だけがそのままコピーされます。

# --instructions--

文字列 `text` を受け取り、ランレングス符号化した形式を返す関数 `encodeRun` を書いてください。

同じ文字が2回以上続く連続した並びは、その長さを十進数で書いたものに、その文字を付けた形になります。長さ1の並びは、前に数字を付けずに、その1文字だけがそのままコピーされます。

例:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- テキストには `A` から `Z` までの大文字とスペースだけが含まれます。
- 9文字より長い並びは、十進数の回数をすべて使うため、`W` が12個なら `12W` となり、`9W3W` にはなりません。
- スペースも普通の文字です。文字とまったく同じように数えられ、エンコードされます。
- 空の文字列は空の文字列にエンコードされます。

# --seed--

```kotlin
fun encodeRun(text: String): String {
    
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

空の文字列は空の文字列にエンコードされる

```kotlin
    tryCatch(encodeRun("") == "")
```

1文字だけの文字はそのままコピーされる

```kotlin
    tryCatch(encodeRun("A") == "A")
```

繰り返しのない文字列は変化せずにそのまま通る

```kotlin
    tryCatch(encodeRun("ABCDE") == "ABCDE")
```

長さ2の並びは、回数の後に文字が付いた形になる

```kotlin
    tryCatch(encodeRun("AA") == "2A")
```

並びが混ざった例 "AABCCCDEEEE" は "2AB3CD4E" になる

```kotlin
    tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

長さ12の並びは十進数の回数をすべて使うため、結果は "12W" で始まる

```kotlin
    tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

スペースの並びも文字の並びと同じようにエンコードされる

```kotlin
    tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

長さ10の並びは "10A" と書かれ、より短い2つの並びに分けられることはない

```kotlin
    tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

交互に現れる1文字はすべてそのままコピーされる

```kotlin
    tryCatch(encodeRun("ABABAB") == "ABABAB")
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
fun encodeRun(text: String): String {
    val result = StringBuilder()
    var i = 0

    while (i < text.length) {
        var run = 1
        while (i + run < text.length && text[i + run] == text[i]) {
            run++
        }
        if (run > 1) {
            result.append(run)
        }
        result.append(text[i])
        i += run
    }

    return result.toString()
}
```
