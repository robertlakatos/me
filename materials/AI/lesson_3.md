---
title: "3. Gyakrolat"
collection: teaching
type: "B.Sc course"
permalink: /materials/AI/lesson_3
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-03-04
location: "Debrecen, Hungary"
---

## Ismétlés

<img src="https://robertlakatos.github.io/me/materials/AI/images/problem.png" alt="Problem">

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

### Gráf

<img src="https://robertlakatos.github.io/me/materials/AI/images/graf.png" alt="Graf">

```python
class Node:
    """Csomópont a kereső fában. 
       Tartalmaz egy mutatót a szülőre (a csomópontra, amelynek ez az utódja) és a 
       csomópont aktuális állapotára. 
       Egy állapotot két útvonalon érünk el, akkor két azonos állapotú csomópont van. 
       Tartalmazza azt a műveletet is, amely ebbe az állapotba juttatott minket, 
       valamint a csomópont eléréséhez szükséges teljes path_cost (más néven g) értéket.
       Más függvények hozzáadhatnak egy f és h értéket; 
       lásd a best_first_graph_search és az astar_search leírását az 
       f és h értékek kezelésének magyarázatához."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Node osztály konstruktora."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        """Speciális metódus mely az objektum string állapotát definiálja"""
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        """Speciálist metódus mely definiálja hogy az adott Node objektum
        mikor kisebb e egy másik Node objektumnál"""
        return self.state < node.state

    def __eq__(self, other):
        """Speciálist metódus mely definiálja hogy az adott Node objektum
        mikor egyenlő egy másik Node objektummal"""
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        """Speciális metódus mely definiálja hogy egy adott Node objektum
        hash állapotát definiálja"""
        return hash(self.state)

    def child_node(self, problem, action):
        """A következő csomópont az adott probléma szerinti elkészítése és visszaadása"""
        next_state = problem.result(self.state, action)
        next_node = Node(state = next_state, 
                         parent = self, 
                         action = action, 
                         path_cost = problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def expand(self, problem):
        """A csomópontból egy lépésben eléhető csomópontok visszadása"""
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def solution(self):
        """A gyökér csomópontól a csompontig terjedő műveletek listájának visszaadása"""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """A gyökér csomópontól a csompontig vezető utvonal csomópontjainak listája"""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
```

### Keresők

<img src="https://robertlakatos.github.io/me/materials/AI/images/trial_error.png" alt="Próba-hiba">

```python
import numpy as np

def trial_error(problem):
    """
    Próba hiba módszer
    """

    # kezdő állapot
    state = Node(problem.initial)

    # végtelen ciklus definiálása
    while True:
        # Ha a probléma megoldva akkor leállítjuk a végtelen ciklust
        if problem.goal_test(state.state):
            print('Got it')
            return state

        # Az alkalmazható operátorok segítsével 
        # gyártsuk le az összes lehetséges utódot 
        succesors=state.expand(problem)

        # Ha nincs új állapot (utód)
        if len(succesors)==0:
            return 'Unsolvable'

        # random választunk egy újat a legyártott utódok közül
        state=succesors[np.random.randint(0,len(succesors))]
        print(state.state)
```

<img src="https://robertlakatos.github.io/me/materials/AI/images/hill_climbing.png" alt="Hegymászó módszer">

## 3 Hanói tornyai

<img src="https://robertlakatos.github.io/me/materials/AI/images/hanoi.png" alt="hanoi">

<img src="https://robertlakatos.github.io/me/materials/AI/images/hanoi_megoldas.png" alt="hanoi_megoldas">

## Állapottér reprezntáció

### Jellemzők

- H1 = {0, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
- H2 = {0, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
- H3 = {0, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}

### Állapotok halmaza

- A ⊆ H1 x H2 x H3
- A = {<a1, a2 , a3 >, <a1, a2, a3> ∈ H1 x H2 x H3 ∧ a1∪a2∪a3={1, 2, 3} ∧ a1∩a2≠0 ∧ a2∩a3≠0 }
- 27 lehetséges állapot

### Kezdő állapot

- a0 = <{1,2,3}, 0, 0>

### Célállapotok

- C = {<0, 0, {1, 2, 3}>}

### Operátorok

- O = {oi,j,k, i ∈{1,2,3} ∧ j ∈{1,2,3} ∧ i ≠j ∧ k ∈{1,2,3}} (18 lehetséges operátor)
- Dom(oi,j,k )={<a1, a2, a3> , <a1, a2, a3> ∈ A ∧ k=min(ai ∪{∞}) ∧ k<min(aj ∪{∞})}
- oi,j,k(<a1, a2, a3>) = <b1, b2, b3>
- Bn, ahol n=1,2,3
    - an ∪ {k}, ha n = j
    - an \ {k}, ha n = i
    - an, egyébként

### Implementáció

```python
from collections import namedtuple
 
Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('Nandini', '19', '2541997')
 
print("Index is :", S[1])
```

```python
State=namedtuple("State", ["disk","char"])

class Hanoi(Problem):
    def __init__(self, n):
        # n darab korongunk van
        self.size = n

        # "1" * n : Kezdő állapot. Hány darab korng van az 1-es rúdon
        # "3" * n : Cél állapot. Hány darab korong van a 2-es rúdon
        super().__init__("1" * n, "3" * n)

    def actions(self, state):
        """Operátorok definiálása"""
        acts = []

        # Nézzük meg az egyes rúdak állapotát
        f1 = state.find("1")
        f2 = state.find("2")
        f3 = state.find("3")
        
        # Ha az 1. rúd nem üres és tartalma kisebb mint ami
        # a 2. rúdon van vagy a 2. rúd üres akkor 
        # 1. rúdról átrakhatunk a második rúdra
        if -1 < f1 and (f1 < f2 or f2 == -1):
            acts.append(State(f1, "2"))

        if -1 < f1 and (f1 < f3 or f3 == -1):
            acts.append(State(f1, "3"))

        if -1 < f2 and (f2 < f1 or f1 == -1):
            acts.append(State(f2, "1"))

        if -1 < f2 and (f2 < f3 or f3 == -1):
            acts.append(State(f2, "3"))

        if -1 < f3 and (f3 < f1 or f1 == -1):
            acts.append(State(f3, "1"))

        if -1 < f3 and (f3 < f2 or f2 == -1):
            acts.append(State(f3, "2"))

        return acts

    def result(self, state, action):
        """Operátorok hatásának definiálása"""

        # diks = korong, char = rúd
        disk, char = action

        # Előtte és utánna lévő korongok helyeinek összefűzése
        return state[0:disk] + char + state[disk + 1:]
```

```python
h = Hanoi(3)

h.size, h.initial, h.goal
```

```python
trial_error(h).solution()
```