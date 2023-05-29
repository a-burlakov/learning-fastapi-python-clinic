from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def get_hello_world():
    return {"answer": "Hello World"}
