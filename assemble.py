import os

css = open('styles.css', encoding='utf-8').read()
body = open('body.html', encoding='utf-8').read()
js = open('app.js', encoding='utf-8').read()

parts = []
parts.append('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
parts.append('<meta charset="UTF-8"/>\n')
parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n')
parts.append('<title>KhetiLink AI \u2014 Smart Selling for Gujarat Farmers</title>\n')
parts.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>\n')
parts.append('<style>\n')
parts.append(css)
parts.append('\n</style>\n</head>\n<body>\n')
parts.append(body)
parts.append('\n<script>\n')
parts.append(js)
parts.append('\n</script>\n</body>\n</html>')

html = ''.join(parts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

lines = html.count('\n') + 1
chars = len(html)
print(f'index.html: {lines} lines, {chars:,} chars')
