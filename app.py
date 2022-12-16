from flask import Flask, render_template, request, redirect
import json 
import uuid
from mypyfiles.jsonHandler import JSONHandler
from mypyfiles.addressBook import Book
from mypyfiles.readAndWriteFiles import ReadAndWrite
from mypyfiles.requestData import RequestData

from cryptography.fernet import Fernet





app = Flask(__name__) 
FILE_PATH = "data/addressbook.json"

requestData = RequestData()
readAndWrite = ReadAndWrite()
jsonDataHandler = JSONHandler(FILE_PATH, readAndWrite)




#VIEW/READ
"""
VIEW/READ
books_data: store data fetched from jsonDataHandler.class using returnBookClassData()
returns: 
    index.html: home page with view and add data functionality. 
    booksData:Book - all the book data fetched. 
    editpage: no
"""
@app.route("/")
def index(): 
    books_data = jsonDataHandler.returnBookClassData()
    return render_template("index.html", booksData = books_data, editpage="no")


#DELETE
"""
DELETE: 
id given, passed to deleteJSONDataWithGivenId from jsonDataHandler.class.
redirect to home page.
"""
@app.route("/delete/<int:id>") 
def delete_data_from_json_file(id): 
    jsonDataHandler.deleteJSONDataWithGivenId(id)
    return redirect("/")

#EDIT/UPDATE
"""
EDIT/UPDATE
On press, single data is fetched by given id and stored in book_data_by_id. 
from ReadAndWrite, it stores the current edit id. 
return: 
    index.html: template with only form to edit. 
    dataById:Book - single book data. 
    editpage: "yes" only will show edit form. 
"""
@app.route("/edit/<int:id>") 
def edit_data_and_submit_to_json_file(id): 
    book_data_by_id = jsonDataHandler.getJsonDataById(id)
    readAndWrite.write_current_editId(id)
    return render_template("index.html", dataById = book_data_by_id, editpage="yes")

"""
EDIT/UPDATE COUT'D
edit_id: get the current id in editing progress from info.txt. 
edited_book:Book -  request new edited data from the form. 
edited_book passed to replaceExistingDataWithEdited from jsonDataHandler.class to be updated. 
"""
@app.route("/submit-edit", methods=["POST"]) 
def edit_data_and_submit_to_json_file1(): #change the name
    edit_id = readAndWrite.read_current_editId()
    edited_book = requestData.requestForm(editId=edit_id)
    jsonDataHandler.replaceExistingDataWithEdited(edited_book)
    return redirect("/")

#ADD/CREATE
"""
ADD/CREATE: 
newBook request the entered value from the form, 
pass it to addDataToJsonFile method from jsonDataHandler.class. 
"""
@app.route("/add", methods=["POST", "GET"])
def add_data(): 
    newBook = requestData.requestForm()
    jsonDataHandler.addDataToJsonFile(newBook.convertToJSONFormat())
    return redirect("/")

"""
Requests the data from the search form. 
Returns updated search results and pass it to the index.html template 
"""
@app.route("/search", methods=["GET", "POST"])
def search_data(): 
    r_search_result = requestData.requestSearchForm() 
    print("Searched " + r_search_result)
    address_book_search_result = jsonDataHandler.returnSearchResults(r_search_result)
    return render_template("index.html", booksData = address_book_search_result, editpage="no", is_it_search="yes", queryData = str(r_search_result))

if __name__ == "__main__": 
    app.run(debug=True) 



    
    