run:
	@gunicorn eatwell_api:app --bind localhost:8080 --worker-class aiohttp.worker.GunicornUVLoopWebWorker -e SIMPLE_SETTINGS=eatwell_api.settings.development

setup:
	@pip install -r requirements/base.txt

requirements-test:
	@pip install -r requirements/test.txt

test:
	@SIMPLE_SETTINGS=eatwell_api.settings.test py.test eatwell_api

check:
	@flake8
	@isort --check
