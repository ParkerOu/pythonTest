import re

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

files = [re.findall('.+/(.+)', url)[0] for url in urls]

count = {}
for file in files:
    try:
        count[file] = count.get(count[file]) + 1
    except:
        count[file] = 1