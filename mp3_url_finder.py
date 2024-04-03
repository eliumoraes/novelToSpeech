import re
from html.parser import HTMLParser

class MP3URLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.mp3_urls = []  # To hold all matching URLs
        self.url_pattern = re.compile(r'https://crikk.com/text-to-speech/audio_cache/\d+\.mp3')

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and self.url_pattern.match(attr[1]):
                    self.mp3_urls.append(attr[1])

    def get_mp3_urls(self):
        return self.mp3_urls

def find_mp3_urls_in_html(html_file_path):
    parser = MP3URLParser()
    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parser.feed(line)
        mp3_urls = parser.get_mp3_urls()
        return mp3_urls
    except FileNotFoundError:
        print(f"File {html_file_path} not found.")
        return []

# Example usage
if __name__ == "__main__":
    html_file_path = 'result_raw.html'  # Change this to your actual HTML file path
    mp3_urls = find_mp3_urls_in_html(html_file_path)
    if mp3_urls:
        print("Found MP3 URLs:")
        for url in mp3_urls:
            print(url)
    else:
        print("No MP3 URLs found.")
