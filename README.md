About
=====

`nx2tikz` is a package for exporting [`networkx`](https://networkx.github.io/) graphs directly to [`TikZ`](https://en.wikipedia.org/wiki/PGF/TikZ), letting [`TikZ` itself layout the graph](http://dx.doi.org/10.7155/jgaa.00301).
Its purpose is to avoid the [`pydot`](https://code.google.com/p/pydot/) -> [`GraphViz`](https://en.wikipedia.org/wiki/PGF/TikZ) -> [`dot2tex`](https://github.com/kjellmf/dot2tex) -> [`dot2texi`](https://github.com/kjellmf/dot2texisty) toolchain, because it is very fragile and inflexible.

Installation
============

Uses `setuptools`:

```
python setup.py install
```

License
=======
[BSD-3](http://opensource.org/licenses/BSD-3-Clause), see `LICENSE` file.