import requests
import json

apikey = input("Key > ")
apisec = input("Secret > ")
req_url = requests.get("https://rest.nexmo.com/account/get-balance?api_key="+apikey+"&api_secret="+apisec).text
de = json.loads(req_url)
print("\nBalance > ", de['value'])
print("AutoReload > ", de['autoReload'])