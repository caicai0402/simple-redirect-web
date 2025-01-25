import time
import requests

while True:
    requests.get("https://simple-redirect-web.onrender.com")
    time.sleep(300)
