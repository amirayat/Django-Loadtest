## World Countries
### Django rest api

Simple Application to test performance of Django together with pythonic webservers.

### Required development packages on Ubuntu
```bash
apt-get install python3-dev
apt-get install libpq-dev
apt-get install libev-dev
apt-get install gcc
```

### .env 
```
DB_ENGINE = django.db.backends.postgresql
DB_NAME = ***
DB_USER = ***
DB_PASSWORD = ***
DB_HOST = ***
DB_PORT = ***

DJANGO_SECRET = ***
ALLOWED_HOSTS = *
```

### Deployment commands
+ Gunicorn
```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 10 --worker-class [eventlet|gevent|tornado|gthread] 
``` 
+ Uvicorn
```bash
uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --workers 10 --loop [asyncio|uvloop]
```
+ Hypercorn
```bash
hypercorn core.asgi:application --bind 0.0.0.0:8000 --workers 10 --worker-class [asyncio|uvloop] 
```
+ uWSGI
```bash
uwsgi --module core.wsgi:application --http 0.0.0.0:8000 --workers 10 --gevent 100
```
+ Bjoern
```bash
bjcli core.wsgi -w 10 -i 0.0.0.0 -p 8000
```

### To see full documentation follow this [link](https://medium.com/p/bfe453a6f7ad/edit)