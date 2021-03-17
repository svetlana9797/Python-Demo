import requests
import os
import unittest
from GithubClass import GithubClass

class TestGithubClass(unittest.TestCase):

    def test_update_header(self):

        test_token = "test"
        test_username = "test_username"
        test_header = {'Content-Type': "test_content_type", 'Accept': "test/accept"}

        obj = GithubClass(test_token, test_username)
        obj.update_header(test_header)
        res = obj.get_header()

        self.assertEqual(test_header['Content-Type'], res['Content-Type'])
        self.assertEqual(test_header['Accept'],res['Accept'])

    def test_update_url(self):
        
        test_token = "test"
        test_username = "test_username"
        test_url = "test.url"

        obj = GithubClass(test_token, test_username)
        obj.update_url(test_url)

        self.assertEqual(test_url, obj.get_url())

    def test_extract_for_freshdesk(self):

        test_token = "test"
        test_username = "test_username"
        test_data = {'name' : "Test Name", 'email' : "test@email.com", 'bio' : "test bio",
                     'login' :"test login",'location': 'test location','followers': 5, 'following': 12}

        obj = GithubClass(test_token, test_username)
        returned_data = obj.extract_for_freshdesk(test_data)

        self.assertEqual(returned_data['name'], test_data['name'])
        self.assertEqual(returned_data['email'], test_data['email'])
        self.assertEqual(returned_data['description'], test_data['bio'])
        
    def test_get_data(self):

        test_username = "svetlana9797"
        test_token = os.environ.get('GITHUB_TOKEN')
        result = { 'name' : "Svetlana Grueva", 'email' : "srgrueva@gmail.com", 'description' : "..."}

        obj = GithubClass(test_token, test_username)
        test_data = obj.get_data()

        self.assertEqual(test_data['name'], result['name'])
        self.assertEqual(test_data['email'], result['email'])
        self.assertEqual(test_data['description'], result['description'])


if __name__=='__main__':
    unittest.main()

