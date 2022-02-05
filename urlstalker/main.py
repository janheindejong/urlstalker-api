from fastapi import FastAPI

app = FastAPI()


urls = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/url/")
def get_url() -> list[str]:
    return urls

@app.post("/url/")
def post_url(url: str) -> int: 
    urls.append(url)
