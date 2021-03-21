run:
	python3 manage.py runserver --settings=base.settings.dev

mg1:
	python3 manage.py makemigrations --settings=base.settings.dev

mg2:
	python3 manage.py migrate --settings=base.settings.dev

sp:
	python3 manage.py shell_plus --settings=base.settings.dev

mg-user:
	python3 manage.py inspectdb --settings=base.settings.dev > user/models.py

