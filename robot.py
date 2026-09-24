import urllib.request
import hashlib
import datetime
urls = ["https://example.com/", "https://demoqa.com/","https://example.com/", "https://demoqa.com/"]
record = {}
for url in urls:
    try:
        with urllib.request.urlopen(url) as response1:
            body1 = response1.read()
            hash_object1 = hashlib.sha256(body1)
            hex_object1 = hash_object1.hexdigest()
            timestamp = datetime.datetime.now(datetime.timezone.utc).astimezone()
            if url in record:
                if record[url][-1][0] == hex_object1:
                    print("no change")
                else:
                    print("change detected")
                record[url][-1][1].append(timestamp.strftime("%Y-%m-%d %H:%M:%S.%f %Z %z"))
            else:
                record[url] = [[hex_object1,[timestamp.strftime("%Y-%m-%d %H:%M:%S.%f %Z %z")]]]
    except Exception as e:
        print(f"An error occurred: {e}")

print(record)