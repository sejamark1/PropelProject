import json 

class JSONHandler():
    def __init__(self): 
        self.FILE_PATH = "data/addressbook.json"

    #
    def returnJSONDataFromJSONFile(self,): 
        file = open(self.FILE_PATH)
        address_book_data = json.load(file) 
        return address_book_data

