run:
	@gunicorn eatwell_api:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=eatwell_api.settings.development
run-prod:
	@gunicorn eatwell_api:app -b 0.0.0.0:80 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=eatwell_api.settings.production
setup:
	@pip install -r requirements/base.txt

requirements-test:
	@pip install -r requirements/test.txt

test:
	@SIMPLE_SETTINGS=eatwell_api.settings.test py.test eatwell_api

check:
	@flake8
	@isort --check
