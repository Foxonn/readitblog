FROM python:3.8

RUN pip install pipenv

WORKDIR /usr/src/webapp

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system --ignore-pipfile
