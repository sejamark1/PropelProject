from app import app 
import unittest
from mypyfiles.jsonHandler import JSONHandler
from mypyfiles.addressBook import Book
from mypyfiles.readAndWriteFiles import ReadAndWrite
from mypyfiles.requestData import RequestData


class testCase(unittest.TestCase): 
    def __init__(self,): 
        self.FILE_PATH = "data/addressbook.json"
        self.requestData = RequestData()
        self.readAndWrite = ReadAndWrite()
        self.jsonDataHandler = JSONHandler(self.FILE_PATH, self.readAndWrite)
            
    """
    Test if home page is loaded with 200 status code.
    """
    def test_if_home_page_loads(self,): 
        tester = app.test_client(self,) 
        res = tester.get("/", content_type="html/text")
        try: 
            self.assertEqual(res.status_code, 200) 
            print("FAILED: test_if_home_page_loads")
        except: 
            print("PASSED: test_if_home_page_loads")


    """
    Test if home page has the correct content. 
    """
    def test_if_home_page_loaded_with_right_content(self,): 
        tester = app.test_client(self,) 
        res = tester.get("/", content_type="html/text")
        try: 
            self.assertTrue('This is home page with home data' in res.data) 
            print("FAILED: test_if_home_page_loaded_with_right_content")
        except: 
            print("PASSED: test_if_home_page_loaded_with_right_content")
            
    """
    Test if it is the edit page
    data with id = 1 (edit/1) must be in the JSON File 
    """
    def test_if_edit_page_loaded_with_right_content(self,): 
        tester = app.test_client(self,)
        res = tester.get("/edit/1")
        try:
            self.assertTrue('This is the edit page for a single data' in res.data)
            print("FAILED: test_if_edit_page_loaded_with_right_content") 
        except:
            print("PASSED: test_if_edit_page_loaded_with_right_content")
    """
    Test if it is the edit page
    
    """
    def test_if_edit_page_has_correct_content_for_id(self,): 
        tester = app.test_client(self,)
        res = tester.get("/edit/1")
        desired_data = b'Bradley Allen' and b'107 Station Rd, Sheffield, South Yorkshire' and b'S35 2XF' and b'07889156989' and b'bradley@gmail.com' in res.data
        try:
            self.assertTrue(desired_data)
            print("FAILED: test_if_edit_page_has_correct_content_for_id") 
        except: 
            print("PASSED: test_if_edit_page_has_correct_content_for_id")

    def test_if_new_book_is_added(self):
        tester = app.test_client()
        res = tester.post("/add", data=dict(contactName = "Test book 1", \
                                            contactAddress="Test address 1",  
                                            contactPostcode="Test address 2", 
                                            contactMobile="Test address 3", 
                                            contactEmail="Test address 4" )) 
        try: 
            self.assertEqual(res.status_code, 302) # Data found
            print("FAILED: test_if_new_book_is_added")  
        except: 
            print("PASSED: test_if_new_book_is_added")

    """
    Test if test data with id = 1312321313123 is deleted after being added to the JSON file. 
    """

    def test_if_delete_by_id_worked(self,): 
        tester = app.test_client()
        newContact = Book("1312321313123", "Test Name", "Test Address", "Test postcode", "Test Mobile", "Test Email") 
        self.jsonDataHandler.addDataToJsonFile(newContact.convertToJSONFormat())
        res = tester.get("delete/1312321313123")
        try:
            self.assertEqual(res.status_code, 302)
            print("FAILED: test_if_delete_by_id_worked") 
        except: 
            print("PASSED: test_if_delete_by_id_worked")


    """
    Run this to run all the test methods.
    """
    def run_all_test(self): 
        self.test_if_home_page_loads()
        self.test_if_home_page_loaded_with_right_content()
        self.test_if_new_book_is_added()
        self.test_if_delete_by_id_worked()
        self.test_if_edit_page_loaded_with_right_content() 
        self.test_if_edit_page_has_correct_content_for_id()



if __name__ == "__main__": 
    tester = testCase() 
    tester.run_all_test()
