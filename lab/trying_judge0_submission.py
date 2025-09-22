import http.client
from dotenv import load_dotenv
import os,json
conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
payload = json.dumps({
    "language_id": 92,
    "source_code": 'print("hello_world")',
    "stdin": ""
})
load_dotenv()
headers = {
    'x-rapidapi-key': os.getenv('KEY'),
    'x-rapidapi-host': "judge0-ce.p.rapidapi.com",
    'Content-Type': "application/json"
}
conn.request("POST", "/submissions?base64_encoded=false&wait=false&fields=*", payload, headers)
res = conn.getresponse()
data = res.read()
print(data)