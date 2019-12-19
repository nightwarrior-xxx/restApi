import requests
import json

BASE_ENDPOINT = "http://127.0.0.1:8000/api/status/"
BASE_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_AUTH_ENDPOINT = BASE_AUTH_ENDPOINT + "refresh/"

img_path = "/home/nightwarrior-xxx/Downloads/osdhacktelegram.png"
data = {
    "username": "restapi",
    "password": "restapi@123"
}
headers = {
    "Content-Type": "application/json"
}

res = requests.post(BASE_AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
auth_token = res.json()["token"]
print(auth_token)

header_new = {
    "Content-Type": "application/json",
    "Authorization": "JWT " + auth_token,
}

with open(img_path, 'rb') as image:
    file_data = {
        "image": image
    }
    data = {
    "content": "This is JWT updated data"
    }
    # req = requests.post(BASE_ENDPOINT, data=data, headers=header_new, files=file_data)
    req = requests.put(BASE_ENDPOINT + str(11) + "/", data=json.dumps(data), headers=header_new)#, files=file_data)
    print(req.text)





# refresh_token = {
#     "token": auth_token
# }

# res = requests.post(AUTH_ENDPOINT, data=json.dumps(refresh_token),  headers=headers)
# auth_token = res.json()["token"]
# print("\nrefresh token '%s'" % auth_token)




# BASE_URL = "http://127.0.0.1:8000/api/status/"
# img_path = "/home/nightwarrior-xxx/Downloads/osdhacktelegram.png"

# def req(method, data, is_json=True, image_path=None):
#     headers = {}
#     if is_json:
#         headers["content-type"] = "application/json"
#         data = json.dumps(data)
#     if img_path:
#         with open(img_path, 'rb') as image:
#             file_data = {
#                 "image": image
#             }
#             r = requests.request(method, BASE_URL, data=data, headers=headers, files=file_data)
#     r = requests.request(method, BASE_URL, data=data, headers=headers)
#     print(r.status_code)
#     print(r.text)

# req(method="put", data={"id": "5", "user": 1,  "content": "This is a so good"},is_json=False, image_path=img_path)
