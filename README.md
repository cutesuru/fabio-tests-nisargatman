# Wikiapp

## What is WikiApp?
Wikiapp is used to perform CRUD operations based on geographical information.

Models Used:
1)Continent
2)Country
3)City

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