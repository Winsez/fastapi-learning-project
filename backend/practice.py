from fastapi import FastAPI


app = FastAPI()


@app.get("/books/{book_id}")
def winse(
    book_id: int,
    language: str = "en"
):
    return {
        "book_id": book_id,
        "language": language
    }