# import http.client

# conn = http.client.HTTPSConnection("crikk.com")

# headersList = {
#  "Host": "crikk.com",
#  "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
#  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#  "Accept-Language": "en-US,en;q=0.5",
# #  "Accept-Encoding": "gzip, deflate, br",
#  "Referer": "https://crikk.com/text-to-speech/",
#  "Content-Type": "application/x-www-form-urlencoded",
#  "Content-Length": "304",
#  "Origin": "https://crikk.com",
#  "Connection": "keep-alive",
#  "Upgrade-Insecure-Requests": "1",
#  "Sec-Fetch-Dest": "document",
#  "Sec-Fetch-Mode": "navigate",
#  "Sec-Fetch-Site": "same-origin",
#  "Pragma": "no-cache",
#  "Cache-Control": "no-cache" 
# }

# payload = "language=&charecter=en-GB-ThomasNeural&text=Meng+Qianqian's+eyes+lit+up+slightly+upon+seeing+this,+and+she+continued+to+stroke+the+surface+of+the+egg+with+the+feather+while+simultaneously+stroking+the+egg+with+her+other+hand.%0D%0A%0D%0AAll+of+a+sudden,+the+egg+stopped+swaying+and+fell+completely+still."

# conn.request("POST", "/text-to-speech/", payload, headersList)
# response = conn.getresponse()
# result = response.read()

# print("Result html:")
# print(result)

# print("Result decoded:")
# print(result.decode("utf-8"))



import http.client
import os

conn = http.client.HTTPSConnection("crikk.com")

headersList = {
 "Host": "crikk.com",
 "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
 "Accept-Language": "en-US,en;q=0.5",
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

payload = "language=&charecter=en-GB-ThomasNeural&text=Meng+Qianqian's+eyes+lit+up+slightly+upon+seeing+this,+and+she+continued+to+stroke+the+surface+of+the+egg+with+the+feather+while+simultaneously+stroking+the+egg+with+her+other+hand.%0D%0A%0D%0AAll+of+a+sudden,+the+egg+stopped+swaying+and+fell+completely+still."

conn.request("POST", "/text-to-speech/", payload, headersList)
response = conn.getresponse()
result = response.read()

# Define the filenames for the raw and decoded result
raw_filename = "result_raw.html"
decoded_filename = "result_decoded.txt"

# Write the raw result
with open(raw_filename, "wb") as file:
    file.write(result)

# Write the decoded result
with open(decoded_filename, "w", encoding="utf-8") as file:
    file.write(result.decode("utf-8"))

print(f"Raw HTML output written to {raw_filename}")
print(f"Decoded output written to {decoded_filename}")
