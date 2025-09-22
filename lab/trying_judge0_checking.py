import http.client
from dotenv import load_dotenv
import os
load_dotenv()
conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
headers = {
    'x-rapidapi-key': os.getenv('KEY'),
    'x-rapidapi-host': "judge0-ce.p.rapidapi.com"
}
conn.request("GET", "/submissions/773650ea-e82c-4310-8ad7-55567f005e00?base64_encoded=false&fields=*", headers=headers)
res = conn.getresponse()
data = res.read()
print(data)