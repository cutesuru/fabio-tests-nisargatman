# Wikiapp

##Part 1
-----------------------------------------------------------------------------
## What is WikiApp?
Wikiapp is used to perform CRUD operations based on geographical information.

Models Used:
1)Continent
2)Country
3)City

Application to store geographical data with the following details:
- name,
- population,
- area per sq meter,
- number of hopsitals,
- number of parks,
- number of roads,
- Date of creation,
- Date of updation

It offers the possibility to (from the index view):
- manually add Country,City and Continents,
- see the whole list of Cities,Countries and Continents (in the table)
- offer option and deleting the entries. 

The api view connects to Django Rest Framework and allows:
- checking the whole list of books,
- adding, updating and deleting entries,
- filtering entries using query strings.

Information about the attributes and the api is documented in /doc/build/index.html.

## Deploy
- Source code deployment
- Docker deployment

**Source code deployment**

1.Install the required dependencies

```
python3 -m pip install -r requirements-test.txt
```
2.Run the service

- Run `python manage.py runserver` to start the service


**Container deployment**

1.Run the Dockerfile to install packages and run the django server


<img src="https://static.scarf.sh/a.png?x-pxid=44779bf0-9262-4801-bb88-4a36ee0fdcfe" />


There are some unit tests set up for this project (testing model). To run them use `python manage.py test` command.

##Part 2
-----------------------------------------------------------------------------

Asynchronous call with CRUD operations for geographical data

Modules Used:
1)RabbitMQ
2)Celery

All the aysnchronus task is added in wikiapp/tasks.py.

For creation,there is no need of concurrency condition.

For updation and deletion atomic function is added to prevent race condition.

RabbitMQ installation with choco package:

`choco install rabbitmq` to install rabbitmq

To check background logs of aysnc task:

`celery -A wikiproject.celery worker --loglevel=debug`
