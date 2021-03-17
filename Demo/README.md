This is a Python program which retrieves the information of a GitHub User and creates a new Contact or updates an existing contact in Freshdesk.

Running the program:

Run the main.py file.The program will start and the user must enter a Github username, from which he wants to pull data, and a Freshdesk subdomain, in which he wishes to create the contact.

*For the program to run successfully, the user must set GITHUB_TOKEN and FRESHDESK_TOKEN environment variables on his machine containing the corresponding personal access tokens for the specified accounts.*

Running the unit tests:

Run the test_Freshdeskclass.py for tests related to the Freshdesk functionality - creating or updating an account in Freshdesk with given input data

Run the test_GithubClass.py for tests related to the Github functionality - getting information for the specified account from the user input