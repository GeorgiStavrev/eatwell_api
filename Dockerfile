FROM python:3.7
COPY ./requirements/base.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["make", "run-prod"]