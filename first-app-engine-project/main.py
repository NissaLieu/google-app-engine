#!/user/bin/python2.7
#main.py This is for GAE gcloud service
# the import section
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 template library.
the_jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

# the handler section
class MainPage (webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!') #the response

class SecretPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1> You found the secret! </h1>') #the response

class memeGenerator(webapp2.RequestHandler):
    def get(self): #the get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        the_variable_dict = {
                "line1":"If Cinderella's shoe was a perfect fit",
                "line2":"Why did it fall off",
                "img_url":"https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
                }
        a_variable_dict = {
                "greeting": "Howdy",
                "adjective": "amazing"
                }
        self.response.write(welcome_template.render(the_variable_dict)) # the response
# etc

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url tothe Main Page Handler
    ('/secret', SecretPage), #this maps '/secret' to the Secret Page Handler
    ('/mg', memeGenerator),
    ], debug=True)

