import requests
import json
BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates"


def get_request():
    new_data = {
        "id": id
    }
    res = requests.get(BASE_URL + ENDPOINT + "/", data = json.dumps(new_data))
    print(res)
    status_code = res.status_code
    if status_code == requests.codes.ok:
        print("Not a good response")
        data = res.json()
        print(data)
    print(res.text)

print(get_request())


def post_request():
    new_data = {
        "user": "1",
        "content": "DRF is fucking awesome !!!!"
    }
    res = requests.post(BASE_URL + ENDPOINT + "/", data=json.dumps(new_data))
    print(res.status_code)
    print(res.headers)
    if res.status_code == requests.codes.ok:
        return(res.json())
    return(res.text)

# print(post_request())


def put_request():
    new_data = {
        "id": '8',
        "content": "This is my new DRF put method"
    }
    res = requests.put(BASE_URL + ENDPOINT + "/", data=json.dumps(new_data))
    print(res.status_code)
    print(res.headers)
    if res.status_code == requests.codes.ok:
        return(res.json())
    return(res.text)


# print(put_request())


def delete_request():
    res = requests.delete(BASE_URL + ENDPOINT + '/5/')
    print(res.headers)
    print(res.headers)
    if res.status_code == requests.codes.ok:
        return(res.json())
    return(res.text)

# print(delete_request())
