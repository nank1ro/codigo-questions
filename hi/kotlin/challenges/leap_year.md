---
language: kotlin
exerciseType: 1
difficulty: 3
title: लीप वर्ष
---

# --description--

एक कैलेंडर वर्ष में ठीक 365.25 दिन होते हैं। लेकिन, अंततः, इससे भ्रम पैदा होगा क्योंकि मनुष्य सामान्यतः 1 की सटीक विभाज्यता से गिनते हैं, दशमलव बिंदुओं से नहीं। इसलिए, इससे बचने के लिए, यह निर्णय लिया गया कि हर चार वर्ष के चक्र में सभी 0.25 दिनों को जोड़ दिया जाए और उस वर्ष को 366 दिन दिए जाएं (29 फरवरी को अधिवर्ष दिवस के रूप में शामिल करते हुए) और इसे __लीप वर्ष__ कहा जाए। चार वर्ष के चक्र में अन्य तीन वर्षों में केवल 365 दिन होंगे और वे __लीप वर्ष नहीं होंगे__।

# --instructions--

इस चुनौती में हम इसे एक नए स्तर पर ले जाएंगे, जहाँ आपको `Date` क्लास, `switch` स्टेटमेंट, __if ब्लॉक__, __if-else ब्लॉक__ या __टर्नरी ऑपरेशन__ (`x ? a : b`) और न ही तार्किक ऑपरेटर __AND__ (`&&`) और __OR__ (`||`) का उपयोग किए बिना यह निर्धारित करना है कि यह लीप वर्ष है या नहीं, __NOT__ (`!`) ऑपरेटर की छूट के साथ।

यदि यह लीप वर्ष है तो `true` लौटाएं, अन्यथा `false`।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(leapYear(2000))
// prints true
```

# --seed--

```kotlin
fun leapYear(year: Int): Boolean {
    
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

`Date`, `switch`, `if`, `else`, `&&`, `||` या `?` का उपयोग अनुमति नहीं है।

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

वर्ष `2016` एक लीप वर्ष है।

```kotlin
    tryCatch(leapYear(2016) == true)
```

वर्ष `1996` एक लीप वर्ष है।

```kotlin
    tryCatch(leapYear(1996) == true)
```

वर्ष `1600` एक लीप वर्ष है।

```kotlin
    tryCatch(leapYear(1600) == true)
```

वर्ष `2020` एक लीप वर्ष है।

```kotlin
    tryCatch(leapYear(2020) == true)
```

वर्ष `2000` एक लीप वर्ष है।

```kotlin
    tryCatch(leapYear(2000) == true)
```

वर्ष `2008` एक लीप वर्ष है।

```kotlin
    tryCatch(leapYear(2008) == true)
```

वर्ष `1521` लीप वर्ष नहीं है।

```kotlin
    tryCatch(leapYear(1521) == false)
```

वर्ष `1800` लीप वर्ष नहीं है।

```kotlin
    tryCatch(leapYear(1800) == false)
```

वर्ष `2007` लीप वर्ष नहीं है।

```kotlin
    tryCatch(leapYear(2007) == false)
```

वर्ष `2002` लीप वर्ष नहीं है।

```kotlin
    tryCatch(leapYear(2002) == false)
```

वर्ष `1979` लीप वर्ष नहीं है।

```kotlin
    tryCatch(leapYear(1979) == false)
```

वर्ष `2006` लीप वर्ष नहीं है।

```kotlin
    tryCatch(leapYear(2006) == false)
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
fun leapYear(year: Int): Boolean {
  var tempYear = year
  while (tempYear % 100 == 0) {
    tempYear = tempYear / 100
  }
  return tempYear % 4 == 0
}
```
