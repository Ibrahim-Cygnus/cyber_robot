from pathlib import Path
import urllib.request
import hashlib
import datetime
import json

urls = ["https://example.com/", "https://demoqa.com/","https://example.com/", "https://demoqa.com/"]
for url in urls:
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            hash_object = hashlib.sha256(body)
            hex_object = hash_object.hexdigest()
            timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone()
            record_file = Path("data.json")
            if not record_file.is_file():
                with open("data.json", "a"):
                    pass
                data = {}
                data[url] = [hex_object,[[hex_object,[timestamp.strftime("%Y-%m-%d %H:%M:%S.%f %Z %z")]]]]
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
                    continue
            else:
                with open("data.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                if url in data:
                    if not data[url][0] == hex_object:
                        data[url][0] = hex_object
                        data[url][1].append([hex_object,[]])
                    data[url][1][-1][1].append(timestamp.strftime("%Y-%m-%d %H:%M:%S.%f %Z %z"))
                else:
                    data[url] = [hex_object,[[hex_object,[timestamp.strftime("%Y-%m-%d %H:%M:%S.%f %Z %z")]]]]
        with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")