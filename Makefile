create-app:
	python3 manage.py startapp bilelesh
create-migrations:
	python3 manage.py makemigrations bilelesh_app
apply-migrations:
	python3 manage.py migrate
create-superuser:
	python3 manage.py createsuperuser
run:
	python3 manage.py runserver
