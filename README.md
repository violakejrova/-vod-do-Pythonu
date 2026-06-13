# Úvod do Pythonu – úkoly

Tyto skripty vznikly jako úkoly do předmětu *Úvod do Pythonu*.

## reverse_ascending_runs.py

Rozdělí seznam čísel na vzestupné úseky a každý úsek obrátí.

Příklad:
[5, -7, 10, 4, 2, 0, 8, 1, 3] → [5, 10, -7, 4, 2, 8, 0, 3, 1]

## check_command_pattern.py

Zkontroluje, jestli řetězec odpovídá binárnímu vzoru – každý bit říká,
jestli má být na daném místě písmeno (1) nebo číslice (0).

Příklad:
42 → binárně 101010 → střídá se: číslice, písmeno, číslice, písmeno...
zkontroluj_prikaz(42, "12a0b3e4") → True
zkontroluj_prikaz(101, "ab23b4zz") → False

## longest_unique_substring.py

Hledá nejdelší podřetězec bez opakujících se znaků v textu básně *The Raven* (Edgar Allan Poe).

Příklad průběhu:
1. Načte text ze souboru `raven.txt`
2. Převede ho na malá písmena a odstraní interpunkci, mezery a pomlčky
3. Najde nejdelší podřetězec(e), ve kterých se žádné písmeno neopakuje
4. Vypíše délku a všechny nalezené sekvence
