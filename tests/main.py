import requests

url = "http://demo-app:5000/"

# sanity test:
simple = requests.get(url)
assert simple.status_code == 200

# post test
myobj = {"f_name": "Batel", "l_name": "Bazak", "city": "Tel", "address": "aana", "phone_number": "0503125487"}
insert_test = requests.post(url + "insert", data=myobj)
assert insert_test.status_code == 200

# Delete test
delete_test = requests.delete(url + "remove/Batel")
assert delete_test.status_code == 202



