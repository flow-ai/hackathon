from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class Service(Resource):

    def NLG(self,input):
        #insert your NLG solution here
        output="you said "+input
        return(output)


    def post(self):
        parser.add_argument('input', type=str)
        args = parser.parse_args()
        output=self.NLG(args['input'])
        return {
            'output': '{}'.format(output)
        }


api.add_resource(Service, '/')

if __name__ == '__main__':
    app.run(debug=True)