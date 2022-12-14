from flask import Flask, render_template
import json 
from mypyfiles.jsonHandler import JSONHandler

FILE_PATH = "data/addressbook.json"

app = Flask(__name__) 
jsonDataHandler = JSONHandler(FILE_PATH)

#Home page: View All Data from the json file.
@app.route("/")
def index(): 
    books_data = jsonDataHandler.returnBookClassData()
    print(books_data[0].getISBNNo())
    return render_template("index.html", booksData = books_data)



#DELETE
@app.route("/delete/<int:id>") 
def delete_data_from_json_file(id): 
    jsonDataHandler.deleteJSONDataWithGivenId(id)
    books_data = jsonDataHandler.returnBookClassData()
    return render_template("index.html", booksData = books_data)


# #EDIT
# @app.route("/edit/<int:id>") 
# def edit_data_and_submit_to_json_file(id): 
#     jsonDataHandler.deleteJSONDataWithGivenId(id)
#     books_data = jsonDataHandler.returnBookClassData()
#     return render_template("index.html", booksData = books_data)


@app.route("/edit")
def edit_page(): 
    pass
    # return render_template("edit-data.html")

if __name__ == "__main__": 
    app.run(debug=True) 



    
    