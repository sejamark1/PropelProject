import json 
from mypyfiles.addressBook import Book
from mypyfiles.readAndWriteFiles import ReadAndWrite


class JSONHandler():
    def __init__(self, file_path:str, readAndWrite:ReadAndWrite): 
        self.FILE_PATH = file_path
        self.readAndWrite = readAndWrite


    """
    Private method.
    params: id:int
    RETURNS: Type:Book - single book based on given id.
    Does a front and back search on all the data (fetched_data_arr_of_book:arr)
    and finds the Book based on given id. 
    """
    def __frontAndBackSearch(self, id): 
        fetched_data_arr_of_book = self.returnBookClassData()
        front = 0 
        back = len(fetched_data_arr_of_book) - 1 
        found_at = None 
        while front <= back: 
            if fetched_data_arr_of_book[front].getId() == id:
                found_at = front
                break 
            elif fetched_data_arr_of_book[back].getId() == id:
                found_at = back 
                break 
        return fetched_data_arr_of_book[found_at]

    """
    params: purpose:str, fetchedData:str, comparedId:str/int, editedData:Book.
    purpose: 
        del: delete the data filter
        edit: Edit the edited data filter
    fetchedData: fetched json data. 
    compareId: id to compare  
    editData: given on purpose="replace"
    """
    def __filterJSONData(self, purpose, fetchedData, compareId, editData:Book = None): 
        update_entry_after = []
        for data in fetchedData:
            if int(data["id"]) == int(compareId):
                if(purpose == "del"): 
                    pass 
                if(purpose == "edit"): 
                    update_entry_after.append(editData.convertToJSONFormat())
            else: 
                update_entry_after.append(data)
        return update_entry_after
                

    """
    RETURN: array of Book.class 
    Get the json response from func: returnRawJsonData() and 
    create instance of Book Object with it. And store it in an array"""
    def returnBookClassData(self,): 
        json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        book_data = [] 
        for data in json_data: 
            book = Book(data["id"], data["name"], data["address"], data["postcode"],data["mobile"],data["email"] )
            book_data.append(book)

        return book_data

    """
    params; newBook:Book (json converted format)
    Gets the new data and inserted into JSON file. 
    """
    def addDataToJsonFile(self, newBook):
        fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        update_entry_after_new_add= []
        for data in fetched_json_data: 
            update_entry_after_new_add.append(data) 
        update_entry_after_new_add.append(newBook) 
        self.readAndWrite.insert_data_into_json_file(update_entry_after_new_add, self.FILE_PATH)

        
    """
    params: deleted_id:int
    Deletes the data from the JSON database based on the id:int provided.
    """

    def deleteJSONDataWithGivenId(self, delete_id):
        fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        del_id = delete_id
        update_entry_after_delete = self.__filterJSONData("del", fetched_json_data, del_id, None)
        self.readAndWrite.insert_data_into_json_file(update_entry_after_delete, self.FILE_PATH)


    """
    params:id:int
    Returns Book data based on Id. 
    Note: for public access. 
    """
    def getJsonDataById(self, id): 
        return self.__frontAndBackSearch(id)

    """
    params: editedData:Book
    Takes the editedData:Book and replaces it with its existing data thus updating the results. 
    """

    def replaceExistingDataWithEdited(self, editedData:Book): 
        fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        update_entry_after_edit = self.__filterJSONData("edit", fetched_json_data, editedData.getId(), editedData)
        self.readAndWrite.insert_data_into_json_file(update_entry_after_edit, self.FILE_PATH)




    """
    params: searchResult:str
    returns: search_result_only:Book:arr
    Go through the JSON File and see if searchResults matches with any of the fields. 
    """
    def returnSearchResults(self,searchResult): 
        books:Book = self.returnBookClassData()
        search_result_only = []
        for book in books: 
            see_if_input_search_matches = (searchResult.lower() in book.getName().lower()) or (searchResult.lower() in book.getAddress().lower()) or \
            (searchResult.lower() in book.getPostcode().lower()) or (searchResult.lower() in book.getMobile().lower()) or (searchResult.lower() in book.getEmail().lower())

            if(see_if_input_search_matches):
                search_result_only.append(book)
        return search_result_only



  
  