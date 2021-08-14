import requests


def login(s, username="test", password="123456"):
    url = "http://49.235.92.12:7005/api/v1/login"

    body = {
        "username": username,
        "password": password
        }
    response = s.post(url, json=body)
    print(response.text)
    token = response.json()["token"]
    print("token:", token)
    # 更新session 会话头部
    h = {
        "Authorization": "Token %s" % token
    }
    s.headers.update(h)
    return response

if __name__ == '__main__':
    s = requests.session()
    r = login(s)
    print(r)
    print(s.headers)