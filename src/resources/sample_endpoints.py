import logging
from flask.ext.restful import Resource, fields, marshal_with, reqparse


test_return_fields = {
    'status': fields.String,
    'message': fields.String,
    'flag': fields.Integer
}


class Test(Resource):

    def __init__(self):
        self._parser = reqparse.RequestParser()
        self._parser.add_argument('param', type=str, required=False)

    @marshal_with(test_return_fields)
    def get(self):
        args = self._parser.parse_args()
        logging.debug("hit Test.get()")
        obj = dict(status="Success", message="hello world: {}".format(args.param), flag=0)
        return obj

