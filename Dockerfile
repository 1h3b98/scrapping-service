FROM python:3.11.6

WORKDIR /src/app


COPY pyproject.toml ./
RUN poetry install --only main

COPY src/main.py src/main.py

CMD [ "uvicorn", "src.main:app" , "--reload", "--host=0.0.0.0"]