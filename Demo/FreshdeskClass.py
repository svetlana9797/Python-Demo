import requests
import base64
import os

class FreshdeskClass():
    
    def __init__(self, data, subdomain, freshdesk_token):
        self.url = "https://"+ subdomain +".freshdesk.com/api/v2/contacts"
        self.headers = {
            'Authorization': self.encode_token(freshdesk_token),
            'Content-Type' : "application/json"}

        self.data = data

        self.s = requests.session()
        self.update_header(self.headers)

    def get_header(self):
        return self.s.headers

    def update_header(self, header):
        self.s.headers.update(header)
        
    def get_url(self):
        return self.url

    def update_url(self, u):
        self.url = u
        print(self.url)

    def get_data(self):
        return self.data

    def update_data(self, d):
        self.data = d

    def encode_token(self, freshdesk_token):
        string = freshdesk_token + ':'
        freshdesk_encoded = base64.b64encode(string.encode()).decode('ascii')
        auth = "Basic %s" %freshdesk_encoded
        return auth
    
    def create_contact(self):
        try:
            r = self.s.post(self.url, json = self.data)
            r.raise_for_status()
            
        except requests.RequestException as e:
            raise SystemExit(e)
        
        j = r.json()
        return j['id']

    def contact_exists(self, id):
        try:
            response = self.s.get(self.url + "/" + str(id))
            
        except requests.RequestException as e:
            raise SystemExit(e)
        return response.ok
    
    def update_contact(self, id):
        try:
            response = self.s.put(self.url+ "/" + str(id), json = self.data)
        
        except requests.RequestException as e:
            raise SystemExit(e)
        return response
    
    def delete_contact(self,id):
        try:
            response = self.s.delete(self.url+ "/" + str(id) + "/hard_delete?force=true")
        except requests.RequestException as e:
            raise SystemExit(e)
        return response

