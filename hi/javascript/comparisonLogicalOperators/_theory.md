आइए **बराबर** `==` तुलना ऑपरेटर से शुरू करें।
यह एक **boolean** (`true` या `false`) लौटाता है जो बताता है कि दो अभिव्यक्तियाँ बराबर हैं या नहीं, उदाहरण के लिए:
```javascript
console.log(2 == 2); 
// prints true
console.log(2 == 3);
// prints false
```

---

आइए **बराबर नहीं** `!=` तुलना ऑपरेटर के साथ आगे बढ़ें।
यह एक **boolean** (`true` या `false`) लौटाता है जो बताता है कि दो अभिव्यक्तियाँ **बराबर नहीं** हैं, उदाहरण के लिए:
```javascript
console.log(2 != 2);
// prints false
console.log(2 != 3); 
// prints true
```
यह *बराबर* ऑपरेटर का बिल्कुल विपरीत है

---

आइए **से बड़ा** `>` तुलना ऑपरेटर के साथ आगे बढ़ें।
यह एक **boolean** (`true` या `false`) लौटाता है जो बताता है कि एक अभिव्यक्ति दूसरी से बड़ी है या नहीं, उदाहरण के लिए:
```javascript
console.log(2 > 2);
// prints false
console.log(3 > 2);
// prints true
```

---

आइए **से छोटा** `<` तुलना ऑपरेटर के साथ आगे बढ़ें।
यह एक **boolean** (`true` या `false`) लौटाता है जो बताता है कि एक अभिव्यक्ति दूसरी से छोटी है या नहीं, उदाहरण के लिए:
```javascript
console.log(2 < 2);
// prints false
console.log(2 < 3);
// prints true
```

---

आइए **से बड़ा या बराबर** `>=` तुलना ऑपरेटर के साथ आगे बढ़ें।
यह एक **boolean** (`true` या `false`) लौटाता है जो बताता है कि एक अभिव्यक्ति दूसरी से बड़ी या बराबर है, उदाहरण के लिए:
```javascript
console.log(2 >= 2); 
// prints true
console.log(3 >= 2);
// prints true
console.log(3 >= 4);
// prints false
```

---

आइए **से छोटा या बराबर** `<=` तुलना ऑपरेटर के साथ आगे बढ़ें।
यह एक **boolean** (`true` या `false`) लौटाता है जो बताता है कि एक अभिव्यक्ति दूसरी से छोटी या बराबर है, उदाहरण के लिए:
```javascript
console.log(2 <= 2); 
// prints true
console.log(3 <= 2);
// prints false
console.log(3 <= 4);
// prints true
```

---

अब आइए **लॉजिकल** ऑपरेटर देखें, पहले __AND__ `&&` से शुरू करते हैं।
यह पहला ऑपरेंड लौटाता है जो *false* का मूल्यांकन करता है या अंतिम ऑपरेंड अगर सभी *true* हैं।
```javascript
console.log(2 == 2 && 2 == 3);
// prints false
console.log(1 == 1 && 1 == 1.0);
// prints true
```

---

आइए **or** `||` लॉजिकल ऑपरेटर के साथ आगे बढ़ें।
यह पहला ऑपरेंड लौटाता है जो *true* का मूल्यांकन करता है या अंतिम ऑपरेंड अगर सभी *false* हैं।
```javascript
console.log(2 == 2 || 2 == 3);
// prints true
console.log(1 == 2 || 1 == 3);
// prints false
```

---

आइए **not** `!` लॉजिकल ऑपरेटर के साथ समाप्त करें।
यह एक boolean लौटाता है जो किसी अभिव्यक्ति की लॉजिकल स्थिति का उल्टा होता है।
```javascript
console.log(!true);
// prints false
console.log(!false);
// prints true
console.log(!(2 == 2));
// prints false
```
