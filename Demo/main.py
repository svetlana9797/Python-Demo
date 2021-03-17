import os
import requests
from GithubClass import GithubClass
from FreshdeskClass import FreshdeskClass


#get information from the command line
#username = input("Enter Github username:")
#subdomain = input("Enter Freshdesk subdomain:")

#hardcoding here for testing purposes
username = "svetlana9797"
subdomain = "newaccount1615460023104"

github_obj = GithubClass(os.environ.get('GITHUB_TOKEN'), username)
#print(obj.get_data())
data = github_obj.get_data()

freshdesk_obj = FreshdeskClass(data, subdomain, os.environ.get('FRESHDESK_TOKEN'))
id = freshdesk_obj.create_contact()

'''
if freshdesk_obj.contact_exists(id):
    print("Freshdesk contact created!")
else:
    print("A contact with id "+ id +" doesn't exist!")

to_del = input("Do you wish to delete the recently created contact?\n Type y/n: ")  
if to_del == "y":
    del_contact = freshdesk_obj.delete_contact(id)
    print("Deletion completed with status code:", del_contact.status_code)
'''

