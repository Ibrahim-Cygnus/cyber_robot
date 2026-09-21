import urllib.request

url = "https://example.com/"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print(f'type of body before decoding {type(body)}')
        body = response.read().decode('utf-8')
        print("Success!")
        print(f'type of response is {type(response)}')
        status_code = response.status
        print(f'status code is {status_code}')
        print(body)
        print(f'the type of the body after decoding is {type(body)}')
        headers_dict = response.info()
        print(headers_dict)
except Exception as e:
    print(f"An error occurred: {e}")