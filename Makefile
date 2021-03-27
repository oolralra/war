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


collect:
	python3 manage.py collectstatic --settings=base.settings.dev

docker:
	docker build -t private_lesson:dev .
	docker tag private_lesson:dev tjdntjr123/private_lesson:dev
	docker push tjdntjr123/private_lesson:dev


port:
	docker pull tjdntjr123/private_lesson:dev
	docker stop dev
	docker run --rm --env-file ./.env.prod -p 8000:8001 -d --name dev tjdntjr123/private_lesson:dev
