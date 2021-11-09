import requests
import json

url = "https://discord.com/channels/@me"
header = {
    "authorization": "ODc4Njc4MTM1NzE2MDUzMDMy.YSfrdA.aqri2UJNBwie-KKf6886dxAdMk8"
}
r = requests.get(url, headers=header)
jsonn = json.loads(r.text)
for value in jsonn:
            print(value)
            print(r.status_code)
