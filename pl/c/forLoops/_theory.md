Wiemy, jak powtarzać kod za pomocą pętli `while`.
Jak ten program powtarzający instrukcje, aby wyświetlić `hello`
```c
int counter = 0;

while (counter < 5) {
    printf("Hello\n");
    counter++;
}
```
Możemy jednak zrobić to samo za pomocą pętli `for`:
```c
for (int i = 0; i < 5; i++) {
    printf("Hello\n");
}
```

---

W pętli `for` możemy określić, ile razy chcemy, aby nasza pętla się wykonała

---

Możemy użyć `<` aby zapętlić do następnej liczby wyłącznie, lub `<=` aby zapętlić do następnej liczby włącznie

---

Zmienna o nazwie `i` to zmienna licznikowa.
Możemy nadać jej dowolną nazwę.
Liczy, na której iteracji pętli aktualnie się znajdujemy
