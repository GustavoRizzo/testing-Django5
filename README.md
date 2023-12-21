# Demo Django5

## Prepare `.env` file

Make a copy from `.env.example` to `.env` file. Edit and adjust the file. After that, just need to load the environment
variables:

```shell
cp .env.example .env
vi .env
```


## Runnig without docker
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
