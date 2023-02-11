import json
json = json.loads(open('/home/dev/Documents/python/json-tutorial/sample.json').read())
value = json['country']
print (value)