# Platzi Awards

## Create project

### Initialize Python environment

```
# Windows
python -m venv <environment name>

## Use environment
.\venv\Scripts\activate

## Close environment
.\venv\Scripts\deactivate

# Linux
python -m venv <environment name>
python3 -m venv <environment name>

## Use environment
./venv/bin/activate

## Close environment
./venv/bin/deactivate
```

### Create Django Project

```
django-admin startproject <project name>
```

### Run Dev Server

```
py manage.py runserver
```

## Start an App

```
py manage.py startapp <app name>
```

## Django concepts

> - A **project** in Django is a set of **apps**\
> For Example:
> Instagram is considered a project and its components are considered apps in Django: **Feed**, **DM's**, **Reels** and **more**

> - Django is used by default with SQL databases, it can be used with NoSQL databases but it is not optimal

### ORM (Object Relation Mapping) Explanation
The ORM approach consists of converting the entities of a relational or SQL database into objects, relating SQL databases to the OOP programming paradigm.

> This approach is achieved through the creation of models, these models correspond to an entity of the SQL database, these models in the programming are classes
> Whereas, the columns of a database in ORM modeling correspond to the attributes of the class or model

```
# Users model
class Users:

  # Attributes (SQL columns)
  name = None
  email = None
  password = None

  # Constructor
  def __init__():
    pass
```
