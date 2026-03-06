निर्णय लेना तब आवश्यक होता है जब हम किसी कोड को केवल तभी निष्पादित करना चाहते हैं जब कोई विशेष शर्त पूरी हो।
मान लीजिए कि हम बाहर खेलना चाहते हैं केवल तभी जब मौसम अच्छा हो।
प्रोग्रामिंग में, हम एक boolean वेरिएबल `nice_weather` सेव कर सकते हैं और बाहर खेलने की क्रिया `if` इस वेरिएबल के `true` होने पर कर सकते हैं, जैसे:
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

आइए पिछले उदाहरण को जारी रखें।
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```
हमने देखा कि `if` स्टेटमेंट कोड ब्लॉक को केवल तभी निष्पादित करता है जब शर्त `true` हो।
एक और महत्वपूर्ण बात **कर्ली ब्रैकेट** `{}` हैं जो एक कोड ब्लॉक को दर्शाती हैं।

---

हमने अभी देखा कि किसी शर्त पूरी होने पर कोड ब्लॉक कैसे निष्पादित करें, अब देखते हैं कि पहली शर्त विफल होने पर दूसरा कोड ब्लॉक कैसे निष्पादित करें।
हम बाहर खेलने जाते हैं अगर मौसम अच्छा है; अन्यथा, हम घर पर रहते हैं।
C में हम `else` स्टेटमेंट का उपयोग कर सकते हैं, जैसे:
```c
bool nice_weather = false;
if (nice_weather) {
    // play outside
} else {
    // stay home
}
```

---

मान लीजिए कि हमारे पास जाँचने के लिए एक और शर्त है, जैसे इस उदाहरण में:
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
और इस कोड का आउटपुट `the number is 3` है।
सबसे पहले, जाँचें कि संख्या 2 के बराबर है या नहीं, यह false है।
तो दूसरे स्टेटमेंट पर चलते हैं और जाँचते हैं कि `num` 3 के बराबर है या नहीं, true होने पर हम `the number is 3` प्रिंट करके निम्नलिखित कोड ब्लॉक निष्पादित करते हैं

---

हम जितने चाहें उतने `else if` स्टेटमेंट जोड़ सकते हैं, कोई सीमा नहीं है
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
और इस कोड का आउटपुट `the number is 4` है।

---

हम एक सशर्त स्टेटमेंट (`if`, `else if` या `else`) को दूसरे सशर्त स्टेटमेंट के अंदर नेस्ट भी कर सकते हैं, ताकि एक अधिक जटिल संरचना बनाई जा सके।
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
और इस कोड का आउटपुट `the number is 4` है।
