>pip stands for ```pip installs packages```.

> pip should have been installed with python, if not, install.
```
pip --version
```
> In linux, it could be pip3 and python3    

## pip commands
>Ask for help
>``` 
>pip help
>pip help <operation>
>```

> List all installed pacakges
>```
>pip list
>```

> Know more about installed package
> ```
> pip show <package-name>
> ```

## Installing packages
>If you are a system administartor, you can install using below command
>```
>pip install pygame
>```
>if you are not admin, you can install for current user only by
>```
>pip install --user pygame
>```

>Lets inspect the gygame
>```
>pip show pygame
>```

>Updating installed package
>```
>pip install -U package_name
>```

>To install specific version of package
>```
>pip install package_name==package_version
>```

>Uninstalling a installed package
>```
>pip uninstall <packagename>
>```
