एक **सेट** **यूनीक** वैल्यू का एक कलेक्शन है: हर वैल्यू अधिकतम एक बार आ सकती है, और पोज़िशन से वैल्यू तक पहुँचने के लिए कोई इंडेक्स नहीं होता।
सेट तब उपयोगी होते हैं जब आपको सिर्फ इस बात की परवाह हो कि *कौन सी* वैल्यू मौजूद हैं, न कि वे कितनी बार या किस क्रम में हैं।
आप `new Set()` से एक खाली सेट बनाते हैं, `add(value)` से एक वैल्यू जोड़ते हैं और `has(value)` से जांचते हैं कि कोई वैल्यू मौजूद है या नहीं:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
```

---

पहले से सेट में मौजूद वैल्यू को जोड़ने पर **कुछ नहीं** होता: डुप्लिकेट को बस नज़रअंदाज़ कर दिया जाता है।
दो और ज़रूरी बातें:
- `delete(value)` सेट से वैल्यू हटाता है
- `size` संग्रहीत वैल्यू की संख्या है (यह एक प्रॉपर्टी है, इसलिए कोष्ठक नहीं लगते)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
```

---

`add()` सेट को खुद ही रिटर्न करता है, इसलिए कई कॉल को चेन किया जा सकता है:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
चेन करें या न करें, पहले से मौजूद वैल्यू दूसरी बार कभी नहीं जोड़ी जाती, इसलिए `size` हर अलग वैल्यू को केवल एक बार गिनता है।

---

आप एक ऐरे को `new Set()` में पास करके एक ही बार में एक सेट बना सकते हैं। ऐरे में मौजूद डुप्लिकेट हटा दिए जाते हैं, इसलिए यह किसी ऐरे की अलग-अलग वैल्यू पता करने का सबसे तेज़ तरीका है:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// prints 3
```
**स्प्रेड** ऑपरेटर `...` इसके उल्टा काम करता है और सेट को वापस ऐरे में बदल देता है:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` भी वही काम करता है।

---

सेट यह याद रखता है कि वैल्यू किस क्रम में जोड़ी गई थीं, और आप इसे `for...of` से लूप कर सकते हैं:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
सेट में हर वैल्यू के लिए एक फ़ंक्शन कॉल करने वाला `forEach()` मेथड भी होता है:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
