import os
import requests

def request(address):
    url = "https://api.api-ninjas.com/v1/iplookup?address={}".format(address)
    response = requests.get(url, headers={'X-Api-Key': 'm/kt1fTkQods5DwclGVhYg==y1SfZTmIJZLImGQG'})
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

address = input("Enter a valid IP address: ")
response_data = request(address)

if response_data:
    print(response_data)

os.system("pause")
