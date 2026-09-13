आप पहले से जानते हैं कि `extends` एक class को दूसरी class की संतान (child) बना देता है। यह कीवर्ड वास्तव में जो देता है वह है **इनहेरिटेंस (inheritance)**: child को parent की हर प्रॉपर्टी और मेथड मुफ़्त में मिल जाती है, और वह उनके ऊपर अपनी चीज़ें भी जोड़ सकता है।

इनहेरिटेंस को उपयोगी बनाने वाला हिस्सा **`super`** है। child के constructor के अंदर `super(...)` parent के constructor को कॉल करता है, ताकि parent ऑब्जेक्ट का वह हिस्सा सेट अप कर सके जो उसका अपना है:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
यहाँ `super(name)` `name` को `Animal` को सौंप देता है, जो उसे संग्रहीत कर देता है, और `Dog` को केवल `breed` की चिंता करनी होती है।

---

एक child class को parent द्वारा पहले से दी गई चीज़ों को फिर से परिभाषित करने की ज़रूरत नहीं होती। मेथड्स भी इनहेरिट होते हैं, इसलिए child का एक instance उन्हें कॉल कर सकता है जैसे कि वे उसके अपने हों:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// prints Max makes a sound
```
जब एक child अपना constructor घोषित करता है, तो उसमें `super(...)` को कॉल करना **अनिवार्य** होता है: इसके बिना ऑब्जेक्ट कभी इनिशियलाइज़ नहीं होता और JavaScript एक `ReferenceError` थ्रो करता है। बिना constructor वाला child बिल्कुल ठीक रहता है, क्योंकि JavaScript खुद एक ऐसा constructor लिख देता है जो हर argument को parent तक पहुँचा देता है।

---

`super()` का नियम "इसे कहीं भी कॉल कर लो" से कहीं अधिक सख़्त है। एक child के constructor में `super()` के चलने तक `this` शब्द मौजूद नहीं होता, क्योंकि ऑब्जेक्ट बनाने का काम parent का constructor करता है। उस पंक्ति से पहले `this` को छूना एरर थ्रो करता है:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
इसलिए `super(...)` किसी भी ऐसे child के constructor का **पहला स्टेटमेंट** होना चाहिए जो `this` का उपयोग करता है।

---

जब एक child वह मेथड परिभाषित करता है जो parent के पास पहले से है, तो child का वर्ज़न जीत जाता है। इसे **ओवरराइडिंग (overriding)** कहते हैं:
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// prints Woof
```
ओवरराइडिंग parent के वर्ज़न को डिलीट नहीं करती, वह उसे केवल छिपा देती है। child के मेथड के अंदर `super.methodName(...)` अब भी उस तक पहुँच सकता है, जिससे आप parent के व्यवहार को बदलने के बजाय उसे बढ़ा सकते हैं:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
अंतर पर ध्यान दें: `super(...)` parent के **constructor** को कॉल करता है, जबकि `super.name(...)` parent की **मेथड** को कॉल करता है।

---

अब तक हर प्रॉपर्टी constructor के अंदर बनाई जाती थी। एक **class field** आपको उसे सीधे class की body में, एक वैकल्पिक प्रारंभिक वैल्यू के साथ घोषित करने देता है:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
फ़ील्ड्स constructor की body चलने से पहले हर नए instance को असाइन कर दी जाती हैं, इसलिए constructor उन पर पहले से भरोसा कर सकता है। बिना वैल्यू वाला फ़ील्ड भी घोषित माना जाता है, वह बस `undefined` से शुरू होता है:
```javascript
class Task {
    done = false;
    title;
}
```
सिंटैक्स पर ध्यान दें: घोषणा में न `let`, न `const`, न `this`, और पंक्ति एक सेमीकोलन के साथ समाप्त होती है।

---

जब classes एक-दूसरे से इनहेरिट करती हैं तो क्रम मायने रखता है। एक `class` घोषणा को `function` की तरह **होइस्ट नहीं** किया जाता: नाम केवल उस पंक्ति से मौजूद होता है जहाँ class लिखी गई है और आगे। इसलिए child class को अपने parent के *बाद* आना चाहिए, अन्यथा `extends` क्लॉज़ एक `ReferenceError` के साथ विफल हो जाता है।

---

कुछ व्यवहार किसी एक instance के बजाय class स्वयं से संबंधित होता है। उदाहरण के लिए, दो यूनिटों के बीच रूपांतरण के लिए किसी ऑब्जेक्ट की ज़रूरत नहीं होती जिस पर काम किया जाए। एक मेथड को **`static`** चिह्नित करने से वह class पर चला जाता है:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
एक static मेथड को class के नाम पर कॉल किया जाता है, कभी भी instance पर नहीं: `new MathUtils().double(4)` एक `TypeError` थ्रो करता है, क्योंकि instances को static सदस्य नहीं मिलते। एक static मेथड के अंदर `this` class को संदर्भित करता है, इसलिए एक static दूसरे को `this.otherStatic(...)` से कॉल कर सकता है।

---

`static` फ़ील्ड्स पर भी काम करता है। एक **static प्रॉपर्टी** class पर एक बार संग्रहीत होती है, हर instance पर नहीं, जिससे वह शेयर किए गए काउंटर या किसी कॉन्स्टेंट के लिए सहज जगह बन जाती है:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
चूँकि केवल एक ही कॉपी होती है, इसे अपडेट करने वाला हर instance एक ही वैल्यू को अपडेट करता है। constructor के अंदर आप इसे class के नाम, `Circle.PI`, से पहुँचते हैं, `this` से नहीं: `this.PI` instance पर प्रॉपर्टी ढूँढेगा, कुछ नहीं पाएगा, और आपको `undefined` दे देगा।

---

एक static मेथड का एक बहुत सामान्य उपयोग **फ़ैक्टरी (factory)** है: एक ऐसा मेथड जो किसी दूसरे आकार के डेटा से एक instance बनाकर लौटाता है। यह `new` को एक ही जगह रखता है और निर्माण को एक ऐसा नाम देता है जो बताता है कि वह क्या करता है:
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// prints 120
```
एक फ़ैक्टरी को किसी भी instance के बनने से पहले कॉल किया जा सकता है, जो एक साधारण मेथड से संभव नहीं था।

---

एक **getter** एक ऐसा मेथड है जिसे प्रॉपर्टी की तरह पढ़ा जाता है। उसके आगे `get` लिखें और कॉल करते समय कोष्ठक छोड़ दें:
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// prints 12
```
`r.area` मेथड को चलाकर उसका परिणाम लौटाता है, इसलिए वह एक number है। कोष्ठक जोड़ने पर आप उस number को कॉल करने की कोशिश करेंगे, जो विफल हो जाता है।

इसका दर्पण रूप **setter** है, जिसे `set` से घोषित किया जाता है और जो प्रॉपर्टी को असाइन करते समय चलता है। यह ठीक एक पैरामीटर लेता है:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

एक setter का असली मूल्य यह है कि वह इनकार कर सकता है। असाइनमेंट और संग्रहीत वैल्यू के बीच आपको आने वाली वैल्यू को जाँचने, सीमित करने या अस्वीकार करने का मौका मिलता है:
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// prints 3, the setter rejected 50
```
एक ही नाम वाला getter और setter मिलकर एक ही प्रॉपर्टी बनाते हैं, इसलिए वे साथ ही एक साधारण फ़ील्ड भी नहीं हो सकते: संग्रहीत वैल्यू किसी दूसरे नाम के अंतर्गत रहती है, परंपरा के अनुसार वही नाम जिसके आगे एक अंडरस्कोर लगा हो।

---

`_temperature` का शुरुआती अंडरस्कोर केवल एक परंपरा है: बाहरी दुनिया को `v._level = 999` लिखकर आपके setter से सीधे गुज़र जाने से कुछ भी नहीं रोकता। एक **प्राइवेट फ़ील्ड (private field)** भाषा द्वारा लागू किया जाता है। उसका नाम `#` से शुरू होता है, उसे class की body में घोषित करना ज़रूरी है, और उसे केवल उसी class के अंदर पढ़ा या लिखा जा सकता है:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
दो बातें हैं जिन पर फिसलना आसान है। `#` नाम का हिस्सा है, इसलिए आप हमेशा `this.#code` लिखते हैं, कभी भी `this.code` नहीं। और एक प्राइवेट फ़ील्ड `Object.keys` में या instance के `console.log` में नहीं दिखता।

---

मेथड्स भी प्राइवेट हो सकते हैं। नाम के आगे `#` लगाएँ और मेथड class की सार्वजनिक सतह से ग़ायब हो जाता है, जबकि वह अब भी किसी अन्य मेथड से `this.#name(...)` के साथ कॉल किया जा सकता है:
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// prints $7
```
इसी तरह आप हेल्पर चरणों को API से बाहर रखते हैं: कॉलर को `print` दिखता है, उसके पीछे की फ़ॉर्मैटिंग की बातें नहीं। प्राइवेट फ़ील्ड्स और प्राइवेट मेथड्स मिलकर एक class को स्पष्ट अंदरूनी और बाहरी हिस्सा देते हैं।

---

एक ऑब्जेक्ट प्रिंट करने पर आमतौर पर कुछ असहायक मिलता है। जब भी JavaScript को एक स्ट्रिंग चाहिए होती है और उसे उसकी जगह एक ऑब्जेक्ट मिल जाता है, तो वह ऑब्जेक्ट की **`toString`** मेथड को कॉल करता है, और डिफ़ॉल्ट मेथड `[object Object]` लौटाती है। अपना खुद का परिभाषित करने पर वह बदल जाता है:
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// prints $7
```
वही मेथड स्ट्रिंग कॉन्कैटिनेशन और `String(value)` द्वारा भी उपयोग किया जाता है। अगर आप एक सहज **number** भी चाहते हैं, तो `[Symbol.toPrimitive](hint)` परिभाषित करें, जो `"string"`, `"number"` या `"default"` प्राप्त करता है और तय करता है कि क्या लौटाना है; जब वह मौजूद होता है तो वह `toString` पर हावी हो जाता है।

---

**`instanceof`** ऑपरेटर पूछता है कि क्या कोई ऑब्जेक्ट किसी class से, या उससे इनहेरिट करने वाली किसी भी class से बना था:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript में कोई `abstract` कीवर्ड नहीं है, लेकिन वही विचार हाथ से लिखा जाता है: एक base class आकार परिभाषित करती है और हर वह मेथड जिसे child को *अवश्य* देना होता है, सीधे एरर थ्रो कर देता है:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
जो child `area` को ओवरराइड करना भूल जाए, वह पहली बार उपयोग किए जाने पर ज़ोर से विफल होता है, चुपचाप `undefined` लौटाने के बजाय।

---

`for...of` और स्प्रेड ऑपरेटर `...` किसी भी ऑब्जेक्ट पर काम नहीं करते: वे **इटरेबल्स (iterables)** पर काम करते हैं, ऐसे ऑब्जेक्ट्स जो विशेष की `Symbol.iterator` के अंतर्गत संग्रहीत एक मेथड देते हैं। अपनी class को वह मेथड दें और वह इस क्लब में शामिल हो जाती है:
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// prints [ 'a', 'b' ]
```
नाम के आगे का `*` उसे एक **जेनरेटर (generator)** बना देता है: एक ऐसा फ़ंक्शन जो वैल्यूज़ को `yield` के साथ एक बार में एक देता है और उनके बीच रुक जाता है। इटरेशन प्रोटोकॉल को पूरा करने का यह सबसे छोटा तरीका है, और यह संग्रहीत होने के बजाय गणना की जाने वाली वैल्यूज़ के लिए भी काम करता है।
