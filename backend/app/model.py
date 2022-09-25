from pydantic import BaseModel, Field, EmailStr


class BooksSchema(BaseModel):

    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)

    class Config:

        schema_extra = {
            "post_demo" : {
                "title" : "Books",
                "content" : "Bookcontent"
            }
        }

# adding comments to a book
class CommentsSchema(BaseModel):

    id : int = Field(default=None)
    comment : str = Field(default=None)

    class Config:

        schema_extra = {
            "post_demo" : {
                "content" : "I love the book alot"
            }
        }


# registration
class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:

        the_schema = {
            "user_demo" : {
                "name" : "Shadrack",
                "email" : "shadcodes@gmail.com",
                "password" : "4090"
            }
        }

# user login schema
class UserLoginSchema(BaseModel):

    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:

        the_schema = {

            "user_demo" : {

                "email" : "shadcodes@gmail.com",
                "password" : "4090"
            }
        }