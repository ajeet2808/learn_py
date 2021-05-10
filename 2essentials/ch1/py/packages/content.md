> packages, like modules, may require initialization.

> The initialization of a module is done by an unbound code (not a part of any function) located inside the module's file. As a package is not a file, this technique is useless for initializing packages.

> You need to use a different trick instead - Python expects that there is a file with a very unique name inside the package's folder: ```__init__.py```.

> The content of the file is executed when any of the package's modules is imported. If you don't want any special initializations, you can leave the file empty, but you mustn't omit it.