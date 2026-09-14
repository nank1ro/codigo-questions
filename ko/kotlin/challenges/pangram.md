---
language: kotlin
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

팬그램은 영어 알파벳의 모든 문자를 적어도 한 번씩 사용하는 문장입니다. 가장 잘 알려진 예는 "the quick brown fox jumps over the lazy dog"이며, 26개의 문자를 모두 아홉 개의 짧은 단어에 담고 있습니다.

이 검사는 대소문자를 구분하지 않으므로 `A`와 `a`는 같은 문자로 셉니다. 숫자, 문장 부호, 공백은 무시됩니다. 이들은 문자가 아니지만, 문장을 거부할 이유도 되지 않습니다.

# --instructions--

문장을 받아 그 문장이 팬그램이면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isPangram`를 작성하세요.

예시:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 빈 문장은 팬그램이 아닙니다.
- `a`부터 `z`까지의 26개 문자만 셉니다.

# --seed--

```kotlin
fun isPangram(sentence: String): Boolean {
    
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

빈 문장은 팬그램이 아니다

```kotlin
    tryCatch(isPangram("") == false)
```

고전적인 문장 "the quick brown fox jumps over the lazy dog"는 팬그램이다

```kotlin
    tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

문자 `x`가 빠진 문장은 팬그램이 아니다

```kotlin
    tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

문장 "the five boxing wizards jump quickly"는 팬그램이다

```kotlin
    tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

밑줄은 무시되므로 그 문장은 여전히 팬그램이다

```kotlin
    tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

숫자는 무시되므로 그 문장은 여전히 팬그램이다

```kotlin
    tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

숫자는 문자 `e`, `i`, `t`를 대신하지 않는다

```kotlin
    tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

대문자로 된 문장도 팬그램이다

```kotlin
    tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

알파벳의 같은 절반의 대소문자를 섞는 것만으로는 충분하지 않다

```kotlin
    tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false)
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
fun isPangram(sentence: String): Boolean {
    val letters = mutableSetOf<Char>()

    for (char in sentence.lowercase()) {
        if (char in 'a'..'z') {
            letters.add(char)
        }
    }

    return letters.size == 26
}
```
