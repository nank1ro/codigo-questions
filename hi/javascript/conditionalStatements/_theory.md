निर्णय लेने की आवश्यकता तब होती है जब हम केवल एक निश्चित शर्त पूरी होने पर ही कोड चलाना चाहते हैं।
मान लीजिए कि हम बाहर खेलना चाहते हैं केवल तभी जब मौसम अच्छा हो।
प्रोग्रामिंग में, हम एक बूलियन वेरिएबल `niceWeather` सेव कर सकते हैं और `if` यह वेरिएबल `true` है तो बाहर खेलने की क्रिया कर सकते हैं, जैसे:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

आइए पिछले उदाहरण को जारी रखें।
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```
हमने देखा कि `if` स्टेटमेंट कोड ब्लॉक को केवल तभी चलाता है जब शर्त `true` हो।
एक और महत्वपूर्ण बात **कर्ली ब्रैकेट्स** `{}` हैं जो एक कोड ब्लॉक को दर्शाते हैं।

---

हमने अभी देखा कि किसी शर्त के पूरा होने पर कोड ब्लॉक कैसे चलाया जाता है, अब देखते हैं कि पहली शर्त विफल होने पर दूसरा कोड ब्लॉक कैसे चलाया जाता है।
अगर मौसम अच्छा है तो हम बाहर खेलने जाते हैं; अन्यथा, हम घर पर रहते हैं।
JavaScript में हम `else` स्टेटमेंट का उपयोग कर सकते हैं, जैसे:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

मान लीजिए कि हमें एक और शर्त जांचनी है, जैसे इस उदाहरण में:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
और इस कोड का आउटपुट `the number is 3` है।
सबसे पहले, जांचते हैं कि संख्या 2 के बराबर है या नहीं, यह गलत है।
तो दूसरे स्टेटमेंट पर चलते हैं और जांचते हैं कि `num` 3 के बराबर है, यह सही होने पर हम `the number is 3` प्रिंट करके अगले कोड ब्लॉक को चलाते हैं

---

हम जितने चाहें उतने `else if` स्टेटमेंट जोड़ सकते हैं, इसकी कोई सीमा नहीं है
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
और इस कोड का आउटपुट `the number is 4` है।

---

हम एक सशर्त स्टेटमेंट (`if`, `else if` या `else`) को दूसरे सशर्त स्टेटमेंट के अंदर नेस्ट भी कर सकते हैं, एक अधिक जटिल संरचना बनाने के लिए।
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
और इस कोड का आउटपुट `the number is 4` है।

---

टर्नरी कंडीशनल ऑपरेटर तीन भागों वाला एक विशेष ऑपरेटर है, जो `question ? answer1 : answer2` के रूप में होता है।
यह `question` के सही या गलत होने के आधार पर दो अभिव्यक्तियों में से एक का मूल्यांकन करने का शॉर्टकट है।
यदि `question` सही है, तो यह `answer1` का मूल्यांकन करता है और उसका मान लौटाता है; अन्यथा, यह `answer2` का मूल्यांकन करता है और उसका मान लौटाता है।
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// prints 10
```
उपरोक्त कोड का शॉर्टहैंड कोड है:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
```
`c` को `a` के बराबर सेट किया गया है, क्योंकि शर्त `a < b` सही थी

---

_nil-coalescing ऑपरेटर_ `a ?? b` एक ऑप्शनल `a` को अनरैप करता है यदि उसमें कोई मान है, या `a` के `nil` होने पर डिफ़ॉल्ट मान `b` लौटाता है।
अभिव्यक्ति `a` हमेशा ऑप्शनल टाइप की होती है।
अभिव्यक्ति `b` का टाइप वही होना चाहिए जो a के अंदर संग्रहीत है।
nil-coalescing ऑपरेटर नीचे दिए गए कोड का शॉर्टहैंड है:
```javascript
a != nil ? a! : b;
```
