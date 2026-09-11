कुछ संक्रियाओं में समय लगता है: फ़ाइल पढ़ना, सर्वर को कॉल करना, टाइमर का इंतज़ार करना। Python `asyncio` मॉड्यूल के साथ ऐसे कोड को **एसिंक्रोनस रूप से** चला सकता है, ताकि एक टास्क दूसरों को ब्लॉक किए बिना इंतज़ार कर सके।

`async def` से परिभाषित फ़ंक्शन एक **कोरूटीन फ़ंक्शन** होता है। इसे कॉल करने पर इसकी बॉडी नहीं चलती: यह एक **कोरूटीन ऑब्जेक्ट** लौटाता है जो किए जाने वाले कार्य का वर्णन करता है। `asyncio.run(coro)` एक इवेंट लूप शुरू करता है, कोरूटीन को पूरा चलाता है और फिर लूप को रोक देता है:
```python
import asyncio

async def greet():
    print("hello")

asyncio.run(greet())  # hello
```
`asyncio.run` एक एसिंक्रोनस प्रोग्राम का एंट्री पॉइंट होता है और इसे साधारण सिंक्रोनस कोड से केवल एक बार कॉल किया जाता है।

---

एक कोरूटीन पैरामीटर ले सकता है और साधारण फ़ंक्शन की तरह ही `return` कर सकता है। कोरूटीन ऑब्जेक्ट बनाते समय वह मान उपलब्ध नहीं होता, केवल कोरूटीन के चलने के बाद ही मिलता है। `asyncio.run` वह मान लौटाता है जो कोरूटीन ने लौटाया हो:
```python
import asyncio

async def double(n):
    return n * 2

result = asyncio.run(double(21))
print(result)  # 42
```
फ़ंक्शन के बारे में जो कुछ भी आप जानते हैं वह `async def` के अंदर भी लागू होता है: लोकल वेरिएबल, शर्तें, लूप और एक से अधिक `return` कथन।

---

`await` वर्तमान कोरूटीन को तब तक रोक देता है जब तक awaited संक्रिया पूरी न हो जाए, और फिर उसका परिणाम लौटा देता है। जिस दौरान कोरूटीन रुका रहता है, इवेंट लूप अन्य कोरूटीन चलाने के लिए स्वतंत्र रहता है। `await` केवल `async def` के अंदर ही अनुमत है।

`asyncio.sleep(seconds)` सबसे सरल awaitable है: यह लूप को ब्लॉक किए बिना दिए गए समय तक इंतज़ार करता है। `time.sleep` के विपरीत, इसे await किया जाना ज़रूरी है:
```python
import asyncio

async def countdown():
    print("ready")
    await asyncio.sleep(0.05)
    print("go")

asyncio.run(countdown())
```
प्रोग्राम `ready` प्रिंट करता है, 50 मिलीसेकंड इंतज़ार करता है और `go` प्रिंट करता है। `asyncio.sleep(0.05)` को `await` के बिना लिखने पर कोरूटीन ऑब्जेक्ट तो बनता है लेकिन वह कभी नहीं चलता, इसलिए कोई इंतज़ार नहीं होता।

---

कोरूटीन फ़ंक्शन को कॉल करना ही उसे चलाने के लिए पर्याप्त नहीं है। कॉल केवल एक कोरूटीन ऑब्जेक्ट बनाता है; उसकी बॉडी तभी चलती है जब उस ऑब्जेक्ट को await किया जाए या उसे `asyncio.run` को पास किया जाए:
```python
async def hello():
    print("hi")

hello()  # nothing is printed
```
Python इस पर चेतावनी भी देता है: `RuntimeWarning: coroutine 'hello' was never awaited`। भूला हुआ `await` सबसे आम एसिंक्रोनस बग है: कोड कॉल किया हुआ दिखता है लेकिन कभी निष्पादित नहीं होता, और जो वेरिएबल उसका परिणाम रखना चाहिए, वह उसकी जगह एक कोरूटीन ऑब्जेक्ट रखता है।

---

कोरूटीन एक-दूसरे को `await` से कॉल करते हैं। एक कोरूटीन किसी भी दूसरे कोरूटीन को await कर सकता है, उसका रिटर्न मान प्राप्त कर सकता है और आगे बढ़ सकता है, बिल्कुल फ़ंक्शन कॉल की श्रृंखला की तरह:
```python
import asyncio

async def fetch_price(item):
    await asyncio.sleep(0.01)  # simulates a slow lookup
    return 10

async def total(item, quantity):
    price = await fetch_price(item)
    return price * quantity

print(asyncio.run(total("pen", 3)))  # 30
```
केवल सबसे बाहरी कोरूटीन `asyncio.run` से गुजरता है; हर भीतरी कोरूटीन तक `await` से पहुँचा जाता है। यदि `total` एक साधारण `def` होता, तो वह `await` बिल्कुल इस्तेमाल नहीं कर सकता था: `async` कीवर्ड श्रृंखला के हर उस फ़ंक्शन तक फैल जाता है जिसे इंतज़ार करना होता है।

---

कोरूटीन को एक के बाद एक await करने पर वे **क्रमिक (sequential)** रूप से चलते हैं: 10 मिलीसेकंड के तीन इंतज़ार में 30 मिलीसेकंड लगते हैं। `asyncio.gather` कई कोरूटीन को **समानांतर (concurrent)** रूप से चलाता है: जब एक सो रहा होता है, तब दूसरे आगे बढ़ते हैं, इसलिए तीनों इंतज़ार कुल मिलाकर लगभग 10 मिलीसेकंड लेते हैं। यह परिणामों की एक लिस्ट लौटाता है जो आर्ग्युमेंट्स के क्रम में होती है:
```python
import asyncio

async def double(n):
    await asyncio.sleep(0.01)
    return n * 2

async def main():
    results = await asyncio.gather(double(1), double(2), double(3))
    print(results)  # [2, 4, 6]

asyncio.run(main())
```
`gather` को खुद भी await करना ज़रूरी है, और यह कोरूटीन को अलग-अलग आर्ग्युमेंट्स के रूप में लेता है। लिस्ट पास करने के लिए उसे अनपैक करें: `asyncio.gather(*coroutines)`।

---

जब संक्रियाओं की संख्या तय न हो, तब कॉन्करेंसी (समानांतर निष्पादन) फ़ायदेमंद होती है। कोरूटीन ऑब्जेक्ट को एक लिस्ट कॉम्प्रिहेंशन में बनाएँ, उन्हें `gather` में अनपैक करें और पूरे बैच का एक साथ इंतज़ार करें:
```python
import asyncio

async def fetch(url):
    await asyncio.sleep(0.02)
    return len(url)

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(u) for u in urls])

print(asyncio.run(fetch_all(["a.com", "bb.com"])))  # [5, 6]
```
दस urls कुल मिलाकर 200 की जगह अब भी लगभग 20 मिलीसेकंड लेते हैं, और परिणाम urls के क्रम में ही रहते हैं।

---

`gather` के साथ कोरूटीन हर `await` पर अपनी बारी लेते हैं। एक कोरूटीन तब तक चलता है जब तक वह किसी ऐसी चीज़ को await न करे जो अभी तैयार न हो, फिर लूप दूसरे कोरूटीन पर स्विच कर देता है। इसलिए `print` जैसे साइड इफ़ेक्ट उस क्रम में होते हैं जिस क्रम में कोरूटीन **फिर से चलना शुरू (resume)** होते हैं, न कि उस क्रम में जिसमें वे पास किए गए थे:
```python
import asyncio

async def step(name, delay):
    await asyncio.sleep(delay)
    print(name)
    return name

async def main():
    print(await asyncio.gather(step("a", 0.03), step("b", 0.01)))

asyncio.run(main())
```
यह पहले `b`, फिर `a`, और फिर `['a', 'b']` प्रिंट करता है: `b` पहले जागता है, लेकिन परिणामों की लिस्ट आर्ग्युमेंट क्रम बनाए रखती है।

---

एक छोटा एसिंक्रोनस प्रोग्राम एक निश्चित आकार का होता है: `asyncio` को इंपोर्ट करें, कोरूटीन फ़ंक्शन परिभाषित करें, एक `main` कोरूटीन परिभाषित करें जो उन्हें await करे, और अंत में `asyncio.run(main())` को केवल एक बार कॉल करें।

---

`asyncio.create_task(coro)` एक कोरूटीन को एक **टास्क** में लपेटता है और उसे बैकग्राउंड में चलने के लिए शेड्यूल करता है। `await` के विपरीत, यह तुरंत लौट जाता है, इसलिए वर्तमान कोरूटीन टास्क के चलते समय अपना काम जारी रख सकता है। टास्क वास्तव में तब शुरू होता है जब वर्तमान कोरूटीन अगली बार किसी `await` पर रुकता है। बाद में टास्क को await करने पर उसका परिणाम मिलता है:
```python
import asyncio

async def background():
    print("task started")
    await asyncio.sleep(0.01)
    return "task done"

async def main():
    task = asyncio.create_task(background())
    print("main continues")
    print(await task)

asyncio.run(main())
```
यह पहले `main continues` प्रिंट करता है, क्योंकि `background` तभी शुरू होता है जब `main` await करता है, और फिर `task started` तथा `task done` प्रिंट होता है।

---

एक टास्क तब भी चलता रहता है चाहे कोई उसका इंतज़ार कर रहा हो या नहीं। उसे पहले बना लें, दूसरा काम करें, और उसे `await` केवल उस बिंदु पर करें जहाँ उसके परिणाम की ज़रूरत हो: इंतज़ार छोटा हो जाता है क्योंकि टास्क का कुछ हिस्सा पहले ही बैकग्राउंड में चल चुका होता है। टास्क की जाँच `task.done()` से भी की जा सकती है, जो उसके पूरा होने पर `True` लौटाता है।

---

कोरूटीन के अंदर उठाया गया अपवाद उस जगह नहीं दिखता जहाँ कोरूटीन ऑब्जेक्ट बनाया गया था: यह उस `await` पर उठता है जो उसे चलाता है, या सबसे बाहरी कोरूटीन के लिए `asyncio.run` द्वारा। इसलिए `try`/`except` को **`await`** को लपेटना (wrap) होता है:
```python
import asyncio

async def load(path):
    await asyncio.sleep(0.01)
    if path == "":
        raise FileNotFoundError("empty path")
    return "contents"

async def safe_load(path):
    try:
        return await load(path)
    except FileNotFoundError:
        return ""

print(asyncio.run(safe_load("")))  # prints an empty line
```
कोई अपवाद जिसे कोई नहीं पकड़ता, वह हर `await` से होता हुआ `asyncio.run` तक फैलता है, जो उसे सिंक्रोनस कोड में दोबारा उठा देता है, बिल्कुल साधारण कॉल स्टैक की तरह।

---

जब `gather` को पास किए गए किसी कोरूटीन में अपवाद उठता है, तो वह अपवाद `await asyncio.gather(...)` लाइन तक फैल जाता है और बाकी के परिणाम खो जाते हैं, हालाँकि वे चलते रहते हैं। `return_exceptions=True` पास करने पर यह बदल जाता है: `gather` कभी अपवाद नहीं उठाता, और अपवाद ऑब्जेक्ट लिस्ट में गुम हुए परिणाम की जगह ले लेता है:
```python
import asyncio

async def ok():
    return 1

async def fail():
    raise ValueError("bad")

async def main():
    results = await asyncio.gather(ok(), fail(), return_exceptions=True)
    print(results)  # [1, ValueError('bad')]

asyncio.run(main())
```
फिर हर एलिमेंट की जाँच `isinstance(result, Exception)` से की जा सकती है ताकि विफलताओं को मानों से अलग किया जा सके।

---

`asyncio.wait_for(awaitable, timeout)` किसी चीज़ का इंतज़ार करता है लेकिन `timeout` सेकंड के बाद हार मान लेता है: संक्रिया रद्द कर दी जाती है और एक `TimeoutError` उठाया जाता है, जिसे किसी भी अपवाद की तरह पकड़ा जा सकता है:
```python
import asyncio

async def slow():
    await asyncio.sleep(0.05)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow(), timeout=0.01)
        print(result)
    except TimeoutError:
        print("timed out")

asyncio.run(main())  # timed out
```
`0.1` के टाइमआउट के साथ वही कोड `done` प्रिंट करता। `asyncio.TimeoutError` बिल्ट-इन `TimeoutError` का दूसरा नाम है।

---

विफल हो रहे कोरूटीन को संभालना सिंक्रोनस पैटर्न जैसा ही है: कोरूटीन अपवाद उठाता है, कॉलर `await` को `try`/`except` में लपेटता है और तय करता है कि एरर ऑब्जेक्ट का क्या करना है, उदाहरण के लिए उसका संदेश `print(e)` से प्रिंट करना।

---

ये सभी हिस्से सहज रूप से आपस में जुड़ते हैं। कई संक्रियाएँ समानांतर रूप से चलाने के लिए, हर एक की अपनी समय सीमा के साथ, हर संक्रिया को एक छोटे कोरूटीन में लपेटें जो `wait_for` लागू करे और `TimeoutError` को पकड़े, फिर सभी रैपर को `gather` करें:
```python
async def guarded(coro, limit):
    try:
        return await asyncio.wait_for(coro, timeout=limit)
    except TimeoutError:
        return None
```
`gather(*[guarded(job(x), limit) for x in items])` फिर समय पर पूरा होने वाले हर जॉब के लिए एक मान और समय पर पूरा न होने वाले हर जॉब के लिए `None` लौटाता है, मूल क्रम में, और पूरा बैच अधिकतर लगभग `limit` सेकंड लेता है।
