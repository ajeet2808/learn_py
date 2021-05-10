>[Install poetry](https://python-poetry.org/docs/#installation)

> Check installed version
```
poetry --version
```
> Check poetry config
```
poetry config --list
```
>Set poetry config for creating virtual env in project folder
```
poetry config poetry config virtualenvs.create true
poetry config poetry config virtualenvs.in-project true
```
> **Create a new project by**
``` 
poetry new pandas-demo
```
>Move to newly created folder and install dependencies
```
cd pandas-demo
poetry install 
```
>To add python package in project (ex- pandas)
```
poetry add pandas
````