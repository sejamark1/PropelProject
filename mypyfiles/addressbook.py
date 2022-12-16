import json
from cryptography.fernet import Fernet

class Book: 

    def __init__(self, id, name, address, postcode, mobile, email):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.id = id
        self.encryptedId = self.fernet.encrypt(str(self.id).encode())
        self.name = self.__if_book_param_empty(name) 
        self.address = self.__if_book_param_empty(address)  
        self.postcode = self.__if_book_param_empty(postcode)  
        self.mobile = self.__if_book_param_empty(mobile)  
        self.email = self.__if_book_param_empty(email)   



    def __if_book_param_empty(self, var): 
        if(str(var) == ""): 
            return "______"
        else: 
            return var

    #SETTER AND GETTERS

    #Get ID
    def getId(self,): 
        return self.id
    def getEncryptedId(self,): 
        return self.fernet.encrypt(str(self.id).encode())

    #Get and set name 
    def getName(self,): 
        return self.name
    def setName(self, name): 
        self.name = name

    #Get and set address
    def getAddress(self,): 
        return self.address
    def setAddress(self, address): 
        self.address = address

    #Get and set Postcode 
    def getPostcode(self,): 
        return self.postcode
    def setPostcod(self, postcode): 
        self.postcode = postcode

    #Get and set mobile
    def getMobile(self,): 
        return self.mobile
    def setMobile(self, mobile): 
        self.mobile = mobile

    #Get and set email
    def getEmail(self,): 
        return self.email
    def setEmail(self,email): 
        self.email = email

    
    """
    RETURNS: Convert Book Data to JSON format
    """
    def convertToJSONFormat(self):
        return     {
        "id": int(self.id),
        "name" : self.name,  
        "address" : self.address,  
        "postcode" : self.postcode, 
        "mobile" : self.mobile, 
        "email" : self.email
    }

