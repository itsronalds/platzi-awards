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

> - A **project** in Django is a set of **apps**. For Example: Instagram is considered a project and its components are considered apps in Django: **Feed**, **DM's**, **Reels** and **more**
> - Django is used by default with SQL databases, it can be used with NoSQL databases but it is not optimal
> - The models name must be written in singular

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

## Creating the database
> * We can use [**dbdiagram.io**](https://dbdiagram.io/) to design relational databases

### Structure
dbdiagram code:

```
Table questions {
  QuestionID int [pk, increment]
  QuestionText text
  Date date
}

Table choices {
  ChoiceID int [pk, increment]
  QuestionID int [ref: > questions.QuestionID]
  ChoiceText text
  Votes bigint
}
```

### Design

![database](https://github.com/itsronalds/platzi-awards/assets/77751686/43ccb80b-ce7e-4ce2-bcbb-f92a8ddc38be)

### Using ORM
Commands to create in database the tables from the models encoded in the models folder of a Django app

```
cd platziawardsapp

# Make migrations in polls app
py manage.py makemigrations polls

# Then, migrate the models to the database in SQL code
py manage.py migrate
```

## Django shell

```
py manage.py shell
```

## Database interaction

```
# Create object from the model
from polls.models import Question, Choice
from django.utils import timezone


q = Question(
  question_text='¿Cuál es el mejor curso de Platzi?',
  date=timezone.now()
)

# Save it in the database
q.save()
```

### Queries using ORM

```
from polls.models import Question, Choice

# Find one match using Question model - get method
Question.objects.get(pk=1) # search object with the primary key equal to 1

```

* Using filter method to filter by specific values

```
from polls.models import Question, Choice
from django.utils import timezone

# The __ help to filter by specific values, in this case filter by specific year
Question.objects.filter(date__year=2023)
Question.objects.filter(date__year=timezone.now().year)

# Filter values by __startswith
Question.objects.filter(question_text__startswith='¿Cuál')
```

* Get related values ​​from two tables via foreign key

```
from polls.models import Question, Choice
from django.utils import timezone

# Obtain the Question with the pk=1 and assign it to a variable
q = Question.objects.get(pk=1)

# Get all Choices of the Question 
q.choice_set.all()
```

* Insert related data to another table

```
from polls.models import Question, Choice
from django.utils import timezone

# Insert Choice related to a some Question
q = Question.objects.get(pk=1)

q.choice_set.create(choice_text='Curso Básico de Django')
q.choice_set.create(choice_text='Fundamentos de Ingeniería del Software')
q.choice_set.create(choice_text='Curso de Elixir')

# Show all choices of question
q.choice_set.all()

# Count all choices of question
q.choice_set.count()

# Get choices by it's Question date
Choices.objects.filter(question__date__year=timezone.now().year)
```

Learn about how to make queries using Django ORM:

* [Making queries](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
* [Queries with lookups](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups)
