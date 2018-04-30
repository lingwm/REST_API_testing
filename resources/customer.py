from flask_restful import Resource
from models.customer import CustomerModel


class Customer(Resource):
    def get(self, customerid):
        customer = CustomerModel.find_by_customerid(customerid)
        if customer:
            return customer.json()
        return {'message': 'Item not found'}, 404


class CustomerList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), CustomerModel.query.all()))}