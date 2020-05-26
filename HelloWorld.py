import math
import os
import sys

import requests

print(sys.version)
# print((sys.version))
# print(sys.version_info)
print(sys.executable)
print("hello world")

r = requests.get("https://google.com")
print(r.status_code)

name = input("Madany Put Your Name: ")
print("hello", name)

