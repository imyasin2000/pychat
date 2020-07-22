from requests import get, post
import json
import webbrowser
import jwt
import base64

client_id = 'dj0yJmk9YUc0Z1NNS1VMYzJCJmQ9WVdrOU1IcEZPVmt6TXpnbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTZj'
client_secret = '99921476f30c4fa680ba5452549ccc9342253b2d'
base_url = 'https://api.login.yahoo.com/'
code_url = f'oauth2/request_auth?client_id={client_id}&redirect_uri=oob&response_type=code&language=en-us'
webbrowser.open(base_url + code_url)
encoded = base64.b64encode((client_id + ':' + client_secret).encode("utf-8"))
headers = {
    'Authorization': f'Basic {encoded.decode("utf-8")}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
code = input("bezan :\n")
data = {
    'grant_type': 'authorization_code',
    'redirect_uri': 'oob',
    'code': code
}
response = post(base_url + 'oauth2/get_token', headers=headers, data=data)
headers = {
    'Authorization': f'Bearer {response.json()["access_token"]}',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response2 = get('https://api.login.yahoo.com/openid/v1/userinfo', headers=headers)
email=response2.json()['email']
name=response2.json()['name']
user_name=response2.json()['nickname']
image=response2.json()['picture']
##############################
import urllib.request
urllib.request.urlretrieve(image, '%s.png'%user_name)
#####################
print(email,name,user_name)