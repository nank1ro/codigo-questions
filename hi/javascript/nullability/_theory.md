JavaScript में "यहाँ कोई मान नहीं है" कहने के दो अलग-अलग तरीके हैं।
`undefined` का मतलब है कि कोई मान **कभी दिया ही नहीं गया**। बिना मान के घोषित किया गया वेरिएबल `undefined` रखता है, और किसी ऑब्जेक्ट में मौजूद न होने वाली प्रॉपर्टी भी ऐसा ही करती है:
```javascript
let city;
console.log(city);
// undefined प्रिंट करता है
const user = { name: "Ana" };
console.log(user.age);
// undefined प्रिंट करता है
```
`null` एक ऐसा मान है जिसे **आप** जानबूझकर असाइन करते हैं ताकि यह बता सकें कि "खाली है, और मुझे पता है":
```javascript
let owner = null;
console.log(owner);
// null प्रिंट करता है
```
तो `undefined` आमतौर पर भाषा की तरफ़ से यह बताने का तरीका है कि कोई मान मौजूद नहीं है, जबकि `null` प्रोग्रामर द्वारा यह जताने का तरीका है कि यह जानबूझकर खाली रखा गया है।

---

फ़ंक्शन दो और स्थितियों में `undefined` देते हैं।
जब आप किसी फ़ंक्शन को उसकी घोषणा से **कम आर्ग्युमेंट** देकर कॉल करते हैं, तो जो पैरामीटर छूट जाते हैं वे `undefined` रखते हैं:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// undefined प्रिंट करता है
```
जब कोई फ़ंक्शन **बिना `return`** के (या सिर्फ़ `return;` के साथ) खत्म होता है, तो उसे कॉल करने पर `undefined` मिलता है:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// पहले hi, फिर undefined प्रिंट करता है
```
ध्यान दें कि जानबूझकर `null` पास करना आर्ग्युमेंट को छोड़ने जैसा नहीं है: `greet(null)` `null` प्रिंट करता है, क्योंकि `null` एक असली मान है जो फ़ंक्शन को दिया गया।

---

`typeof` ऑपरेटर किसी मान का प्रकार एक स्ट्रिंग के रूप में लौटाता है। `undefined` के लिए यह उम्मीद के मुताबिक `"undefined"` बताता है:
```javascript
let city;
console.log(typeof city);
// undefined प्रिंट करता है
```
लेकिन `null` के लिए यह `"object"` बताता है। यह JavaScript के बिल्कुल शुरुआती वर्शन की एक बग है जिसे कभी ठीक नहीं किया गया, क्योंकि बहुत सारा कोड इस पर निर्भर हो चुका है:
```javascript
console.log(typeof null);
// object प्रिंट करता है
```
इसलिए `typeof`, `undefined` का पता लगाने का एक भरोसेमंद तरीका है, लेकिन `null` का नहीं। `null` जाँचने के लिए सीधे उससे तुलना करें: `value === null`।

---

`null` और `undefined` एक-दूसरे से तुलना किए जाने पर कैसा व्यवहार करते हैं? यह ऑपरेटर पर निर्भर करता है।
**ढीली (loose)** समानता `==` उन्हें एक ही चीज़ मानती है, और उन्हें किसी भी दूसरे मान से अलग मानती है, `0`, `""` और `false` समेत:
```javascript
console.log(null == undefined);
// true प्रिंट करता है
console.log(null == 0, undefined == "");
// false false प्रिंट करता है
```
**सख्त (strict)** समानता `===` प्रकार की भी तुलना करती है, और `null` तथा `undefined` के प्रकार अलग-अलग होते हैं:
```javascript
console.log(null === undefined);
// false प्रिंट करता है
console.log(null === null);
// true प्रिंट करता है
```

---

ज़्यादातर समय आपको यह फ़र्क नहीं पड़ता कि "कोई मान नहीं" के दो संकेतकों में से आपको *कौन सा* मिला: आप बस यह जानना चाहते हैं कि कोई मान है भी या नहीं।
चूँकि `null == undefined` `true` होता है और इसके अलावा और कुछ भी ढीले रूप से `null` के बराबर नहीं होता, इसलिए `value == null` तुलना **दोनों** को एक साथ पकड़ने का मानक तरीका है:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// missing missing प्रिंट करता है
console.log(show(0), show(""));
// present present प्रिंट करता है
```
यह वह एक मामला है जहाँ `===` की जगह `==` को प्राथमिकता दी जाती है: `value === null || value === undefined` लिखने से बिल्कुल वही काम होता है, बस लंबा।
`0`, `""` और `false` जैसे मान `null` *नहीं* होते: ये असली मान हैं जो संयोग से फ़ॉल्सी हैं।

---

`null` या `undefined` की कोई प्रॉपर्टी पढ़ना एक एरर है जो प्रोग्राम को रोक देती है:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` `undefined` है, और `undefined` की कोई प्रॉपर्टी नहीं होती। **ऑप्शनल चेनिंग** (optional chaining) ऑपरेटर `?.` इसे हल करता है: अगर उसके बाईं ओर का मान `null` या `undefined` हो, तो पूरी एक्सप्रेशन वहीं रुक जाती है और थ्रो करने की बजाय `undefined` का मान देती है:
```javascript
console.log(user.address?.city);
// undefined प्रिंट करता है
console.log(user.name?.length);
// 3 प्रिंट करता है
```
जब बाईं ओर वाकई कोई मान होता है, तो `?.` बिल्कुल सामान्य `.` की तरह काम करता है। आप कई `?.` को चेन कर सकते हैं: `user.address?.street?.name` किसी भी लिंक के गायब होते ही `undefined` लौटा देता है।

---

ऑप्शनल चेनिंग सिर्फ़ डॉट प्रॉपर्टी तक सीमित नहीं है। इसके दो और रूप भी हैं।
`?.[]` किसी एलिमेंट या कंप्यूटेड key को तभी पढ़ता है जब बाईं ओर कोई मान हो:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// js प्रिंट करता है
const empty = {};
console.log(empty.tags?.[0]);
// undefined प्रिंट करता है
```
`?.()` किसी फ़ंक्शन को तभी कॉल करता है जब वह मौजूद हो, जो ऑप्शनल कॉलबैक के लिए उपयोगी है:
```javascript
const task = { name: "build" };
task.onDone?.();
// कुछ नहीं होता, कोई एरर नहीं
```
हर रूप में, जाँच `?.` से **ठीक पहले** वाले मान पर लागू होती है: `post?.tags?.[0]` तब भी सुरक्षित है जब `post` खुद `null` या `undefined` हो।

---

एक बार जब आपको पता चल जाए कि कोई मान गायब हो सकता है, तो आमतौर पर आप उसकी जगह एक **डिफ़ॉल्ट** मान चाहते हैं। इसके लिए दो ऑपरेटर हैं, और वे इस बात में अलग हैं कि वे किसे "गायब" मानते हैं।
`a || b` तब `b` लौटाता है जब `a` **फ़ॉल्सी** हो: सिर्फ़ `null` और `undefined` ही नहीं, बल्कि `0`, `""`, `false` और `NaN` भी।
**नलिश कोअलेसिंग** (nullish coalescing) ऑपरेटर `a ?? b` तभी `b` लौटाता है जब `a`, `null` या `undefined` हो, और बाकी हर मान को वैसा ही रहने देता है:
```javascript
const count = 0;
console.log(count || 10);
// 10 प्रिंट करता है
console.log(count ?? 10);
// 0 प्रिंट करता है
let name;
console.log(name ?? "Guest");
// Guest प्रिंट करता है
```
`??` का उपयोग तब करें जब `0`, `""` या `false` वैध मान हों जिन्हें बनाए रखना ज़रूरी है, और `||` का उपयोग तब करें जब आप वाकई हर फ़ॉल्सी मान को बदलना चाहते हों।

---

एक बहुत आम पैटर्न है "इस प्रॉपर्टी को तभी भरें जब यह अभी सेट न हो"। `??` से लिखने पर नाम दोहराना पड़ता है:
```javascript
options.timeout = options.timeout ?? 1000;
```
**नलिश असाइनमेंट** (nullish assignment) ऑपरेटर `??=` यही काम एक ही चरण में करता है: यह दाईं ओर का मान तभी असाइन करता है जब बाईं ओर का मान फ़िलहाल `null` या `undefined` हो, और किसी भी अन्य मान को बिना छेड़े छोड़ देता है:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// { retries: 0, timeout: 1000 } प्रिंट करता है
```
`retries`, `0` ही रहता है क्योंकि `0` नलिश नहीं है; `timeout` पहले मौजूद ही नहीं था, इसलिए उसे `1000` मिल जाता है। `||` के लिए भी यही विचार `||=` के रूप में मौजूद है, जो हर फ़ॉल्सी मान को ओवरराइट कर देता है।

---

एक **डिफ़ॉल्ट पैरामीटर** (default parameter) किसी पैरामीटर को तब मान देता है जब कॉलर कोई मान नहीं देता। नियम स्पष्ट है: डिफ़ॉल्ट तभी उपयोग होता है जब आर्ग्युमेंट `undefined` हो, जिसमें उसे छोड़ना भी शामिल है। `null` पास करने से डिफ़ॉल्ट **लागू नहीं** होता, क्योंकि `null` खुद एक मान है:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// abab प्रिंट करता है
console.log(repeat("ab", undefined));
// abab प्रिंट करता है
console.log(repeat("ab", null));
// एक खाली स्ट्रिंग प्रिंट करता है, क्योंकि null को 0 में बदल दिया जाता है
```
डिफ़ॉल्ट पैरामीटर `undefined` वाले नियम का पालन करते हैं, जबकि `??` `null` और `undefined` दोनों को कवर करता है: वह चुनें जो आपके फ़ंक्शन के कॉल होने के तरीके से मेल खाए।

---

ऑप्शनल चेनिंग और `== null` गार्ड मिलकर अच्छे से काम करते हैं: चेन बिना थ्रो किए नेस्टेड मान पढ़ती है, और गार्ड यह तय करता है कि परिणाम गायब होने पर क्या करना है:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
आख़िरी `return` के अंदर एक सादा `.` सुरक्षित है, क्योंकि गार्ड पहले ही यह साबित कर चुका है कि हर लिंक मौजूद है।

---

कई बिल्ट-इन मेथड "कुछ नहीं मिला" को `undefined` लौटाकर बताते हैं। ऐरे मेथड `find(callback)` इसका एक आम उदाहरण है: यह उस पहले एलिमेंट को लौटाता है जिसके लिए कॉलबैक `true` हो, या कोई एलिमेंट मेल न खाने पर `undefined`:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// undefined प्रिंट करता है
```
यहाँ `found.price` पढ़ने से एरर आएगी, इसलिए `?.` और `??`, `find` के स्वाभाविक साथी हैं:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// no price प्रिंट करता है
```

---

जब किसी ऑब्जेक्ट को `JSON.stringify()` से JSON में बदला जाता है, तो `null` और `undefined` अलग-अलग व्यवहार करते हैं।
JSON में `null` मान होता है लेकिन `undefined` नहीं, इसलिए जिस प्रॉपर्टी का मान `undefined` हो उसे बस **छोड़ दिया** जाता है, जबकि `null` वाली प्रॉपर्टी बनी रहती है:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// {"name":"Ana","email":null} प्रिंट करता है
```
ऐरे के अंदर पोज़िशन गायब नहीं हो सकतीं, इसलिए वहाँ `undefined`, `null` बन जाता है:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// [1,null,3] प्रिंट करता है
```

---

`obj.key === undefined` जाँचने से दो स्थितियों में फ़र्क नहीं किया जा सकता: या तो प्रॉपर्टी मौजूद ही नहीं है, या वह मौजूद है और उसका मान `undefined` है।
`Object.hasOwn(obj, key)` सिर्फ़ पहला सवाल पूछता है: यह `true` लौटाता है जब ऑब्जेक्ट में `key` नाम की उसकी **खुद की** प्रॉपर्टी हो, चाहे उसका मान कुछ भी हो:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// true true प्रिंट करता है
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// true false प्रिंट करता है
```
"खुद की" का मतलब है ऑब्जेक्ट पर सीधे घोषित की गई: इनहेरिट किए गए सदस्य जैसे `toString` हर ऑब्जेक्ट पर उपलब्ध होते हैं, लेकिन `Object.hasOwn(config, "toString")` `false` होता है।
