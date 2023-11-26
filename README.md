# scrapping-service

## Running the application
1. Clone the repository
```bash
  git clone https://github.com/1h3b98/scrapping-service.git
  ```

2. To build the application API with all required software dependencies:

```bash
$ pip install -r requirements.txt

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
  docker-compose up -d --build 
  ```
3. Open swagger on `http://localhost:8080/docs`

## Testing
If you want to run the integration and unit tests locally or on the docker container, you can run the command using pytest
```bash
  $ pytest -v
  ```
To test the code quality, using the installed linter ruff, run the command
```bash
  $ ruff check .
  ```
