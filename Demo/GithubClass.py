import requests
import os

class GithubClass(): 

    def __init__(self, github_token, username):

        self.headers = {
            "Authorization": "token " + github_token,
            "Accept": "application/vnd.github.v3+json"}
            
        self.url = "https://api.github.com/user"
        self.payload = {"username": username}

        self.s = requests.session()
        #self.s.headers.update(self.headers)
    
    def get_header(self):
        return self.s.headers

    def update_header(self, header):
        self.s.headers.update(header)
        #print(self.s.headers)
    
    def get_url(self):
        return self.url

    def update_url(self, u):
        self.url = u
        print(self.url)

    def extract_for_freshdesk(self, data):

        return_data = {'name': data['name'],
                       'email': data['email'],
                       'description': data['bio']
                       }

        return return_data

    def get_data(self):
        try:
            self.update_header(self.headers)
            response = self.s.get(self.url, data = self.payload, timeout = 3)
            response.raise_for_status()
        
        except requests.RequestError as e:
            raise SystemExit(e)

        return self.extract_for_freshdesk(response.json())


