एक **मैप** **की-वैल्यू जोड़े** संग्रहीत करता है: हर वैल्यू एक की के अंतर्गत सेव होती है, और आप उस की का उपयोग करके वैल्यू को फिर से खोज सकते हैं।
आप `new Map()` से एक खाली मैप बनाते हैं, `set(key, value)` से एक जोड़ा जोड़ते हैं और `get(key)` से एक वैल्यू पढ़ते हैं:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// 30 प्रिंट करता है
```
पहले से मौजूद की के साथ `set()` को कॉल करने पर उसकी वैल्यू बदल जाती है।

---

मैप में कुछ और आवश्यक मेथड और प्रॉपर्टीज़ होती हैं:
- `has(key)` `true` लौटाता है यदि की मौजूद है
- `delete(key)` उस की वाले जोड़े को हटा देता है
- `size` संग्रहीत जोड़ों की संख्या है

```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
console.log(stock.has("apple"));
// true प्रिंट करता है
stock.delete("pear");
console.log(stock.size);
// 1 प्रिंट करता है
```
ध्यान दें कि `size` एक प्रॉपर्टी है, मेथड नहीं, इसलिए इसमें कोष्ठक नहीं होते।

---

मैप से ऐसी की माँगना जो उसमें मौजूद नहीं है, कोई त्रुटि नहीं है: `get()` बस `undefined` लौटाता है।
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// undefined प्रिंट करता है
```
इसीलिए `has()` मौजूद है: यह किसी अनुपस्थित की और ऐसी की के बीच अंतर बताता है जिसकी वैल्यू संयोगवश `undefined` है।
`set()` मैप को ही लौटाता है, इसलिए कॉल्स को चेन किया जा सकता है:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

एक साधारण ऑब्जेक्ट में हर की को स्ट्रिंग में बदल दिया जाता है: `user[1]` और `user["1"]` एक ही की हैं।
मैप अपनी कीज़ का **टाइप** बनाए रखता है, इसलिए एक number, एक string, एक boolean, या यहाँ तक कि एक object भी अलग-अलग की बन सकते हैं:
```javascript
let lookup = new Map();
lookup.set(1, "number one");
lookup.set("1", "string one");
console.log(lookup.size);
// 2 प्रिंट करता है
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// an object key प्रिंट करता है
```
ऑब्जेक्ट कीज़ की तुलना पहचान (identity) से होती है: केवल वही ऑब्जेक्ट वापस वैल्यू पा सकता है।

---

एक मैप उस क्रम को याद रखता है जिसमें जोड़े जोड़े गए थे, और आप इसे `for...of` से लूप कर सकते हैं।
`entries()` मेथड हर जोड़े को `[key, value]` ऐरे के रूप में देता है, जिसे आप लूप के अंदर ही अनपैक कर सकते हैं:
```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
for (const [name, qty] of stock.entries()) {
  console.log(`${name}: ${qty}`);
}
// apple: 3 प्रिंट करता है
// pear: 5 प्रिंट करता है
```
मैप पर सीधे लूप करना, `for (const [name, qty] of stock)`, बिल्कुल वही काम करता है।

---

जब आपको जोड़े के केवल एक पक्ष की आवश्यकता हो, तो `entries()` की जगह लूप में `keys()` या `values()` का उपयोग करें:
```javascript
let prices = new Map();
prices.set("tea", 2);
prices.set("cake", 4);
for (const name of prices.keys()) {
  console.log(name);
}
// tea प्रिंट करता है
// cake प्रिंट करता है
for (const price of prices.values()) {
  console.log(price);
}
// 2 प्रिंट करता है
// 4 प्रिंट करता है
```

---

`set()` को कई बार कॉल करने के बजाय, आप **जोड़ों के ऐरे** को `new Map()` में पास करके एक ही बार में मैप बना सकते हैं:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// 2 प्रिंट करता है
```
चूँकि `Object.entries(obj)` ठीक ऐसा ही जोड़ों का ऐरे लौटाता है, यह किसी ऑब्जेक्ट को मैप में बदलने का सबसे तेज़ तरीका है:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// 30 प्रिंट करता है
```

---

मैप और साधारण ऑब्जेक्ट दोनों ही कीज़ के अंतर्गत वैल्यूज़ संग्रहीत करते हैं, लेकिन इनमें कुछ महत्वपूर्ण अंतर होते हैं:
- ऑब्जेक्ट की कीज़ हमेशा स्ट्रिंग (या symbol) होती हैं, मैप की कीज़ **किसी भी** टाइप की हो सकती हैं
- एक मैप अपनी पेयर्स का सटीक **सम्मिलन क्रम (insertion order)** याद रखता है
- मैप को अपना `size` पता होता है, जबकि किसी ऑब्जेक्ट के लिए आपको `Object.keys(obj).length` की ज़रूरत होती है
- एक मैप वाकई खाली शुरू होता है, जबकि एक ऑब्जेक्ट को अपने prototype से `toString` जैसी कीज़ विरासत में मिलती हैं

---

मैप में `sort()` या `filter()` जैसे ऐरे मेथड नहीं होते। इन्हें उपयोग करने के लिए, मैप (या इसकी कीज़ या वैल्यूज़) को `Array.from()` या स्प्रेड ऑपरेटर `...` से ऐरे में बदलें:
```javascript
let ages = new Map([["Bob", 25], ["Ann", 30]]);
let pairs = Array.from(ages);
console.log(pairs);
// [ [ 'Bob', 25 ], [ 'Ann', 30 ] ] प्रिंट करता है
let names = [...ages.keys()];
console.log(names);
// [ 'Bob', 'Ann' ] प्रिंट करता है
let values = [...ages.values()];
console.log(values);
// [ 25, 30 ] प्रिंट करता है
```
उल्टा रूपांतरण, `Object.fromEntries(ages)`, मैप को वापस एक साधारण ऑब्जेक्ट में बदल देता है।

---

ऐरे की तरह, मैप में भी `forEach()` मेथड होती है जो हर जोड़े के लिए एक फ़ंक्शन को कॉल करती है।
पैरामीटर्स के क्रम का ध्यान रखें: कॉलबैक को पहले **वैल्यू** मिलती है, फिर की:
```javascript
let stock = new Map([["apple", 3], ["pear", 5]]);
stock.forEach((qty, name) => {
  console.log(`${name} x${qty}`);
});
// apple x3 प्रिंट करता है
// pear x5 प्रिंट करता है
```

---

`delete(key)` `true` लौटाता है जब कोई जोड़ा हटाया गया हो, और `false` जब वह की मौजूद नहीं थी।
एक ही बार में **सभी** जोड़ों को हटाने के लिए, `clear()` को कॉल करें:
```javascript
let cart = new Map([["pen", 2], ["ink", 1]]);
console.log(cart.delete("pen"));
// true प्रिंट करता है
console.log(cart.delete("pen"));
// false प्रिंट करता है
cart.clear();
console.log(cart.size);
// 0 प्रिंट करता है
```

---

तो एक साधारण ऑब्जेक्ट के बजाय `Map` का उपयोग कब करना चाहिए?
- **Map** का उपयोग करें जब कीज़ रनटाइम पर जोड़ी और हटाई जाती हों, जब वे स्ट्रिंग न हों, या जब आपको `size` और भरोसेमंद क्रम चाहिए
- एक **object** का उपयोग करें ज्ञात फ़ील्ड नामों वाले निश्चित रिकॉर्ड के लिए, जैसे `{ name, email }`, और जब भी आपको डेटा को JSON में बदलना हो, क्योंकि `JSON.stringify()` किसी मैप की सामग्री को अनदेखा कर देता है
