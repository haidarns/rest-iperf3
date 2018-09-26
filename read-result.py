import json, re, csv

f = open('./test.json')
data = f.read()
data = re.sub(r'}\n{', '},{', data)
data = "["+data+"]"

jsondata =  json.loads(data)

prevtime = 0

streamlist = []
for d in jsondata:
  if 'intervals' in d.keys():
    for i in range(len(d['intervals'])):
      s = d['intervals'][i]['streams'][0]

      t = float(s['end']) + prevtime
      bps = s['bits_per_second']
      los = s['lost_packets']

      print t, bps, los

      streamlist.append([t, bps, los])

      if i == len(d['intervals'])-1:
        prevtime = t

    print

with open('test.csv', mode='w') as testcsv_file:
  testcsv_writer = csv.writer(
                     testcsv_file,
                     delimiter=',',
                     quotechar='"',
                     quoting=csv.QUOTE_MINIMAL
                   )
  for x in streamlist:
    testcsv_writer.writerow(x)
