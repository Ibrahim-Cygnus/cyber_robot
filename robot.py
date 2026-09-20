# import requests

# url = "https://example.com/"

# # Send a GET request
# response = requests.get(url)

# # Check if the request was successful (Status Code 200)
# if response.status_code == 200:
#     print("Success!")
#     # If the response is HTML/Text:
#     print(response.text)
#     # If the response is JSON data:
#     # print(response.json())
# else:
#     print(f"Failed with status code: {response.status_code}")
import urllib.request
import json

# Define the target URL
url = "https://example.com/"

try:
    # Send the GET request using a context manager
    with urllib.request.urlopen(url) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print("Success!")
        print(body)
except Exception as e:
    print(f"An error occurred: {e}")