एक **रेगुलर एक्सप्रेशन** (या **रेगेक्स**) टेक्स्ट की एक आकृति का वर्णन करने वाला एक छोटा पैटर्न है: "चार अंक", "`@` के बाद एक शब्द", "कोट्स के बीच की कोई भी चीज़"। Kotlin में एक पैटर्न एक `Regex` ऑब्जेक्ट होता है, जिसे दो समतुल्य तरीकों से बनाया जाता है:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
पैटर्न के अधिकांश कैरेक्टर खुद का ही प्रतिनिधित्व करते हैं, लेकिन कुछ **शॉर्टहैंड** होते हैं:
- `\d` कोई भी अंक है, Kotlin स्ट्रिंग में `"\\d"` लिखा जाता है क्योंकि `\` को एस्केप करना ज़रूरी होता है
- `[a-z]` कोई भी लोअरकेस अक्षर है, और `[abc]` में से कोई भी `a`, `b` या `c` है
- किसी एलिमेंट के बाद `+` का मतलब है "उसका एक या अधिक", इसलिए `\d+` अंकों की एक श्रृंखला है

सबसे सरल सवाल जो आप पूछ सकते हैं वह `matches` है, जो केवल तब `true` होता है जब पैटर्न **पूरी** स्ट्रिंग का वर्णन करता हो:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` अक्सर बहुत सख़्त होता है: आमतौर पर आप केवल यह जानना चाहते हैं कि पैटर्न टेक्स्ट में **कहीं भी** दिखाई देता है या नहीं। वह `containsMatchIn` है:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
`\d` के अलावा दो और शॉर्टहैंड हैं जिनका उपयोग आप बार-बार करेंगे: `\w` एक वर्ड कैरेक्टर है (अक्षर, अंक या `_`) और `\s` एक व्हाइटस्पेस कैरेक्टर है। इनमें से हर एक को एक **quantifier** के साथ दोहराया जा सकता है:
- `+` एक या अधिक
- `*` शून्य या अधिक
- `?` शून्य या एक
- `{3}` ठीक तीन, `{2,4}` दो से चार तक

हर बैकस्लैश को दोगुना करने से कोड गड़बड़ हो जाता है, इसलिए पैटर्न आमतौर पर ट्रिपल कोट्स वाली **raw strings** के रूप में लिखे जाते हैं, जहाँ `\` सिर्फ एक साधारण कैरेक्टर है:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` केवल यह बताता है कि पैटर्न वहाँ *है या नहीं*। `find` यह भी बताता है कि **क्या** और **कहाँ**: वह पहला मैच एक `MatchResult` के रूप में लौटाता है, या `null` जब खोजने को कुछ न हो।
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` मैच किया गया टेक्स्ट है और `range` वे इंडेक्स हैं जिन्हें वह मूल स्ट्रिंग में कवर करता है। क्योंकि परिणाम nullable होता है, आप उसे safe call `?.` से एक्सेस करते हैं, जो मैच न मिलने पर क्रैश होने की बजाय `null` देता है:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

पैटर्न में कोष्ठक (parentheses) एक **capturing group** बनाते हैं: मैच का वह हिस्सा जिसे आप अलग से पढ़ना चाहते हैं। `MatchResult.groupValues` उन्हें रखता है, जिसमें इंडेक्स `0` पूरे मैच के लिए है और `1`, `2`, ... ग्रुप के लिए, बाएँ से दाएँ:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
जब कोई मैच बिल्कुल नहीं होता, तो `find` `null` लौटाता है और पढ़ने को कुछ नहीं होता, इसलिए ग्रुप निकालने वाला फ़ंक्शन आमतौर पर तय करता है कि उस स्थिति में क्या लौटाना है:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

यह जानने के लिए कि host ग्रुप `2` है कोष्ठकों की गिनती करना पैटर्न के बढ़ते ही नाज़ुक हो जाता है। एक ग्रुप को `(?<name>...)` के साथ एक **नाम** दिया जा सकता है और उसी नाम से `groups` से पढ़ा जा सकता है:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` ग्रुप को एक `MatchGroup?` के रूप में लौटाता है, इसलिए आपको फिर भी उसका `.value` माँगना होता है। नाम वाला ग्रुप पहले की तरह नंबर भी होता है, इसलिए `groupValues[1]` उसके साथ-साथ काम करता रहता है।

---

`find` पहले मैच पर रुक जाता है। `findAll` **हर** मैच लौटाता है, एक `Sequence<MatchResult>` के रूप में: एक lazy चेन जिसे आप `map`, `filter`, `count` और `toList` के साथ एक लिस्ट की तरह मान सकते हैं।
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
जब कुछ भी मैच नहीं होता, तो `findAll` `null` की जगह एक खाली sequence लौटाता है, इसलिए कोई safe call लिखने की ज़रूरत नहीं होती। Sequence को खुद प्रिंट करना उपयोगी नहीं है, वह ऑब्जेक्ट दिखाता है, मैच नहीं: पहले उसे एक लिस्ट में बदलें।

---

`replace` टेक्स्ट को फिर से लिखता है: वह एक **नई** स्ट्रिंग लौटाता है जिसमें हर मैच रिप्लेसमेंट से बदल दिया जाता है, और मूल स्ट्रिंग अछूती रहती है।
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
रिप्लेसमेंट स्ट्रिंग में, `$1`, `$2`, ... उस मैच के कैप्चर किए गए ग्रुप दर्शाते हैं, इसलिए आप मैच किए गए टुकड़ों का क्रम बदल सकते हैं या उन्हें दोबारा उपयोग कर सकते हैं:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` पूरा मैच होता है। अगर आपको रिप्लेसमेंट में एक literal `$` चाहिए, तो उसे `\$` के रूप में एस्केप करें।
`replace` **हर** मैच को फिर से लिखता है, इसलिए जब केवल एक पूरी स्ट्रिंग को फिर से लिखना हो, तो पैटर्न को **anchors** `^` (टेक्स्ट की शुरुआत) और `$` (टेक्स्ट का अंत) से पिन करें:
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

एक रिप्लेसमेंट स्ट्रिंग केवल उन्हीं टुकड़ों को फिर से व्यवस्थित कर सकती है जो उसे दिए गए थे। जब नए टेक्स्ट को **compute** किया जाना हो, तो इसकी बजाय `replace` को एक लैम्ब्डा पास करें: लैम्ब्डा को `MatchResult` मिलता है और वह वह स्ट्रिंग लौटाता है जो उसकी जगह लेती है।
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
लैम्ब्डा के अंदर आपके पास पूरा `MatchResult` होता है, इसलिए `m.value`, `m.range` और `m.groupValues` सब उपलब्ध होते हैं। ध्यान दें कि `$1` का यहाँ कोई मतलब नहीं है: वह आपके द्वारा लौटाई गई किसी भी स्ट्रिंग में एक साधारण कैरेक्टर है।

---

`split` स्ट्रिंग को जहाँ-जहाँ पैटर्न मैच करता है वहाँ काटता है और टुकड़ों को एक `List<String>` के रूप में लौटाता है। किसी निश्चित डेलिमिटर स्ट्रिंग पर स्प्लिट करने के विपरीत, एक regex सेपरेटर सेपरेटर का पूरा परिवार बता सकता है:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
मैच हुए सेपरेटर परिणाम का हिस्सा नहीं होते। अगर टेक्स्ट किसी सेपरेटर से शुरू या खत्म होता है, तो उसके बगल का टुकड़ा खाली होता है:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` दूसरे आर्ग्युमेंट के रूप में एक `limit` स्वीकार करता है, ताकि दी गई संख्या के टुकड़ों के बाद रुक जाए और बाकी को आखिरी टुकड़े में अछूता रखे।

---

पैटर्न केस-सेंसिटिव होते हैं: `Regex("kotlin")` `"Kotlin"` से मैच नहीं करता। `[kK][oO]...` लिखने की बजाय, दूसरे आर्ग्युमेंट के रूप में एक ऑप्शन पास करें:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
ऑप्शन `Regex` से जुड़ा होता है, इसलिए उस ऑब्जेक्ट की हर मेथड उसका पालन करती है: `matches`, `find`, `findAll`, `replace` और `split` समान रूप से। अन्य उपयोगी ऑप्शन हैं `RegexOption.MULTILINE`, जो `^` और `$` को हर लाइन पर मैच कराता है, और `RegexOption.DOT_MATCHES_ALL`। उन्हें मिलाने के लिए एक सेट पास करें: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`।

---

`Regex("cat")` `catalog` के अंदर वाले `cat` से भी मैच करता है। एक पूरा शब्द माँगने के लिए, **word boundary** `\b` का उपयोग करें: वह वर्ड कैरेक्टर और किसी और चीज़ के बीच की खाली पोज़िशन से मैच करता है, जिसमें टेक्स्ट की शुरुआत और अंत भी शामिल है।
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
एक पैटर्न एक साधारण स्ट्रिंग होता है, इसलिए उसे runtime पर टुकड़ों से बनाया जा सकता है:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

कैरेक्टर `. * + ? ( ) [ ] { } | ^ $ \` का पैटर्न के अंदर एक विशेष मतलब होता है। उनमें सबसे धोखेबाज़ `.` है, जो **कोई भी** कैरेक्टर से मैच करता है, डॉट से नहीं। कैरेक्टर के खुद का मतलब देने के लिए, उसे एक बैकस्लैश के साथ एस्केप करें:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
जब खोजने के लिए टेक्स्ट किसी वेरिएबल से आता है और उसे literal लिया जाना ज़रूरी हो, तो एस्केपिंग `Regex.escape` से लाइब्रेरी को करने दें:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` और ग्रुप मिलकर टेक्स्ट की एक लाइन को संरचित डेटा में बदल देते हैं। Sequence का हर `MatchResult` अपने `groupValues` साथ रखता है, इसलिए एक ही चेन एक लिस्ट, एक मैप या एक कुल योग बना सकती है:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` लैम्ब्डा द्वारा लौटाए गए `key to value` जोड़ों से एक मैप बनाता है। जब पैटर्न में ग्रुप की संख्या निश्चित होती है, तो `destructured` आपको उन्हें इंडेक्स से पढ़ने की बजाय नाम वाले वेरिएबल में अनपैक करने देता है:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

स्क्वायर ब्रैकेट एक **character class** परिभाषित करते हैं: सूचीबद्ध सेट में से एक कैरेक्टर। उनके अंदर आप रेंज का उपयोग कर सकते हैं, और शुरू में लगा `^` पूरी क्लास को negate कर देता है:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
एक क्लास केवल एकल कैरेक्टर के बीच चुनती है। पूरे विकल्पों के बीच चुनने के लिए, `|` का उपयोग करें, आमतौर पर एक ग्रुप में लपेटा हुआ ताकि वह पैटर्न का बाकी हिस्सा निगल न जाए:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

चूंकि `findAll` एक sequence देता है, आपके द्वारा पहले से जानी जाने वाली एग्रीगेटिंग मेथड मैच पर भी काम करती हैं: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`। फ्री टेक्स्ट से संख्याएँ निकालना एक दो-चरण का काम है: पहले उन्हें मैच करें, फिर टेक्स्ट को एक संख्या में बदलें।
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

एक यथार्थवादी पैटर्न आमतौर पर सब कुछ एक साथ मिलाता है: ग्रुप, जो आपके काम के हिस्से रखते हैं; literal डॉट के लिए एस्केप किया हुआ `\.`; और उनके चारों ओर टेक्स्ट को फिर से बनाने के लिए एक लैम्ब्डा रिप्लेसमेंट।
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
पैटर्न को जितना सरल काम अनुमति देता है उतना सरल रखें: हर कानूनी ईमेल एड्रेस का वर्णन करने की कोशिश करने वाला पैटर्न अपठनीय होता है, जबकि `\w+@\w+\.\w+` एक वाक्य में एड्रेस खोजने के लिए काफी है।
