A **regular expression** (or **regex**) is a small pattern that describes a shape of text: "four digits", "a word followed by `@`", "anything between quotes". In Kotlin a pattern is a `Regex` object, built in two equivalent ways:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
Most characters in a pattern stand for themselves, but a few are **shorthands**:
- `\d` is any digit, written `"\\d"` in a Kotlin string because `\` must be escaped
- `[a-z]` is any lowercase letter, and `[abc]` is any of `a`, `b` or `c`
- `+` after an element means "one or more of it", so `\d+` is a run of digits

The simplest question you can ask is `matches`, which is `true` only when the pattern describes the **whole** string:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` is often too strict: usually you only want to know whether the pattern appears **somewhere** in the text. That is `containsMatchIn`:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
Next to `\d` there are two more shorthands you will use constantly: `\w` is a word character (letter, digit or `_`) and `\s` is a whitespace character. Each of them can be repeated with a **quantifier**:
- `+` one or more
- `*` zero or more
- `?` zero or one
- `{3}` exactly three, `{2,4}` from two to four

Doubling every backslash gets noisy, so patterns are usually written as **raw strings** with triple quotes, where `\` is just a character:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` only says *if* the pattern is there. `find` also says **what** and **where**: it returns the first match as a `MatchResult`, or `null` when there is nothing to find.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` is the matched text and `range` are the indices it covers in the original string. Because the result is nullable you reach into it with the safe call `?.`, which gives `null` instead of crashing when no match was found:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Parentheses in a pattern create a **capturing group**: a piece of the match you want to read back separately. `MatchResult.groupValues` holds them, with index `0` for the whole match and `1`, `2`, ... for the groups, from left to right:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
When there is no match at all, `find` returns `null` and there is nothing to read, so a function that extracts a group usually decides what to return in that case:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Counting parentheses to find out that the host is group `2` gets fragile as soon as the pattern grows. A group can be given a **name** with `(?<name>...)` and read from `groups` by that name:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` returns the group as a `MatchGroup?`, so you still ask for its `.value`. A named group is also numbered as usual, so `groupValues[1]` keeps working next to it.

---

`find` stops at the first match. `findAll` returns **every** match, as a `Sequence<MatchResult>`: a lazy chain you can treat like a list with `map`, `filter`, `count` and `toList`.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
When nothing matches, `findAll` returns an empty sequence instead of `null`, so there is no safe call to write. Printing the sequence itself is not useful, it shows the object, not the matches: turn it into a list first.

---

`replace` rewrites the text: it returns a **new** string where every match is swapped for the replacement, leaving the original untouched.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
In the replacement string, `$1`, `$2`, ... stand for the captured groups of that match, so you can reorder or reuse the pieces you matched:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` is the whole match. If you need a literal `$` in the replacement, escape it as `\$`.
`replace` rewrites **every** match, so when only a complete string should be rewritten, pin the pattern with the **anchors** `^` (start of the text) and `$` (end of the text):
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

A replacement string can only rearrange the pieces it was given. When the new text has to be **computed**, pass a lambda to `replace` instead: it receives the `MatchResult` and returns the string that takes its place.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Inside the lambda you have the full `MatchResult`, so `m.value`, `m.range` and `m.groupValues` are all available. Note that `$1` has no meaning here: it is an ordinary character in whatever string you return.

---

`split` cuts a string wherever the pattern matches and returns the pieces as a `List<String>`. Unlike splitting on a fixed delimiter string, a regex separator can describe a whole family of separators:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
The matched separators are not part of the result. If the text starts or ends with a separator, the piece next to it is empty:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` accepts a `limit` as second argument to stop after a given number of pieces, keeping the rest untouched in the last one.

---

Patterns are case sensitive: `Regex("kotlin")` does not match `"Kotlin"`. Instead of writing `[kK][oO]...`, pass an option as second argument:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
The option belongs to the `Regex`, so every method of that object obeys it: `matches`, `find`, `findAll`, `replace` and `split` alike. Other useful options are `RegexOption.MULTILINE`, which makes `^` and `$` match at every line, and `RegexOption.DOT_MATCHES_ALL`. To combine them, pass a set: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` also matches the `cat` inside `catalog`. To require a whole word, use the **word boundary** `\b`: it matches the empty position between a word character and anything else, including the start and the end of the text.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
A pattern is an ordinary string, so it can be built from parts at runtime:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

The characters `. * + ? ( ) [ ] { } | ^ $ \` have a special meaning inside a pattern. The most treacherous is `.`, which matches **any** character, not a dot. To mean the character itself, escape it with a backslash:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
When the text to look for comes from a variable and must be taken literally, let the library do the escaping with `Regex.escape`:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` and groups together turn a line of text into structured data. Each `MatchResult` of the sequence carries its own `groupValues`, so one chain can build a list, a map or a total:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` builds a map out of the `key to value` pairs returned by the lambda. When a pattern has a fixed number of groups, `destructured` lets you unpack them into named variables instead of reading them by index:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Square brackets define a **character class**: one character out of the listed set. Inside them you can use ranges, and a leading `^` negates the whole class:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
A class only chooses between single characters. To choose between whole alternatives, use `|`, usually wrapped in a group so that it does not swallow the rest of the pattern:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Because `findAll` gives a sequence, the aggregating methods you already know work on matches too: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Extracting numbers from free text is a two-step job: match them, then convert the text to a number.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

A realistic pattern usually mixes everything at once: groups to keep the parts you need, an escaped `\.` for the literal dots, and a lambda replacement to rebuild the text around them.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Keep patterns as simple as the job allows: a pattern that tries to describe every legal email address is unreadable, while `\w+@\w+\.\w+` is enough to find the addresses in a sentence.
