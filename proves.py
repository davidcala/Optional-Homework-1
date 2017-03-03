import sys
import urllib2
from bs4 import BeautifulSoup

api_key = None
location = "Lleida"


class WeatherClient(object):
    url_base = "http://api.wunderground.com/api/"
    url_service = {
        "almanac": "/almanac/q/CA/",
        "hourly": "/hourly/q/CA/"
        }

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def keep_html(self, location):
        url = WeatherClient.url_base + self.api_key + WeatherClient.url_service["hourly"] + location + ".xml"
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()
        return data

    def hourly_temp(self, data, i):
        soup = BeautifulSoup(data, 'lxml')
        elements = soup.find_all("temp")
        element = elements[i].find("metric")
        return element.text

    def hourly_feels(self, data, i):
        soup = BeautifulSoup(data, 'lxml')
        elements = soup.find_all("feelslike")
        element = elements[i].find("metric")
        return element.text

    def hourly_hour(self, data, i):
        soup = BeautifulSoup(data, 'lxml')
        elements = soup.find_all("civil")
        return elements[i].text


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "API Key must be in command option"
    wc = WeatherClient(api_key)
    data = wc.keep_html(location)
    print "La previsio es sobre les 5 seguents hores a la ciutat de " + location + "\n"
    count = 0
    while count < 5:
        temperature = wc.hourly_temp(data, count)
        feelslike = wc.hourly_feels(data, count)
        hour = wc.hourly_hour(data, count)
        print hour
        print "La temperatura sera de: " + temperature + " graus i la sensacio sera de: " + feelslike
        count = count + 1
