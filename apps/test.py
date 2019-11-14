import json


s = '{"B07WS6WQJD": "2019-10-26 18:01:51", "	B07XNYCFB8": "2019-10-30 11:45:17"}'
s = s.replace('	','')
print(json.loads(s))