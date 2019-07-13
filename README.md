# specific_hash_of_data
Реализован класс, реализующий специфическое хэширование входных данных

На входе: любой объект - строка, число, словарь, объект, массив - всё, что
можно сериализовать и привести к строковому виду.
Для хэширования объекты должны обладать методом dumps, который возврашает данные в формате строки.

На выходе: Массив строк из английских слов (например AlphaBravoCharlie, WhatWonderfulWorld, HaveNiceDay)

Реализована возможность указания следующих параметров:
- количество слов в строке в диапазоне 1-10 ('Alpha', 'AlphaBravo', 'AlphaBravoCharlie', 'AlphaBravoCharlieDelta' и т.д.)
- разделитель (например, один из этих [ '', '-', '_', ' ', ' - ' ... ]: Alpha-Bravo-Charlie, Alpha_Bravo_Charlie, Alpha Bravo
Charlie, Alpha - Bravo - Charlie и т.д.
- количество предлагаемых вариантов

В качестве источника слов использовались данные: https://github.com/dwyl/english-words

Для записка тестов

```
python -m unittest tests/test.py
```

Для того, чтобы запустить решение, выполните следующие строчки кода:

```
from specific_hash import SpecificHash

h = SpecificHash("It is my test")
h.get_hash() # ['Sashoon-Branchiocardiac-Sledgemeter', 'Upclimber-Succeedingly-Caulinary', 'Schizopelmous-Overjacket-Shamim']

h.set_data(["A", "BB", "CCC"])
h.set_count_words(2)
h.get_hash() # ['Gamps-Reviviscency', 'Crocks-Resupination', 'Shallots-Powered']

h.set_data({"name": "Evgenii"})
h.set_count_options(5)
h.get_hash() # ['Habitudes-Interstellar', 'Procondemnation-Voglite', 'Zoologized-Metaphysics', 'Susceptiveness-Ranaria', 'Pronating-Pictograph']
```
