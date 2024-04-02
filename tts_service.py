import http.client
from html.parser import HTMLParser
import re
from find_mp3_url import find_mp3_urls_in_html

def make_tts_request(chunk, chunk_size):
    conn = http.client.HTTPSConnection("crikk.com")    
    payload = f"language=&charecter=en-GB-ThomasNeural&text={chunk}"
    headersList = {
 "Host": "crikk.com",
 "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
 "Accept-Language": "en-US,en;q=0.5",
 "Referer": "https://crikk.com/text-to-speech/",
 "Content-Type": "application/x-www-form-urlencoded",
 "Content-Length": f"{str(len(payload))}",
 "Origin": "https://crikk.com",
 "Connection": "keep-alive",
 "Upgrade-Insecure-Requests": "1",
 "Sec-Fetch-Dest": "document",
 "Sec-Fetch-Mode": "navigate",
 "Sec-Fetch-Site": "same-origin",
 "Pragma": "no-cache",
 "Cache-Control": "no-cache" 
}

    conn.request("POST", "/text-to-speech/", payload, headersList)
    response = conn.getresponse()
    result = response.read()

    # Define the filenames for the raw and decoded result
    raw_filename = "result_raw.html"

    # Write the raw result
    with open(raw_filename, "wb") as file:
        file.write(result)
    
    mp3_urls = find_mp3_urls_in_html(raw_filename)

    if mp3_urls:
        print("Found MP3 URLs:")
        for url in mp3_urls:
            print(url)
            return url
    else:
        print("No MP3 URLs found.")
        return None