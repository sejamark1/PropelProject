from flask import Flask, render_template, request, redirect
import json 
import uuid
from mypyfiles.jsonHandler import JSONHandler
from mypyfiles.book import Book

FILE_PATH = "data/addressbook.json"

app = Flask(__name__) 
jsonDataHandler = JSONHandler(FILE_PATH)



def __requestForm(): 
    generate_unique_id = uuid.uuid4().int
    r_isbn_no = request.form["isbn"]
    r_book_name = request.form["bookname"]
    r_author_name = request.form["authorname"]
    newBook = Book(generate_unique_id, r_isbn_no, r_book_name,r_author_name)
    return newBook



#Home page: View All Data from the json file.
@app.route("/")
def index(): 
    books_data = jsonDataHandler.returnBookClassData()
    return render_template("index.html", booksData = books_data)



#DELETE
@app.route("/delete/<int:id>") 
def delete_data_from_json_file(id): 
    jsonDataHandler.deleteJSONDataWithGivenId(id)
    return redirect("/")


# #EDIT
# @app.route("/edit/<int:id>") 
# def edit_data_and_submit_to_json_file(id): 
#     jsonDataHandler.deleteJSONDataWithGivenId(id)
#     books_data = jsonDataHandler.returnBookClassData()
#     return render_template("index.html", booksData = books_data)


#ADD

@app.route("/add", methods=["POST", "GET"])
def add_data(): 
    newBook = __requestForm()
    print(newBook.convertToJSONFormat())
    jsonDataHandler.addDataToJsonFile(newBook.convertToJSONFormat())

    return redirect("/")










if __name__ == "__main__": 
    app.run(debug=True) 



    
    