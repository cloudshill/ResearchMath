from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5"+"find?q={}&type=like"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)
        print(request)
        print('Request sent!')
    def found_location(self, request, data):
        print('Here')
        data = json.loads(data.decode()) # if not is instance(data, dict): else data
        cities = ["{} ({})".format(d['name'],d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()


        hahahahahahaha
        rsrsrsrs
        jajajaja
        lol
        kkkkkkk

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
