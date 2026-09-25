# install virtual Environment
pip install virtualenv

#create a virtual environment
python -m venv virtualenv_name
python -m venv venv/env
or
virtualenv name
virtualenv env/venv

#activate virtual environment
env\scripts\activate  #for windows

#deactivate virtual environment
deactivate

#install Django
pip install django

# project create
django-admin startproject project_name .  ['.' is optional]


