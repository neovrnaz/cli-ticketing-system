import json


def bitcoin_price():
    try:
        import urllib.request as urllib2
    except ImportError:
        raise ImportError('There was a problem importing urllib2')

    url = "http://api.coindesk.com/v1/bpi/currentprice/EUR.json"

    json_url = urllib2.urlopen(url)

    json_object = json.load(json_url)

    print(json_object['bpi']['USD']['code'])
    print(json_object['bpi']['USD']['rate'])
