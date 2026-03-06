String _interpolation_ एक प्रोग्रामेटिक तरीका है String बनाने का।
Dart में हम `+` चिह्न (concatenation) का उपयोग करके दो या अधिक strings को एक साथ प्रदर्शित कर सकते हैं, जैसे:
```dart
print("Hello " + "Dart!");
// prints "Hello Dart!"
```

---

लेकिन `+` चिह्न का उपयोग करके '10' जैसी संख्या को ` "friends"` जैसी string में जोड़ने पर एक त्रुटि आती है क्योंकि वे अलग-अलग प्रकार के मान हैं

---

String interpolation हमें बिना किसी त्रुटि के string में संख्या जोड़ने जैसे expressions प्रदर्शित करने की अनुमति देता है।
`${}` के अंदर एक expression रखने पर वह evaluate होता है।
लौटाया गया मान String में बदल जाता है और परिणामी String में डाला जाता है

---

यदि आप किसी identifier नाम के पहले `$` लगाते हैं, तो string interpolation उस identifier की सामग्री को `String` में डाल देगा

---

यदि `$` चिह्न के बाद जो आता है वह प्रोग्राम identifier के रूप में पहचाना नहीं जा सकता, तो आपको एक त्रुटि मिलेगी

---

हम डॉलर चिह्न के बाद variables भी डाल सकते हैं ताकि उनका मान दिखाया जा सके

---

हम string interpolation का उपयोग करके curly brackets से जितनी बार चाहें उतनी बार मान डाल सकते हैं

---

`${}` के अंदर हम conditions भी रख सकते हैं, उदाहरण के लिए:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

String interpolation का सबसे अच्छा उपयोग print statements में होता है, लेकिन हम उन्हें सामान्य strings की तरह variables में भी स्टोर कर सकते हैं।
