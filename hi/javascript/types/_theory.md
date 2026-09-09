JavaScript में हर मान का एक **टाइप** होता है। सात **प्रिमिटिव** टाइप होते हैं:
- किसी भी संख्या के लिए `number`, जैसे `42` या `3.14`
- टेक्स्ट के लिए `string`, जैसे `"Ana"`
- `true` और `false` के लिए `boolean`
- कभी दिए न गए मान के लिए `undefined`
- जानबूझकर खाली रखे गए मान के लिए `null`
- किसी भी आकार की पूर्ण संख्याओं के लिए `bigint`, जैसे `9007199254740993n`
- `Symbol()` से बनाए गए अद्वितीय पहचानकर्ताओं के लिए `symbol`

बाकी सब कुछ (ऐरे, फंक्शन, `{}` से बनाए गए ऑब्जेक्ट्स, डेट्स...) एक `object` होता है।
`typeof` ऑपरेटर आपको किसी मान का टाइप एक स्ट्रिंग के रूप में बताता है:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript **डायनामिकली टाइप्ड** है: एक वेरिएबल का अपना कोई टाइप नहीं होता, टाइप केवल उस मान का होता है जिसे वह इस समय रखे होता है। वही वेरिएबल अभी एक संख्या रख सकता है और बाद में एक स्ट्रिंग, और `typeof` मान के साथ बदलता रहता है:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
यह सुविधाजनक है, लेकिन इसका यह मतलब भी है कि एक फंक्शन अप्रत्याशित टाइप का मान प्राप्त कर सकता है, इसलिए `typeof` से जाँच करना एक सामान्य पहला कदम है। चूँकि `typeof` एक स्ट्रिंग लौटाता है, आप उसके परिणाम की तुलना एक स्ट्रिंग से करते हैं:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` के कुछ उत्तर ऐसे हैं जो लोगों को चौंका देते हैं।
फंक्शन्स को अपना अलग उत्तर मिलता है, `"function"`, भले ही वे ऑब्जेक्ट्स होते हैं:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
ऐरे को अपना अलग उत्तर **नहीं** मिलता: वे साधारण `"object"` होते हैं, बिल्कुल `{}` की तरह:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
और `typeof null` `"object"` है, एक ऐतिहासिक बग जो कभी ठीक नहीं किया गया। इसलिए `typeof` प्रिमिटिव्स और फंक्शन्स को अच्छी तरह पहचान लेता है, लेकिन यह ऐरे, ऑब्जेक्ट और `null` में अंतर नहीं कर सकता।

---

आप किसी मान को दूसरे टाइप में **स्पष्ट रूप से** बदल सकते हैं, टाइप को एक फंक्शन की तरह कॉल करके:
- `Number(value)` संख्या में बदलता है: `Number("42")` का परिणाम `42` है
- `String(value)` स्ट्रिंग में बदलता है: `String(42)` का परिणाम `"42"` है
- `Boolean(value)` बूलियन में बदलता है: `Boolean("")` का परिणाम `false` है

परिणाम एक बिल्कुल नया मान होता है; मूल मान नहीं बदलता:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
स्पष्ट रूप से बदलना आपके इरादे को साफ दिखाता है: जो कोई भी `Number(input)` पढ़ता है, उसे पता होता है कि `input` टेक्स्ट था।

---

`Number()` सख्त है: पूरी स्ट्रिंग एक संख्या होनी चाहिए, अन्यथा परिणाम `NaN` ("Not a Number") होता है:
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` और `parseFloat()` अधिक उदार होते हैं: वे स्ट्रिंग की शुरुआत से अंक पढ़ते हैं, शुरुआती स्पेस छोड़ देते हैं, और पहले ऐसे अक्षर पर रुक जाते हैं जो संख्या का हिस्सा नहीं है। `parseInt` केवल पूर्ण भाग रखता है:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
जब स्ट्रिंग किसी ऐसी चीज़ से शुरू नहीं होती जो एक संख्या की शुरुआत कर सके (एक वैकल्पिक चिह्न, फिर एक अंक), तो वे भी `NaN` लौटाते हैं:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` एकमात्र ऐसा मान है जो स्वयं के बराबर नहीं होता, इसलिए `x === NaN` हमेशा `false` होता है; इसे पकड़ने के लिए `Number.isNaN(x)` का उपयोग करें।

---

"क्या यह `NaN` है?" पूछने के दो तरीके हैं, और वे अलग-अलग सवालों के उत्तर देते हैं।
पुराना ग्लोबल `isNaN(value)` पहले `value` को संख्या में **बदलता** है, फिर जाँच करता है। इसलिए यह किसी भी ऐसी चीज़ के लिए `true` कहता है जो संख्या नहीं बन सकती, भले ही वह वास्तव में `NaN` न हो:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` बदलता **नहीं** है: यह केवल तब `true` होता है जब `value` वास्तव में संख्या `NaN` हो:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
`Number.isNaN` को प्राथमिकता दें, और यदि आप जानना चाहते हैं कि बदलाव असफल हुआ या नहीं, तो पहले बदलें।

---

JavaScript **अंतर्निहित रूप से** भी बदलाव करता है, और `+` ऑपरेटर वह जगह है जहाँ यह सबसे अधिक परेशान करता है। यदि कोई एक पक्ष स्ट्रिंग है, तो `+` **जोड़ता (concatenate करता)** है और दूसरे पक्ष को स्ट्रिंग में बदल दिया जाता है:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
हर दूसरा अंकगणितीय ऑपरेटर दोनों पक्षों को **संख्या** में बदल देता है:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
इसलिए टेक्स्ट से आने वाले मानों (यूज़र इनपुट, फ़ाइलें, URLs) को जोड़ने पर योग की जगह चुपचाप एक स्ट्रिंग बन सकती है। सुरक्षित रहने के लिए जोड़ने से पहले `Number()` से बदलें।

---

स्ट्रिंग को संख्या में बदलने का एक छोटा तरीका **यूनरी प्लस** है: किसी एक मान के आगे लगाया गया `+` उसे बिल्कुल वैसे ही बदल देता है जैसे `Number()` बदलता है:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
यह संक्षिप्त है, लेकिन जोड़ से उलझा लेने लायक भी है, इसलिए कई टीमें स्पष्ट `Number("5")` को प्राथमिकता देती हैं।

---

**लूज़** समानता `==` तुलना करने से पहले दोनों पक्षों को एक सामान्य टाइप में बदल देती है, ऐसे नियमों का पालन करते हुए जिन्हें याद रखना कठिन है:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
**स्ट्रिक्ट** समानता `===` कभी बदलाव नहीं करती: अलग-अलग टाइप के मान बस बराबर नहीं होते:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
डिफ़ॉल्ट रूप से `===` (और `!==`) का उपयोग करें। एकमात्र सामान्य अपवाद `value == null` है, जो `null` और `undefined` दोनों को एक साथ जाँचता है।

---

जब JavaScript को एक बूलियन की ज़रूरत होती है, उदाहरण के लिए एक `if` शर्त में या `Boolean(value)` में, तो वह मान को बदल देता है। केवल आठ मान `false` बनते हैं; उन्हें **falsy** कहा जाता है:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` और `NaN`।
**बाकी सब कुछ truthy है**, जिनमें कुछ ऐसे मान भी शामिल हैं जो खाली दिखते हैं:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` एक गैर-खाली स्ट्रिंग है, इसलिए वह truthy है; एक खाली ऐरे एक ऑब्जेक्ट है, इसलिए वह भी truthy है।

---

किसी भी मान को बूलियन में बदलने का एक सामान्य शॉर्टकट **डबल निगेशन** `!!` है: पहला `!` उसे बूलियन में बदलकर पलट देता है, दूसरा उसे वापस पलट देता है:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` और `Boolean(value)` बिल्कुल वही परिणाम देते हैं; स्पष्ट रूप पढ़ने में आसान होता है।

---

JavaScript में पूर्ण संख्याओं और दशमलव के लिए एक ही `number` टाइप होता है: हर संख्या एक 64-बिट फ्लोटिंग पॉइंट मान (एक *double*) होती है। इसलिए `5` और `5.0` एक ही मान हैं, और कोई अलग इंटीजर टाइप नहीं है:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
यह पता लगाने के लिए कि क्या संख्या का दशमलव भाग नहीं है, `Number.isInteger` का उपयोग करें:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
टेम्पलेट लिटरल्स इंटरपोलेट किए गए मान को `String()` के उन्हीं नियमों से स्ट्रिंग में बदलते हैं, इसलिए `${5.0}` `"5"` बनता है, `"5.0"` नहीं।

---

क्योंकि संख्याएँ double होती हैं, कुछ दशमलव सटीक रूप से संग्रहीत नहीं हो सकते और छोटी त्रुटियाँ दिखाई देने लगती हैं:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
`toFixed(digits)` मेथड एक संख्या को `digits` दशमलवों तक राउंड करता है, लेकिन वह एक **स्ट्रिंग** लौटाता है, जो प्रदर्शन के लिए ठीक है और आगे के गणित के लिए गलत:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
एक राउंड की हुई **संख्या** पाने के लिए, परिणाम को `Number()` से वापस बदलें:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

एक `number` पूर्ण संख्याओं को केवल `Number.MAX_SAFE_INTEGER` तक ही सटीक रूप से दर्शा सकता है, जो `9007199254740991` है। इससे आगे, अंक खो जाते हैं:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
बड़ी पूर्ण संख्याओं के लिए `bigint` का उपयोग करें: लिटरल को `n` प्रत्यय के साथ लिखें, या `BigInt()` से बदलें:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` `n` प्रत्यय दिखाता है; `String(big)` सादे अंक देता है।
एक `bigint` और एक `number` को अंकगणित में मिलाया नहीं जा सकता: `big + 1` एक `TypeError` फेंकता है। किसी एक पक्ष को स्पष्ट रूप से बदलें, `BigInt(count)` या `Number(big)` से।

---

चूँकि `typeof` ऐरे, ऑब्जेक्ट्स और `null` के लिए `"object"` उत्तर देता है, उनमें अंतर करने के लिए दो अतिरिक्त जाँचों की ज़रूरत होती है।
`Array.isArray(value)` केवल ऐरे के लिए `true` होता है:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
`null` के लिए सीधे तुलना करें, `value === null`। इन्हें मिलाकर किसी भी मान की पूरी तस्वीर मिल जाती है:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
पहले `null` और ऐरे की जाँच करें, क्योंकि सादा `typeof` उनमें अंतर नहीं कर सकता।

---

फॉर्म, फ़ाइलों या URLs से आने वाला टेक्स्ट हमेशा एक स्ट्रिंग होता है, भले ही वह एक संख्या या बूलियन दर्शाता हो। उसे वापस सही टाइप में बदलने में वह सब कुछ आता है जो आपने देखा है: बूलियन के लिए `"true"` और `"false"` से तुलना करें, और संख्याओं के लिए `Number()` आज़माएँ, यह याद रखते हुए कि `Number("")` `0` होता है और `Number.isNaN` आपको बताता है कि बदलाव कब असफल हुआ:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
जब कुछ भी मेल न खाए, तो स्ट्रिंग को वैसे ही रखें।
