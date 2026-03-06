---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 दरवाज़े
---

# --description--

एक पंक्ति में 100 दरवाज़े हैं जो सभी शुरू में बंद हैं।
आप दरवाज़ों से 100 बार गुज़रते हैं।
पहली बार, हर दरवाज़े पर जाएं और दरवाज़े को 'टॉगल' करें (यदि दरवाज़ा बंद है, तो उसे खोलें; यदि वह खुला है, तो उसे बंद करें)।
दूसरी बार, केवल हर दूसरे दरवाज़े पर जाएं (यानी, दरवाज़ा #2, #4, #6, ...) और उसे टॉगल करें।
तीसरी बार, हर तीसरे दरवाज़े पर जाएं (यानी, दरवाज़ा #3, #6, #9, ...), आदि, जब तक आप केवल 100वें दरवाज़े पर नहीं पहुँच जाते।

# --instructions--

अंतिम पास के बाद दरवाज़ों की स्थिति निर्धारित करने के लिए एक फ़ंक्शन लागू करें।
अंतिम परिणाम एक ऐरे में लौटाएं, जिसमें केवल उस दरवाज़े का नंबर शामिल हो जो खुला है।
> यह विधि दरवाज़ों की परिवर्तनीय संख्या के साथ काम करने में सक्षम होनी चाहिए।

# --seed--

```kotlin
fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    
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

100 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

10 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

950 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```kotlin
    val solution3 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900)
    tryCatch(getFinalOpenedDoors(950) == solution3)
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
fun square(num: Int): Int {
    return Math.pow(num.toDouble(), 2.0).toInt()
}

fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    val openDoors = ArrayList<Int>()
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.add(square(i))
        i += 1
    }
    return openDoors
}
```
