# First import package
import requests
# Define an URL 
URL = "http://www.python.org"
# Send a GET request 
# and store in variable 
my_response = requests.get(url=URL)
# Content is now saved
# let's print response code 
print("Your response code is:")
print(my_response.status_code)
# Now let's view the content
print("Your response content is")
print(my_response.status.content)
# Similarily requests.post will generate a post request