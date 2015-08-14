About
=====

`nx2tikz` is a package for exporting [`networkx`](https://networkx.github.io/) graphs directly to [`TikZ`](https://en.wikipedia.org/wiki/PGF/TikZ), letting [`TikZ` itself layout the graph](http://dx.doi.org/10.7155/jgaa.00301).
Its purpose is to avoid the [`pydot`](https://code.google.com/p/pydot/) -> [`GraphViz`](https://en.wikipedia.org/wiki/PGF/TikZ) -> [`dot2tex`](https://github.com/kjellmf/dot2tex) -> [`dot2texi`](https://github.com/kjellmf/dot2texisty) toolchain, because it is very fragile and inflexible.


Usage
=====

Either `import nx2tikz` or invoke it from the command line.
The input is a Python module that contains a function `graph` that returns a `networkx` graph.

To write a `tikzpicture` as a file:

```shell
nx2tikz --input example.py --output out.tex --format tikz
```

When you include such pictures in your main document, remember to import the necessary TikZ packages in the preamble, and compile with LuaTeX.

To compile with `lualatex` an image as a PDF file:

```shell
nx2tikz --input example.py --output out --format pdf
```


Installation
============

Use `setuptools`:

```shell
python setup.py install
```

the package can be imported, or invoked from the command line as `nx2tikz` (creates an [entry point](https://pythonhosted.org/setuptools/setuptools.html#id8)).


References
==========

[1] Jannis Pohlmann
	[Configurable graph drawing algorithms for the TikZ graphics description language](http://www.tcs.uni-luebeck.de/downloads/papers/2011/2011-configurable-graph-drawing-algorithms-jannis-pohlmann.pdf)
	Diplomarbeit, Universitat zu Lubeck, 2011

[2] Till Tantau
	[Graph drawing in TikZ](http://www.emis.de/journals/JGAA/accepted/2013/Tantau2013.17.4.pdf)
	Journal of graph algorithms and applications
	Vol.17, No.4, pp.495--513, 2013
	[DOI:10.7155/jgaa.00301](http://dx.doi.org/10.7155/jgaa.00301)
	[slides](http://www.tcs.uni-luebeck.de/downloads/mitarbeiter/tantau/2012-gd-presentation.pdf)


License
=======
[BSD-3](http://opensource.org/licenses/BSD-3-Clause), see `LICENSE` file.