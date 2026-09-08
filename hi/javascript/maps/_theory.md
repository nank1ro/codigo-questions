एक **मैप** **की-वैल्यू जोड़े** संग्रहीत करता है: हर वैल्यू एक की के अंतर्गत सेव होती है, और आप उस की का उपयोग करके वैल्यू को फिर से खोज सकते हैं।
आप `new Map()` से एक खाली मैप बनाते हैं, `set(key, value)` से एक जोड़ा जोड़ते हैं और `get(key)` से एक वैल्यू पढ़ते हैं:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
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
// prints true
stock.delete("pear");
console.log(stock.size);
// prints 1
```
ध्यान दें कि `size` एक प्रॉपर्टी है, मेथड नहीं, इसलिए इसमें कोष्ठक नहीं होते।

---

मैप से ऐसी की माँगना जो उसमें मौजूद नहीं है, कोई त्रुटि नहीं है: `get()` बस `undefined` लौटाता है।
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
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
// prints 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// prints an object key
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
// prints apple: 3
// prints pear: 5
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
// prints tea
// prints cake
for (const price of prices.values()) {
  console.log(price);
}
// prints 2
// prints 4
```

---

`set()` को कई बार कॉल करने के बजाय, आप **जोड़ों के ऐरे** को `new Map()` में पास करके एक ही बार में मैप बना सकते हैं:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
चूँकि `Object.entries(obj)` ठीक ऐसा ही जोड़ों का ऐरे लौटाता है, यह किसी ऑब्जेक्ट को मैप में बदलने का सबसे तेज़ तरीका है:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
