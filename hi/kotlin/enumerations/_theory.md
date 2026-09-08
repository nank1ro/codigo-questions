एक **enumeration** (या *enum*) संबंधित मानों के समूह के लिए एक सामान्य प्रकार परिभाषित करता है, ताकि आप उन मानों के साथ टाइप-सेफ तरीके से काम कर सकें।
Kotlin में आप इसे `enum class` कीवर्ड से घोषित करते हैं, और इसकी **entries** को कॉमा से अलग करके सूचीबद्ध करते हैं:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
परंपरा के अनुसार entry के नाम बड़े अक्षरों में लिखे जाते हैं। प्रत्येक entry enum प्रकार का एक मान है और क्लास के नाम के माध्यम से एक्सेस की जाती है:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
enum class को फ़ाइल के टॉप लेवल पर (या किसी अन्य क्लास के अंदर) घोषित किया जाना चाहिए, कभी भी किसी फ़ंक्शन के अंदर नहीं।

---

हर enum entry में दो built-in properties होती हैं:

- `name` उस entry का नाम एक `String` के रूप में है
- `ordinal` घोषणा में इसकी स्थिति है, जो `0` से शुरू होती है

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

enum entries की तुलना `==` से की जाती है:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

एक `when` expression किसी enum पर branch करने का स्वाभाविक तरीका है। जब यह **हर** entry को कवर करता है तो यह *exhaustive* होता है और इसे किसी `else` branch की ज़रूरत नहीं होती:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
अगर आप कोई entry भूल जाते हैं, तो bug के रनटाइम तक पहुँचने के बजाय compiler एक error रिपोर्ट करता है।

---

एक enum class में, एक सामान्य class की तरह, एक **constructor** हो सकता है। हर entry अपने खुद के arguments पास करती है, और वे मान properties में संग्रहीत हो जाते हैं:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
constructor की properties आमतौर पर `val` के साथ घोषित की जाती हैं, क्योंकि किसी entry का डेटा बदलने के लिए नहीं होता।

---

enum classes **methods** भी घोषित कर सकती हैं। member घोषणाओं से पहले entries की सूची को सेमीकोलन `;` से बंद करना ज़रूरी है:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
किसी method के अंदर आप उस entry की properties के साथ-साथ `name` और `ordinal` भी एक्सेस कर सकते हैं।

---

हर enum class एक `entries` property को expose करती है: घोषणा क्रम में उसकी सभी entries की एक लिस्ट। यह iterate करने के लिए बहुत उपयोगी है:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
एक लिस्ट होने के कारण, `entries` `size` और indexing को भी सपोर्ट करती है, जैसे `Direction.entries[0]` का मान `NORTH` है।

पुराना कोड इसके बजाय `values()` फ़ंक्शन का उपयोग करता है, जो एक array लौटाता है; Kotlin 1.9 से `entries` ही अनुशंसित विकल्प है।

---

किसी `String` से वापस entry पाने के लिए, `valueOf` फ़ंक्शन का उपयोग करें। यह उस entry को खोजता है जिसका `name` बिल्कुल मेल खाता हो:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
यह मिलान case-sensitive होता है: `Direction.valueOf("east")` एक `IllegalArgumentException` throw करता है क्योंकि उस नाम की कोई entry मौजूद नहीं है।

---

एक enum class एक **abstract method** घोषित कर सकती है और हर entry को braces में लिपटे एक body में अपना खुद का implementation देने दे सकती है:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
हर entry एक ही प्रकार और मेथड सिग्नेचर साझा करते हुए भी अलग-अलग व्यवहार करती है।

---

एक **interface** बिना body के methods घोषित करता है; इसे implement करने वाले किसी भी type को उन्हें ज़रूर प्रदान करना होगा:
```kotlin
interface Greeter {
    fun greet(): String
}
```
enum classes interfaces को implement कर सकती हैं। आप कोलन के बाद interface की सूची देते हैं और हर implementation को `override` से चिह्नित करते हैं। enum की body के अंदर, वर्तमान entry `this` होती है और बाकी entries को क्लास के नाम के बिना संदर्भित किया जा सकता है:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
