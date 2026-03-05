---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

数値を引数として受け取り、`"Fizz"`、`"Buzz"`または`"FizzBuzz"`を返す関数を作成してください。

# --instructions--

- 数値が`3`の倍数の場合、出力は`"Fizz"`になります
- 数値が`5`の倍数の場合、出力は`"Buzz"`になります。
- 数値が`3`と`5`の両方の倍数の場合、出力は`"FizzBuzz"`になります。
- 数値が`3`でも`5`の倍数でもない場合、以下の例に示すようにその数値自体を出力します。
- 出力は`3`や`5`の倍数でなくても常に文字列でなければなりません。

例：
```kotlin
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```kotlin
fun fizzBuzz() {
    
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

数値`3`は`"Fizz"`に等しくなければなりません

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

数値`5`は`"Buzz"`に等しくなければなりません

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

数値`15`は`"FizzBuzz"`に等しくなければなりません

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

数値`10`は`"Buzz"`に等しくなければなりません

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

数値`98`は`"98"`に等しくなければなりません

```kotlin
    tryCatch(fizzBuzz(98) == "98");
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
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0 && number % 5 == 0) {
        return "FizzBuzz"
    }
    if (number % 3 == 0) {
        return "Fizz"
    }
    if (number % 5 == 0) {
        return "Buzz"
    }
    return number.toString()
}
```
