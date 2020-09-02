
import urllib.request
import urllib.parse
import urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if not address:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    counter = -1
    info = js["results"][0]["address_components"]
    for item in info:
        counter += 1
        if js["results"][0]["address_components"][counter]["types"] == ['country', 'political']:
            print(js["results"][0]["address_components"][counter]["short_name"])
        else:
            continue
