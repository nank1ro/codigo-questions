एक `enumeration` संबंधित मानों के समूह के लिए एक सामान्य प्रकार परिभाषित करता है और आपको अपने कोड में उन मानों के साथ टाइप-सेफ तरीके से काम करने में सक्षम बनाता है।
हम `enum` कीवर्ड का उपयोग करके enumerations घोषित करते हैं:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
एक enumeration में परिभाषित मान (जैसे `blue`, `red` और `green`) इसके _enumeration cases_ हैं।
हम नए enumeration cases पेश करने के लिए `case` कीवर्ड का उपयोग करते हैं।

---

एक ही पंक्ति में कई cases अल्पविराम से अलग करके लिखे जा सकते हैं:
```swift
enum Colors {
    case blue, red, green
}
```

---

हम `switch` स्टेटमेंट के साथ अलग-अलग enumeration मानों को मैच कर सकते हैं:
```swift
let color = Colors.red
switch color {
    case .blue:
        print("Blue")
    case .red:
        print("Red")
    case .green:
        print("Green")
}
// prints "Red"
```
ध्यान रखें कि यदि आपको हर enumeration case के लिए `case` प्रदान करने की आवश्यकता नहीं है, तो आप उन cases को कवर करने के लिए `default` case प्रदान कर सकते हैं जो स्पष्ट रूप से संबोधित नहीं हैं

---

कुछ enumerations के लिए, उस enumeration के सभी cases का संग्रह होना उपयोगी होता है।
आप enumeration के नाम के बाद `: CaseIterable` लिखकर इसे सक्षम करते हैं।
Swift enumeration प्रकार की `allCases` प्रॉपर्टी के रूप में सभी cases का संग्रह प्रदान करता है:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
