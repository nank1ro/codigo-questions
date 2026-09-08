एक **एन्युमरेशन** (या *enum*) संबंधित, निश्चित वैल्यूज़ के एक समूह के लिए एक सामान्य टाइप परिभाषित करता है, जैसे सप्ताह के दिन या ट्रैफ़िक लाइट के रंग।
बिखरी हुई स्ट्रिंग्स या संख्याएँ इधर-उधर घुमाने के बजाय, आप हर वैल्यू को एक **नाम** देते हैं, जिससे कोड अधिक पढ़ने योग्य हो जाता है और टाइपिंग की गलतियाँ एरर बन जाती हैं।
Python में आप `enum` मॉड्यूल से `Enum` इम्पोर्ट करके और उससे इनहेरिट करने वाली एक क्लास घोषित करके एक enum बनाते हैं।
क्लास की प्रत्येक एट्रिब्यूट enum का एक **मेंबर** होता है, जिसका एक नाम और एक वैल्यू होता है:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
परंपरा के अनुसार मेंबर नाम अपर केस में लिखे जाते हैं। आप किसी मेंबर को क्लास के माध्यम से एक्सेस करते हैं, और उसे प्रिंट करने पर क्लास और मेंबर के नाम दिखाई देते हैं:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

enum की हर मेंबर की दो एट्रिब्यूट्स होती हैं: `name`, जो वह आइडेंटिफ़ायर है जो आपने क्लास में लिखा, और `value`, जो वह वैल्यू है जो आपने उसे असाइन की:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
वैल्यू किसी भी टाइप की हो सकती है, केवल पूर्णांक ही नहीं: स्ट्रिंग्स, टुपल्स और फ़्लोट्स आम विकल्प हैं।
मेंबर एक सामान्य ऑब्जेक्ट होता है, इसलिए आप उसे एक वेरिएबल में स्टोर कर सकते हैं और बाद में उसकी एट्रिब्यूट्स पढ़ सकते हैं:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

हर enum मेंबर **केवल एक बार** मौजूद होता है: जब भी आप `Color.RED` लिखते हैं, आपको बिल्कुल वही ऑब्जेक्ट मिलता है।
इसी वजह से आप मेंबर्स की तुलना `is` (आइडेंटिटी) और `==` दोनों से कर सकते हैं, और दोनों एक ही रिज़ल्ट देते हैं:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
कोई मेंबर अपनी रॉ वैल्यू के **बराबर नहीं** होता, क्योंकि एक मेंबर और एक साधारण संख्या अलग-अलग चीज़ें हैं:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
यही enums को सुरक्षित बनाता है: प्रोग्राम में कहीं और से आया `1` `Color.RED` समझा नहीं जा सकता।

---

एक enum क्लास **इटरेबल** होती है: क्लास पर एक `for` लूप हर मेंबर से उनके घोषित होने के क्रम में गुज़रता है:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` बताता है कि enum में कितनी मेंबर्स हैं, और `list(Color)` उनकी एक लिस्ट बनाता है:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
लिस्ट के अंदर मेंबर्स अपने `repr()` के साथ दिखाए जाते हैं, जिसमें वैल्यू एंगल ब्रैकेट्स के बीच होती है।

---

आप किसी मेंबर को उसकी **वैल्यू** से क्लास को फ़ंक्शन की तरह कॉल करके, या उसके **नाम** से स्क्वायर ब्रैकेट्स का उपयोग करके प्राप्त कर सकते हैं:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
दोनों तब काम आते हैं जब वैल्यू या नाम प्रोग्राम के बाहर से आता हो, जैसे किसी फ़ाइल या यूज़र इनपुट से।
अगर कुछ भी मैच नहीं होता, तो `Color(9)` एक `ValueError` उठाता है और `Color["PINK"]` एक `KeyError` उठाता है।

---

अक्सर सटीक वैल्यूज़ मायने नहीं रखतीं: आपको केवल यह चाहिए कि मेंबर्स अलग-अलग हों।
ऐसे में आप `auto()` के साथ वैल्यूज़ चुनने के लिए Python को छोड़ सकते हैं, जिसे भी `enum` मॉड्यूल से इम्पोर्ट किया जाता है।
यह पहली मेंबर को `1` असाइन करता है और फिर गिनता जाता है:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

एक साधारण `Enum` मेंबर की तुलना `<` से नहीं की जा सकती और न ही उसे किसी संख्या में जोड़ा जा सकता है।
जब मेंबर्स ऐसे **लेवल** दर्शाते हैं जिन्हें क्रम में रखने की ज़रूरत होती है, तब इसके बजाय `IntEnum` से इनहेरिट करें: इसकी मेंबर्स पूर्णांक भी होती हैं, इसलिए वे तुलना, अंकगणित और सॉर्टिंग को सपोर्ट करती हैं:
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
कोई `IntEnum` मेंबर अपनी पूर्णांक वैल्यू के बराबर भी होता है: `Priority.LOW == 1` का मान `True` है।

---

`StrEnum` (Python 3.11 से उपलब्ध) `IntEnum` का स्ट्रिंग समकक्ष है: इसकी मेंबर्स स्ट्रिंग्स भी हैं, अपनी वैल्यू के बराबर।
इससे वे वहाँ सुविधाजनक हो जाती हैं जहाँ साधारण स्ट्रिंग्स अपेक्षित होती हैं, जैसे कॉन्फ़िगरेशन कीज़ या API पैरामीटर:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
साधारण `Enum` के विपरीत, किसी `StrEnum` मेंबर को `str()` से या f-string के अंदर टेक्स्ट में बदलने पर उसकी **वैल्यू** मिलती है, `Mode.DARK` नहीं।

---

एक enum एक क्लास है, इसलिए उसमें किसी भी दूसरी क्लास की तरह **मेथड्स** और **प्रॉपर्टीज़** हो सकते हैं।
उनके अंदर, `self` वह मेंबर होता है जिस पर मेथड कॉल किया गया था, इसलिए आप `self.name`, `self.value` देख सकते हैं या `self` की तुलना दूसरी मेंबर्स से कर सकते हैं:
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
क्लास बॉडी में असाइन की गई कोई भी साधारण वैल्यू एक मेंबर बन जाती है, जबकि फ़ंक्शन्स और प्रॉपर्टीज़ कभी नहीं बनते, चाहे वे कहीं भी दिखाई दें।

---

अगर दो मेंबर्स की वैल्यू एक ही हो, तो दूसरी कोई नई मेंबर नहीं होती बल्कि पहली का एक **उपनाम (alias)** होती है:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
इटरेट करते समय उपनाम छोड़ दिए जाते हैं और `len()` उन्हें गिनता नहीं है।
आमतौर पर डुप्लीकेट वैल्यू एक गलती होती है। `enum` से इम्पोर्ट किया गया `unique` डेकोरेटर Python को उसी क्षण एक `ValueError` उठाने पर मजबूर करता है जैसे ही उपनामों वाला कोई enum घोषित होता है:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

एक `Flag` ऐसा enum है जिसकी मेंबर्स को **जोड़ा (combine)** जा सकता है: एक वैल्यू एक साथ कई मेंबर्स रख सकती है, जैसे विकल्पों का एक सेट।
इसकी मेंबर्स को `auto()` से घोषित करें, जो एक `Flag` के लिए दो की घातें (`1`, `2`, `4`, ...) असाइन करता है, ताकि हर कॉम्बिनेशन की एक अलग वैल्यू हो:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
मेंबर्स को जोड़ने के लिए `|`, यह जाँचने के लिए `in` कि कोई मेंबर किसी कॉम्बिनेशन का हिस्सा है, और रिज़ल्टिंग संख्या देखने के लिए `value` का उपयोग करें:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Enums का `match` स्टेटमेंट (Python 3.10 से उपलब्ध) के साथ स्वाभाविक मेल बैठता है, जो एक वैल्यू की तुलना `case` पैटर्न्स की एक श्रृंखला से करता है और पहला मैच होने वाला चलाता है:
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
हमेशा मेंबर को उसकी क्लास के साथ लिखें, जैसे `Light.RED`: `case RED:` जैसा एक खाली नाम कुछ भी तुलना नहीं करेगा, वह बस वैल्यू को एक नए वेरिएबल `RED` में कैप्चर कर लेगा और हर चीज़ से मैच कर देगा।
वाइल्डकार्ड `case _:` डिफ़ॉल्ट है और आखिरी में आना चाहिए, क्योंकि उसके बाद कोई भी पैटर्न कभी नहीं पहुँचा जा सकता।

---

Enum मेंबर्स **हैशेबल** होती हैं, इसलिए उन्हें डिक्शनरी कीज़ और सेट एलिमेंट्स के रूप में उपयोग किया जा सकता है।
किसी enum द्वारा कीड (keyed) डिक्शनरी हर मेंबर से डेटा जोड़ने का एक साफ़ तरीका है, और किसी मेंबर से उसे खोजना एक रॉ स्ट्रिंग उपयोग करने से अधिक सुरक्षित है जिसकी वर्तनी गलत हो सकती है:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
चूँकि मेंबर्स किसी भी कलेक्शन में दिखाई दे सकती हैं, लिस्ट्स, सेट्स और कॉम्प्रिहेंशन्स के बारे में आपकी जानी-मानी हर चीज़ उनके साथ भी काम करती है:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

किसी मेंबर की वैल्यू एक **टुपल** हो सकती है, जिससे आप हर मेंबर से कई डेटा टुकड़े जोड़ सकते हैं।
अगर enum एक `__init__` मेथड परिभाषित करता है, तो Python उसे हर मेंबर के लिए एक बार कॉल करता है, टुपल को उसके पैरामीटर्स में अनपैक करते हुए, ताकि आप हर टुकड़े को उसकी अपनी एट्रिब्यूट में सेव कर सकें:
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
मेंबर की `value` पूरा टुपल ही रहती है।

---

क्लास पर इटरेट करना और मेंबर्स को नाम से खोजना साथ में अच्छी तरह काम करते हैं जब आप बाहर से आने वाला डेटा प्रोसेस करते हैं, जैसे लॉग लाइन्स या कोई फ़ाइल।
क्लास पर एक डिक्शनरी कॉम्प्रिहेंशन हर मेंबर के लिए एक एंट्री तैयार करती है, फिर `Level[name]` हर आने वाली स्ट्रिंग को मैच करने वाली मेंबर में बदलता है:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
चूँकि enum घोषणा का क्रम बनाए रखता है, बाद में `counts` पर इटरेट करना उसी क्रम में मेंबर्स देता है।

---

नियमित मेथड्स के अलावा, एक enum `@classmethod` के साथ **क्लास मेथड्स** भी परिभाषित कर सकता है। उन्हें enum क्लास स्वयं `cls` के रूप में मिलती है, इसलिए वे किसी मेंबर को खोजने के वैकल्पिक तरीकों के लिए सही जगह हैं:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
`auto()`, मेथड्स, प्रॉपर्टीज़ और लुकअप्स के साथ मिलकर, यह आपको ऐसे enums बनाने देता है जो अपना व्यवहार साथ रखते हैं।
