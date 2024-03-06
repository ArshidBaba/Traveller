From python:3.10
WORKDIR /app
COPY . /app
RUN pip install poetry
EXPOSE 8001
CMD ["/bin/bash", "-c", " poetry install ; poetry run ./prestart.sh ; poetry run ./run.sh"]