import json 
from mypyfiles.addressbook import Book


class JSONHandler():
    def __init__(self, file_path:str): 
        self.FILE_PATH = file_path



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
    RETURN: Array of JSON Data
    """
    #Directly go through the FILE_PATH and returns json data. 
    def returnRawJsonData(self): 
        file = open(self.FILE_PATH)
        address_book_data = json.load(file)
        file.close()
        return address_book_data

    def __insert_data_into_json_file(self, json_array_data, json_file_path):
        with open(json_file_path, "w") as file: 
            json.dump(json_array_data, file, indent=4)


    """
    RETURN: array of Book.class 
    Get the json response from func: returnRawJsonData() and 
    create instance of Book Object with it. And store it in an array"""
    def returnBookClassData(self,): 
        json_data = self.returnRawJsonData()
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
        fetched_json_data = self.returnRawJsonData()
        update_entry_after_new_add= []
        for data in fetched_json_data: 
            update_entry_after_new_add.append(data) 
        update_entry_after_new_add.append(newBook) 
        self.__insert_data_into_json_file(update_entry_after_new_add, self.FILE_PATH)

        
    """
    DELETE: 
    """
    def deleteJSONDataWithGivenId(self, delete_id):
        fetched_json_data = self.returnRawJsonData()
        del_id = delete_id
        update_entry_after_delete = [] 
        for data in fetched_json_data: 
            if(data["id"] == del_id): 
                pass 
            else: 
                update_entry_after_delete.append(data) 
        self.__insert_data_into_json_file(update_entry_after_delete, self.FILE_PATH)



    """

    """
    def getJsonDataById(self, id): 
        return self.__frontAndBackSearch(id)
        
    def replaceExistingDataWithEdited(self, editedData:Book): 
        fetched_json_data = self.returnRawJsonData()
        update_entry_after_edit = []
        for i in range(len(fetched_json_data)): 
            if str(fetched_json_data[i]["id"]) == str(editedData.getId()): 
                update_entry_after_edit.append(editedData.convertToJSONFormat())
            else: 
                update_entry_after_edit.append(fetched_json_data[i])
        self.__insert_data_into_json_file(update_entry_after_edit, self.FILE_PATH)




            