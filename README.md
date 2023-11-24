# scrapping-service

## Running the application
1. Clone the repository
```bash
  git clone https://github.com/1h3b98/scrapping-service.git
  ```

2. Poetry

You will need to have Python Poetry installed on your machine to be able to build and run the application in a local virtual environment with all dependencies met.
If you are using Linux, macOS or Windows (WSL), the easiest way to install Poetry is to run the following command:
```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

If you are on Windows, you may want to use the powershell install command
```bash
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

  ```
To build the application API with all required software dependencies:

```bash
$ poetry build
```
To install the API and its dependencies in a virtual environment on your machine:

```bash
$ poetry install
```
To enter the shell with all required software available:

```bash
$ poetry shell
```
3. Run the application using uvicorn
```bash
$ uvicorn src.app:main --reload
```

## Running the application with Docker

1. Clone the repository
```bash
  git clone https://github.com/1h3b98/scrapping-service.git
  ```

2. Using Docker, create your scrapper container
```bash
  docker compose up
  ```
3. Open swagger on `http://localhost:8080/`

## Testing
If you want to run the integration and unit tests locally or on the docker container, you can run the command using pytest
```bash
  $ poetry run pytest -v
  ```
To test the code quality, using the installed linter ruff, run the command
```bash
  $ poetry run ruff check .
  ```
