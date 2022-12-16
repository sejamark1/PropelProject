from app import app 
import unittest

class testCase(unittest.TestCase): 
    """
    Test if home page is loaded with 200 status code.
    """
    def test_if_home_page_loads(self,): 
        print("[+] Testing if HOME PAGE load with status code 200")
        tester = app.test_client(self,) 
        res = tester.get("/", content_type="html/text")
        self.assertEqual(res.status_code, 200) 
    """
    Test if home page has the correct content. 
    """
    def test_if_home_page_loaded_with_right_content(self,): 
        print("[+] Testing if the loaded HOME PAGE is correct")
        tester = app.test_client(self,) 
        res = tester.get("/", content_type="html/text")
        self.assertTrue(b'This is home page with home data' in res.data) 

    """
    Test if it is the edit page
    
    """
    def test_if_edit_page_loaded_with_right_content(self,): 
        print("[+] Testing if the loaded EDIT PAGE is correct")
        tester = app.test_client(self,)
        res = tester.get("/edit/1")
        self.assertTrue(b'This is the edit page for a single data' in res.data) 
    """
    Test if it is the edit page
    
    """
    def test_if_edit_page_has_correct_content_for_id(self,): 
        print("[+] Testing if the loaded EDIT PAGE has the correct content for the provided id")
        tester = app.test_client(self,)
        res = tester.get("/edit/1")
        desired_data = b'Bradley Allen' and b'107 Station Rd, Sheffield, South Yorkshire' and b'S35 2XF' \
            and b'07889156989' and b'bradley@gmail.com' in res.data
        self.assertTrue(desired_data)
    
if __name__ == "__main__": 
    unittest.main() 
