コードの一部を、少し異なる値で再利用したい場面を考えたことがあるかもしれません。
コード全体を書き直す代わりに、関数を定義して繰り返し使用する方がはるかにすっきりします。
Cでは`return_type`の後に`function`名を記述します。例えば：
```c
void say_hello() {
    printf("Hello!\n");
}

int main() {
    say_hello();
    // prints "Hello!"
    return 0;
}
```

---

パラメータを指定したい場合、__関数定義__の括弧は空でなくても構いません

---

関数から値を__返したい__場合があります。
そのためには`return`キーワードを使います。

---

関数は複数の入力パラメータを持つことができ、関数の括弧内にカンマで区切って記述します。
```c
void say_hello(char *name, bool new_user) {
  char greet[40] = "Hello ";
  strcat(greet, name);
  if (new_user) {
    strcat(greet, "! Welcome on board :)");
  }
  printf("%s\n", greet);
}

int main() {
    // prints "Hello Tom"
    say_hello("Tom", true);
    return 0;
};
```

---

関数には、その関数が何をするかを説明する_オプションのコメント_を追加できます：
```c
/*
 * Function:  hello_world
 * --------------------
 * prints "Hello, World!" to the screen
 */
function hello_world() {
    printf("Hello, World!\n");
}
```
`//`を使って1行コメントを、`/* */`を使って複数行コメントを書くことができます
