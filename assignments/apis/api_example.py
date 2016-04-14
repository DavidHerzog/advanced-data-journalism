import urllib2, json, urllib

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session').read()

bills = json.loads(response)

for bill in bills:

    # This is the processing piece I mentioned in the assignment description. To include
    # a bill ID (which has spaces in it)through a URL in Python, you need to do this first.
    encoded_bill_id = urllib.quote(bill['bill_id'])
    
    print encoded_bill_id