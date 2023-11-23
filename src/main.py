from fastapi import FastAPI


description= """
    scrapping service. 🚀

    ## /health (Implemented)

    Status of the service. Include instance uptimes

    ## /query (Implemented)

    Run the provided query against a dataset/Parquet file.
    Optionally passing along the client request/span id

    ## /batch (Implemented)

    This allows multiple queries to be sent at once
    and we definitely want the cache advantages of hitting a single node I believe
    - though we do want it to process in parallel if possible

    """

app = FastAPI(description=description)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}