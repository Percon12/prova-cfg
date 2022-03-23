# Gramáticas EBNF


Considere as gramáticas no formato EBNF abaixo onde símbolos em letras minúsculas são considerados não-terminais e os símbolos em letra maiúsculas são considerados terminais e o símbolo inicial é representado pela letra "s". Produções vazias são representadas por ε.

**G1**
```
s : A s B
  | A B
```

**G2**
```
s : A B s
  | ε
```

**G3**
```
s : r A
r : A B r
  | ε
```

**G4**
```
s : A
  | s s B
```

**G5**
```
s : r 
  | t

t : r A
  | ε

r : t B
  | ε
```

**G6**
```
s : A
  | B
  | r

r : s s
  | ε
```

**Parte I (competência: cfg 4 pts)**

Classifique as sequências de símbolos abaixo de acordo com qual gramática elas pertencem. Uma sequência pode pertencer a mais de uma gramática. Deixamos a letra (a) resolvida no formato esperado para cada resposta.

Mantenha o ε como resposta das strings que não obedecem a nenhuma gramática.

a) AB: G1, G2
b) B: ε
b) ABA: ε
c) ABBA: ε
d) ABABAB: ε
e) BABA: ε
f) AABB: ε
h) AABAB: ε

**Parte II (medalha cfg, se acertar todas)**

Resuma todas as gramáticas acima com uma descrição informal que diga intuitivamente o que cada linguagem representa. Você pode atribuir significados específicos aos símbolos terminais A e B, se necessário.

G1: ...
G2: ...
G3: ...
G4: ...
G5: ...
G6: ...