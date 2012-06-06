import os, random
import webapp2, jinja2
from google.appengine.ext import db

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class Visitor(db.Model):
    country = db.StringProperty(default=None)
    region = db.StringProperty(default=None)
    city = db.StringProperty(default=None)
    coordinates = db.StringProperty(default=None)
    datetime = db.DateTimeProperty(auto_now_add=True)
    
    @staticmethod
    def get_list(results):
        list = []
        for result in results:
            # I have the feeling that 0.000000,0.000000 can't be right...
            if result.coordinates and result.coordinates != '0.000000,0.000000':
                latitude, longitude = result.coordinates.split(',')
                location_name = '%s, %s (%s)' % (result.city, result.region, result.country)
                list.append({'lat': latitude, 'lon': longitude, 'name': location_name, 'date': result.datetime})
        return list

class GeoJS(webapp2.RequestHandler):
    def get(self):
        results = db.GqlQuery("SELECT * FROM Visitor")
        visits = Visitor.get_list(results)
        template_values = { 'visits': visits }
        template = jinja_environment.get_template('visitors.js')
        
        # Response
        self.response.headers.add_header('Content-Type', 'text/javascript; charset=UTF-8')
        self.response.out.write(template.render(template_values))

class MainPage(webapp2.RequestHandler):
    def get(self):
        # recent visits
        results = db.GqlQuery("SELECT * FROM Visitor ORDER BY datetime DESC LIMIT 10")
        recent = Visitor.get_list(results)
        
        # store new visit
        visitor = Visitor()
        if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Development'):
            visitor.country = 'X-AppEngine-Country-%d' % random.randint(1, 100)
            visitor.region = 'X-AppEngine-Region-%d' % random.randint(1, 100)
            visitor.city = 'X-AppEngine-City-%d' % random.randint(1, 100)
            visitor.coordinates = '%d,%d' % (random.randint(-90, 90), random.randint(0, 180))
        else:
            visitor.country = self.request.headers.get('X-AppEngine-Country')
            visitor.region = self.request.headers.get('X-AppEngine-Region')
            visitor.city = self.request.headers.get('X-AppEngine-City')
            visitor.coordinates = self.request.headers.get('X-AppEngine-CityLatLong')
        visitor.put()
        
        if visitor.coordinates:
            autodected = True
            text = "We've located you at %s, %s (%s)" % (visitor.city, visitor.region, visitor.country)
            pair = visitor.coordinates
        else:
            autodected = False
            text = "Sorry, we couldn't detect your location."
            pair = '40.749444,-73.968056' # Defaults to UNHQ (international territory)
        
        latitude, longitude = pair.split(',')
        
        template_values = {
            'autodected': autodected, # not in use yet
            'latitude': latitude,
            'longitude': longitude,
            'text': text,
            'recent': '; '.join(item['name'] for item in recent)
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage), ('/visitors.js', GeoJS)], debug=True)
