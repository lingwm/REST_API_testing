from flask import Flask
from flask_restful import Api
from resources.customer import Customer, CustomerList
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://user1:user1pass@localhost/northwind"
api = Api(app)

api.add_resource(Customer, "/customer/<string:customerid>")
api.add_resource(CustomerList, "/customers")
db.init_app(app)

if __name__ == '__main__':

    app.run(port=5000, debug=True)
