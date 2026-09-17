**स्ट्रिंग** उद्धरण चिह्नों में लिपटे वर्णों का एक क्रम है, जैसे `"hello"` या `'hello'`।
हर स्ट्रिंग में एक `length` प्रॉपर्टी होती है जो बताती है कि उसमें कितने वर्ण हैं:
```javascript
let greeting = "hello";
console.log(greeting.length);
// 5 प्रिंट करता है
```
स्पेस और विराम चिह्न भी वर्णों के रूप में गिने जाते हैं।

---

स्ट्रिंग में हर वर्ण का एक **इंडेक्स** होता है, जो `0` से शुरू होता है।
आप स्क्वायर ब्रैकेट या `charAt()` मेथड से एक भी वर्ण पढ़ सकते हैं:
```javascript
let word = "hello";
console.log(word[0]);
// h प्रिंट करता है
console.log(word.charAt(1));
// e प्रिंट करता है
```
आखिरी वर्ण इंडेक्स `length - 1` पर होता है:
```javascript
console.log(word[word.length - 1]);
// o प्रिंट करता है
```

---

स्ट्रिंग्स में कई बिल्ट-इन **मेथड** आते हैं। इनमें से दो सबसे सरल मेथड हर अक्षर का केस बदल देते हैं:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// HELLO प्रिंट करता है
console.log(word.toLowerCase());
// hello प्रिंट करता है
```
दोनों मेथड कोई आर्गुमेंट नहीं लेते, इसलिए कोष्ठक लगाना न भूलें।

---

यह जाँचने के लिए कि कोई स्ट्रिंग दूसरी स्ट्रिंग को शामिल करती है या नहीं, इन मेथड का उपयोग करें, जो सभी एक बूलियन लौटाते हैं:
- `includes(text)` `true` होता है अगर `text` कहीं भी मौजूद हो
- `startsWith(text)` `true` होता है अगर स्ट्रिंग `text` से शुरू होती हो
- `endsWith(text)` `true` होता है अगर स्ट्रिंग `text` पर समाप्त होती हो

```javascript
let file = "photo.png";
console.log(file.includes("."));
// true प्रिंट करता है
console.log(file.startsWith("ph"));
// true प्रिंट करता है
console.log(file.endsWith(".jpg"));
// false प्रिंट करता है
```
तुलना केस-सेंसिटिव होती है: `"Hello".includes("h")` `false` है।

---

`indexOf()` मेथड वह इंडेक्स लौटाता है जहाँ कोई टेक्स्ट स्ट्रिंग में **पहली बार** दिखाई देता है।
अगर टेक्स्ट नहीं मिलता, तो यह `-1` लौटाता है:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// 2 प्रिंट करता है
console.log(word.indexOf("z"));
// -1 प्रिंट करता है
```

---

`slice(start, end)` मेथड इंडेक्स `start` से इंडेक्स `end` से ठीक पहले तक (`end` को शामिल किए बिना) स्ट्रिंग का एक हिस्सा निकालता है:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// Java प्रिंट करता है
console.log(word.slice(4));
// Script प्रिंट करता है
```
अगर आप `end` छोड़ देते हैं, तो स्लाइस स्ट्रिंग के अंत तक जाती है।
एक ऋणात्मक इंडेक्स अंत से गिना जाता है: `word.slice(-3)` `"ipt"` है।
`substring(start, end)` मेथड भी उसी तरह काम करता है, लेकिन यह ऋणात्मक इंडेक्स स्वीकार नहीं करता।

---

`indexOf()` और `slice()` एक साथ अच्छी तरह काम करते हैं: पहले पता करें कि कोई चीज़ कहाँ है, फिर वहाँ से स्ट्रिंग काटें।
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// 45 प्रिंट करता है
```

---

`split(separator)` मेथड हर `separator` पर काटकर एक स्ट्रिंग को टुकड़ों की एक **ऐरे** में तोड़ता है:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// [ 'I', 'like', 'JavaScript' ] प्रिंट करता है
```
इसका उल्टा ऐरे मेथड `join(separator)` है, जो टुकड़ों को वापस एक स्ट्रिंग में जोड़ देता है:
```javascript
console.log(words.join("-"));
// I-like-JavaScript प्रिंट करता है
```

---

यूज़र इनपुट में अक्सर आगे-पीछे अतिरिक्त स्पेस होते हैं। `trim()` मेथड स्ट्रिंग की एक कॉपी लौटाता है जिसमें **दोनों** सिरों से व्हाइटस्पेस हटा दिया गया हो:
```javascript
let input = "   hello   ";
console.log(input.trim());
// hello प्रिंट करता है
```
`trimStart()` केवल शुरुआती व्हाइटस्पेस हटाता है और `trimEnd()` केवल आखिरी व्हाइटस्पेस।
स्ट्रिंग के बीच में मौजूद स्पेस कभी नहीं बदले जाते।

---

`replace(search, replacement)` मेथड एक नई स्ट्रिंग लौटाता है जिसमें `search` की **पहली** मौजूदगी को `replacement` से बदल दिया जाता है:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// blue red प्रिंट करता है
```
**हर** मौजूदगी को बदलने के लिए `replaceAll()` का उपयोग करें:
```javascript
console.log(text.replaceAll("red", "blue"));
// blue blue प्रिंट करता है
```

---

`repeat(count)` मेथड स्ट्रिंग को `count` बार दोहराकर लौटाता है:
```javascript
console.log("ab".repeat(3));
// ababab प्रिंट करता है
console.log("ab".repeat(0));
// an empty string प्रिंट करता है
```

---

`padStart(targetLength, padString)` मेथड स्ट्रिंग के `targetLength` वर्णों तक पहुँचने तक उसके **शुरुआत** में `padString` जोड़ता है। `padEnd()` अंत में भी वही काम करता है:
```javascript
console.log("7".padStart(3, "0"));
// 007 प्रिंट करता है
console.log("Tea".padEnd(6, "."));
// Tea... प्रिंट करता है
```
अगर स्ट्रिंग पहले से ही पर्याप्त लंबी है, तो वह बिना बदले लौटा दी जाती है।
संख्याओं में स्ट्रिंग मेथड नहीं होते, इसलिए पहले उन्हें `String(number)` से बदलें।

---

दो स्ट्रिंग्स `===` से तभी बराबर होती हैं जब उनमें बिल्कुल एक जैसे वर्ण, एक जैसे केस में हों:
```javascript
console.log("hello" === "hello");
// true प्रिंट करता है
console.log("hello" === "Hello");
// false प्रिंट करता है
```
`<` और `>` ऑपरेटर स्ट्रिंग्स की तुलना वर्णानुक्रम में, वर्ण दर वर्ण करते हैं।
अपरकेस अक्षर लोअरकेस अक्षरों से पहले आते हैं, इसलिए `"Zoo" < "apple"` `true` है।

---

स्ट्रिंग्स **इम्यूटेबल** होती हैं: एक बार बन जाने के बाद, एक स्ट्रिंग को कभी बदला नहीं जा सकता।
किसी इंडेक्स पर वैल्यू असाइन करने से कुछ नहीं होता, और हर स्ट्रिंग मेथड मूल स्ट्रिंग को बदलने के बजाय एक **नई** स्ट्रिंग लौटाता है:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// hello प्रिंट करता है
word.toUpperCase();
console.log(word);
// hello प्रिंट करता है
```
परिणाम को बनाए रखने के लिए, इसे वापस वेरिएबल में असाइन करें:
```javascript
word = word.toUpperCase();
```

---

खाली सेपरेटर के साथ `split("")` को कॉल करने पर एक स्ट्रिंग उसके अलग-अलग वर्णों की ऐरे में बदल जाती है।
ऐरे में `reverse()` मेथड होता है, इसलिए आप विभाजित करके, उलटकर और फिर जोड़कर किसी स्ट्रिंग को उलट सकते हैं:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// cba प्रिंट करता है
```
