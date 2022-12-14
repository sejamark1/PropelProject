import json 
from mypyfiles.book import Book


class JSONHandler():
    def __init__(self, file_path:str): 
        self.FILE_PATH = file_path


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
            book = Book(data["id"], data["isbn_no"], data["book_name"], data["author_name"])
            book_data.append(book)

        return book_data


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



