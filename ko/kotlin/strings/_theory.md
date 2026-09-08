`String`은 큰따옴표로 둘러싸서 작성하는 문자의 나열입니다.
`length` 프로퍼티는 공백을 포함해 문자열에 몇 개의 문자가 들어 있는지 알려줍니다:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

문자열의 각 문자에는 **인덱스**가 있으며, 첫 번째 문자는 `0`부터 시작합니다.
대괄호나 `get` 함수를 사용해 문자 하나를 읽을 수 있으며, 결과는 `Char`입니다:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
마지막 문자는 인덱스 `length - 1`에 있습니다. `first()`와 `last()` 함수는 편리한 단축 방법입니다:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()`는 문자열의 모든 글자를 대문자로 바꾼 사본을 반환하고, `lowercase()`는 그 반대의 일을 합니다.
원본 문자열은 변경되지 않습니다:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

문자열에 특정 텍스트가 포함되어 있는지 확인하려면 `contains`, `startsWith`, `endsWith`를 사용합니다. 이들은 모두 `Boolean`을 반환합니다:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
이 비교는 대소문자를 구분하지만, `ignoreCase = true`를 전달하면 구분하지 않습니다:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf`는 어떤 텍스트가 **처음** 나타나는 인덱스를 반환하며, 전혀 나타나지 않으면 `-1`을 반환합니다.
`lastIndexOf`는 대신 끝에서부터 검색합니다:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring`은 문자열의 일부를 추출합니다. 인자를 두 개 전달하면 시작 인덱스부터 끝 인덱스 **직전까지**(끝 인덱스는 포함하지 않음)의 문자를 가져옵니다.
인자가 하나면 그 인덱스부터 끝까지 전부를 가져옵니다:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
`indexOf`와 `substring`을 조합하면 표시 문자를 기준으로 문자열을 잘라낼 수 있습니다:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split`은 구분자를 기준으로 문자열을 `List` 조각으로 나누고, `joinToString`은 그 반대로 컬렉션의 요소들을 원하는 구분자로 하나의 문자열로 이어 붙입니다:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

`split`은 `List`를 반환하므로 다른 리스트와 마찬가지로 요소를 순회할 수 있습니다:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

사용자 입력에는 종종 불필요한 공백이 포함됩니다. `trim()`은 앞뒤 공백을 제거한 문자열을 반환하며, `trimStart()`와 `trimEnd()`는 한쪽만 제거합니다:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()`는 `""`일 때 `true`이지만, `isBlank()`는 공백만으로 이루어진 문자열에도 `true`입니다:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)`는 `old`가 나타나는 **모든** 부분을 `new`로 바꾼 사본을 반환합니다:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)`은 문자열을 `n`번 이어붙인 것을 반환합니다:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)`는 문자열이 `width` 길이에 도달할 때까지 앞쪽에 `char`를 추가합니다. `padEnd`는 뒤쪽에 추가합니다.
문자열이 이미 충분히 길면 변경 없이 그대로 반환됩니다:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
숫자는 문자열이 아니므로, `42.toString().padStart(4, '0')`처럼 먼저 `toString()`을 호출하세요.
