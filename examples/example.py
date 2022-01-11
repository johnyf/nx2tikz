"""Dump file containing TikZ code for drawing an example graph.

Alternatively, `nx2tikz` can be called from the command line,
and this script passed as argument:

```python
nx2tikz --input example.py --output out.tex --format tikz
```

or

```python
nx2tikz --input example.py --output out --format pdf
```

or

```python
nx2tikz --input example.py --output out --format tex
```
"""
import networkx as nx
import nx2tikz


def write_tikz():
    fname = 'mygraph'
    g = graph()
    tikz = nx2tikz.dumps_tikz(g)
    print(tikz)
    with open(fname, 'w') as f:
        f.write(tikz)


def graph():
    g = nx.DiGraph()
    # nodes
    g.add_node(1, label='$a$', color='yellow', shape='ellipse')
    g.add_node(2, label='$b$', color='blue', fill='orange', shape='circle')
    g.add_node(3, label='$c$', shape='rectangle')
    g.add_node(4, label='$E=mc^2$')
    g.add_node(5, label=r'$\begin{bmatrix} x_1\\ x_2\\ x_3\end{bmatrix}$')
    # edges
    g.add_edge(1, 2, label=r'$\{p\}$')
    g.add_edge(1, 3, label=r'$\{a,b\}$', color='purple')
    g.add_edge(3, 4, label=r'$\begin{matrix} x=1\\ y=2\\ z=10 \end{matrix}$')
    g.add_edge(4, 5)
    g.add_edge(5, 4, color='red')
    g.add_edge(2, 2, color='blue')
    g.add_edge(4, 1)
    return g


if __name__ == '__main__':
    write_tikz()
