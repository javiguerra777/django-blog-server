Blog Server

This Django Server uses Django-Knox for token authentication. Currently users can sign up to create an account with a profile picture URL. Users can get all posts, create new posts edit their own posts, delete their own posts. View their own posts and view their profile details

1) start virtual environment python env/Scripts/activate for windows
2) to add new dependencies to project pip install "name of python dependency"

how to install dependencies
first start virtual environment
second run pip install -r requirements.txt

important command line commands
1) cd to project name "ex: cd socialmedia"
2) to migrate run "python manage.py migrate"
3) to run server "python manage.py runserver"
4) to add new model to database "python manage.py makemigrations python manage.py migrate"