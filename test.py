import random
import requests
import base64

Client_ID = "___"
Secret_Key = "___"
Callback_URL = "http://localhost/oauth-callback"

URL = "https://login.eveonline.com/v2/oauth/authorize/"


def random_string():
    return "".join(random.choice("0123456789ABCDEF") for i in range(16))


URL = (
    URL
    + "?response_type=code&redirect_uri="
    + Callback_URL
    + "&client_id="
    + Client_ID
    + "&scope=esi-characters.read_blueprints.v1&state="
    + random_string()
)

print(URL)

Code = "___"
string = Client_ID + ":" + Secret_Key
Auth_base64 = string.encode("ascii")
Auth_base64 = base64.b64encode(Auth_base64).decode()
print(Auth_base64)
headers = {
    "Authorization": "Basic " + Auth_base64,
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "login.eveonline.com",
}

data = {"grant_type": "authorization_code", "code": Code}

response = requests.post(URL, headers=headers, data=data)

print(response.status_code)
