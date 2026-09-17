एक **एनम** (या *enum*) संबंधित, निश्चित मानों के एक छोटे समूह के लिए एक सामान्य प्रकार है: सप्ताह के दिन, ताश के पत्तों के सूट, किसी ऑर्डर की संभावित स्थितियाँ।
कई अन्य भाषाओं के विपरीत, JavaScript में `enum` कीवर्ड **नहीं** है। इसका पारंपरिक विकल्प एक साधारण ऑब्जेक्ट है जिसके प्रॉपर्टीज़ सदस्य होते हैं, जिसे `Object.freeze()` को पास किया जाता है ताकि बाद में कोई भी उसे बदल न सके:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// red प्रिंट करता है
```
परंपरा के अनुसार यह ऑब्जेक्ट `const` से डिक्लेयर किया जाता है, इसका नाम बड़े अक्षर से शुरू होता है, और सदस्यों के नाम अन्य कॉन्स्टेंट की तरह ही `UPPER_CASE` में लिखे जाते हैं।

---

हर सदस्य में कौन-सा मान स्टोर करना है, यह आप पर निर्भर है। **स्ट्रिंग्स** सबसे आम विकल्प हैं क्योंकि प्रिंट, लॉग या फ़ाइल में सेव करने पर ये पढ़ने में आसान होती हैं:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// done प्रिंट करता है
```
एक बार फ़्रीज़ हो जाने पर ऑब्जेक्ट को नई प्रॉपर्टीज़ भी नहीं मिल सकतीं, और `Object.isFrozen(obj)` बताता है कि कोई ऑब्जेक्ट फ़्रीज़ किया गया है या नहीं:
```javascript
console.log(Object.isFrozen(Status));
// true प्रिंट करता है
```

---

ऑब्जेक्ट को फ़्रीज़ ही क्यों करें? एक फ़्रीज़ किया गया ऑब्जेक्ट हर बदलाव को अस्वीकार कर देता है: किसी मौजूदा सदस्य को मान असाइन करना, नया सदस्य जोड़ना या किसी को हटाना, इनमें से किसी का भी कोई असर नहीं होता।
यह अस्वीकृति कैसे दिखती है, यह इस बात पर निर्भर करता है कि आपका कोड किस मोड में चल रहा है:
- **स्लॉपी मोड** (सादे स्क्रिप्ट्स के लिए डिफ़ॉल्ट) में असाइनमेंट को **चुपचाप नज़रअंदाज़** कर दिया जाता है
- **स्ट्रिक्ट मोड** (`"use strict"` से शुरू होने वाली फ़ाइलें, ES मॉड्यूल और क्लास बॉडी) में यह `TypeError` **थ्रो** करता है

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// s प्रिंट करता है
console.log(Size.MEDIUM);
// undefined प्रिंट करता है
```
दोनों ही स्थितियों में एनम आपके द्वारा परिभाषित मानों को बनाए रखता है, जो कि कॉन्स्टेंट के एक समूह से बिल्कुल यही अपेक्षित होता है।

---

सदस्य **नंबर** भी रख सकते हैं। संख्यात्मक मान तब उपयोगी होते हैं जब सदस्यों के बीच एक स्वाभाविक क्रम होता है, क्योंकि आप उन्हें सामान्य ऑपरेटरों से तुलना कर सकते हैं:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// true प्रिंट करता है
```
इसकी कीमत पठनीयता है: `Priority.HIGH` प्रिंट करने पर `3` दिखता है, जो स्ट्रिंग `"high"` की तुलना में बहुत कम जानकारी देता है।

---

क्योंकि एनम बस एक ऑब्जेक्ट है, इसलिए सामान्य ऑब्जेक्ट हेल्पर आपको इसकी जांच करने देते हैं:
- `Object.keys(Enum)` सदस्यों के **नामों** वाला एक ऐरे लौटाता है
- `Object.values(Enum)` सदस्यों के **मानों** वाला एक ऐरे लौटाता है
- `Object.entries(Enum)` `[नाम, मान]` जोड़ों का एक ऐरे लौटाता है

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// [ 'RED', 'BLUE' ] प्रिंट करता है
console.log(Object.values(Color));
// [ 'red', 'blue' ] प्रिंट करता है
```
`Object.values()` को ऐरे मेथड `includes()` के साथ मिलाना, यह जांचने का मानक तरीका है कि कोई मनमाना मान, उदाहरण के लिए यूज़र इनपुट से पढ़ा गया मान, कोई मान्य सदस्य है या नहीं:
```javascript
console.log(Object.values(Color).includes("red"));
// true प्रिंट करता है
console.log(Object.values(Color).includes("pink"));
// false प्रिंट करता है
```

---

एनम स्वाभाविक रूप से `switch` स्टेटमेंट के साथ जोड़े में काम करते हैं, जो एक मान की तुलना `case` लेबल की एक सूची से करता है और पहले मैच करने वाले का कोड चलाता है।
हर शाखा `return` या `break` पर खत्म होती है, और वैकल्पिक `default` शाखा तब चलती है जब कुछ भी मैच नहीं करता:
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// go प्रिंट करता है
```
हमेशा सदस्यों (`Light.RED`) से तुलना करें, कभी कच्चे मानों (`"red"`) से नहीं: अगर मान कभी बदल जाए, तो भी `switch` काम करता रहेगा।

---

किसी मान से वापस उसके सदस्य नाम तक जाने को **रिवर्स लुकअप** कहा जाता है। `Object.keys()` से नामों पर लूप करें और ऐरे मेथड `find()` का उपयोग करके पहला वह नाम चुनें जिसका मान मैच करता है। `find()` उस पहले एलिमेंट को लौटाता है जिसके लिए कॉलबैक `true` होता है (या अगर कोई न हो तो `undefined`):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// HIGH प्रिंट करता है
```
`Priority[key]` उस सदस्य को पढ़ता है जिसका नाम वेरिएबल `key` में स्टोर है, यह वही ब्रैकेट नोटेशन है जिसका उपयोग आप किसी भी ऑब्जेक्ट के लिए करते हैं।

---

स्ट्रिंग सदस्यों में एक कमज़ोरी होती है: समान टेक्स्ट वाली कोई भी स्ट्रिंग एक सदस्य के रूप में स्वीकार कर ली जाती है।
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// true प्रिंट करता है
```
जब आप ऐसे सदस्य चाहते हैं जो **सिर्फ** खुद के बराबर हों, तो `Symbol` का उपयोग करें। `Symbol(description)` एक बिल्कुल नया मान बनाता है जो हर दूसरे सिंबल से अलग होता है, भले ही वह समान विवरण के साथ बनाया गया हो:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// true प्रिंट करता है
console.log(Suit.HEARTS === Symbol("hearts"));
// false प्रिंट करता है
console.log(typeof Suit.HEARTS);
// symbol प्रिंट करता है
```
आपके द्वारा दिया गया टेक्स्ट सिर्फ डिबगिंग के लिए एक लेबल है; आप इसे `description` प्रॉपर्टी से वापस पढ़ सकते हैं (`Suit.HEARTS.description` `"hearts"` है)।

---

एनम मानों का उपयोग अक्सर किसी दूसरे ऑब्जेक्ट की **कुंजियों** के रूप में किया जाता है, उदाहरण के लिए हर सदस्य को किसी लेबल या कीमत से जोड़ने के लिए। ऑब्जेक्ट लिटरल के अंदर, किसी कुंजी को स्क्वेयर ब्रैकेट `[ ]` में लपेटने पर वह एक्सप्रेशन इवैल्यूएट होता है और उसका परिणाम कुंजी के रूप में उपयोग होता है (एक **कंप्यूटेड की**)। यह स्ट्रिंग और सिंबल, दोनों प्रकार के सदस्यों के साथ काम करता है:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// Completed प्रिंट करता है
```
ब्रैकेट के बिना, `Status.DONE: "Completed"` एक सिंटैक्स एरर होता, और `"Status.DONE"` एक साधारण स्ट्रिंग कुंजी होती।

---

जब हर सदस्य को कई डेटा या अपने खुद के मेथड की ज़रूरत होती है, तो एक **क्लास** एनम की भूमिका निभा सकती है। हर सदस्य उस क्लास का एक इंस्टेंस होता है, जिसे एक `static` प्रॉपर्टी में स्टोर किया जाता है, यानी ऐसी प्रॉपर्टी जो हर इंस्टेंस के बजाय खुद क्लास से संबंधित होती है:
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// Earth प्रिंट करता है
```
क्लास के बाद `Object.freeze(Planet)` को कॉल करें ताकि कोई भी सदस्य जोड़ या बदल न सके, और कंस्ट्रक्टर में `Object.freeze(this)` से हर इंस्टेंस को फ़्रीज़ करें ताकि सदस्य खुद रीड-ओनली बने रहें।
