from flask import Flask                 # from the flask module import the Flask class

app = Flask(__name__)                   # create an instance of Flak into our variable "app"
                                        # from here on out, "app" is now an "object"

@app.get("/")                           # We can noe use our projec's method "get" as decorator.
def index():                            # A decorator wraps a funtion (more on this in bit)
    me = {                              # On line 8, we create a new dictionary with key/value pairs.
        "first_name": "Giancarlo",
        "last_name": "Calette",
        "hobbies": "3D Printing",
        "is_active": True
    }
    return me                           # When you return a dictionary from a view function,
                                        # flask automatically converts it to JSON for compatibility.