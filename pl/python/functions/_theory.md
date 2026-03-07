Być może zastanawiałeś się nad sytuacją, w której chciałbyś ponownie użyć fragmentu kodu, tylko z kilkoma różnymi wartościami.
Zamiast przepisywać cały kod, znacznie czystszym rozwiązaniem jest zdefiniowanie funkcji, której można następnie używać wielokrotnie.
W Pythonie używamy słowa kluczowego `def`, po którym następuje nazwa funkcji:
```python
def say_hi():
    print("Hello!")
```

---

Nawiasy w __definicji funkcji__ nie muszą być puste.
Możemy w nich określić parametry

---

Czasami chcemy, aby funkcja __zwróciła__ wartość.
Do tego służy słowo kluczowe `return`

---

W funkcjach możemy dodać _opcjonalny komentarz_ wyjaśniający, co funkcja robi:
```python
"""
Prints 'Hello World' to the console.
"""
```
