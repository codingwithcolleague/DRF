import json
import requests

# URL = "http://127.0.0.1:8000/studentinfo/2"
# r = requests.get(url= URL)
# data = r.json()

# print(data)


URL = "http://127.0.0.1:8000/studentapi/"
data = {
    
    "name" : "Love ",
    "roll" : 101,
    "city" : "Ranchi"
} 

json_data = json.dumps(data)
# r = requests.get(url= URL,data=json_data)
r = requests.post(url= URL,data=json_data)

data = r.json()
print(data)

import json
import requests

# URL = "http://127.0.0.1:8000/studentinfo/2"
# r = requests.get(url= URL)
# data = r.json()

# print(data)

# URL = "http://127.0.0.1:8000/studentinfo/2"
# r = requests.get(url= URL)
# data = r.json()

# print(data)


# URL = "http://127.0.0.1:8000/studentcreate/"
# data = {
#     'id' : 1,
#     "name" : "rahul",
#     "roll" : 141,
#     "city" : "Ranchi"
# } 

# json_data = json.dumps(data)
# r = requests.post(url= URL, data=json_data)

# data = r.json()
# print(data)

# URL = "http://127.0.0.1:8000/studentupdate/"
# data = {
#     'id' : 1,
#     "name" : "Kiran",
#     "roll" : 101,
#     "city" : "Ranchi"
# } 

# json_data = json.dumps(data)
# r = requests.put(url= URL, data=json_data)

# data = r.json()
# print(data)


# URL = "http://127.0.0.1:8000/studentdelete/"
# data = {
#     'id' : 2
# } 
# json_data = json.dumps(data)
# r = requests.delete(url= URL, data=json_data)

# data = r.json()
# print(data)