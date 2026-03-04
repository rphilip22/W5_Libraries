import requests
import json
import sys

response = requests.get("https://itunes.apple.com/search?&entity=song&limit=" + sys.argv[2] + "&term=eminem")

##print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])