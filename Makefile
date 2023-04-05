dev:
	poetry run python manage.py runserver

install:
	poetry install

seed:
	poetry run python manage.py shell < seed.py

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

lint:
	poetry run flake8 task_manager --exclude=migrations

console:
	poetry run python manage.py shell_plus --ipython
