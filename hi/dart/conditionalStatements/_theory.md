एक **`if` कथन** एक कोड ब्लॉक को केवल तभी निष्पादित करता है जब कोई शर्त `true` हो।

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

घुंघराले ब्रेसेज़ के अंदर का कोड केवल तभी चलता है जब शर्त `age >= 18` का मान `true` हो।

---

जब कोई शर्त पूरी होती है तो आप `if` ब्लॉक के अंदर `print()` का उपयोग करके संदेश प्रदर्शित कर सकते हैं।

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

यदि `isRaining` का मान `false` है, तो कुछ भी नहीं छपता।

---

एक **`if-else` कथन** शर्त `true` होने पर `if` ब्लॉक चलाता है और `false` होने पर `else` ब्लॉक चलाता है।

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

दो शाखाओं में से हमेशा ठीक एक ही निष्पादित होती है।

---

**`else if`** आपको क्रम में कई शर्तें जाँचने देता है। पहली शाखा जिसकी शर्त `true` है वह निष्पादित होती है, और बाकी छोड़ दी जाती हैं।

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

**टर्नरी ऑपरेटर** `condition ? expr1 : expr2` एक सरल `if-else` अभिव्यक्ति लिखने का संक्षिप्त तरीका है।

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

यदि शर्त `true` है तो `expr1` उपयोग होता है; अन्यथा `expr2` उपयोग होता है।
