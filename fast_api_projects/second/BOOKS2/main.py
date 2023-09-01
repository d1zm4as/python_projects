
from typing import Optional
from fastapi import FastAPI,HTTPException
# from enum import Enum
from pydantic import BaseModel, Field
from uuid import UUID
app = FastAPI()

class Book(BaseModel):
    id:UUID
    title:str = Field(min_length = 1)
    author:str = Field(min_legth = 1,max_length = 100)
    description:Optional[str] = Field(title = 'Description of the book', max_length = 100,min_length = 1)
    rating:int = Field(gt=-1,lt=101)

    class Config:
        schema_extra = {
            "example":{
                "id": "34f773f87-c8f2-46ea-ba20-a8f484d7af47",
                "title": "sla um exemplo ai",
                "author": "o autor é quem escreveu o livro tlgd",
                "description":"Descrevendo a descrição?!",
                "rating":55
            }
        }




BOOKS = []

@app.get("/")
async def read_all_books(books_to_return:Optional[int] = None):
    if len(BOOKS)<1:
        create_book_no_api()
    if books_to_return and len(BOOKS)>= books_to_return >0:
        i = 1
        new_books =[]
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i+=1
        return new_books
    return BOOKS

@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.put("/{book_id}")
async def update_book(book_id: UUID, book:Book):
    counter = 0

    for x in BOOKS:
        counter+=1
        if x.id == book_id:
            BOOKS[counter-1] = book
            return BOOKS[counter-1]




@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter = 0
    for x in BOOKS:
        counter+=1
        if x.id == book_id:
            del BOOKS[counter-1]
            return f"ID:{book_id} deleted"

    raise raise_item_cannot_be_found_exception()






@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book

def create_book_no_api():
    book_1 = Book(id = "7f773f87-c8f2-46ea-ba20-a8f484d7af47",
                  title = "Derivações de Cleiton", 
                author = "Wolfgang Von Cleiton",
                description = "Reflexões Cleitianas",
                rating = 99)
    book_2 = Book(id = "8f773f87-c8f2-46ea-ba20-a8f484d7af47",
                  title = "Estudo sobre a natureza dos líquidos gasosos a base de ceváda", 
                author = "Wolfgang Von Cleiton",
                description = "Apenas O mais do mesmo",
                rating = 99)

    book_3 = Book(id = "9f773f87-c8f2-46ea-ba20-a8f484d7af47",
                  title = "Descrepância das diferenças não semelhantes.", 
                author = "Wolfgang Von Cleiton",
                description = "Cuidado pra não se perder",
                rating = 99)

    book_4 = Book(id = "3f773f87-c8f2-46ea-ba20-a8f484d7af47",
                  title = "Damn all this beatiful girls", 
                author = "Wolfgang Von Cleiton",
                description = "De volta ao príncipio",
                rating = 99)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)



def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404,detail = "book not foound", headers = {"X-Header_Error": "Nothing to be seen at this UUID"})