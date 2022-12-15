import json 
class ReadAndWrite(): 

    """
    params: filePath:str
    Go through the JSON file path and return JSON array data. 
    """
    def returnJsonDataFromFile(self, filePath):
        with open(filePath, "r") as jsonFile:
            address_book_data = json.load(jsonFile) 
            return address_book_data
    """
    params:json_array_data:arr, json_file_path:str
    Insert new JSON data into the given JSON file path. 
    """
    def insert_data_into_json_file(self, json_array_data, json_file_path):
        with open(json_file_path, "w") as file: 
            json.dump(json_array_data, file, indent=4)

    """
    params: data:str
    Writes (current edit id) to the info.txt
    """
    def write_current_editId(self,data):
        with open("info.txt", "w") as file: 
            file.write(str(data))
    """
    returns: str
    Writes (read edit id) to the info.txt
    """
    def read_current_editId(self,):
        with open("info.txt", "r") as file: 
            return file.read()