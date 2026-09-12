**정규 표현식**(또는 **정규식**)은 텍스트의 모양을 묘사하는 작은 패턴입니다: "숫자 네 개", "`@` 앞에 오는 단어", "따옴표 사이의 모든 것"처럼요. Kotlin에서 패턴은 `Regex` 객체이며, 두 가지 동등한 방법으로 만들 수 있습니다:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
패턴의 대부분 문자는 자기 자신을 뜻하지만, 몇 가지 **축약 표현**이 있습니다:
- `\d`는 임의의 숫자이며, `\`는 이스케이프해야 하므로 Kotlin 문자열에서는 `"\\d"`로 씁니다
- `[a-z]`는 임의의 소문자이고, `[abc]`는 `a`, `b`, `c` 중 하나입니다
- 요소 뒤의 `+`는 "하나 이상"을 뜻하므로, `\d+`는 연속된 숫자입니다

가장 단순한 질문은 `matches`입니다. 패턴이 문자열 **전체**를 묘사할 때만 `true`가 됩니다:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches`는 너무 엄격할 때가 많습니다. 보통은 패턴이 텍스트 **어딘가에** 나타나는지만 알면 되니까요. 그때 쓰는 것이 `containsMatchIn`입니다:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
`\d` 외에도 늘 사용하게 될 축약 표현이 두 가지 더 있습니다. `\w`는 단어 문자(글자, 숫자 또는 `_`)이고 `\s`는 공백 문자입니다. 둘 다 **수량자**로 반복할 수 있습니다:
- `+` 하나 이상
- `*` 0개 이상
- `?` 0개 또는 1개
- `{3}` 정확히 3개, `{2,4}` 2개부터 4개

백슬래시를 매번 두 배로 쓰면 번거롭기 때문에, 패턴은 보통 삼중 따옴표로 쓴 **raw 문자열**로 작성합니다. 여기서는 `\`가 그냥 문자입니다:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn`은 패턴이 있는지 *여부*만 알려줍니다. `find`는 **무엇이** **어디에** 있는지도 알려줍니다. 첫 번째 매치를 `MatchResult`로 반환하고, 찾을 것이 없으면 `null`을 반환합니다:
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value`는 매치된 텍스트이고, `range`는 원본 문자열에서 그 텍스트가 차지하는 인덱스입니다. 결과는 널 가능 타입이므로 안전 호출 `?.`로 접근합니다. 매치가 없을 때 크래시하는 대신 `null`을 얻습니다:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

패턴 안의 괄호는 **캡처 그룹**을 만듭니다. 매치 중에서 따로 읽어 보고 싶은 부분입니다. `MatchResult.groupValues`에 담기며, 인덱스 `0`은 매치 전체를, `1`, `2`, ...는 왼쪽부터 차례로 각 그룹을 가리킵니다:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
매치가 아예 없으면 `find`가 `null`을 반환해 읽을 것이 없으므로, 그룹을 추출하는 함수는 보통 그 경우 무엇을 반환할지 스스로 정합니다:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

패턴이 길어지면 괄호를 세어 호스트가 그룹 `2`임을 찾아내는 방식은 금방 다루기 어려워집니다. 그룹에는 `(?<name>...)`으로 **이름**을 붙일 수 있고, `groups`에서 그 이름으로 읽을 수 있습니다:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups`는 그룹을 `MatchGroup?`으로 반환하므로 여전히 `.value`를 요청해야 합니다. 이름 붙은 그룹도 평소처럼 번호를 가지므로, `groupValues[1]`은 그와 함께 계속 동작합니다.

---

`find`는 첫 번째 매치에서 멈춥니다. `findAll`은 **모든** 매치를 `Sequence<MatchResult>`로 반환합니다. `map`, `filter`, `count`, `toList`와 함께 리스트처럼 다룰 수 있는 지연 계산 체인입니다:
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
아무것도 매치되지 않으면 `findAll`은 `null` 대신 빈 시퀀스를 반환하므로, 안전 호출을 쓸 필요가 없습니다. 시퀀스 자체를 출력하는 것은 유용하지 않습니다. 매치가 아니라 객체가 보이니, 먼저 리스트로 바꾸세요.

---

`replace`는 텍스트를 다시 씁니다. 모든 매치를 대체 문자열로 바꾼 **새로운** 문자열을 반환하며, 원본은 그대로 유지됩니다:
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
대체 문자열에서 `$1`, `$2`, ...는 그 매치의 캡처 그룹을 가리키므로, 매치한 조각들을 재배치하거나 재사용할 수 있습니다:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0`은 매치 전체입니다. 대체 문자열에 문자 그대로의 `$`가 필요하면 `\$`로 이스케이프하세요.
`replace`는 **모든** 매치를 다시 쓰므로, 완전한 문자열만 다시 쓰고 싶다면 **앵커**인 `^`(텍스트의 시작)와 `$`(텍스트의 끝)로 패턴을 고정하세요:
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

대체 문자열은 주어진 조각들을 재배치할 수만 있습니다. 새 텍스트를 **계산**해야 한다면 대신 람다를 `replace`에 전달하세요. 람다는 `MatchResult`를 받고 그 자리를 대신할 문자열을 반환합니다:
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
람다 안에서는 `MatchResult` 전체를 사용할 수 있으므로 `m.value`, `m.range`, `m.groupValues` 모두 쓸 수 있습니다. `$1`은 여기서 아무 의미가 없다는 점에 유의하세요. 반환하는 문자열에서 그저 평범한 문자일 뿐입니다.

---

`split`은 패턴이 매치되는 곳마다 문자열을 자르고 조각들을 `List<String>`으로 반환합니다. 고정된 구분자 문자열로 자르는 것과 달리, 정규식 구분자는 한 부류의 구분자 전체를 묘사할 수 있습니다:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
매치된 구분자는 결과에 포함되지 않습니다. 텍스트가 구분자로 시작하거나 끝나면 그 옆의 조각은 빈 문자열입니다:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split`은 두 번째 인자로 `limit`를 받아 주어진 개수의 조각을 만든 뒤 멈출 수 있으며, 나머지는 마지막 조각에 그대로 남습니다.

---

패턴은 대소문자를 구분합니다. `Regex("kotlin")`은 `"Kotlin"`에 일치하지 않습니다. `[kK][oO]...`처럼 쓰는 대신, 옵션을 두 번째 인자로 전달하세요:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
옵션은 `Regex`에 속하므로 그 객체의 모든 메서드가 따릅니다. `matches`, `find`, `findAll`, `replace`, `split` 모두 마찬가지입니다. 그 외 유용한 옵션으로는 `^`와 `$`가 매 줄에서 일치하도록 만드는 `RegexOption.MULTILINE`과 `RegexOption.DOT_MATCHES_ALL`이 있습니다. 조합하려면 set을 전달하세요: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")`은 `catalog` 안의 `cat`에도 일치합니다. 완전한 단어를 요구하려면 **단어 경계** `\b`를 사용하세요. 단어 문자와 그 외의 것 사이의 빈 위치에 일치하며, 텍스트의 시작과 끝도 포함합니다:
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
패턴은 평범한 문자열이므로, 실행 시점에 여러 조각으로 만들 수 있습니다:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

`. * + ? ( ) [ ] { } | ^ $ \` 문자들은 패턴 안에서 특별한 의미를 가집니다. 가장 까다로운 것은 `.`인데, 점이 아니라 **임의의** 문자에 일치합니다. 문자 자체를 뜻하려면 백슬래시로 이스케이프하세요:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
찾으려는 텍스트가 변수에서 나오고 문자 그대로 다뤄져야 한다면, `Regex.escape`로 라이브러리에 이스케이프를 맡기세요:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll`과 그룹을 함께 쓰면 한 줄의 텍스트를 구조화된 데이터로 바꿀 수 있습니다. 시퀀스의 각 `MatchResult`는 자신만의 `groupValues`를 가지므로, 하나의 체인으로 리스트, map 또는 합계를 만들 수 있습니다:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate`는 람다가 반환한 `key to value` 쌍으로 map을 만듭니다. 패턴이 정해진 개수의 그룹을 가진다면, 인덱스로 읽는 대신 `destructured`로 이름 붙은 변수에 풀어 담을 수 있습니다:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

대괄호는 **문자 클래스**를 정의합니다. 나열된 집합 중 한 문자입니다. 안에서는 범위를 쓸 수 있고, 맨 앞의 `^`는 클래스 전체를 부정합니다:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
문자 클래스는 단일 문자 사이에서만 선택합니다. 완전한 대안들 사이에서 선택하려면 `|`를 사용하세요. 보통은 패턴의 나머지 부분을 삼키지 않도록 그룹으로 감쌉니다:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

`findAll`이 시퀀스를 주기 때문에, 이미 아는 집계 메서드들이 매치에도 동작합니다. `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`입니다. 자유로운 텍스트에서 숫자를 추출하는 일은 두 단계입니다. 숫자를 매치한 다음, 텍스트를 숫자로 변환합니다:
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

현실적인 패턴은 보통 이 모든 것을 한꺼번에 섞습니다. 필요한 부분을 담아 둘 그룹, 문자 그대로의 점을 위한 이스케이프한 `\.`, 그리고 그 주변으로 텍스트를 다시 조립하는 람다 대체입니다.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
패턴은 일이 허락하는 한 최대한 단순하게 유지하세요. 모든 올바른 이메일 주소를 묘사하려는 패턴은 읽을 수 없지만, `\w+@\w+\.\w+`면 문장에서 주소를 찾기에 충분합니다.
