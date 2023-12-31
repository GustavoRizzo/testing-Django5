# Demo Django5

## Prerequisites

- [Docker](https://www.docker.com/)
- [Make](https://www.gnu.org/software/make/)


## Prepare `.env` file

Make a copy from `.env.example` to `.env` file. Edit and adjust the file. After that, just need to load the environment
variables:

```shell
cp .env.example .env
vi .env
```

## Run aplication with Docker and Makefile

```shell
make up # production
make up-dev # development
```

On the first time running the application:

```shell
make setup
```

## Run application locally (without docker)

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
