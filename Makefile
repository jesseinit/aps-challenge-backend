prod:
	@echo "Staring Up Production Server"
	gunicorn config.wsgi:application

make-migrations:
	@echo "Generating Migrations"
	python manage.py makemigrations

migrate:
	@echo "Running Migrations"
	python manage.py migrate

dev:
	@echo "Staring Up Dev Server"
	python manage.py runserver
