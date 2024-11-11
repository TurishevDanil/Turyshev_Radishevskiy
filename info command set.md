## Initial installation of tools and packages

> Note: Creating and using virtual environments.

Сreating venv python [mac].

```sh
python3 -m venv venv
```

Сreating venv python [windows].

```sh


python -m venv .venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.venv\Scripts\Activate.ps1

pip install django==4.2

pip install django-bootstrap-v5

python manage.py runserver

python manage.py makemigration

python manage.py migrate
```

Activating venv python [mac].

```sh
source venv/bin/activate 
```
Activating venv python [windows -> powershell].


Deactivation venv python.

```sh
deactivate
```

> Note: Create and use an application dependency file.

Getting a list of packages used in a project

```sh
pip freeze
```

Recording a list of packages used in the project
```sh
python -m pip freeze > requirements.txt
```

Installing packages used in the project from the list
```sh
python -m pip install -r requirements.txt
```
Basic Django Commands
```sh

django-admin startproject "name project" ->  creating a new project
```