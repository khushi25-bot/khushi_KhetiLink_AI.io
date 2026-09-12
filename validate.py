import re
content = open('index.html', encoding='utf-8').read()

opens = {tag: len(re.findall(f'<{tag}[ >]', content, re.I)) for tag in ['div','script','style','header','nav','body','html','head']}
closes = {tag: len(re.findall(f'</{tag}>', content, re.I)) for tag in ['div','script','style','header','nav','body','html','head']}

all_ok = True
for tag in opens:
    o, c = opens[tag], closes[tag]
    ok = o == c
    if not ok:
        all_ok = False
    print(f'  <{tag}>: open={o} close={c} {"OK" if ok else "MISMATCH"}')

screens = re.findall(r'id="screen-([a-z]+)"', content)
print(f'\nScreens: {screens}')
print('HTML structure: OK' if all_ok else 'HTML structure: ISSUES FOUND')
