# Scout - API
Reach talented people more easily in recruiting 

.env
--------

```
POSTGRES_DB=scout-db
POSTGRES_USER=root
POSTGRES_PASSWORD=*****
```


Migrations and Migrate
--------

```
$docker-compose run --rm app sh -c"python manage.py makemigrations"
$docker-compose run --rm app sh -c"python manage.py migrate"
```

Server Up!
--------

```
 $docker-compose up 
 (0.0.0.0:8000)
```

Test and Lint
--------

```
$docker-compose run --rm app sh -c"python manage.py test && flake8"
```