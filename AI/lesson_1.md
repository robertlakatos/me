---
title: "1. Gyakrolat"
collection: teaching
type: "M.Sc course"
permalink: /AI/lesson_1
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024
location: "Debrecen, Hungary"
---

1. hét	<ins><b>Állapottér reprezentáció, Problem és Node osztály implelemtálása</ins></b>
2. hét  Hagyományos rejtvények - 3 korsó probléma
3. hét	Hagyományos rejtvények - Hanói tornyai, 8 királynő
4. hét	Hagyományos rejtvények - Nem informált algoritmusok
5. hét	Hagyományos rejtvények - informált algoritmusok - A*
6. hét	1. Zárthelyi dolgozat
7. hét	Kényszerkielégítéses feladatok
8. hét	Lépésajánló min-max módszer, alfa béta vágás
9. hét	Szünet
10. hét	Naiv Bayes osztályozó
11. hét	Neurális hálók
12. hét	Megerősítéses tanulás I.
13. hét	Megerősítéses tanulás II.
14. hét	2. Zárthelyi dolgozat
15. hét	Pót zárthelyi dolgozat


## Probléma

![Problem]("/images/problem.png")

```python
class Problem:
    """A formális problémát leíró absztrakt osztálya.
    Az __init__, goal_test és path_cost metódusok adott esetben felülírhatók. 
    A létrehozzott alosztály példányai, megoldhatók a különféle keresési funkciókkal."""

    def __init__(self, initial, goal=None):
        """Konstruktor. Szükség esetén további tulajdonságokkal bővíthető"""
        # kezdő állapot
        self.initial = initial 

        # cél állapot
        self.goal = goal

    def actions(self, state):
        """Az adott állapotban végrehajtható műveletek visszaadásár szolgáló metódus. 
        Az eredmény általában egy lista, de ha sok művelet van, akkor célszerű lehet 
        iterátor alkalmazás a teljes lista vissza adása helyett."""
        raise NotImplementedError

    def result(self, state, action):
        """Azt az állapotot adja vissza, amely az adott művelet adott állapotban 
        történő végrehajtásából adódik.A cselekvésnek a self.actions(state) egyikének kell lennie."""
        raise NotImplementedError

    def goal_test(self, state):
        """Igaz értékkel tér vissza, ha az adott állapot egy cél állapot. 
        Az alapértelmezett metódus összehasonlítja az állapotot a self.goal-al, 
        vagy ellenőrzi a self.goal állapotát, ha az egy lista, a konstruktorban megadottak szerint. 
        A módszer felülírása szükséges lehet, ha nem elegendő egyetlen self.goal összehasonlítása."""
        if isinstance(self.goal, list):
            for s in self.goal:
                if s==state:
                    return True

            return False
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Egy olyan megoldási útvonal költségét adja vissza.
        Ha a probléma olyan, hogy az elérési út nem számít, ez a függvény csak az állapot2-t nézi. 
        Ha az elérési út számít, figyelembe veszi a c-t, esetleg az állapot1-et és az akciót. 
        Az alapértelmezetten a költség 1 az elérési út minden lépéséért."""
        return c + 1

    def value(self, state):
        """Optimalizálási problémák esetén minden állapotnak van értéke. 
        A hegymászó és más hasonló algoritmusok megpróbálják maximalizálni ezt az értéket."""
        raise NotImplementedError
```

```python
from libs.problem import Problem

problem = Problem((5,0,0), [(4,1,0),(4,0,1)])
problem.initial, problem.goal
```

![Problem]("/images/graf.png")

```python
from libs.problem import Problem

problem = Problem((5,0,0), [(4,1,0),(4,0,1)])
problem.initial, problem.goal
```

```python
from libs.node import Node
```

```python
# __repr__
state2 = Node(state=2, parent=state1)
# print(state2)
state2
```

```python
# __eq__
print(state1 is object)
```

```python
# __hash__
state1 = Node(1)
hash(state1)
```