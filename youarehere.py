import webapp2
import jinja2
import os
from google.appengine.ext import db

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Visitor(db.Model):
    country = db.StringProperty(default=None)
    region = db.StringProperty(default=None)
    city = db.StringProperty(default=None)
    coordinates = db.StringProperty(default=None)
    datetime = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        # recent visits
        recent = []
        visits = db.GqlQuery("SELECT * FROM Visitor ORDER BY datetime DESC LIMIT 15")
        for visit in visits:
            if visit.coordinates:
                recent.append('%s, %s (%s)' % (visit.city, visit.region, visit.country))
        
        # store new visit
        visitor = Visitor()
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
        
        # some safe defaults :)
        template_values = {
            'autodected': autodected, # not in use yet
            'latitude': latitude,
            'longitude': longitude,
            'text': text,
            'recent': '; '.join(recent)
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
