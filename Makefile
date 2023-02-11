.PHONY: init init-migration build start stop test tox

init:  build start
	@echo "Init done, containers running"

createAdmin: 
	docker compose exec api flask createSuperAdmin
	
build:
	docker compose build

start:
	@mkdir -p db
	docker compose up

stop:
	docker compose down

test:
	docker compose run -v $(PWD)/tests:/code/tests:ro api tox -e test

tox:
	docker compose run -v $(PWD)/tests:/code/tests:ro api tox -e py38

lint:
	docker compose run api tox -e lint
