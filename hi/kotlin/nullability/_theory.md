कभी-कभी एक मान सचमुच अनुपस्थित होता है: बिना मिडल नेम वाला उपयोगकर्ता, कुछ न ढूंढ पाने वाली खोज, वह टेक्स्ट जिसे संख्या में बदला नहीं जा सकता।
Kotlin अनुपस्थित मान को `null` से दर्शाता है, लेकिन एक सामान्य वेरिएबल उसे कभी नहीं रख सकता। हर टाइप डिफ़ॉल्ट रूप से **non-null** होता है:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
अनुपस्थित मान की अनुमति देने के लिए आप टाइप के बाद प्रश्नचिह्न `?` जोड़कर एक **nullable** टाइप घोषित करते हैं।
एक `String?` में या तो `String` होता है या `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` और `String?` दो अलग टाइप हैं: एक `String` कभी अनुपस्थित नहीं होता, जबकि एक `String?` हो सकता है।

---

`String` और `String?` के बीच का अंतर रनटाइम पर नहीं, बल्कि **कंपाइलर** द्वारा जांचा जाता है।
किसी non-null टाइप को `null` असाइन करना, या जहां non-null मान अपेक्षित हो वहां एक nullable मान पास करना, एक कंपाइल एरर है, इसलिए प्रोग्राम शुरू होती ही नहीं:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
इसी तरह Kotlin अन्य भाषाओं में आम "null pointer" क्रैश से बचता है: कोई मान केवल वहीं अनुपस्थित हो सकता है जहां आपने `?` के साथ स्पष्ट रूप से घोषित किया हो।

---

`?` टाइप लिखे जाने की हर जगह काम करता है: एक फंक्शन nullable पैरामीटर स्वीकार कर सकता है और nullable मान लौटा सकता है।
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
आप किसी nullable मान पर सीधे मेथड कॉल नहीं कर सकते, क्योंकि वह `null` हो सकता है।
**सेफ कॉल** ऑपरेटर `?.` मेथड को केवल तब कॉल करता है जब मान `null` न हो; अन्यथा पूरी एक्सप्रेशन `null` हो जाती है:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
सेफ कॉल का परिणाम हमेशा nullable होता है: `word?.length` एक `Int?` है, `Int` नहीं।

---

अक्सर आप किसी nullable मान से जो चाहते हैं वह बस मान स्वयं या एक डिफ़ॉल्ट होता है।
**Elvis ऑपरेटर** `?:` बिल्कुल यही करता है: जब बायां हिस्सा `null` न हो तो वही लौटाता है, अन्यथा दाईं ओर का मान:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
चूंकि दायां हिस्सा केवल तब उपयोग किया जाता है जब बायां `null` हो, डिफ़ॉल्ट के non-null होने पर परिणाम भी non-null होता है।
`?:`, `?.` के साथ अच्छी तरह मिलकर एक सेफ कॉल को वापस साधारण मान में बदल देता है:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

सेफ कॉल को **चेन** किया जा सकता है: जैसे ही एक कड़ी `null` हो जाती है, चेन का बाकी हिस्सा छोड़ दिया जाता है और पूरी एक्सप्रेशन `null` हो जाती है।
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
`?:` पर समाप्त होने वाला चेन एक ही पंक्ति में non-null परिणाम देता है:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

सेफ कॉल चेन नेस्टेड ऑब्जेक्ट्स के साथ बेहतरीन काम करती हैं, जहां कोई भी स्तर अनुपस्थित हो सकता है:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
हर `?.` अगला चरण सुरक्षित रखता है, और अंतिम `?:` डिफ़ॉल्ट मान देता है।

---

**not-null एसर्शन** ऑपरेटर `!!` एक nullable मान को non-null में बदल देता है, और कंपाइलर को बताता है "मुझे पक्का यकीन है कि यह `null` नहीं है":
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
यदि आप गलत होते हैं और मान `null` होता है, तो प्रोग्राम रनटाइम पर `NullPointerException` के साथ क्रैश हो जाती है — वही एरर जिसे रोकने के लिए Kotlin बनाया गया था:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
`!!` का उपयोग केवल तब करें जब मान सचमुच `null` नहीं हो सकता; बाकी हर जगह `?.`, `?:` और null जांच को प्राथमिकता दें।

---

जब आप `if` से किसी मान की `null` जांच करते हैं, तो कंपाइलर उसे याद रखता है: उस ब्रांच के अंदर जहां मान non-null ज्ञात होता है, यह non-null टाइप में **स्मार्ट कास्ट** हो जाता है और आप उसे सीधे उपयोग कर सकते हैं, बिना `?.` या `!!` के:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
वही बात अर्ली एक्ज़िट के बाद भी होती है:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
स्मार्ट कास्ट `val` वेरिएबल और फंक्शन पैरामीटर पर काम करते हैं, जिनका मान जांच और उपयोग के बीच बदल नहीं सकता।

---

`let` जिस मान पर कॉल किया जाता है उसी के साथ कोड का एक ब्लॉक चलाता है; वह मान ब्लॉक के अंदर `it` के रूप में उपलब्ध होता है।
एक सेफ कॉल के साथ मिलाकर, `?.let` ब्लॉक को **केवल** तब चलाता है जब मान `null` न हो, और ब्लॉक के अंदर `it` non-null होता है:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
जब आपको मान केवल ब्लॉक के अंदर चाहिए हो, तो यह `if (x != null) { ... }` का संक्षिप्त विकल्प है।

---

`let` अपने ब्लॉक की आखिरी एक्सप्रेशन का मान **लौटाता** भी है, इसलिए `?.let` एक nullable मान को बदल सकता है और उसके `null` होने पर `?:` डिफ़ॉल्ट मान भर सकता है:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
जब `price` `null` होता है तो `let` ब्लॉक छोड़ दिया जाता है, एक्सप्रेशन `null` हो जाती है और Elvis ऑपरेटर `"free"` लौटाता है।

---

कलेक्शंस nullable तत्व भी रख सकते हैं: एक `List<Int?>` में `null` entries हो सकती हैं, जबकि एक `List<Int>` में कभी नहीं होतीं।
`filterNotNull()` एक नई लिस्ट लौटाता है जिसमें `null` entries हटा दी जाती हैं, और उसका एलिमेंट टाइप non-null हो जाता है, इसलिए आप तत्वों का स्वतंत्र रूप से उपयोग कर सकते हैं:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

कई स्टैंडर्ड फंक्शन विफल होने की जगह `null` लौटाते हैं। `toIntOrNull()` एक स्ट्रिंग को `Int` में बदलता है, या टेक्स्ट के पूर्ण संख्या न होने पर `null` लौटाता है:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` हर तत्व को `map` की तरह बदलता है, लेकिन `null` परिणामों को छोड़ देता है:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

कभी-कभी ऑब्जेक्ट बनते समय किसी प्रॉपर्टी को मान नहीं दिया जा सकता, लेकिन आप जानते हैं कि उपयोग से पहले वह सेट हो जाएगी।
उसे nullable बनाने की जगह `lateinit` से चिह्नित करें: टाइप non-null रहता है और पढ़ते समय `?.` की आवश्यकता नहीं होती:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` के कुछ नियम हैं: यह केवल `var` प्रॉपर्टी पर, केवल non-null टाइप के साथ काम करता है, और `Int` या `Boolean` जैसे प्रिमिटिव टाइप के साथ नहीं।
असाइन करने से पहले `lateinit` प्रॉपर्टी पढ़ने पर एक `UninitializedPropertyAccessException` थ्रो होती है; आप इसे पहले `::player.isInitialized` से जांच सकते हैं।

---

जब एक `null` का मतलब हो कि कॉलर ने गलती की है, तो `requireNotNull` के साथ जल्दी विफल हों।
यह मान के मौजूद होने पर उसे non-null के रूप में लौटाता है, और `null` होने पर एक वैकल्पिक संदेश के साथ `IllegalArgumentException` थ्रो करता है:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
कॉल के बाद कंपाइलर `name` को भी `String` में स्मार्ट कास्ट कर देता है, इसलिए उस पंक्ति से `name.length` की अनुमति होती है।
`!!` के विपरीत, विफलता के साथ एक स्पष्ट संदेश होता है और वह बताता है कि *argument* गलत था।

---

एक एक्सटेंशन फंक्शन को **nullable रिसीवर** पर घोषित किया जा सकता है, इसलिए उसे `null` मान पर भी कॉल किया जा सकता है। अंदर, `this` nullable होता है और उसे जांचा जाना चाहिए:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
ध्यान दें कि कॉल साइट पर `?.` की आवश्यकता नहीं है: फंक्शन स्वयं `null` केस को संभालता है।
स्टैंडर्ड लाइब्रेरी इस तरीके का उपयोग `isNullOrEmpty()` और `orEmpty()` में करती है, जिन्हें किसी भी `String?` पर सुरक्षित रूप से कॉल किया जा सकता है।

---

`?:` का दायां हिस्सा कोई भी एक्सप्रेशन हो सकता है, जिसमें `return` भी शामिल है। इससे मान के अनुपस्थित होते ही फंक्शन से बाहर निकलने का एक संक्षिप्त तरीका मिलता है:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
आपके द्वारा देखे गए हर टूल अच्छी तरह मिलते हैं: nullable पैरामीटर और रिटर्न टाइप बताते हैं कि मान *कहां* अनुपस्थित हो सकता है, और `?.`, `?:`, `let`, स्मार्ट कास्ट तथा `toIntOrNull` उसे कभी क्रैश हुए बिना संभालते हैं।
