Dart में, एक **सूची** (list) वस्तुओं का एक क्रमबद्ध संग्रह होती है। सूची बनाने का सबसे सरल तरीका `[]` लिटरल सिंटैक्स है:

```dart
List<int> numbers = [1, 2, 3];
```

आप `var` के साथ टाइप अनुमान का भी उपयोग कर सकते हैं:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

टाइप एनोटेशन `List<String>` Dart को बताती है कि सूची का प्रत्येक तत्व एक `String` होना चाहिए।

---

Dart में सूचियाँ **शून्य-इंडेक्स** (zero-indexed) होती हैं, यानी पहला तत्व इंडेक्स `0` पर, दूसरा इंडेक्स `1` पर, और इसी तरह आगे होता है।

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

इंडेक्स द्वारा किसी तत्व तक पहुँचना `list[index]` सिंटैक्स से किया जाता है।

---

`.add()` मेथड सूची के **अंत** में एक तत्व जोड़ता है:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

ध्यान दें कि `.add()` सूची को **स्थान पर** संशोधित करता है और `void` लौटाता है।

---

`.length` प्रॉपर्टी सूची में तत्वों की संख्या लौटाती है:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

एक खाली सूची की लंबाई `0` होती है:

```dart
var empty = [];
print(empty.length); // 0
```

---

`.contains()` मेथड जाँचता है कि किसी सूची में कोई दिया गया मान है या नहीं। यदि मिलता है तो `true` लौटाता है, अन्यथा `false`:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

यह लूप की आवश्यकता के बिना सदस्यता जाँच के लिए उपयोगी है।
