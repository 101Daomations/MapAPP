import json
import urllib.parse
import urllib.request

class MapQuest:
    def __init__(self):
        self.key = 'wQ3sH7PEvqUujVMa7ZsvnmUCLyILr77a'
        self.baseURL = 'http://open.mapquestapi.com/directions/v2/route'

    def totalDistance(self, locations: list) -> float:
        total = 0
        if len(locations) > 1:
            query_parameters = [('key', self.key), ('from', locations[0]), ('to', locations[1:])]
            URL = self.baseURL + '?' + urllib.parse.urlencode(query_parameters, True)
            distance = self.getResult(URL)
            total += distance['route']['distance']
        else:
            return 0
        return total

    def totalTime(self, locations: list) -> int:
        total = 0
        if len(locations) > 1:
            query_parameters = [('key', self.key), ('from', locations[0]), ('to', locations[1:])]
            URL = self.baseURL + '?' + urllib.parse.urlencode(query_parameters, True)
            distance = self.getResult(URL)
            total += distance['route']['time']
        else:
            return 0
        return total

    def directions(self, locations: list) -> str:
        direction = ''
        if len(locations) > 1:
            query_parameters = [('key', self.key), ('from', locations[0]), ('to', locations[1:])]
            URL = self.baseURL + '?' + urllib.parse.urlencode(query_parameters, True)
            distance = self.getResult(URL)
            for x in range(len(distance['route']['legs'])):
                for y in range(len(distance['route']['legs'][x]['maneuvers'])):
                    direction += distance['route']['legs'][x]['maneuvers'][y]['narrative'] + '\n'
        else:
            return ''
        return direction

    def pointOfInterest(self, locations:str, keyword:str, results:int) -> list:
        geocode_parameters = [('key', self.key), ('location', locations)]
        geoURL = 'http://www.mapquestapi.com/geocoding/v1/address?' + urllib.parse.urlencode(geocode_parameters)
        location = self.getResult(geoURL)
        lat = location["results"][0]["locations"][0]["displayLatLng"]['lat']
        long = location["results"][0]["locations"][0]["displayLatLng"]['lng']
        query_parameters = [('location', str(long) + ',' + str(lat)), ('sort', 'distance'), ('feedback', 'false'), ('key', self.key), ('pageSize', results), ('q', keyword)]
        URL = 'http://www.mapquestapi.com/search/v4/place?' + urllib.parse.urlencode(query_parameters)
        print(URL)

    def getResult(self, url):
        response = None
        try:
            response = urllib.request.urlopen(url)
            return json.load(response)
        finally:
            if response != None:
                response.close()
