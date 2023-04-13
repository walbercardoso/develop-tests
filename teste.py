# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import sys
import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com",timeout=300)


