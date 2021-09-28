import requests
import json

print("\nSIMPLE SENDGRID APIKEY CHECKER")

apikey = input("APIKEY => ")
url = 'https://api.sendgrid.com/v3/user/credits'
headers = {"authorization": "Bearer "+ apikey }
getInfo = requests.get(url, headers=headers)
# print(getInfo.text)
if 'access forbidden' in getInfo.text:
	print("APIKEY FORBIDDEN")
else:
	limit = json.loads(getInfo.text)['total']
	used = json.loads(getInfo.text)['used']
	reset = json.loads(getInfo.text)['reset_frequency']
	print("\nAPIKEY: "+apikey+"\nLimit: "+str(limit)+"\nUsed: "+str(used)+"\nReset: "+str(reset))