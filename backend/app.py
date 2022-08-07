# calling the custom 'all library imported' file 
from ESS import *
from ESS import app
from ESS import db

# the database model
from backend.Database.database import Library



# accessing detailed and the needed book data from the api
class BooksData:

    def __init__(self):
        self.URL = "https://anapioficeandfire.com/api/books/1"
        self.characters_url = "https://anapioficeandfire.com/api/characters"

        # reading from the url
        self.response = httpx.get(self.URL)
        self.response.headers['content-type']
        self.response_book_data = self.response.json()
    
    # gettin all books
    def all_books(self):
        
        all_book_url = {}
        all_book_url['urls'] = []

        count = 1

        # caching the results for faster execution time later
        for book in range(12):
            self.books_url = "https://anapioficeandfire.com/api/books/{}".format(count)
            all_book_url['urls'].append(self.books_url)

            count += 1

        # for url in all_book_url['urls']:

        #     self.book_count = httpx.get(url)
        #     self.book_count.headers['content-type']
        #     self.books_count_data = self.book_count.json()

        return all_book_url['urls']

    def authors(self):
        return self.response_book_data['authors']

    def book_name(self):
        return self.response_book_data['name']
    
    def release_date(self):
        return self.response_book_data['released']

    def characters(self):
        
        # for characters in :
        #     self.characters = httpx.get(characters)
        #     self.characters.headers['content-type']
        
        return len(self.response_book_data['characters'])



# response routes [books, authtors and comments]
@app.route('/books', methods=['GET', 'POST'])
def books():

    # reading different authors and books
    data = BooksData()
    book_data = {}

    # creating our new end point with the values from the API
    book_data['authors'] = data.authors()
    book_data['book_name'] = data.book_name()
    book_data['books'] = data.all_books()
    book_data['release_date'] = data.release_date()
    book_data['characters'] = data.characters()


    # displaying the book details [authors, book name and the charactors]
    if request.method == 'GET':
        return jsonify(book_data)

    # adding comments to data base  -- await the database model
    if request.method == 'POST':

        comment = "I love the book alot, I really do"
    
        db.session.add(book_data['authors'], book_data['book_name'], comment)
        db.session.commit()
        
        # flash('Record was successfully added')
        
        return jsonify(book_data)


# initilizing the server
def server(host, port, mode=True):
    return app.run(host=host, port=port, debug=mode)


# running the server
if __name__ == '__main__':
    host = "192.168.88.247"
    port = 5000
    server(host, port)