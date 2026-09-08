**स्ट्रिंग** उद्धरण चिह्नों में लिपटे वर्णों का एक क्रम है, जैसे `"hello"` या `'hello'`।
हर स्ट्रिंग में एक `length` प्रॉपर्टी होती है जो बताती है कि उसमें कितने वर्ण हैं:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
स्पेस और विराम चिह्न भी वर्णों के रूप में गिने जाते हैं।

---

स्ट्रिंग में हर वर्ण का एक **इंडेक्स** होता है, जो `0` से शुरू होता है।
आप स्क्वायर ब्रैकेट या `charAt()` मेथड से एक भी वर्ण पढ़ सकते हैं:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
आखिरी वर्ण इंडेक्स `length - 1` पर होता है:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

स्ट्रिंग्स में कई बिल्ट-इन **मेथड** आते हैं। इनमें से दो सबसे सरल मेथड हर अक्षर का केस बदल देते हैं:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
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
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
तुलना केस-सेंसिटिव होती है: `"Hello".includes("h")` `false` है।

---

`indexOf()` मेथड वह इंडेक्स लौटाता है जहाँ कोई टेक्स्ट स्ट्रिंग में **पहली बार** दिखाई देता है।
अगर टेक्स्ट नहीं मिलता, तो यह `-1` लौटाता है:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

`slice(start, end)` मेथड इंडेक्स `start` से इंडेक्स `end` से ठीक पहले तक (`end` को शामिल किए बिना) स्ट्रिंग का एक हिस्सा निकालता है:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
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
// prints 45
```
