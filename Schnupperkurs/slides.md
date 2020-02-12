---
title: Schnupperkurs Programmieren
theme: black
---

# Programmieren für Lektorinnen und Lektoren
```python
for name in anwesende:
    print(f'Willkommen, {name}!')
```
---

# Python für Lektorinnen und Lektoren
```python
for name in anwesende:
    print(f'Willkommen, {name}!')
```

---

# Ablauf
- Vorbemerkungen / Warum Python?
- Python installieren
- Einige Begriffe: _Terminal_, _Shell_, _IDLE_, _Skripte_
- Einfach mal loslegen: >>>
- Gesprächsrunde: Warum das Ganze? Was kann man automatisieren?
- Beispiele
- Feedback

---

# Vorbemerkungen
- uk ist kein Programmierer
- Denglish
- Viele Wege führen zum Ziel
- Lernen aus Fehlern (Wo ist das Phrasenschwein?)
- Von anderen lernen
- Warum Python?

---

# Stricken ist kompliziert

```
RM 1M li 1M re 2M li 1M re 5M li 1M re 2M li 1M re 1M li RM
RM 1M re 1M li 2M re 5M li 1M re 1M li 2M re 1M li 1M re RM
RM 1M li 1M re 2M li 1M re 1M li 5M re 2M li 1M re 1M li RM
RM 1M re 1M li 2M re 1M li 5M re 1M li 2M re 1M li 1M re RM
RM 1M li 1M re 2M li 5M re 1M li 1M re 2M li 1M re 1M li RM
RM 1M re 1M li 2M re 1M li 1M re 5M li 2M re 1M li 1M re RM
RM 1M li 1M re 2M li 1M re 5M li 1M re 2M li 1M re 1M li RM
```

---

# Python ist einfach
```python
for countdown in 5, 4, 3, 2, 1, "los!":
    print(countdown)
```

```python
a = 5
if a == 5:
    print("a ist 5")
else:
    print("a ist nicht fünf")
```

---

# Warum Python?
- Einfach (Syntax und Handling)
- Populär
- große Community
- zahlreiche Tutorials, Bücher, Module ...
- breite Palette an Anwendungen, _von_ ...
  - Verzeichnisse umbenennen _über_
  - Data Science _bis_
  - KI / Machine Learning