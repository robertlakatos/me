---
title: "2. Gyakrolat"
collection: teaching
type: "M.Sc course"
permalink: /materials/AI/lesson_3
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-26
location: "Debrecen, Hungary"
---

## 3 N királynői

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen.png" alt="nqueen">

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_megoldas.png" alt="nqueen_megoldas">

### Jellemzők

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_jellemzok.png" alt="nqueen_jellemzok"> 

### Állapotok halmaza

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_allapotok.png" alt="nqueen_allapotok">

### Kezdő állapot

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_kezdo.png" alt="nqueen_kezdo">

### Célállapotok

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_cel.png" alt="nqueen_cel">

### Operátorok

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_logika.png" alt="nqueen_logika">

<img src="https://robertlakatos.github.io/me/materials/AI/images/nqueen_operatorok.png" alt="nqueen_operatorok">

### Implementáció

```python
class NQueens(Problem):
    """N királynő elhelyezésének problémája egy NxN táblán úgy, hogy egyik sem üti a másikat. 
    Egy állapotot N-elemű tömbként ábrázolunk, ahol a c-edik bejegyzésben szereplő r értéke azt jelenti, hogy a 
    c oszlopban, az r sorban van egy királynő, a -1 érték pedig azt, hogy a c-edik oszlop még nem lett kitöltve. 
    Balról jobbra töltjük ki az oszlopokat.
    """

    def __init__(self, N):
        super().__init__(tuple([-1] * N))
        self.N = N

    def actions(self, state):
        """A bal szélső üres oszlopban próbálja ki az összes nem ütköző sort. """
        if state[-1] != -1:
            return []  # Minden oszlop kitöltve;
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        """Helyezze a következő királynőt a megadott sorba."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        """Egy királynő elhelyezése (sor, oszlop) ütközik?"""
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Összeütközésbe kerülne két királynő elhelyezése (sor1, oszlop1) és (sor2, oszlop2)?"""
        return (row1 == row2 or  # ugyanabban a sorban
                col1 == col2 or  # ugyanabban az oszlopban
                row1 - col1 == row2 - col2 or  # ugyanabban az átlóban, irány: \
                row1 + col1 == row2 + col2)  # ugyanabban az átlóban, irány: /

    def goal_test(self, state):
        """Ellenőrizze, hogy minden oszlop megtelt-e és nincs ütközés."""
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))

    def h(self, node):
        """Az ütésben lévő királynők számát adja vissza egy adott csomóponthoz"""
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return num_conflicts
```