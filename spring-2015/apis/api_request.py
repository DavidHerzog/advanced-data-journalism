import urllib2, json

API_KEY = 'd7b45f3b788240acb4ab8c8aa56d7446'

for i in range(1, 6):
    response = urllib2.urlopen('http://realtime.influenceexplorer.com/api/new_filing/?page=%s&page_size=10&format=json&apikey=%s' % (i, API_KEY))
    json_object = json.load(response)

    for result in json_object['results']:
        print result['committee_name']