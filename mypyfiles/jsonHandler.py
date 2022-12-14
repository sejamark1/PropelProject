import json 
from mypyfiles.book import Book


class JSONHandler():
    def __init__(self, file_path:str): 
        self.FILE_PATH = file_path

    #Directly go through the FILE_PATH and returns json data. 
    def returnRawJsonData(self,): 
        file = open(self.FILE_PATH)
        address_book_data = json.load(file)
        return address_book_data

    #Get the json response from func: returnRawJsonData() and create instance of Book Object with it. And store it in an array 
    def returnBookClassData(self,): 
        json_data = self.returnRawJsonData()
        book_data = [] 
        for data in json_data: 
            book = Book(data["id"], data["isbn_no"], data["book_name"], data["author_name"])
            book_data.append(book)

        return book_data

