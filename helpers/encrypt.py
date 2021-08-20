import os
from Crypto.Cipher import AES
from dotenv import load_dotenv
load_dotenv()

# Fixed data
nonce = b'b\xd6\xee\xe2\xd0\x06\x9d\t\x14v\xf5+Y\x1f\x8d\x98'
tag = b'\r\xf8T\xc6\x0c\x03A\xfb\xe8\\\xa6\xc4\x98\xdf@/'
key = bytes(os.getenv("KEY"), encoding='utf-8')


def encrypt_url(url: bytes):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    encrypted_url, tag = cipher.encrypt_and_digest(url)
    print("Tag", tag, "\n", "Url", encrypted_url)
    return (tag, encrypted_url)


def decrypt_url(encrypted_url: bytes, tag: bytes):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(encrypted_url, tag)
    return str(data)


if __name__ == "__main__":
    tag, e_url = encrypt_url(url=bytes(input("url"), encoding="utf-8"))
