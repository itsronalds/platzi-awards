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
