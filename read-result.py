import json, re

f = open('./test.json')
data = f.read()
data = re.sub(r'}\n{', '},{', data)
data = "["+data+"]"
# print data
jsondata =  json.loads(data)

for d in jsondata:
  if 'intervals' in d.keys():
    for stream in d['intervals']:
      s = stream['streams'][0]
      # print s
      print s['end'], s['bits_per_second'], s['lost_packets']
    print
