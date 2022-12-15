from flask import Flask, render_template, request, redirect
import json 
import uuid
from mypyfiles.jsonHandler import JSONHandler
from mypyfiles.addressbook import Book
from mypyfiles.readandwritefiles import ReadAndWrite
FILE_PATH = "data/addressbook.json"

app = Flask(__name__) 
readAndWrite = ReadAndWrite()
jsonDataHandler = JSONHandler(FILE_PATH, readAndWrite)

"""
This function is used for both requesting <form> value for the purpose of adding to the JSON FILE and adding the 
edited data to the JSON FILE. 

"""
def __requestForm(editId=None): 
    if(editId == None): 
        generate_unique_id = uuid.uuid4().int
    else: 
        generate_unique_id = editId # an existing id        
    r_name = request.form["contactName"]
    r_address = request.form["contactAddress"]
    r_postcode = request.form["contactPostcode"]
    r_mobile = request.form["contactMobile"]
    r_email = request.form["contactEmail"]
    newBook = Book(generate_unique_id, r_name, r_address, r_postcode, r_mobile, r_email)
    return newBook



#Home page: View All Data from the json file.
@app.route("/")
def index(): 
    books_data = jsonDataHandler.returnBookClassData()
    return render_template("index.html", booksData = books_data, editpage="no")



#DELETE
@app.route("/delete/<int:id>") 
def delete_data_from_json_file(id): 
    jsonDataHandler.deleteJSONDataWithGivenId(id)
    return redirect("/")


#EDIT
@app.route("/edit/<int:id>") 
def edit_data_and_submit_to_json_file(id): 
    book_data_by_id = jsonDataHandler.getJsonDataById(id)
    readAndWrite.write_current_editId(id)
    return render_template("index.html", dataById = book_data_by_id, editpage="yes")


@app.route("/submit-edit", methods=["POST"]) 
def edit_data_and_submit_to_json_file1(): #change the name
    edit_id = readAndWrite.read_current_editId()
    edited_book = __requestForm(editId=edit_id)
    jsonDataHandler.replaceExistingDataWithEdited(edited_book)
    return redirect("/")








#ADD
@app.route("/add", methods=["POST", "GET"])
def add_data(): 
    newBook = __requestForm()
    print(newBook.convertToJSONFormat())
    jsonDataHandler.addDataToJsonFile(newBook.convertToJSONFormat())
    return redirect("/")










if __name__ == "__main__": 
    app.run(debug=True) 



    
    