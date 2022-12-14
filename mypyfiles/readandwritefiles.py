class ReadAndWrite(): 
    def write_current_editId(self,data):
        with open("info.txt", "w") as file: 
            file.write(str(data))

    def read_current_editId(self,):
        with open("info.txt", "r") as file: 
            return file.read()