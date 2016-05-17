Documentation of the SFS Toolbox
================================

This repository provides the sphinx sources for building the online
documentation.

## Usage

To compile the documentation for viewing on your local host (it will still need
an internet connection to load some CSS and JS files), you can execute:

```bash
$ make html-preview
```

The files are then located under `_build/html-preview/latest`.

For the publishable web pages, run

```bash
$ make html
```

After that copy the directory `_build/html/latest` under the `doc/` folder of
the [web page repo](https://github.com/sfstoolbox/sfstoolbox.github.io).

## License
[Creative Commons Attribution (CC BY
4.0)](https://creativecommons.org/licenses/by/4.0/)
