import re

htmlString = '<p>Hello World</p>'


output = re.sub(r'<.*?>','',htmlString)
print(output)
