from mypyfiles.addressBook import Book 
from flask import request
import uuid

class RequestData: 
    """
    params: editedId
    returns: newBook:Book
    This function is used for both requesting <form> value for the purpose of adding to the JSON FILE and adding the 
    edited data to the JSON FILE. 
    Get data from <div id="add-contact-form"> and <div id="edit-form">
    """
    def requestForm(self, editId=None): 
        if(editId == None): 
            generate_unique_id = uuid.uuid4().int
        else: 
            generate_unique_id = editId # an existing id        
        r_name = request.form["contactName"]
        r_address = request.form["contactAddress"]
        r_postcode = request.form["contactPostcode"]
        r_mobile = request.form["contactMobile"]
        r_email = request.form["contactEmail"]
        newBook = Book(generate_unique_id, r_name, r_address, r_postcode, r_mobile, r_email)
        return newBook
    """
    return: r_search_results:str 
    Returns search result from search box.
    """
    def requestSearchForm(self,): 
        r_search_results = request.form["searchResults"]
        return r_search_results