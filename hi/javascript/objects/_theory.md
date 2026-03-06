**Objects** arrays के समान होते हैं, लेकिन आप index के बजाय *key* का उपयोग करके values तक पहुँचते हैं।
key कोई भी string या number हो सकती है।
Objects को curly brackets में रखा जाता है, इस प्रकार:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
यह `objectName` नामक एक dictionary है जिसमें तीन *key-value pairs* हैं।
key `key1` value `1` की ओर इंगित करती है, `key2` `2` की ओर, और इसी तरह आगे।

---

key द्वारा dictionary values तक पहुँचना बिल्कुल वैसा ही है जैसे index द्वारा array values तक पहुँचना:
```javascript
// user dictionary से age value प्राप्त करता है
user['age'];
```

---

Arrays की तरह, Dictionaries _mutable_ होती हैं।
इसका मतलब है कि उन्हें बनाने के बाद बदला जा सकता है (यदि उन्हें constant घोषित नहीं किया गया है)।
इसका एक फायदा यह है कि हम dictionary बनने के बाद उसमें नए _key/value pairs_ जोड़ सकते हैं, इस प्रकार:
```javascript
dictName[newKeyName] = newValue;
```

---

चूंकि dictionaries variables mutable होते हैं, उन्हें कई तरीकों से बदला जा सकता है।
'delete' keyword के साथ dictionary से items हटाए जा सकते हैं:
```javascript
delete dictName[keyName];
```
यह dictionary से key `keyName` और उसकी संबंधित value को हटा देगा।

---

क्या होगा अगर हम dictionary की सभी keys की सूची बनाना चाहते हैं?
तो, इसके लिए `Object.keys()` method है।

---

क्या होगा अगर हम dictionary की सभी values की सूची बनाना चाहते हैं?
तो, इसके लिए `Object.values()` method है।

---

Arrays की तरह, हम `Object.entries()` method का उपयोग करके dictionary elements के बीच loop कर सकते हैं।
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
