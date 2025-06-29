import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_data = response.json()

for i in range(len(complete_data)):
 print(f"ID: {complete_data[0]['id']}, Number: {complete_data[0]['number']}")