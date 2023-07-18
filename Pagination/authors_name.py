import requests

r = requests.get("https://quotes.toscrape.com/")

authors = r.text

with open("authors.txt", "w") as a:
    for line in authors.split("\n"):
        if '<span>by <small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
            line = line.strip()
            a.write(line)
            a.write('\n')
