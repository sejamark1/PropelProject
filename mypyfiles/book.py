import json
class Book: 
    def __init__(self, id, isbn_no, book_name, author_name):
        self.id = id 
        self.isbn_no = isbn_no
        self.book_name = book_name
        self.author_name = author_name 


    #SETTER AND GETTERS



    #Get ID
    def getId(self,): 
        return self.id
    #Get and Set isbn_no
    def getISBNNo(self,): 
        return self.isbn_no
        
    def setISBNNo(self, isbn_no):
        self.isbn_no = isbn_no

    #Get and Set book_name
    def getBookName(self): 
        return self.book_name
    
    def setBookName(self,book_name):
        self.book_name = book_name
        
    #Get and Set author_name
    def getAuthorName(self,): 
        return self.author_name 
    
    def setAuthorName(self, author_name): 
        self.author_name = author_name
        
    def convertToJSONFormat(self):
        return {
           "id" : self.id,
            "isbn_no": self.isbn_no,
            "book_name": self.book_name,
            "author_name": self.author_name 
        }

