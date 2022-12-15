import json
class Book: 
    def __init__(self, id, name, address, postcode, mobile, email):
        self.id = id
        self.name = name 
        self.address = address 
        self.postcode = postcode
        self.mobile = mobile
        self.email = email 



    #SETTER AND GETTERS



    #Get ID
    def getId(self,): 
        return self.id

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

    
        
    def convertToJSONFormat(self):
        return     {
        "id": int(self.id),
        "name" : self.name,  
        "address" : self.address,  
        "postcode" : self.postcode, 
        "mobile" : self.mobile, 
        "email" : self.email
    }

