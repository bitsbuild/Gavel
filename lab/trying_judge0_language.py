import http.client
from dotenv import load_dotenv
import os
conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
load_dotenv()
headers = {
    'x-rapidapi-key': os.getenv('KEY'),
    'x-rapidapi-host': "judge0-ce.p.rapidapi.com"
}
conn.request("GET", "/languages/92", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# OUTPUT BELOW
# {  
#     "id":92,
#     "name":"Python (3.11.2)",
#     "is_archived":false,
#     "source_file":"script.py",
#     "compile_cmd":null,
#     "run_cmd":"source /usr/local/bin/conda_init \u0026\u0026 conda activate python3.11.2 \u0026\u0026 python3 script.py"
# }