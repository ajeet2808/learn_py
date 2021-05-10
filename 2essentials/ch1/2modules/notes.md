> module - python source file => same as files in os

> package - group of modules => same as folder in os


> When Python imports a module for the first time, it translates its contents into a somewhat compiled shape.

> The file doesn't contain machine code - it's internal Python semi-compiled code, ready to be executed by Python's interpreter. As such a file doesn't require lots of the checks needed for a pure source file, the execution starts faster, and runs faster, too.

> Thanks to that, every subsequent import will go quicker than interpreting the source text from scratch.

> Python is able to check if the module's source file has been modified (in this case, the pyc file will be rebuilt) or not (when the pyc file may be run at once). As this process is fully automatic and transparent, you don't have to keep it in mind.


> When a module is imported, its content is implicitly executed by Python. It gives the module the chance to initialize some of its internal aspects (e.g., it may assign some variables with useful values).

> Note: the initialization takes place only once, when the first import occurs, so the assignments done by the module aren't repeated unnecessarily.


> when you run a file directly, its ```__name__``` variable is set to ```__main__```
```
python module.py
```
>when a file is imported as a module, its ```__name__``` variable is set to the file's name (excluding .py)
```
python main.py
```

# Import module from different folder
> how Python searches for modules. There's a special variable (actually a list) storing all locations (folders/directories) that are searched in order to find a module which has been requested by the import instruction.

> Python browses these folders in the order in which they are listed in the list - if the module cannot be found in any of these directories, the import fails.

>The variable is named path, and it's accessible through the module named sys. This is how you can check its regular value:
```
import sys

for p in sys.path:
    print(p)
```