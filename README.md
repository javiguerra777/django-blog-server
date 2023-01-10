# Blog Server

## Description

This Django Server uses Django-Knox for token authentication. Currently users can sign up to create an account with a profile picture URL. Users can get all posts, create new posts edit their own posts, delete their own posts. View their own posts and view their profile details

## Getting Started

1) clone the repository 
```bash
git clone https://github.com/javiguerra777/django-blog-server.git
```

2) create a new python virtualenv 
```bash
python -m venv env
```
note: make sure you are in the directory of your project

3) start virtual environment
```bash
source env/Scripts/activate
``` 
for windows 
```bash
source env/bin/activate
``` 
for mac

4) install the python dependencies 
```bash
pip install -r requirements.txt
``` 
note: make sure you have a python version of 3.8 or higher installed on your computer

## How to add new depenecies

You won't need to add any dependencies since django is a batteries included framework. But if you need to add any new dependencies
```bash
pip install "name of python dependency"
```
note: make sure the python virtual environment is active

## CMD line prompts and what they do

First cd to project directory
```bash
cd socialmedia
```
How to migrate changes in database when you update models or add new dependencies
```bash
python manage.py migrate
```
How to run the django server
```bash
python manage.py runserver
```
After adding new model to database or editing current model
```bash
python manage.py makemigrations python manage.py migrate
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.