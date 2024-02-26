---
title: "2. Gyakrolat"
collection: teaching
type: "M.Sc course"
permalink: /materials/AI/lesson_2
venue: "University of Debrecen, Department of Data Science and Visualization"
location: "Debrecen, Hungary"
---

## Ismétlés

<img src="https://robertlakatos.github.io/me/materials/AI/images/problem.png" alt="Problem">

<img src="https://robertlakatos.github.io/me/materials/AI/images/graf.png" alt="Graf">

## 3 Korsó

<img src="https://robertlakatos.github.io/me/materials/AI/images/3korso.png" alt="3korso">

### Gondolkodjunk közösen

<video controls><source src="https://robertlakatos.github.io/me/materials/AI/videos/3korso.mp4" type="video/mp4"></video>

### Állapottér reprezntáció

#### Jellemzők

- H1 = {0, 1, 2, 3, 4, 5}, 
- H2 = {0, 1, 2, 3}, 
- H3 = {0, 1, 2}

#### Állapotok halmaza

- A ⊆ H1xH2xH3
- A = {<a1, a2, a3>, <a1, a2, a3> ∈ H1 x H2 x H3 ∧ a1+a2+a3 = 5}
- 12 lehetséges állapot

#### Kezdő állapot:

- a0=<5, 0, 0>

#### Célállapotok:

- C = {< 4, 1, 0 > , < 4, 0, 1 >}
- C = {<a1, a2, a3 >, <a1, a2, a3> ∈ A ∧ a1 = 4}

#### Operátorok:

- O = {o1,2, o1,3, o2,1, o2,3, o3,1, o3,2} = {oi,j , i ∈{1,2,3} ∧ j ∈{1,2,3} ∧ i ≠j} 
- Dom(oi,j)={<a1, a2, a3>, <a1, a2, a3> ∈ A ∧ ai > 0 ∧ aj < max(Hj)}, ahol oi,j ∈ O
- oi,j(<a1, a2, a3>) = <b1, b2, b3>)
- m = min(ai, max(Hj) – aj)
- bk, ahol b=1,2,3
    - ak + m, ha k = j
    - ak - m, ha k = i
    - ak, egyébként


### Programozzunk

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

```python
class Cup3(Problem):
    def actions(self, state):
        """Operátorok definiálása"""
        acts = []
        five, three, two = state
        if five > 0 and three < 3:
            acts.append("5-->3")
        if five > 0 and two < 2:
            acts.append("5-->2")
        if three > 0 and five < 5:
            acts.append("3-->5")
        if three > 0 and two < 2:
            acts.append("3-->2")
        if two > 0 and five < 5:
            acts.append("2-->5")
        if two > 0 and three < 3:
            acts.append("2-->3")
        return acts

    def result(self, state, action):
        """Operátorok hatásának definiálása"""
        five, three, two = state
        if action == "5-->3":
            m = min(five, 3-three)
            return (five-m, three+m, two)
        if action == "5-->2":
            m = min(five, 2-two)
            return (five-m, three, two+m)
        if action == "3-->5":
            m = min(three, 5-five)
            return (five+m, three-m, two)
        if action == "3-->2":
            m = min(three, 2-two)
            return (five, three-m, two+m)
        if action == "2-->5":
            m = min(two, 5-five)
            return (five+m, three, two-m)
        if action == "2-->3":
            m = min(two, 3-three)
            return (five, three+m, two-m)
```

```python
from libs.cup3 import Cup3

c = Cup3((5,0,0), [(4,1,0),(4,0,1)])
```

#### Próba-hiba módszer

<img src="https://robertlakatos.github.io/me/materials/AI/images/trial_error.png" alt="Próba-hiba">

```python
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

```python
print(trial_error(c).solution())
```

#### Hegymászó módszer

<img src="https://robertlakatos.github.io/me/materials/AI/images/hill_climbing.png" alt="Hegymászó">

```python
def hill_climbing(problem, heuristic):
    # kezdő állapot
    state = Node(problem.initial)

    # végtelen ciklus definiálása
    while True:
        # Ha a probléma megoldva akkor leállítjuk a végtelen ciklust
        if problem.goal_test(state.state):
            return state

        # Az alkalmazható operátorok segítsével 
        # gyártsuk le az összes lehetséges utódot 
        succesors=state.expand(problem)

        # keresünk egy jobb állapotott a heurisztikának megfelelően
        test_succesors=[]
        for s_test in succesors:
            if heuristic(state.state)>=heuristic(s_test.state):
                test_succesors.append(s_test)

        # Ha nincs jobb állapot
        if len(test_succesors)==0:
            return 'Unsolvable'

        # ha több azonosan jó van akkor random választunk egyet
        state=test_succesors[np.random.randint(0,len(test_succesors))]
        print(state.state)
```

```python
# A heurisztika lényeg az hogy ha minél több üres korsót találunk 
# annál távolabb vagyunk a megoldástól
def heuristic_calc_empty_jar(State):
    if State==(4,0,1) or State == (4,1,0):
        return 0
    c=0
    for i in State:
        if i == 0:
            c+=1
    return c+1

print(hill_climbing(c, heuristic_calc_empty_jar).solution())
```

```python
for i in range(10):
    print(hill_climbing(c, heuristic_calc_empty_jar).solution())
```

```python
def heuristic_zero(State):
    return 0

print(hill_climbing(c, heuristic_zero).solution())
```