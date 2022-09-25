import uvicorn
from fastapi import FastAPI
from fastapi import Body, Depends

# schema
from app.model import BooksSchema, UserLoginSchema, UserSchema, CommentsSchema
from app.auth import jwt_handler
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

# dummy data
books = [
    {
        "id" : 1,
        "title" : "Atomic habbits",
        "text" : "Help your self be better"
    },

    {
        "id" : 2,
        "title" : "Automating boring staff with python",
        "text" : "Learning automation and machine learning with this book"
    },

    {
        "id" : 3,
        "title" : "Machine learning",
        "text" : "Accelerate you machine learning skills with this book and learn about neural nets"
    }
]

users = []

comments = [
    {
        "id" : 1,
        "text": "I hate game of thrones it has a bad ending to it" 
    }
]

app = FastAPI()


# user sign up
@app.post('/user/signup', tags=["user auth"])
def user_signup(user: UserSchema = Body(default=None)):

    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):

    for user in users:

        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False

# login
@app.post("/user/login", tags=["user auth"])
def user_login(user: UserLoginSchema=Body(default=None)):

    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "Error" : "Invalid login details"
        }



# all books
@app.get('/books', tags=["book actions"])
def get_books():
    
    return  {
        "data" : books
    }


# books by id
@app.get('/books/{id}', tags=["book actions"])
def get_one_book(id: int):

    if id > len(books):
        return  {
            "error" : "No such book"
        }
    
    for book in books:
        if book["id"] == id:
            return {
                "data" : book
            }

# add book
@app.post('/books', dependencies=[Depends(jwtBearer)],tags=["book actions"])
def add_book(book: BooksSchema):
    
    book.id = len(books) + 1
    books.append(book.dict())

    return {
        "Added" : "Book added"
    }

# all comments
@app.get('/comments', tags=["book actions"])
def get_comments():

    return  {
        "data" : comments
    }


# add comment to a book
@app.post('/comments',dependencies=[Depends(jwtBearer)], tags=["book actions"])
def add_comment(comment: CommentsSchema):
    
    comment.id = len(books) + 1
    comments.append(comment.dict())

    return {
        "Added" : "Comment added"
    }