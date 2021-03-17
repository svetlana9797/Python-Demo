import requests
import os
import unittest
import base64
from unittest.mock import patch
from FreshdeskClass import FreshdeskClass

class TestFreshdeskClass(unittest.TestCase):
    
    def test_update_header(self):

        test_freshdesk_token = "test"
        test_subdomain = "test_subdomain"
        test_data = {'name' : "test_name", 'email' : "test_name@test.com", 'description' : "test_desc"}
        test_header = {'Content-Type': "test_content_type", 'Accept': "test/accept"}

        obj = FreshdeskClass(test_data, test_subdomain, test_freshdesk_token)
        obj.update_header(test_header)
        res = obj.get_header()

        self.assertEqual(test_header['Content-Type'], res['Content-Type'])
        self.assertEqual(test_header['Accept'],res['Accept'])
    
    def test_contact_exists(self):

        test_contact_id = "123"
        test_freshdesk_token = os.environ.get('FRESHDESK_TOKEN')
        test_subdomain = "newaccount1615460023104"
        test_data = { 'name' : "test_not_exist", 'email' : "test_not_exist@test.com", 'description' : "test_desc"}
        
        obj = FreshdeskClass(test_data, test_subdomain, test_freshdesk_token)

        #pass a non-existing id to contact_exists()
        check_contact = obj.contact_exists(id)
        self.assertEqual(check_contact, False)
    

    def test_update_contact(self):

        test_freshdesk_token = os.environ.get('FRESHDESK_TOKEN')
        test_subdomain = "newaccount1615460023104"
        test_data = { 'name' : "name_test", 'email' : "email_test@test.com", 'description' : "test_desc"}
        test_updated_data = { 'name' : "updated_name", 'email' : "updated_email@test.com", 'description' : "test_desc"}
        
        obj = FreshdeskClass(test_data, test_subdomain, test_freshdesk_token)

        #create a dummy contact
        id = obj.create_contact()
        self.assertTrue(id, "Could not create test contact!")

        #update the dummy contact
        obj.update_data(test_updated_data)
        #print(obj.get_data())

        res = obj.update_contact(id)
        print(res)
        print(res.json())
        res_json = res.json()
        
        #check if the contact updates successfully
        self.assertEqual(res_json['name'], test_updated_data['name'])
        self.assertEqual(res_json['email'], test_updated_data['email'])
        self.assertEqual(res_json['description'], test_updated_data['description'])

        #delete the created contact
        del_contact = obj.delete_contact(id)
        self.assertEqual(del_contact.status_code,204)

      
    def test_create_contact(self):

        test_freshdesk_token = os.environ.get('FRESHDESK_TOKEN')
        test_subdomain = "newaccount1615460023104"
        test_data = { 'name' : "testname", 'email' : "testname@test.com", 'description' : "testdesc"}

        obj = FreshdeskClass(test_data, test_subdomain, test_freshdesk_token)

        #create a dummy contact
        response_id = obj.create_contact()
        self.assertTrue(response_id, "Could not create test contact!")

        #check if the contact we've just created exists
        check_contact = obj.contact_exists(response_id)
        self.assertTrue(check_contact, "Contact does not exist!")

        #delete the created contact
        del_contact = obj.delete_contact(response_id)
        self.assertEqual(del_contact.status_code,204)
    

if __name__=='__main__':
    unittest.main()

