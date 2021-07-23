# Recipe Box

Simple application for all your favorite recipes.

## Deployment

Common steps,

- Clone this repository,
- `cd` into the project repository,

The simplest way to deploy locally is through Docker.

To run with `docker-compose`,

- Run `docker-compose up`

Or, follow these steps to run without docker if you prefer,

- create a virtual environment, `python -m venv env` or `virtualenv env`
- activate environment, `source env/bin/activate`
- using sqlite for local deployment is preferred, comment out or remove line 5 (`mysqlclient==2.0.3`) from `requirements.txt`.
- install requirements, `pip install -r requirements.txt`
- update settings to use sqlite,

In `settings.py` on line 82 you'll find the database settings, replace the entire `DATABASES` dictionary with the following,

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Then run the server with either of `python manage.py runserver` or `gunicorn recipe_box.wsgi`

Your server should be up and running on `localhost:8000` for `manage.py` or `localhost:8080` for docker/gunicorn.
