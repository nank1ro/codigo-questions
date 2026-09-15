---
language: dart
exerciseType: 1
difficulty: 2
title: बबल सॉर्ट
---

# --description--

बबल सॉर्ट सबसे सरल सॉर्टिंग एल्गोरिदम में से एक है। यह एक सूची से गुज़रता है और आसन्न तत्वों के हर जोड़े की तुलना करता है, और जब भी वे गलत क्रम में होते हैं तो उन्हें आपस में बदल देता है। हर पूरे चक्र के बाद सबसे बड़ा शेष मान "बुलबुले" की तरह अपनी अंतिम जगह पर पहुँच जाता है, और जैसे ही कोई चक्र बिना एक भी अदला-बदली के पूरा होता है, सूची क्रमबद्ध हो जाती है।

# --instructions--

`bubbleSort` नाम का एक फ़ंक्शन लिखें जो एक `List<int>` लेता है और उन्हीं मानों के साथ एक **नई** सूची आरोही क्रम में क्रमबद्ध करके लौटाता है। पास की गई सूची में बदलाव नहीं होना चाहिए।

आपको बबल सॉर्ट एल्गोरिदम स्वयं लागू करना होगा, आसन्न तत्वों की तुलना करके और उन्हें आपस में बदलकर। मानक लाइब्रेरी के किसी सॉर्टिंग फ़ंक्शन का उपयोग न करें।

आपका फ़ंक्शन एक खाली सरणी, एक ही तत्व वाली सरणी, पहले से क्रमबद्ध सरणी, दोहराए गए मानों और ऋणात्मक संख्याओं के साथ भी काम करना चाहिए।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(bubbleSort([3, 1, 2]));
// [1, 2, 3] प्रिंट करता है
```

# --seed--

```dart
List<int> bubbleSort(List<int> arr) {
    
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

एक खाली सरणी को एक खाली सरणी लौटानी चाहिए

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

एक ही तत्व वाली सरणी वैसी ही रहनी चाहिए

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

पहले से क्रमबद्ध सरणी उसी क्रम में रहनी चाहिए

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

उल्टे क्रम में क्रमबद्ध सरणी को आरोही क्रम में बदलना चाहिए

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

दोहराए गए सभी मान बने रहने चाहिए

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

ऋणात्मक संख्याओं को धनात्मक संख्याओं से पहले क्रमबद्ध होना चाहिए

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

एक लंबी मिश्रित सरणी आरोही क्रम में क्रमबद्ध होनी चाहिए

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

पास की गई सूची में बदलाव नहीं होना चाहिए

```dart
    test("test8", () {
      final original = [3, 1, 2];
      bubbleSort(original);
      expect(original, [3, 1, 2], reason: "--err-t8--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
List<int> bubbleSort(List<int> arr) {
    final result = List<int>.from(arr);
    var end = result.length;
    var swapped = true;
    while (swapped) {
        swapped = false;
        for (var i = 1; i < end; i++) {
            if (result[i - 1] > result[i]) {
                final temp = result[i - 1];
                result[i - 1] = result[i];
                result[i] = temp;
                swapped = true;
            }
        }
        end--;
    }
    return result;
}
```
