from flask import Flask
from flask_restful import Api
from resources.customer import Customer, CustomerList
from resources.testing import Testing
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://lingwm:qwer1234@northwind.cuwveprzzhbn.us-west-2.rds.amazonaws.com:3306/northwind"
api = Api(app)

api.add_resource(Customer, "/customer/<string:customerid>")
api.add_resource(CustomerList, "/customers")
api.add_resource(Testing, "/testing")
db.init_app(app)

if __name__ == '__main__':

    app.run(port=5000, debug=True)
