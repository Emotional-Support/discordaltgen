import random


def rand_gen_email():
    email = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(10))
    return email


def rand_gen_user():
    username = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(10))
    return username


def rand_gen_pass():
    password = "".join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(10))
    return password


def rand_gen_birth():
    year = random.randint(1984, 2001)
    month = random.randint(1, 12)
    day = random.randint(1, 12)
    concat = year, "-", month, "-", day
    return concat


email = rand_gen_email()
username = rand_gen_user()
password = rand_gen_pass()
bday = rand_gen_birth()


payload = {
    "fingerprint": "956833213890846760.kebhTMLabvfSte5HxhOrNPtcc2I",
    "email": email,
    "username": username,
    "password": password,
    "invite": "null",
    "consent": "true",
    "date_of_birth": bday,
    "gift_code_sku_id": "null",
    "captcha_key": "null",
}
