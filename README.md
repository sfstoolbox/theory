Documentation of the SFS Toolbox
================================

This repository provides the sphinx sources for building the online
documentation.

## Usage

The different parts of the documentation are independently of each other and
have to be compiled independently as well:

```bash
$ cd theory
$ make clean
$ make dirhtml
$ cd ../matlab
$ make clean
$ make dirhtml
$ cd ../pyhton
$ make clean
$ make dirhtml
$ cd ../code_references
$ make clean
$ make dirhtml
```
## License
[Creative Commons Attribution (CC BY
4.0)](https://creativecommons.org/licenses/by/4.0/)

## Credits

This documentation is developed by (in alphabetical order):  
Jens Ahrens, TU Berlin  
Vera Erbes, University of Rostock  
Matthias Geier, University of Rostock  
Nara Hahn, University of Rostock  
Till Rettberg, University of Rostock  
Frank Schultz, University of Rostock  
Sascha Spors, University of Rostock  
Hagen Wierstorf, TU Ilmenau  
Fiete Winter, University of Rostock  
