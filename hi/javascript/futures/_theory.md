कुछ संक्रियाएँ तुरंत पूरी नहीं होतीं: कोई फ़ाइल डाउनलोड करना, डेटाबेस से पढ़ना, किसी टाइमर का इंतज़ार करना। इनके चलते समय JavaScript जम नहीं जाता। इसके बजाय वह आपको एक **`Promise`** देता है: एक ऑब्जेक्ट जो एक ऐसे मान का प्रतिनिधित्व करता है जो **बाद में** उपलब्ध होगा।

**`async`** से चिह्नित कोई फ़ंक्शन हमेशा एक प्रॉमिस लौटाता है। फ़ंक्शन जो भी लौटाता है, वही उस प्रॉमिस के अंदर का मान बन जाता है:
```javascript
async function fetchNumber() {
  return 42;
}
```
प्रॉमिस से मान निकालने के लिए आप **`await`** का उपयोग करते हैं। यह फ़ंक्शन को तब तक रोक देता है जब तक प्रॉमिस के पास उसका मान न आ जाए, और फिर आपको सादा मान दे देता है। `await` केवल किसी `async` फ़ंक्शन के अंदर ही अनुमत है:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
`await` के बिना, `n` स्वयं प्रॉमिस होता और `console.log(n)` संख्या के बजाय `Promise { 42 }` प्रिंट करता।

---

किसी फ़ंक्शन के आगे `async` जोड़ना वह बदल देता है जो वह वापस देता है: बॉडी अब भी एक साधारण मान गणना करती है, लेकिन कॉल करने वाले को उसके चारों ओर लिपटा हुआ प्रॉमिस मिलता है।
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
दोनों फ़ंक्शनों में वही कोड है; केवल परिणाम पढ़ने का तरीका अलग है। `"HI"` वापस पाने के लिए `shoutLater("hi")` को किसी दूसरे `async` फ़ंक्शन के अंदर await किया जाना चाहिए।

किसी फ़ंक्शन को `async` चिह्नित करने का तब कोई खर्च नहीं होता जब इंतज़ार करना ही न हो, और यही आपको बाद में उसके अंदर `await` का उपयोग करने देता है।

---

जब मान वास्तव में बाद में आता है, तो आप प्रॉमिस स्वयं **`new Promise`** से बनाते हैं। इसमें एक फ़ंक्शन दिया जाता है, जिसे एक **`resolve`** callback मिलती है: `resolve(value)` कॉल करें जब मान तैयार हो, और प्रॉमिस उसी के साथ fulfilled हो जाता है।
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` को `callback` को `ms` मिलीसेकंड के बाद चलाने के लिए शेड्यूल करता है और तुरंत लौट आता है, इसलिए इस बीच कुछ भी रुकता नहीं है।

`new Promise` को दिया गया फ़ंक्शन तुरंत चल जाता है, लेकिन प्रॉमिस **pending** बना रहता है जब तक `resolve` कॉल न किया जाए। उसे await करने पर मान मिल जाता है:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

एक प्रॉमिस हमेशा तीन स्थितियों में से किसी एक में रहता है:

- **pending**: काम अब भी चल रहा है;
- **fulfilled**: काम सफल रहा और प्रॉमिस के पास एक मान है;
- **rejected**: काम विफल हुआ और प्रॉमिस के पास एक त्रुटि है।

एक प्रॉमिस pending से शुरू होता है और अधिक से अधिक एक बार स्थिति बदलता है। एक बार fulfilled या rejected हो जाने पर वह **settled** हो जाता है और फिर कभी नहीं बदलता।

किसी `async` फ़ंक्शन को कॉल करना कभी इंतज़ार नहीं करता: वह काम शुरू करता है और तुरंत एक pending प्रॉमिस दे देता है, इसलिए कॉल के बाद की पंक्ति काम पूरा होने से पहले चल जाती है। वह प्रॉमिस एक साधारण ऑब्जेक्ट है, उसके अंदर का मान नहीं — इसीलिए `await` भूल जाना इतनी आम गलती है।

---

`await` प्रॉमिस पढ़ने का एकमात्र तरीका नहीं है। हर प्रॉमिस में एक **`.then(callback)`** मेथड होता है: प्रॉमिस के fulfilled होते ही callback को वह मान मिल जाता है।
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** ऐसा प्रॉमिस बनाता है जो पहले से `value` के साथ fulfilled है, जो तब काम आता है जब मान आपके पास मौजूद हो लेकिन प्रॉमिस लौटाना ज़रूरी हो।

`.then` एक **नया** प्रॉमिस लौटाता है जो callback के जो कुछ भी लौटाने पर fulfilled होता है, इसलिए कॉल को **श्रृंखलाबद्ध** किया जा सकता है, जहाँ हर कदम पिछले कदम के परिणाम पर काम करता है:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

कोई `async` फ़ंक्शन किसी और फ़ंक्शन की तरह ऊपर से नीचे पढ़ा जाता है: `await` बस उसे तब तक रोक देता है जब तक awaited किया गया प्रॉमिस fulfilled न हो जाए, फिर निष्पादन अगली पंक्ति से आगे बढ़ जाता है।
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
आख़िरी पंक्ति पर ध्यान दें: किसी `async` फ़ंक्शन को अब भी **कॉल** करना पड़ता है। `main` को कोष्ठक के बिना लिखना काम को परिभाषित तो करता है पर कभी शुरू नहीं करता, और कुछ भी प्रिंट नहीं होता।

---

एसिंक्रोनस काम विफल भी हो सकता है। `new Promise` को दिए गए फ़ंक्शन को एक दूसरी callback भी मिलती है, **`reject`**: `reject(error)` कॉल करें और प्रॉमिस fulfilled होने के बजाय rejected हो जाता है।
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
हमेशा एक `Error` ऑब्जेक्ट के साथ reject करें: उसमें एक `message` और एक स्टैक ट्रेस होता है, जो किसी खाली स्ट्रिंग में नहीं होता।

एक rejection को **`.catch(callback)`** से पढ़ा जाता है, जो `.then` का दर्पण है। **`Promise.reject(error)`** ऐसा प्रॉमिस बनाता है जो पहले से rejected है, बिलकुल वैसे जैसे `Promise.resolve` fulfilled बनाता है:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
`resolve` और `reject` दोनों को कॉल करने, या दो बार कॉल करने से कुछ नहीं बदलता: केवल पहली कॉल गिनती है।

---

`.then`, `.catch` और `.finally` एक ही श्रृंखला की कड़ियाँ हैं। एक rejection हर `.then` को छोड़ देती है जब तक वह किसी `.catch` से न मिले; एक बार `.catch` callback कोई मान लौटा देने पर श्रृंखला फिर से fulfilled हो जाती है और सामान्य रूप से आगे बढ़ती है।

**`.finally(callback)`** तब चलता है जब श्रृंखला settled हो जाती है, चाहे वह fulfilled हुई हो या rejected। उसकी callback कोई आर्ग्युमेंट नहीं लेती और उसका लौटाया मान अनदेखा किया जाता है, इसलिए मान अगले `.then` तक बहता रहता है। यह सफ़ाई के कामों की जगह है, जैसे किसी स्पिनर को छिपाना:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

किसी `async` फ़ंक्शन के अंदर आपको `.catch` की ज़रूरत नहीं है। एक rejected प्रॉमिस को await करना त्रुटि को **थ्रो** कर देता है, इसलिए साधारण `try` / `catch` / `finally` कथन उसे संभाल लेता है:
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
दूसरी दिशा में भी यह काम करता है: किसी `async` फ़ंक्शन के अंदर एक `throw` कॉल करने वाले को क्रैश नहीं करता, बल्कि उस प्रॉमिस को reject कर देता है जो फ़ंक्शन ने लौटाया था।
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
किसी भी `try` ब्लॉक की तरह, विफल `await` के बाद की पंक्तियाँ छोड़ दी जाती हैं, `catch` ब्लॉक चलता है, और `finally` ब्लॉक दोनों ही स्थितियों में चलता है।

---

`await` के चारों ओर `try` / `catch` का एक आम उपयोग किसी विफलता को एक उचित डिफ़ॉल्ट मान से बदलना है, ताकि कॉल करने वाले को कभी त्रुटि से निपटना न पड़े:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
`measure(path)` के आगे `await` रखें, भले ही मान तुरंत ही लौटाया जाता है। इसके बिना प्रॉमिस `try` ब्लॉक से कभी गुज़रे बिना ही फ़ंक्शन से बाहर निकल जाता, और एक rejection `catch` से बच निकलती।

---

जब कई परिणाम चाहिए हों, तो उन्हें एक के बाद एक await करना समय बर्बाद करता है: हर एक तभी शुरू होता है जब पिछला पूरा हो चुका हो। **`Promise.all(promises)`** पहले से चल रहे प्रॉमिसों की एक ऐरे लेता है और एक ऐसा प्रॉमिस लौटाता है जो उनके सभी मानों की एक ऐरे के साथ fulfilled होता है:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
दो नियम याद रखने लायक हैं:

- मान **ऐरे की क्रम** में वापस आते हैं, न कि उस क्रम में जिसमें वे पूरे हुए;
- यदि कोई भी प्रॉमिस rejected हो जाए, तो `Promise.all` द्वारा लौटाया गया प्रॉमिस उसी पहली त्रुटि के साथ तुरंत rejected हो जाता है, और बाकी मान खो जाते हैं।

---

`Promise.all` किसी भी लंबाई की ऐरे के साथ काम करता है, खाली ऐरे सहित: `Promise.all([])` को await करने पर तुरंत एक खाली ऐरे ही वापस मिलती है। इससे रन टाइम पर बनी कोई सूची पास करना सुरक्षित रहता है, बिना "इंतज़ार करने जैसा कुछ नहीं" के लिए किसी विशेष मामले की ज़रूरत के।
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
जो ऐरे वह वापस देता है उसमें हमेशा ठीक उतनी ही प्रविष्टियाँ होती हैं जितनी उसे मिली थीं, उन्हीं स्थितियों पर, इसलिए उसे किसी और ऐरे की तरह लूप किया जा सकता है।

---

**क्रमिक** और **समानांतर** इंतज़ार का फ़र्क़ इस बात से तय होता है कि आप `await` *कहाँ* रखते हैं:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
पहले रूप में दूसरा डाउनलोड तभी शुरू होता है जब पहला पूरा हो चुका हो, क्योंकि `await` फ़ंक्शन को उसी पंक्ति पर रोक देता है। दूसरे में, दोनों कॉल किसी भी await से पहले कर दी जाती हैं, इसलिए `Promise.all` के इंतज़ार के दौरान दोनों डाउनलोड पहले से चल रहे होते हैं।

क्रमिक await केवल तब उपयोग करें जब दूसरे काम को सचमुच पहले के परिणाम की ज़रूरत हो। अन्यथा पहले सब कुछ शुरू करें और एक साथ await करें।

---

`Promise.all` जैसे ही एक प्रॉमिस rejected हो जाए, हार मान लेता है। जब आप फिर भी हर परिणाम चाहते हैं, तो **`Promise.allSettled(promises)`** का उपयोग करें: वह कभी rejected नहीं होता, और हर प्रॉमिस के लिए एक छोटा ऑब्जेक्ट लेकर, उसी क्रम में fulfilled होता है:

- `{ status: "fulfilled", value: ... }` उनके लिए जो सफल रहे;
- `{ status: "rejected", reason: ... }` उनके लिए जो विफल रहे।

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
`value` केवल तब पढ़ें जब `status` `"fulfilled"` हो, और `reason` केवल तब जब वह `"rejected"` हो: दूसरी प्रॉपर्टी बस मौजूद नहीं होती।

---

**`Promise.race(promises)`** जैसे ही प्रॉमिसों में से **पहला** settle होता है, तब settle हो जाता है, और उसका परिणाम कॉपी कर लेता है: पहले मान के साथ fulfilled, या पहली त्रुटि के साथ rejected। बाकी रद्द नहीं किए जाते, वे चलते रहते हैं, लेकिन जो कुछ भी वे दें वह अनदेखा किया जाता है।
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
इसका ख़ास उपयोग एक समय-सीमा है: असली काम को एक ऐसे प्रॉमिस के साथ race करें जो थोड़ी देर बाद विफल हो जाता है, और आपको परिणाम या एक टाइमआउट त्रुटि में से कोई एक मिल जाएगा।

खाली ऐरे से सावधान रहें: `Promise.race([])` हमेशा के लिए pending रहता है, क्योंकि ऐसा कोई चीज़ नहीं जो उसे settle कर सके।

---

आख़िरी टुकड़ों को जोड़ने पर एक छोटा औज़ार बनता है जो लगभग हर असली एप्लिकेशन में उपयोग होता है: एक समय-सीमा। एक ऐसा प्रॉमिस बनाएँ जो `ms` मिलीसेकंड के बाद rejected हो जाए, उसे असली काम के साथ race करें, और जो पहले settle हो वही परिणाम तय कर देता है:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
किसी `async` फ़ंक्शन से प्रॉमिस लौटाना ठीक है: फ़ंक्शन द्वारा लौटाया गया प्रॉमिस उसका पीछा करता है, इसलिए कॉल करने वाला अंतिम मान await करता है, प्रॉमिस के प्रॉमिस को नहीं।
