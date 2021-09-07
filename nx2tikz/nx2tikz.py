"""Export NetworkX graphs to TikZ graphs with automatic layout."""
import argparse
import subprocess



def dumps_tikz(g, layout='layered', use_label=True):
    """Return TikZ code as `str` for `networkx` graph `g`."""
    if layout not in ('layered', 'spring'):
        raise ValueError('Unknown layout: {s}'.format(s=layout))
    s = ''
    for n, d in g.nodes(data=True):
        # label
        label = d.get('label', '')
        label = 'as={' + label + '}' if label else ''
        # geometry
        color = d.get('color', '')
        fill = d.get('fill', '')
        shape = d.get('shape', '')
        # style
        style = ', '.join(filter(None, [label, color, fill, shape]))
        style = '[' + style + ']' if style else ''
        # pack them
        s += '{n}{style};\n'.format(n=n, style=style)
    s += '\n'
    if g.is_directed():
        line = ' -> '
    else:
        line = ' -- '
    for u, v, d in g.edges(data=True):
        if use_label:
            label = d.get('label', '')
            color = d.get('color', '')
        else:
            label = str(d)
            color = ''
        if label:
            label = '"' + label + '"\' above'
        loop = 'loop' if u is v else ''
        style = ', '.join(filter(None, [label, color, loop]))
        style = ' [' + style + '] ' if style else ''
        s += str(u) + line + style + str(v) + ';\n'
    tikzpicture = (
        r'\begin{{tikzpicture}}' '\n'
        r'\graph[{layout} layout, sibling distance=5.0cm,'
        # 'edge quotes mid,'
        'edges={{nodes={{ sloped, inner sep=10pt }} }},'
        'nodes={{circle, draw}} ]{{\n'
        '{s}'
        '}};\n'
        r'\end{{tikzpicture}}' '\n').format(
            layout=layout,
            s=s)
    return tikzpicture


def _preamble(layout='layered'):
    """Return preamble and begin/end document."""
    if layout == 'layered':
        layout_lib = 'layered'
    elif layout == 'spring':
        layout_lib = 'force'
    else:
        raise ValueError(
            'Unknown which library contains layout: {s}'.format(s=layout))
    document = (
        '\\documentclass{{standalone}}\n'
        '\\usepackage{{amsmath}}\n'
        '\n'
        '\\usepackage{{tikz}}\n'
        '\\usetikzlibrary{{graphs,graphs.standard,'
        'graphdrawing,quotes,shapes}}\n'
        '\\usegdlibrary{{ {layout_lib} }}\n').format(
            layout_lib=layout_lib)
    return document


def _document(g, layout, use_label):
    """Return `str` that contains a preamble and tikzpicture."""
    tikz = dumps_tikz(g, layout, use_label=use_label)
    preamble = _preamble(layout)
    return (
        '{preamble}\n'
        r'\begin{{document}}' '\n'
        '\n'
        '{tikz}'
        '\\end{{document}}\n').format(
            preamble=preamble,
            tikz=tikz)


def dump_tikz(g, fname):
    """Write TikZ picture as TeX file."""
    s = dumps_tikz(g)
    with open(fname, 'w') as f:
        f.write(s)


def dump_tex(g, fname, use_label=True):
    """Write TeX document (use this as an example)."""
    s = _document(g, layout='layered', use_label=use_label)
    with open(fname, 'w') as f:
        f.write(s)


def dump_pdf(g, fname, use_label=True):
    """Write PDF file, by involing `lualatex`."""
    s = _document(g, layout='layered', use_label=use_label)
    # typeset
    opt = ['lualatex', '--jobname', fname]
    p = subprocess.Popen(opt,
        stdin=subprocess.PIPE,
        universal_newlines=True)
    p.stdin.write(s)
    p.stdin.close()
    p.wait()


def command_line():
    """Entry point for script installed by `setuptools`."""
    description = (
        'Convert a NetworkX graph to TikZ.',
        'Write a function `graph` that returns a `networkx` graph.',
        "Then call `nx2tikz` with that module's name as `--input`.",
        'You can also `import nx2tikz` in your own code.')
    description = '\n'.join(description)
    parser = argparse.ArgumentParser(
        prog='nx2tikz',
        description=description,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '--input', '-i',
        help='import function `graph` from this Python module')
    parser.add_argument(
        '--output', '-o',
        help='write output to this file')
    parser.add_argument(
        '--format', '-f', help='output format',
        choices={'pdf', 'tikz', 'tex'}, default='pdf')
    # run
    opts = parser.parse_args()
    in_fname = opts.input
    out_fname = opts.output
    out_format = opts.format
    # create graph
    try:
        module = dict()
        with open(in_fname, 'r') as f:
            exec(f.read(), module)
    except ImportError:
        raise ImportError(
            'could not find module `{m}`'.format(m=in_fname))
    try:
        g = module['graph']()
    except AttributeError:
        raise AttributeError('could not call function `{m}.graph`'.format(
            m=in_fname))
    # write output
    if out_format == 'pdf':
        dump_pdf(g, out_fname)
    elif out_format == 'tex':
        dump_tex(g, out_fname)
    elif out_format == 'tikz':
        dump_tikz(g, out_fname)
    else:
        raise Exception(
            'Unknow output format: {f}'.format(f=opts.format))


if __name__ == '__main__':
    command_line()
