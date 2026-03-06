आपने ऐसी स्थिति पर विचार किया होगा जहाँ आप कोड के एक टुकड़े को दोबारा उपयोग करना चाहते हैं, बस कुछ अलग मानों के साथ।
पूरा कोड दोबारा लिखने के बजाय, एक function परिभाषित करना बहुत बेहतर है, जिसे बार-बार उपयोग किया जा सकता है।
JavaScript में हम `function` कीवर्ड का उपयोग करते हैं जिसके बाद function का नाम आता है:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

__function definition__ में कोष्ठक खाली नहीं होने चाहिए अगर हम parameters निर्दिष्ट करना चाहते हैं

---

कभी-कभी हम चाहते हैं कि function एक मान __return__ करे।
इसके लिए `return` कीवर्ड है।

---

Functions में कई input parameters हो सकते हैं, जो function के कोष्ठकों के अंदर अल्पविराम से अलग करके लिखे जाते हैं।
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

आप किसी function में किसी भी parameter के लिए _default_ मान परिभाषित कर सकते हैं, parameter के प्रकार के बाद उसे एक मान assign करके।
अगर default मान परिभाषित है, तो आप function को कॉल करते समय उस parameter को छोड़ सकते हैं
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

__rest parameter__ सिंटैक्स हमें अनिश्चित संख्या में arguments को एक array के रूप में दर्शाने की अनुमति देता है।
parameter के नाम से पहले तीन बिंदु अक्षर `...` डालकर rest parameters लिखें।
rest parameter को पास किए गए मान function के body के अंदर एक array के रूप में उपलब्ध होते हैं।
उदाहरण के लिए, `numbers` नाम वाला rest parameter, function के body के अंदर numbers नामक एक constant array के रूप में उपलब्ध होता है

---

Functions में हम एक _वैकल्पिक टिप्पणी_ जोड़ सकते हैं जो बताती है कि function क्या करता है:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
हम एक पंक्ति की टिप्पणी के लिए `//` और बहु-पंक्ति टिप्पणी के लिए `/** */` का उपयोग कर सकते हैं
