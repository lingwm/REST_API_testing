from flask_restful import Resource


class Testing(Resource):
    def get(self):
        return {'message': 'The REST API is running'}