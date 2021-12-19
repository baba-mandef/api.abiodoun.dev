# {dev} | Backend
Personal website backend.

## Set your environment

```shell script
pip install virtualenv
virtualenv venv -p3
source venv/bin/activate
```

## Run the app

```shell script
python3 manage.py makemigrations
python3 manage.py migrate
python3 mange.py runserver
```
For database, you can work with Sqlite, Mysql or Postgresql.

[Get the front end source code here](https://github.com/shadowcompiler/henri-front)

