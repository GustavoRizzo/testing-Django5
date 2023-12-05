# testing-Django5

To create the local environment:

````shell
pyenv local && pyenv install
virtualenv --python=`pyenv which python` venv
source venv/bin/activate
pip install pip setuptools --upgrade
pip install -r requirements.txt
````

to run the first time:

````shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
````
