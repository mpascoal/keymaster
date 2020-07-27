from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import models
import json
import allbundle as a

# init_app
app = Flask(__name__)

# init db
#db = SQLAlchemy(app)
# init ma
ma = Marshmallow(app)



@app.route('/')
def hello():
    return a.get().text

if __name__ == "__main__":
    pass
    