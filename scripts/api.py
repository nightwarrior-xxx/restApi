import requests
import json
BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates"


def get_request():
    res = requests.get(BASE_URL + ENDPOINT + "/")
    print(res)
    status_code = res.status_code
    if status_code != 200:
        print("Not a good response")
    data = res.json()
    print(data)


def post_request():
    new_data = {
        "user": "1",
        "content": ""
    }

    res = requests.delete(BASE_URL + ENDPOINT + "/", data=new_data)
    print(res.status_code)
    print(res.headers)
    if res.status_code == requests.codes.ok:
        return(res.json())
    return(res.text)


if __name__ == '__main__':
    print(post_request())
