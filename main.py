import requests
import details_generator as DG

payload = {
    "fingerprint": "956833213890846760.kebhTMLabvfSte5HxhOrNPtcc2I",
    "email": DG.email,
    "username": DG.username,
    "password": DG.password,
    "invite": "null",
    "consent": "true",
    "date_of_birth": DG.bday,
    "gift_code_sku_id": "null",
    "captcha_key": "null",
}

url = "https://discord.com/register"
param = {"email": DG.email}

r = requests.Session()
register = r.post(url, data=payload)
print(register)
