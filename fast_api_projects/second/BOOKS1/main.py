from fastapi import FastAPI

app = FastAPI()



BOOKS = {
    'Book_1':{'title':'Title One','author':"Author One"},
    'Book_2':{'title':'Title Two','author':"Author Two"},
    'Book_3':{'title':'Title Three','author':"Author Three"},
    'Book_4':{'title':'Title Four','author':"Author Four"},

    
}


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title":"My favorite book"}


@app.get("/books/{book_id}")
async def read_book(book_id:int):
    return {"book_tile":book_id}
