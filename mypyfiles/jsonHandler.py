import json 
from mypyfiles.addressbook import Book
from mypyfiles.readandwritefiles import ReadAndWrite


class JSONHandler():
    def __init__(self, file_path:str, readAndWrite:ReadAndWrite): 
        self.FILE_PATH = file_path
        self.readAndWrite = readAndWrite



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
    ADD: 
    par: newBook : json converted format 
    """
    def addDataToJsonFile(self, newBook):
        fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        update_entry_after_new_add= []
        for data in fetched_json_data: 
            update_entry_after_new_add.append(data) 
        update_entry_after_new_add.append(newBook) 
        self.readAndWrite.insert_data_into_json_file(update_entry_after_new_add, self.FILE_PATH)

        
    """
    DELETE: 
    """
    # def deleteJSONDataWithGivenId(self, delete_id):
    #     fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
    #     del_id = delete_id
    #     update_entry_after_delete = [] 
    #     for data in fetched_json_data: 
    #         if(data["id"] == del_id): 
    #             pass 
    #         else: 
    #             update_entry_after_delete.append(data) 
    #     self.readAndWrite.insert_data_into_json_file(update_entry_after_delete, self.FILE_PATH)


    def deleteJSONDataWithGivenId(self, delete_id):
        fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        del_id = delete_id
        update_entry_after_delete = self.__filter("del", fetched_json_data, del_id, None)
        self.readAndWrite.insert_data_into_json_file(update_entry_after_delete, self.FILE_PATH)


    """

    """
    def getJsonDataById(self, id): 
        return self.__frontAndBackSearch(id)
        
    # def replaceExistingDataWithEdited(self, editedData:Book): 
    #     fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
    #     update_entry_after_edit = []
    #     for data in fetched_json_data: 
    #         if int(data["id"]) == int(editedData.getId()): 
    #             update_entry_after_edit.append(editedData.convertToJSONFormat())
    #         else: 
    #             update_entry_after_edit.append(data)
    #     self.readAndWrite.insert_data_into_json_file(update_entry_after_edit, self.FILE_PATH)

    def replaceExistingDataWithEdited(self, editedData:Book): 
        fetched_json_data = self.readAndWrite.returnJsonDataFromFile(self.FILE_PATH)
        update_entry_after_edit = self.__filter("edit", fetched_json_data, editedData.getId(), editedData)
        self.readAndWrite.insert_data_into_json_file(update_entry_after_edit, self.FILE_PATH)
    """
    purpose: 
        del: delete the data filter
        edit: Edit the edited data filter
    fetchedData: fetched json data. 
    compareId: id to compare  
    editData: given on purpose="replace"
    """
    def __filter(self, purpose, fetchedData, compareId, editData:Book = None): 
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
                




     
     
  
  