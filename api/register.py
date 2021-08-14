import requests
import time


def register(username="test_xx1", password="123456"):
    url = "http://49.235.92.12:7005/api/v1/register"
    # user = username+str(int(time.time()*1000))
    body = {
        "username": username,
        "password": password
    }
    r = requests.post(url, json=body)
    print(r.text)
    return r

if __name__ == '__main__':
    r = register(username="test_xx1")
    print(r)