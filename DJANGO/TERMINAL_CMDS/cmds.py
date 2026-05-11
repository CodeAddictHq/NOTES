#Terminal commends


django-admin startproject projectname/.
#start a project . for creating project in current dir

python manage.py startapp appname
#start a app . for creating oroject in current dir

python manage.py runserver
# runs server

python manage.py makemigrations
#makes a db file to make tables

python manage.py migrate
#makes tabls to db file

python manage.py showmigrations
#shows all histry 

python manage.py createsuperuser
#creates admin 

python manage.py shell
# Shell (testing / ORM)

python manage.py check
# Project check

python manage.py collectstatic
# Static files (production use)

python manage.py dbshell
# Database terminal (if configured)