SFS Toolbox -- Theory
=====================

Discussion of the theory of sound field synthesis, see

http://sfstoolbox.org/

This repository holds the sources in reStructuredText/Sphinx format, from which
the online version is generated automatically.

## Usage

In order to generate a version on your local machine run:

```bash
$ sphinx-build -b html -A web=0 -d ./_build/doctrees . ./_build/html-preview/
```

Alternatively you can use the <code>Makefile</code>:

```bash
$ make html-preview
```

The files are then located under `_build/html-preview/latest`.

## License and feedback

If you have questions, bug reports or feature requests, please use the [Issue
Section](https://github.com/sfstoolbox/sfs-documentation/issues) to report them.

[Creative Commons Attribution (CC BY
4.0)](https://creativecommons.org/licenses/by/4.0/)

Copyright (c) 2016 SFS Toolbox Developers
