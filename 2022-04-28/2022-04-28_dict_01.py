d = {}
if 'hello' in d:
    d['hello'] = d['hello'].append('привет')
else:
    d['hello'] = ['добрый день']
print(d['hello'])

if 'hello' in d:
    d['hello'].append('привет')
else:
    d['hello'] = ['добрый день']

print(d['hello'])

