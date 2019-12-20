import requests
import json

BASE_ENDPOINT = "http://127.0.0.1:8000/api/status/"
BASE_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_AUTH_ENDPOINT = BASE_AUTH_ENDPOINT + "refresh/"

img_path = "/home/nightwarrior-xxx/Downloads/osdhacktelegram.png"

# data = {
#     "username": "test3",
#     "email": "test3@gmail.com",
#     "password": "test@123",
#     "password2": "test@123"
# }
# headers = {
#     "Content-Type": "application/json",
#     "Authentication": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMCwidXNlcm5hbWUiOiJ0ZXN0NCIsImV4cCI6MTU3Njg0NzkyMiwiZW1haWwiOiJ0ZXN0NEBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU3Njg0NzYyMn0.TZM6KFW6u3vM23gc72kM9flZ0k1uQh8epsd77CLVUas', 'expires': '2019-12-27T13:13:42.591804Z', 'response': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMCwidXNlcm5hbWUiOiJ0ZXN0NCIsImV4cCI6MTU3Njg0NzkyMiwiZW1haWwiOiJ0ZXN0NEBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU3Njg0NzYyMn0.TZM6KFW6u3vM23gc72kM9flZ0k1uQh8epsd77CLVUas"
# }

# res = requests.post(BASE_AUTH_ENDPOINT + "register/",
#                     data=json.dumps(data), headers=headers)
# auth_token = res.json()
# print(auth_token)

headers = {
    "Content-Type": "application/json"
}

data = {
    "username": "restapi",
    "password": "restapi@123"
}

req = requests.post(BASE_AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = req.json()["token"]
print(req.text)

header_new = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

with open(img_path, 'rb') as image:
    file_data = {
        "image": image
    }
    data = {
        "content": "This is JWT now way updated data"
    }
    # req = requests.post(BASE_ENDPOINT, data=data, headers=header_new, files=file_data)
    req = requests.put(BASE_ENDPOINT + "11/",
                       data=data, headers=header_new, files=file_data)
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
