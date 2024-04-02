import requests
from bs4 import BeautifulSoup

# The URL to which the request is sent
url = "https://crikk.com/text-to-speech/"

# Headers based on the successful JavaScript request
headers = {
    "Host": "crikk.com",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    # "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://crikk.com/text-to-speech/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "304",
    "Origin": "https://crikk.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

# The data payload as form data
data = {
    "language": "",
    "charecter": "en-GB-ThomasNeural",
    "text": "Meng+Qianqian's+eyes+lit+up+slightly+upon+seeing+this,+and+she+continued+to+stroke+the+surface+of+the+egg+with+the+feather+while+simultaneously+stroking+the+egg+with+her+other+hand.%0D%0A%0D%0AAll+of+a+sudden,+the+egg+stopped+swaying+and+fell+completely+still."
}

# Sending the POST request
response = requests.post(url, headers=headers, data=data)

# If you need to parse the HTML content you can use BeautifulSoup here

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)

# For now, let's just print the response text to see if it worked
print(response.text)
