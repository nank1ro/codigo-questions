特定の条件が満たされた場合にのみコードを実行したいとき、意思決定が必要になります。
天気が良いときだけ外で遊びたいとしましょう。
プログラミングでは、ブール変数`nice_weather`を保存し、この変数が`true`の場合に外で遊ぶというアクションを`if`で実行できます：
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

前の例の続きを見てみましょう。
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```
`if`文は条件が`true`の場合にのみコードブロックを実行することを見てきました。
もう一つ重要なことは、コードブロックを示す**波括弧**`{}`です。

---

条件が成立した場合にコードブロックを実行する方法を見てきました。次に、最初の条件が成立しなかった場合に別のコードブロックを実行する方法を見てみましょう。
天気が良ければ外で遊び、そうでなければ家にいます。
C言語では`else`文を使うことができます：
```c
bool nice_weather = false;
if (nice_weather) {
    // play outside
} else {
    // stay home
}
```

---

もう一つチェックする条件があるとしましょう。この例のように：
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
このコードの出力は`the number is 3`です。
まず、数値が2に等しいかチェックします。これはfalseです。
次の文に進み、`num`が3に等しいかチェックします。trueなので、次のコードブロックを実行し、`the number is 3`と出力します。

---

`else if`文はいくつでも追加でき、制限はありません
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
このコードの出力は`the number is 4`です。

---

条件文（`if`、`else if`、`else`）を別の条件文の中にネストして、より複雑な構造を作ることもできます。
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
このコードの出力は`the number is 4`です。
