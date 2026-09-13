A **regular expression** (or **regex**) is a small pattern that describes a shape of text. You use it to answer questions like "does this string contain a number?" or "where does the word `cat` appear?".

In JavaScript the shortest way to write one is a **regex literal**: the pattern between two slashes.
```javascript
const pattern = /cat/;
```
Ordinary characters in a pattern match themselves, so `/cat/` matches the three letters `c`, `a`, `t` anywhere inside a string.

The simplest thing you can do with a pattern is ask whether it appears in a string. The **`test`** method takes the text and returns `true` or `false`:
```javascript
console.log(/cat/.test("the cat sleeps"));
// prints true
console.log(/cat/.test("the dog sleeps"));
// prints false
```
Note that `test` looks for the pattern *somewhere* in the string; the whole string does not have to match.

---

Patterns become useful when they describe a *kind* of character instead of one exact character. A few **escape sequences** cover most needs:
- `\d` any digit, from `0` to `9`
- `\w` any word character: a letter, a digit or `_`
- `\s` any whitespace: a space, a tab, a newline

```javascript
console.log(/\d/.test("room 12"));
// prints true
console.log(/\d/.test("lobby"));
// prints false
```
A **quantifier** says how many times the previous piece may repeat. The most common one is `+`, meaning "one or more":
```javascript
console.log(/\d+/.test("42"));
// prints true
```
So `/\d/` matches a single digit and `/\d+/` matches a run of digits. For a plain `test` the two behave the same, because both only need one digit to be present.

---

A literal like `/\d+/` is fixed once you write it. When the pattern has to be **built at run time**, use the **`RegExp` constructor**, which takes the pattern as a string:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// prints true
```
There is one trap. Inside a string, a backslash starts an escape sequence for the *string*, so it disappears before the regex ever sees it. To put a real backslash in the pattern you must double it:
```javascript
const digits = new RegExp("\\d+");
// the same pattern as /\d+/
```
Writing `new RegExp("\d+")` instead gives the pattern `/d+/`, which matches the letter `d`, not a digit.

Prefer the literal when the pattern is known while writing the code; it is shorter and needs no doubled backslashes.

---

Two more building blocks let you describe almost any shape of text.

A **character class** is a set of characters between square brackets; it matches exactly one of them. A dash writes a range, and a `^` at the start negates the set:
```javascript
/[aeiou]/   // one vowel
/[a-z]/     // one lowercase letter
/[A-Z0-9]/  // one uppercase letter or one digit
/[^0-9]/    // one character that is not a digit
```
**Quantifiers** say how many times the previous piece repeats: `+` one or more, `*` zero or more, `?` zero or one, and `{n}` exactly `n` times.

Finally, **anchors** tie the pattern to the ends of the text: `^` means "start here" and `$` means "end here". Without them a pattern may match anywhere inside the string, so `/\d{2}/.test("abc12def")` is `true`. With both anchors the whole string has to match:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// prints false
console.log(/^\d{2}$/.test("12"));
// prints true
```

---

`test` only says yes or no. To get the matched text itself, call **`match`** on the string:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
When nothing matches, `match` returns `null`. When something matches, it returns an array-like result:
- `match[0]` is the text that was matched
- `match.index` is the position where the match starts
- `match.input` is the whole string that was searched

```javascript
console.log(match[0]);
// prints 42
console.log(match.index);
// prints 6
```
Because the result can be `null`, check it before reading `match[0]`.

---

Since `match` returns `null` when the pattern is absent, reading `match[0]` straight away throws `TypeError: Cannot read properties of null`. Guard it:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
The nullish coalescing operator writes the same guard on one line, because `match?.[0]` is `undefined` when `match` is `null`:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Parentheses around a part of a pattern create a **capture group**: the text that part matched is kept aside so you can read it back.

The groups appear after `match[0]`, numbered from left to right by their opening parenthesis:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// prints 2026-09-12
console.log(match[1]);
// prints 2026
console.log(match[3]);
// prints 12
```
So `match[0]` is always the whole match, and `match[1]`, `match[2]`, ... are the groups. A group that is part of a pattern which does not match at all makes the whole `match` return `null`.

---

Capture only what you need. A group is not just a way to read a piece back; it also tells the reader which part of the pattern matters. In a time pattern where you only want the minutes, group the minutes alone and leave the rest ungrouped:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// prints 35
```
The whole pattern still has to match, so the hours and the seconds are still required; they are simply not captured. Fewer groups mean fewer numbers to keep track of when you read `match[1]`, `match[2]` and so on.

---

Counting parentheses gets tiring, and adding a group in the middle of a pattern renumbers everything after it. A **named group** avoids both problems: write `?<name>` right after the opening parenthesis and read the piece back from `match.groups`:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// prints 2026
console.log(match.groups.month);
// prints 09
```
Named groups are still numbered, so `match[1]` keeps working, but `match.groups.year` says what the value means. When the pattern has no named group at all, `match.groups` is `undefined`.

---

Everything so far stopped at the first match. **Flags**, written after the closing slash of a literal, change that and other details of the search:
- `g` global: find every match, not just the first
- `i` ignore case, so `/cat/i` also matches `Cat` and `CAT`

With the `g` flag, `match` behaves differently: it returns a plain array of the matched **strings**, without `index` and without groups, or `null` when there is no match:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// prints [ '1', '22', '333' ]
console.log(numbers.length);
// prints 3
```
Flags can be combined in any order, as in `/cat/gi`. With the `RegExp` constructor they go in the second argument: `new RegExp("\\d+", "g")`.

---

The `g` flag gives you every matched string, but it throws the groups away. When you need the groups of *every* match, use **`matchAll`**. It returns an iterator of full match objects, each one exactly like the result of a plain `match`:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// prints a -> 1
// prints b -> 2
```
`matchAll` requires the `g` flag; without it, it throws a `TypeError`. Because it returns an iterator, spread it with `[...text.matchAll(pattern)]` when you want a real array, and note that it yields nothing at all when the pattern never matches.

---

**`replace`** returns a new string with the match swapped for something else. The original string is never changed.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// prints the dog sleeps
```
Inside the replacement string a few sequences have a special meaning:
- `$1`, `$2`, ... the text captured by group 1, group 2, ...
- `$<name>` the text captured by a named group
- `$&` the whole match

That is what makes `replace` a rewriting tool and not only a swap:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// prints 12/09/2026
```
Without the `g` flag only the **first** match is replaced.

---

To rewrite **every** match instead of the first one you have two options:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// prints a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// prints a# b#
```
**`replaceAll`** is the clearer of the two, and it also accepts a plain string as the pattern. When you give it a regex, that regex **must** carry the `g` flag, otherwise it throws a `TypeError`; this is exactly what stops the silent bug of writing `replace` and only fixing the first match.

---

The replacement does not have to be a string. When you pass a **function**, it is called once per match and whatever it returns is inserted in place of that match.

The function receives the whole match first, then each capture group:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// prints 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// prints Ann Lee
```
This is the only way to compute the replacement from the matched text, which `$1` alone cannot do.

---

**`split`** cuts a string into an array. Given a plain string it cuts on that exact text, but given a regex it cuts on every match of the pattern, which lets one call handle separators that vary:
```javascript
console.log("a, b;c".split(", "));
// prints [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// prints [ 'a', 'b', 'c' ]
```
The separators themselves are not part of the result. Watch out for a separator at the start or the end of the string: it produces an empty string in the array, because there is an empty field on that side.

---

One last flag completes the set. By default `^` and `$` mean the start and the end of the **whole string**, so a pattern anchored with `^` can only match at the very beginning, even when the text has several lines.

The **`m`** (multiline) flag changes that: `^` and `$` then also match right after and right before every newline, so each line is anchored on its own:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// prints [ 'note a' ]
console.log(text.match(/^note.*/gm));
// prints [ 'note a', 'note c' ]
```
Two details matter here. By default the `.` does not match a newline (only the `s` flag changes that), so `.*` stops at the end of the line by itself. And `match` with the `g` flag returns `null`, not an empty array, when nothing matches, so pair it with `?? []` when you promise to return an array.
