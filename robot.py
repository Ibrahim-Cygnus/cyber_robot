import urllib.request
import hashlib
url = "https://example.com/"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        hash_object = hashlib.sha256(body)
        hex_object = hash_object.hexdigest()
        print(hex_object)
except Exception as e:
    print(f"An error occurred: {e}")